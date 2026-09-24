import json, os, shutil, time, threading, keyboard
from datetime import datetime
from packages.midi_controller import MidiController
from packages.web_socket_handler import Dot2WebSocketHandler


class _GuiWing:
    def __init__(self, gui, device_id):
        self.gui, self.device_id = gui, device_id

    def set_button_label(self, button_id, short_label, long_label):
        self.gui.set_button_label(button_id, self.device_id, short_label, long_label)

    def set_button_color(self, button_id, hex_color):
        self.gui.set_button_color(button_id, self.device_id, hex_color)

    def set_fader_value(self, fader_id, value):
        self.gui.set_fader_value(fader_id, self.device_id, value)


class MidiControllerHandler:
    DATA_FILEPATH = "../data/data.json"
    HEARTBEAT_STEP = 10

    def __init__(self, data_filepath=None, gui_instances=None):
        self.DATA_FILEPATH = data_filepath or self.DATA_FILEPATH
        self.config_mode = 0
        self.executor_note_dictionary = {}
        self.executor_states = set()
        self.temporary_exec_states = set()
        self.dot2_ws = None
        self.gui_instances = gui_instances or [None, None]
        self.gui_instances = [
            _GuiWing(gui, i) if gui is not None else None
            for i, gui in enumerate(self.gui_instances, 1)
        ]
        self.data = {}
        self.controllers = [
            MidiController(1, {}, self.gui_instances[0], self.websocket_callback),
            MidiController(2, {}, self.gui_instances[1], self.websocket_callback),
        ]

    def setup(self):
        self.load_json()
        for c in self.controllers:
            c.select_midi_ports()
        self.dot2_ws = Dot2WebSocketHandler(
            host=self.data.get("default_ip_address", "10.0.0.50"),
            password=self.data.get("dot2_password", "1"),
            heartbeat_step=self.HEARTBEAT_STEP,
            debug=True,
        )
        self.dot2_ws.connect()
        self.dot2_ws.on("playbacks", self.handle_playbacks)
        self.load_labels()
        self.load_colors()
        keyboard.add_hotkey("F1", self.invert_devices)
        keyboard.add_hotkey("F2", self.toggle_config_mode)

    def _read_data_file(self):
        with open(self.DATA_FILEPATH) as f:
            return json.load(f)

    def _write_data_file(self, data):
        os.makedirs(os.path.dirname(self.DATA_FILEPATH) or ".", exist_ok=True)
        with open(self.DATA_FILEPATH, "w") as f:
            json.dump(data, f, indent=2)

    def load_json(self):
        self.data = self._read_data_file()
        self.config_mode = self.data.get("config_mode", 0)
        for i, c in enumerate(self.controllers, 1):
            c.default_brightness_level = self.data.get("default_brightness_level", 6)
            c.default_blink_channel = self.data.get("default_blink_channel", 10)
            c.load_data(self.data.get("devices", {}).get(str(i), {}))
        self.initiate_executor_note_dictionary()

    def persist(self):
        self.data["config_mode"] = int(self.config_mode)
        self.data.setdefault("devices", {})
        for i, c in enumerate(self.controllers, 1):
            self.data["devices"][str(i)] = c.get_persisted_data()
        self._write_data_file(self.data)

    def websocket_callback(self, kind, *args, **kwargs):
        if not self.dot2_ws:
            return
        if kind == "click":
            self.dot2_ws.send_playback_click(
                args[0], pressed=kwargs.get("pressed", True)
            )
        elif kind == "fader":
            self.dot2_ws.send_playback_fader(fader_index=args[0], fader_value=args[1])

    def initiate_executor_note_dictionary(self):
        self.executor_note_dictionary = {}
        for i, c in enumerate(self.controllers, 1):
            for note, entry in c.note_executor_dictionary.items():
                self.executor_note_dictionary.setdefault(
                    entry["executor_index"], []
                ).append((note, i))

    def invert_devices(self):
        self.controllers[0].midi_inport, self.controllers[1].midi_inport = (
            self.controllers[1].midi_inport,
            self.controllers[0].midi_inport,
        )
        self.controllers[0].midi_outport, self.controllers[1].midi_outport = (
            self.controllers[1].midi_outport,
            self.controllers[0].midi_outport,
        )
        for c in self.controllers:
            c.update_colors()

    def toggle_config_mode(self):
        self.config_mode = not self.config_mode
        self.persist()
        for c in self.controllers:
            c.update_colors()

    def load_labels(self):
        for c in self.controllers:
            c.load_labels()

    def load_colors(self):
        for c in self.controllers:
            c.update_colors()

    def imitate_midi_message(
        self, device_id, type, channel, note=None, velocity=None, cc=None, value=None
    ):
        self.controllers[device_id - 1].imitate_midi_message(
            type, channel, note, velocity, cc, value, self.config_mode
        )
        self.persist()

    def poll(self):
        for c in self.controllers:
            c.poll(self.config_mode)

    def get_executor_state(self, data):
        running = set()
        dtype = 1 if data.get("responseSubType") == 2 else 0
        for row in data.get("itemGroups", []):
            for item in row.get("items", []):
                if item[0].get("isRun") == 1 and item[0].get("iExec") is not None:
                    running.add(item[0]["iExec"])
        return running, dtype

    def handle_playbacks(self, data):
        current, dtype = self.get_executor_state(data)
        if dtype == 0:
            self.temporary_exec_states = current
            return
        current |= self.temporary_exec_states
        for executor in self.executor_states ^ current:
            for note, device_id in self.executor_note_dictionary.get(executor, []):
                self.controllers[device_id - 1].toggle_blink_note(
                    note, executor in current
                )
        self.executor_states = current
        self.temporary_exec_states = set()
