"""
MidiController: manages MIDI communication with two MA lighting console
control surfaces (Wing devices), syncs colors/states with a dot2 console
over websocket, and persists button-to-executor mappings to a JSON file.
"""

from web_socket_handler import Dot2WebSocketHandler
from tkinter import simpledialog
from datetime import datetime

import tkinter as tk
import mido
import os
import glob
import json
import time
import shutil
import keyboard
import threading


class MidiController:

    # ---- Class-level constants (do not change between instances) ----
    FADER_NOTES = tuple(range(81, 99))
    NORMAL_BUTTON_NOTES = tuple(range(65))
    SPECIAL_BUTTON_NOTES = (100, 101, 102, 103, 104, 105, 106, 107,
                             112, 113, 114, 115, 116, 117, 118, 119)
    SHIFT_KEY = 122

    BUTTON_COLORS_DEVICE1 = list(range(0, 65))
    BUTTON_COLORS_DEVICE2 = list(range(65, 128))

    HEARTBEAT_STEP = 10
    PERIODIC_PLAYBACK_INTERVAL = 3  # in seconds

    BWING_START_INDEX = [300, 400, 500, 600, 700, 800]
    BWING_ITEMS_COUNT = [16, 16, 16, 16, 16, 16]
    BWING_ITEMS_TYPE = [3, 3, 3, 3, 3, 3]
    BWING_VIEW = 3
    BWING_EXEC_VIEW_MODE = 2

    FWING_START_INDEX = [0, 100, 200]
    FWING_ITEMS_COUNT = [22, 22, 22]
    FWING_ITEMS_TYPE = [2, 3, 3]
    FWING_VIEW = 2
    FWING_EXEC_VIEW_MODE = 1

    USERNAME = "remote"

    DATA_FILEPATH = "data.json"

    def __init__(self, data_filepath=None):
        self.DATA_FILEPATH = data_filepath or self.DATA_FILEPATH

        # MIDI ports
        self.midi_inport_device1 = None
        self.midi_outport_device1 = None
        self.midi_inport_device2 = None
        self.midi_outport_device2 = None

        self.default_midi_inport_device1 = ""
        self.default_midi_outport_device1 = ""
        self.default_midi_inport_device2 = ""
        self.default_midi_outport_device2 = ""
        self.inverted_devices = False

        # Data loaded from JSON
        self.note_executor_dictionary_device1 = {}
        self.note_executor_dictionary_device2 = {}
        self.executor_note_dictionary = {}
        self.executor_states = set()
        self.temporary_exec_states = set()

        self.default_brightness_level = 6
        self.default_blink_channel = 10
        self.config_mode = 1

        # Dot2 connection info (populated by load_json)
        self.host = "192.168.0.6"
        self.plaintext_password = "1"

        self.dot2_ws = None
        self._playback_poll_thread = None

    # =================================================================
    #                         Tools / Utils
    # =================================================================

    @staticmethod
    def ask_input(prompt=""):
        """Opens a small Tkinter dialog to ask the user for text input."""
        root = tk.Tk()
        root.withdraw()
        result = simpledialog.askstring("Input", prompt)
        print(result)
        root.destroy()
        return result

    def invert_devices(self):
        (self.midi_inport_device1, self.midi_inport_device2) = \
            (self.midi_inport_device2, self.midi_inport_device1)
        (self.midi_outport_device1, self.midi_outport_device2) = \
            (self.midi_outport_device2, self.midi_outport_device1)

        self.inverted_devices = not self.inverted_devices
        self.set_correct_bmt_preset()
        self.update_colors()

    @staticmethod
    def get_last_backup(backup_directory_path):
        backups = glob.glob(os.path.join(backup_directory_path, "data_backup_*.json"))
        if not backups:
            return None
        backups.sort()  # timestamp format YYYY-MM-DD_HH-MM sorts correctly as strings
        return backups[-1]

    def restore_last_backup(self):
        backup_directory_path = os.path.join(
            os.path.dirname(os.path.abspath(self.DATA_FILEPATH)), "backups"
        )
        last_backup = self.get_last_backup(backup_directory_path)

        if not last_backup:
            print("No backup found to restore.")
            return

        if not self._confirm_destructive_action(
            "Are you sure you want to load the last backup?(Y/N) \n"
            "YOUR CURRENT COLORS WILL BE OVERWRITTEN."
        ):
            return

        shutil.copy2(last_backup, self.DATA_FILEPATH)

        self.load_json()
        self.update_colors()

    def _confirm_destructive_action(self, warning_prompt):
        """
        Shared confirmation flow used by destructive actions:
        first a Y/N prompt, then a typed "CONFIRM" prompt.
        Returns True only if both steps pass.
        """
        if self.ask_input(warning_prompt).lower() == "y":
            if self.ask_input('Type "CONFIRM" to proceed. Your current file will be LOST.') != "CONFIRM":
                return False
            return True
        return False

    def initiate_executor_note_dictionary(self):
        """
        Builds a reverse-lookup dict:
        {"executor_id": [[note, device_id], [note, device_id], ...], ...}
        This allows multiple notes to be mapped to the same executor.
        """
        self.executor_note_dictionary = {}

        for note, entry in self.note_executor_dictionary_device1.items():
            executor = entry["executor_index"]
            self.executor_note_dictionary.setdefault(executor, []).append([note, 1])

        for note, entry in self.note_executor_dictionary_device2.items():
            executor = entry["executor_index"]
            self.executor_note_dictionary.setdefault(executor, []).append([note, 2])

    def set_correct_bmt_preset(self):
        if self.inverted_devices:
            self.send_midi_message("note_on", 0, 127, 67)
        else:
            self.send_midi_message("note_on", 0, 127, 69)

    # =================================================================
    #                            JSON
    # =================================================================

    def load_json(self):
        with open(self.DATA_FILEPATH, "r") as f:
            data = json.load(f)

        self.note_executor_dictionary_device1 = data["note_executor_dictionary_device1"]
        self.note_executor_dictionary_device2 = data["note_executor_dictionary_device2"]
        self.default_brightness_level = data["default_brightness_level"]
        self.default_blink_channel = data["default_blink_channel"]
        self.host = data["default_ip_address"]
        self.plaintext_password = data["dot2_password"]
        self.config_mode = data["config_mode"]

        if data["DEFAULT_MIDI_INPORT_DEVICE1"] != "":
            self.default_midi_inport_device1 = data["DEFAULT_MIDI_INPORT_DEVICE1"]

        if data["DEFAULT_MIDI_OUTPORT_DEVICE1"] != "":
            self.default_midi_outport_device1 = data["DEFAULT_MIDI_OUTPORT_DEVICE1"]

        if data["DEFAULT_MIDI_INPORT_DEVICE2"] != "":
            self.default_midi_inport_device2 = data["DEFAULT_MIDI_INPORT_DEVICE2"]

        if data["DEFAULT_MIDI_OUTPORT_DEVICE2"] != "":
            self.default_midi_outport_device2 = data["DEFAULT_MIDI_OUTPORT_DEVICE2"]

    def _read_data_file(self):
        with open(self.DATA_FILEPATH, "r") as f:
            return json.load(f)

    def _write_data_file(self, data):
        with open(self.DATA_FILEPATH, "w") as f:
            json.dump(data, f, indent=2)

    def append_note_to_json(self, note, executor_index, device_id, color=None):
        data = self._read_data_file()

        entry = {"executor_index": executor_index}
        if color is not None:
            entry["color"] = color

        if device_id == 1:
            data["note_executor_dictionary_device1"][str(note)] = entry
        elif device_id == 2:
            data["note_executor_dictionary_device2"][str(note)] = entry

        data["note_executor_dictionary_device1"] = dict(
            sorted(data["note_executor_dictionary_device1"].items(), key=lambda x: int(x[0]))
        )
        data["note_executor_dictionary_device2"] = dict(
            sorted(data["note_executor_dictionary_device2"].items(), key=lambda x: int(x[0]))
        )

        self._write_data_file(data)

    def set_default_devices(self, device1_input="", device1_output="",
                             device2_input="", device2_output=""):
        data = self._read_data_file()

        if device1_input != "":
            data["DEFAULT_MIDI_INPORT_DEVICE1"] = device1_input
        if device2_input != "":
            data["DEFAULT_MIDI_INPORT_DEVICE2"] = device2_input
        if device1_output != "":
            data["DEFAULT_MIDI_OUTPORT_DEVICE1"] = device1_output
        if device2_output != "":
            data["DEFAULT_MIDI_OUTPORT_DEVICE2"] = device2_output

        self._write_data_file(data)

    def toggle_config_mode(self):
        self.config_mode = not self.config_mode

        data = self._read_data_file()

        if self.config_mode:
            self.flash_color(2, 5)
            data["config_mode"] = 1
        else:
            self.flash_color(2, 21)
            data["config_mode"] = 0

        self._write_data_file(data)

    def remove_color_from_data(self):
        self.flash_color(2, 120)

        if not self._confirm_destructive_action(
            "Are you sure you want to remove all colors?(Y/N) \nA backup will be created."
        ):
            return

        self._backup_data_file()

        data = self._read_data_file()

        for note in data["note_executor_dictionary_device1"]:
            data["note_executor_dictionary_device1"][note]["color"] = -1
        for note in data["note_executor_dictionary_device2"]:
            data["note_executor_dictionary_device2"][note]["color"] = -1

        self._write_data_file(data)

        self.load_json()
        self.update_colors()

    def _backup_data_file(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%M")  # no colons!

        base_dir = os.path.dirname(os.path.abspath(self.DATA_FILEPATH))
        backup_directory_path = os.path.join(base_dir, "backups")
        backup_filepath = os.path.join(backup_directory_path, f"data_backup_{timestamp}.json")

        os.makedirs(backup_directory_path, exist_ok=True)
        shutil.copy2(self.DATA_FILEPATH, backup_filepath)

    def link_executor_note(self, note, device_id):
        """
        Updates the data.json file
        :param note: the MIDI note number to link
        :param device_id: the device ID to link the executor to
        """
        if device_id == 1 and str(note) in self.note_executor_dictionary_device1:
            executor_index = self.note_executor_dictionary_device1[str(note)]["executor_index"]
        elif device_id == 2 and str(note) in self.note_executor_dictionary_device2:
            executor_index = self.note_executor_dictionary_device2[str(note)]["executor_index"]
        else:
            temp = self.ask_input("Please input the id of the executor")
            if temp is None:
                return
            executor_index = int(temp) - 1

        if note in self.NORMAL_BUTTON_NOTES:
            color = self.choose_color()
            self.append_note_to_json(note, executor_index, device_id=device_id, color=color)

        elif note in self.SPECIAL_BUTTON_NOTES or note == self.SHIFT_KEY:
            self.append_note_to_json(note, executor_index, device_id=device_id, color=1)

        self.load_json()
        self.update_colors()

    # =================================================================
    #                            MIDI
    # =================================================================

    def _prompt_for_port(self, port_names, label):
        print(f"Please select the {label}\n",
              '\n '.join(f"{i + 1}- {item}" for i, item in enumerate(port_names)))
        choice = port_names[int(self.ask_input("Please select an available port")) - 1]
        return choice

    def select_midi_ports(self):
        available_inputs = mido.get_input_names()
        available_outputs = mido.get_output_names()

        # --- Input Device 1 ---
        if self.default_midi_inport_device1 not in available_inputs:
            temp = self._prompt_for_port(available_inputs, "first device Input(Wing-1)")
            self.midi_inport_device1 = mido.open_input(temp)
            available_inputs.remove(temp)
            if self.ask_input(f"Do you want to make {temp} your default INPUT device 1 ?(Y/N)").lower() == "y":
                self.default_midi_inport_device1 = temp
        else:
            self.midi_inport_device1 = mido.open_input(self.default_midi_inport_device1)

        # --- Input Device 2 ---
        if self.default_midi_inport_device2 not in available_inputs:
            temp = self._prompt_for_port(available_inputs, "second device Input(Wing-2)")
            self.midi_inport_device2 = mido.open_input(temp)
            if self.ask_input(f"Do you want to make {temp} your default INPUT device 2 ?(Y/N)").lower() == "y":
                self.default_midi_inport_device2 = temp
        else:
            self.midi_inport_device2 = mido.open_input(self.default_midi_inport_device2)

        # --- Output Device 1 ---
        if self.default_midi_outport_device1 not in available_outputs:
            temp = self._prompt_for_port(available_outputs, "first device Output(Wing-1)")
            self.midi_outport_device1 = mido.open_output(temp)
            available_outputs.remove(temp)
            if self.ask_input(f"Do you want to make {temp} your default OUTPUT device 1 ?(Y/N)").lower() == "y":
                self.default_midi_outport_device1 = temp
        else:
            self.midi_outport_device1 = mido.open_output(self.default_midi_outport_device1)

        # --- Output Device 2 ---
        if self.default_midi_outport_device2 not in available_outputs:
            temp = self._prompt_for_port(available_outputs, "second device Output(Wing-2)")
            self.midi_outport_device2 = mido.open_output(temp)
            if self.ask_input(f"Do you want to make {temp} your default OUTPUT device 2 ?(Y/N)").lower() == "y":
                self.default_midi_outport_device2 = temp
        else:
            self.midi_outport_device2 = mido.open_output(self.default_midi_outport_device2)

        self.set_default_devices(
            device1_input=self.default_midi_inport_device1,
            device2_input=self.default_midi_inport_device2,
            device1_output=self.default_midi_outport_device1,
            device2_output=self.default_midi_outport_device2,
        )
        print(
            f"Midi Device IN 1: {self.midi_inport_device1}\n"
            f"Midi Device IN 2: {self.midi_inport_device2}\n"
            f"MIDI Device OUT 1: {self.midi_outport_device1}\n"
            f"MIDI Device OUT 2: {self.midi_outport_device2}\n"
        )

    def flash_color(self, duration, color):
        self.set_all_pads(velocity=color, channel=11)
        time.sleep(duration)
        self.update_colors()

    def set_all_pads(self, velocity=0, channel=None):
        channel = self.default_brightness_level if channel is None else channel
        for pad in self.NORMAL_BUTTON_NOTES:
            self.send_midi_message(midi_message_type="note_on", channel=channel, note=pad, velocity=velocity)

    def send_midi_message(self, midi_message_type, channel, note, velocity, device_id=3):
        midi_message = mido.Message(
            type=str(midi_message_type), channel=int(channel), note=int(note), velocity=int(velocity)
        )
        if device_id == 1:
            self.midi_outport_device1.send(midi_message)
        elif device_id == 2:
            self.midi_outport_device2.send(midi_message)
        else:
            self.midi_outport_device1.send(midi_message)
            self.midi_outport_device2.send(midi_message)

    def listen_to_note(self):
        while True:
            for incoming_message in self.midi_inport_device1.iter_pending():
                return incoming_message, 1

            for incoming_message in self.midi_inport_device2.iter_pending():
                return incoming_message, 2

    def choose_color(self):
        for pad in range(len(self.BUTTON_COLORS_DEVICE1)):
            self.send_midi_message(
                midi_message_type='note_on', channel=6, note=pad,
                velocity=self.BUTTON_COLORS_DEVICE1[pad], device_id=1
            )

        for pad in range(len(self.BUTTON_COLORS_DEVICE2)):
            self.send_midi_message(
                midi_message_type='note_on', channel=6, note=pad,
                velocity=self.BUTTON_COLORS_DEVICE2[pad], device_id=2
            )

        message, device_id = self.listen_to_note()
        while message.type != 'note_on':
            message, device_id = self.listen_to_note()
            if message.note not in self.NORMAL_BUTTON_NOTES:
                return -1

        if device_id == 1:
            return self.BUTTON_COLORS_DEVICE1[message.note]
        elif device_id == 2:
            return self.BUTTON_COLORS_DEVICE2[message.note]

    def turn_off_pad(self):
        self.set_all_pads(0, 6)

        for pad in self.SPECIAL_BUTTON_NOTES:
            self.send_midi_message(midi_message_type='note_on', channel=0, note=pad, velocity=0)

    def update_colors(self):
        """Updates all colors of the pad including special buttons."""
        self.turn_off_pad()
        note_executor_dictionaries = [
            self.note_executor_dictionary_device1,
            self.note_executor_dictionary_device2,
        ]

        for device in range(2):
            for button_note, entry in note_executor_dictionaries[device].items():
                color = entry["color"]
                if color < 0:
                    continue

                if int(button_note) in self.NORMAL_BUTTON_NOTES:
                    self.send_midi_message(
                        midi_message_type='note_on',
                        channel=self.default_brightness_level,
                        note=button_note, velocity=color, device_id=device + 1
                    )
                elif int(button_note) in self.SPECIAL_BUTTON_NOTES:
                    # Channel 0 is the only channel that should be used with special buttons
                    self.send_midi_message(
                        midi_message_type='note_on', channel=0,
                        note=button_note, velocity=1, device_id=device + 1
                    )

        self.update_all_blinking()

    def set_colors(self, note_list, color, device_id):
        for note in note_list:
            self.send_midi_message(
                "note_on", self.default_brightness_level, note, velocity=color, device_id=device_id
            )

    def toggle_blink_note(self, note, device_id, toggle_on):
        print(f"toggle_blink_note:\nNote: {note}\nDeviceId: {device_id}\ntoggle_on: {toggle_on}\n\n")

        if int(note) in self.SPECIAL_BUTTON_NOTES:
            velocity = 2 if toggle_on else 1
            self.send_midi_message("note_on", 0, note, velocity=velocity, device_id=device_id)

        elif int(note) in self.NORMAL_BUTTON_NOTES:
            if device_id == 1:
                color = self.note_executor_dictionary_device1[str(note)]["color"]
            elif device_id == 2:
                color = self.note_executor_dictionary_device2[str(note)]["color"]
            else:
                return

            if color == -1:
                return

            channel = self.default_blink_channel if toggle_on else self.default_brightness_level
            self.send_midi_message("note_on", channel, note, velocity=color, device_id=device_id)

    def update_all_blinking(self):
        self.executor_states = set()
        self.temporary_exec_states = set()
        self.dot2_ws.poll_exec_state()

    def dot2_logo(self):
        self.set_all_pads(109, 6)
        self.set_colors((8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 23, 28, 37, 38, 47, 51, 55, 60, 61, 62), 3, 1)
        self.set_colors((8, 11, 13, 14, 15, 16, 19, 22, 24, 25, 26, 27, 30, 32, 35, 38, 40, 43, 45, 46, 47), 3, 2)

    # =================================================================
    #                          Playbacks
    # =================================================================

    @staticmethod
    def get_executor_state(data):
        """
        Takes the top-level data structure and returns a set of executor ids
        (from the 'iExec' field) that are currently ON (isRun == 1), along with
        the data type: 0 if B-Wing, 1 if F-Wing.

        Each entry in data['itemGroups'] is a row containing one or more
        executor dicts. We iterate through all of them and check 'isRun'.
        """
        running_ids = set()
        data_type = 0  # 0 If B-Wing, 1 if F-Wing
        if data.get("responseSubType", None) == 2:
            data_type = 1

        items_group = data.get("itemGroups", [])
        if len(items_group) == 0:
            return

        for row in items_group:
            for exec_item in row.get("items", []):
                exec_id = exec_item[0].get('iExec', None)
                if exec_item[0].get('isRun') == 1 and exec_id is not None:
                    running_ids.add(exec_id)

        return running_ids, data_type

    def handle_playbacks(self, data):
        """
        Serves as a hub for playback management, including feedback to the controller.

        Because of how the websocket is made it is IMPOSSIBLE to get every executor
        in a single request. Therefore, handle_playbacks is called twice for every
        playback poll (there are 2 requests made by dot2_ws.poll_exec_state()).
        This means that the data received is INCOMPLETE and must not be treated
        as absolute until both calls have come in.
        """
        current_running_execs, exec_data_type = self.get_executor_state(data)
        # F-Wing is always the second set of data to come in, therefore we know
        # we treat the data if exec_data_type is equal to 1
        if exec_data_type == 0:
            self.temporary_exec_states = current_running_execs
            return

        old_exec_states = self.executor_states
        current_running_execs = current_running_execs | self.temporary_exec_states
        print(f"Current running execs: {current_running_execs}")

        if old_exec_states == current_running_execs:
            return  # No need to continue if they're the same

        # Symmetric difference: only keep the executors whose state changed
        old_current_symmetry = old_exec_states ^ current_running_execs

        for executor in old_current_symmetry:
            turned_on = executor in current_running_execs
            for note, device_id in self.executor_note_dictionary[executor]:
                print(f"Note {'ON' if turned_on else 'OFF'}: {note}")
                self.toggle_blink_note(note, device_id, turned_on)

        self.executor_states = current_running_execs
        self.temporary_exec_states = set()

    def periodic_playback_poll(self):
        while True:
            time.sleep(self.PERIODIC_PLAYBACK_INTERVAL)
            self.dot2_ws.poll_exec_state()

    def note_loop(self, message, device_id):
        note = message.note
        if int(note) in self.FADER_NOTES:
            return

        if message.type == 'note_on' and self.config_mode:
            self.link_executor_note(note, device_id)
            return

        note_executor_dict = (
            self.note_executor_dictionary_device1 if device_id == 1
            else self.note_executor_dictionary_device2
        )

        if str(note) in note_executor_dict:
            executor_index = note_executor_dict[str(note)]["executor_index"]
            self.dot2_ws.send_playback_click(executor_index, pressed=message.velocity == 127)
            self.dot2_ws.poll_exec_state()

    # =================================================================
    #                      Setup / Run / Lifecycle
    # =================================================================

    def setup(self):
        """Loads config, opens MIDI ports, connects to the dot2 console, and
        registers hotkeys. Must be called before run()."""
        self.load_json()
        self.initiate_executor_note_dictionary()
        self.select_midi_ports()
        self.dot2_logo()

        self.dot2_ws = Dot2WebSocketHandler(
            host=self.host,
            username=self.USERNAME,
            password=self.plaintext_password,
            heartbeat_step=self.HEARTBEAT_STEP,

            bwing_start_index=self.BWING_START_INDEX,
            bwing_items_count=self.BWING_ITEMS_COUNT,
            bwing_items_type=self.BWING_ITEMS_TYPE,
            bwing_view=self.BWING_VIEW,
            bwing_exec_view_mode=self.BWING_EXEC_VIEW_MODE,

            fwing_start_index=self.FWING_START_INDEX,
            fwing_items_count=self.FWING_ITEMS_COUNT,
            fwing_items_type=self.FWING_ITEMS_TYPE,
            fwing_view=self.FWING_VIEW,
            fwing_exec_view_mode=self.FWING_EXEC_VIEW_MODE,

            debug=True,
        )
        self.dot2_ws.connect()

        while not self.dot2_ws.logged_in:
            time.sleep(0.1)

        self._register_hotkeys()

        time.sleep(2)  # For the dot2 logo to stay on

        self.dot2_ws.on("playbacks", self.handle_playbacks)
        self.update_colors()

        self._playback_poll_thread = threading.Thread(
            target=self.periodic_playback_poll, daemon=True
        )
        self._playback_poll_thread.start()

    def _register_hotkeys(self):
        keyboard.add_hotkey("F1", self.invert_devices)
        keyboard.add_hotkey("F2", self.toggle_config_mode)
        keyboard.add_hotkey("F11", self.restore_last_backup)
        keyboard.add_hotkey("F12", self.remove_color_from_data)

    def run(self):
        """Main blocking loop: listens for MIDI notes on both devices."""
        while True:
            for msg in self.midi_inport_device1.iter_pending():
                self.note_loop(msg, device_id=1)

            for msg in self.midi_inport_device2.iter_pending():
                self.note_loop(msg, device_id=2)