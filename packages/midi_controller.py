"""
MidiController: manages MIDI communication with two MA lighting console
control surfaces (Wing devices), syncs colors/states with a dot2 console
over websocket, and persists button-to-executor mappings to a JSON file.
"""

from packages.web_socket_handler import Dot2WebSocketHandler
from packages.dialogs.midi_port_dialog import MidiPortDialog
from packages.dialogs import input_prompts
from packages.gui_thread import GuiThreadDispatcher
from packages.app_info import BUNDLED_PROFILE_PATH
from packages import profile_manager
from datetime import datetime
from PySide6.QtCore import QTimer

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
    FADER_CONTROLS = tuple(range(48, 57))  # Control change numbers of the 9 faders (56 is the master fader)
    FIRST_FADER_CONTROL = 48
    # Config mode: a fader must stay still this long before touching it again opens a new prompt
    FADER_SETTLE_SECONDS = 1.0
    NORMAL_BUTTON_NOTES = tuple(range(65))
    SPECIAL_BUTTON_NOTES = (100, 101, 102, 103, 104, 105, 106, 107,
                             112, 113, 114, 115, 116, 117, 118, 119)
    SHIFT_KEY = 122

    BUTTON_COLORS_DEVICE1 = list(range(0, 64))
    BUTTON_COLORS_DEVICE2 = list(range(64, 128))
    NOTE_COLOR_MAP = {0: '#000000', 1: '#1E1E1E', 2: '#7F7F7F', 3: '#FFFFFF', 4: '#FF4C4C', 5: '#FF0000', 6: '#590000', 7: '#190000', 8: '#FFBD6C', 9: '#FF5400', 10: '#591D00', 11: '#271B00', 12: '#FFFF4C', 13: '#FFFF00', 14: '#595900', 15: '#191900', 16: '#88FF4C', 17: '#54FF00', 18: '#1D5900', 19: '#142B00', 20: '#4CFF4C', 21: '#00FF00', 22: '#005900', 23: '#001900', 24: '#4CFF5E', 25: '#00FF19', 26: '#00590D', 27: '#001902', 28: '#4CFF88', 29: '#00FF55', 30: '#00591D', 31: '#001F12', 32: '#4CFFB7', 33: '#00FF99', 34: '#005935', 35: '#001912', 36: '#4CC3FF', 37: '#00A9FF', 38: '#004152', 39: '#001019', 40: '#4C88FF', 41: '#0055FF', 42: '#001D59', 43: '#000819', 44: '#4C4CFF', 45: '#0000FF', 46: '#000059', 47: '#000019', 48: '#874CFF', 49: '#5400FF', 50: '#190064', 51: '#0F0030', 52: '#FF4CFF', 53: '#FF00FF', 54: '#590059', 55: '#190019', 56: '#FF4C87', 57: '#FF0054', 58: '#59001D', 59: '#220013', 60: '#FF1500', 61: '#993500', 62: '#795100', 63: '#436400', 64: '#033900', 65: '#005735', 66: '#00547F', 67: '#0000FF', 68: '#00454F', 69: '#2500CC', 70: '#7F7F7F', 71: '#202020', 72: '#FF0000', 73: '#BDFF2D', 74: '#AFED06', 75: '#64FF09', 76: '#108B00', 77: '#00FF87', 78: '#00A9FF', 79: '#002AFF', 80: '#3F00FF', 81: '#7A00FF', 82: '#B21A7D', 83: '#402100', 84: '#FF4A00', 85: '#88E106', 86: '#72FF15', 87: '#00FF00', 88: '#3BFF26', 89: '#59FF71', 90: '#38FFCC', 91: '#5B8AFF', 92: '#3151C6', 93: '#877FE9', 94: '#D31DFF', 95: '#FF005D', 96: '#FF7F00', 97: '#B9B000', 98: '#90FF00', 99: '#835D07', 100: '#392b00', 101: '#144C10', 102: '#0D5038', 103: '#15152A', 104: '#16205A', 105: '#693C1C', 106: '#A8000A', 107: '#DE513D', 108: '#D86A1C', 109: '#FFE126', 110: '#9EE12F', 111: '#67B50F', 112: '#1E1E30', 113: '#DCFF6B', 114: '#80FFBD', 115: '#9A99FF', 116: '#8E66FF', 117: '#404040', 118: '#757575', 119: '#E0FFFF', 120: '#A00000', 121: '#350000', 122: '#1AD000', 123: '#074200', 124: '#B9B000', 125: '#3F3100', 126: '#B35F00', 127: '#4B1502'}

    HEARTBEAT_STEP = 10
    PERIODIC_PLAYBACK_INTERVAL = 3  # in seconds
    LOGO_DURATION_MS = 2000  # How long the dot2 logo stays on the pads at startup

    DEVICE_IDS = (1, 2)
    DATA_FILEPATH = str(BUNDLED_PROFILE_PATH)  # Replaced by the profile given to setup() / load_profile()

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
        self.cc_fader_index_dictionary_device1 = {}
        self.cc_fader_index_dictionary_device2 = {}
        self.fader_last_value_dictionary_device1 = {}
        self.fader_last_value_dictionary_device2 = {}

        self.default_brightness_level = 6
        self.default_blink_channel = 10
        self.config_mode = 0

        # Dot2 connection info (populated by load_json)
        self.host = "10.0.0.50"
        self.plaintext_password = "1"

        self.dot2_ws = None
        self._playback_poll_thread = None

        # Config mode: True while the executor/label prompts are open, so pad presses are ignored meanwhile
        self._link_in_progress = False
        # Config mode: the link waiting for the user to press a color on the palette (dict) or None
        self._pending_color_link = None
        # Config mode: (device_id, cc) -> time of the last message received from that fader
        self._fader_last_config_touch = {}

        # GUI
        self.gui_instance = None
        self._hotkey_dispatcher = None

# =================================================================
#                         Tools / Utils
# =================================================================

    def invert_devices(self):
        (self.midi_inport_device1, self.midi_inport_device2) = \
            (self.midi_inport_device2, self.midi_inport_device1)
        (self.midi_outport_device1, self.midi_outport_device2) = \
            (self.midi_outport_device2, self.midi_outport_device1)

        self.inverted_devices = not self.inverted_devices
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
            os.path.dirname(os.path.abspath(self.DATA_FILEPATH)), "../backups"
        )
        last_backup = self.get_last_backup(backup_directory_path)

        if not last_backup:
            input_prompts.show_info("No backup found to restore.", parent=self.gui_instance)
            return

        if not self._confirm_destructive_action(
            "Are you sure you want to load the last backup?\n"
            "YOUR CURRENT COLORS WILL BE OVERWRITTEN."
        ):
            return

        shutil.copy2(last_backup, self.DATA_FILEPATH)

        self.load_json()
        self.update_colors()

    def _confirm_destructive_action(self, warning_prompt):
        """Yes/No question then a typed "CONFIRM". Returns True only if both steps pass."""
        return input_prompts.confirm_destructive_action(warning_prompt, parent=self.gui_instance)

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

    def initiate_last_value_dictionary(self):
        self.fader_last_value_dictionary_device1 = {cc: 0.0 for cc in self.cc_fader_index_dictionary_device1}
        self.fader_last_value_dictionary_device2 = {cc: 0.0 for cc in self.cc_fader_index_dictionary_device2}

    def _note_dictionaries_by_device(self):
        """{device_id: note -> executor dictionary} for both controllers."""
        return {1: self.note_executor_dictionary_device1, 2: self.note_executor_dictionary_device2}

# =================================================================
#                            GUI Actions
# =================================================================

    def send_gui_instance(self, gui_instance):
        self.gui_instance = gui_instance

    def ask_labels(self):
        """Asks the short then the long label. Returns (None, None) if the short label prompt is cancelled."""
        short_label = input_prompts.ask_text('Please input the "Short" label', parent=self.gui_instance)
        if short_label is None:
            return None, None
        long_label = input_prompts.ask_text('Please input the "Long" label', parent=self.gui_instance)
        if not long_label:
            long_label = short_label
        return short_label, long_label

    def load_labels(self):
        """Shows the labels of the current profile on the GUI pads of both wings."""
        for device_id, note_dictionary in self._note_dictionaries_by_device().items():
            for button_id, entry in note_dictionary.items():
                short_label = entry.get("short_label")
                if short_label is None:
                    continue
                long_label = entry.get("long_label") or short_label
                self.set_button_label(button_id=button_id, device_id=device_id,
                                      short_label=short_label, long_label=long_label)

    def set_button_label(self, button_id, device_id, short_label, long_label):
        self.gui_instance.set_button_label(button_id=int(button_id),
                                           device_id=int(device_id),
                                           short_label=short_label,
                                           long_label=long_label
                                           )

    def set_gui_button_color(self, button_id, device_id, color_note):
        self.gui_instance.set_button_color(button_id=int(button_id),
                                           device_id=int(device_id),
                                           hex_color=self.get_hex_color_from_note(note=color_note))

    def set_gui_fader_value(self, fader_id, device_id, value):
        self.gui_instance.set_fader_value(fader_id=fader_id,
                                          device_id=device_id,
                                          value=value)

    def update_gui_button_colors(self):
        """Updates all colors of the pad including special buttons."""
        note_executor_dictionaries = [
            self.note_executor_dictionary_device1,
            self.note_executor_dictionary_device2,
        ]

        for device in range(2):
            for button_note, entry in note_executor_dictionaries[device].items():
                color = entry["color"]
                if color < 0 or int(button_note) == self.SHIFT_KEY:
                    self.set_gui_button_color(button_id=button_note,
                                              device_id=device + 1,
                                              color_note=3)

                if int(button_note) in self.NORMAL_BUTTON_NOTES:
                    self.set_gui_button_color(button_id=button_note,
                                               device_id=device + 1,
                                               color_note=color)

                elif int(button_note) in self.SPECIAL_BUTTON_NOTES:
                    # Channel 0 is the only channel that should be used with special buttons
                    self.set_gui_button_color(button_id=button_note,
                                               device_id=device + 1,
                                               color_note=21 if int(button_note) > 111 else 5)
        self.gui_instance.refresh_gui()

    def set_temp_gui_button_color(self, button_id, device_id, hex_color):
        self.gui_instance.set_temp_button_color(button_id=button_id, device_id=device_id, hex_color=hex_color)

    def restore_permanent_gui_button_color(self, button_id, device_id):
        self.gui_instance.restore_permanent_button_color(button_id=int(button_id), device_id=int(device_id))

    def show_color_gui_palette(self):
        self.gui_instance.set_blank_gui()
        for pad in range(len(self.BUTTON_COLORS_DEVICE1)):
            color = self.get_hex_color_from_note(self.BUTTON_COLORS_DEVICE1[pad])
            self.set_temp_gui_button_color(
                button_id=pad,
                device_id=1,
                hex_color=color
            )

        for pad in range(len(self.BUTTON_COLORS_DEVICE2)):
            color = self.get_hex_color_from_note(self.BUTTON_COLORS_DEVICE2[pad])
            self.set_temp_gui_button_color(
                button_id=pad,
                device_id=2,
                hex_color=color
            )

        for pad in self.SPECIAL_BUTTON_NOTES:
            self.set_temp_gui_button_color(
                button_id=pad,
                device_id=1,
                hex_color='#FFFFFF'
            )
            self.set_temp_gui_button_color(
                button_id=pad,
                device_id=2,
                hex_color='#FFFFFF'
            )

        #shift key
        self.set_temp_gui_button_color(
            button_id=self.SHIFT_KEY,
            device_id=1,
            hex_color='#FFFFFF'
        )
        self.set_temp_gui_button_color(
            button_id=self.SHIFT_KEY,
            device_id=2,
            hex_color='#FFFFFF'
        )
        self.gui_instance.refresh_gui()

    def restore_all_permanent_gui_button_colors(self):
        self.gui_instance.restore_all_permanent_gui_button_colors()

    def toggle_check_menu_button(self):
        self.gui_instance.toggle_check_menu_button(menu_id="tools", button_id="config_mode")

    def clear_all_colors(self):
        """Turns off every pad of both controllers and removes the colors and labels of the GUI."""
        self.turn_off_pad()
        self.gui_instance.clear_all_buttons()

# =================================================================
#                            JSON
# =================================================================

    def load_profile(self, profile_path):
        """
        Replaces the current profile by the given file.

        The file is validated first, so a bad file leaves everything untouched
        (profile_manager.ProfileError is raised). Then the pads and the GUI are
        cleared, the new data is applied and its colors and labels are shown.
        """
        data = profile_manager.read_profile(profile_path)

        self._pending_color_link = None  # A half-done config mode link belongs to the old profile
        self.clear_all_colors()
        self.DATA_FILEPATH = profile_path
        self._apply_profile_data(data)
        self._sync_defaults_with_open_ports()
        self.initiate_executor_note_dictionary()
        self.initiate_last_value_dictionary()
        self.update_colors()
        self.load_labels()

    def load_json(self):
        """Re-reads the current profile file (used after it was modified on disk)."""
        config_mode = self.config_mode  # Runtime state: re-reading must not switch config mode off mid-session
        self._apply_profile_data(self._read_data_file())
        self.config_mode = config_mode

    def read_current_profile(self):
        """Content of the current profile file as a dictionary."""
        return self._read_data_file()

    def _apply_profile_data(self, data):
        """Copies the content of a profile dictionary into the controller attributes."""
        self.note_executor_dictionary_device1 = data["note_executor_dictionary_device1"]
        self.note_executor_dictionary_device2 = data["note_executor_dictionary_device2"]
        self.cc_fader_index_dictionary_device1 = data["cc_fader_index_dictionary_device1"]
        self.cc_fader_index_dictionary_device2 = data["cc_fader_index_dictionary_device2"]
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

    def append_note_to_json(self, note, executor_index, device_id, short_label, long_label, color=None):
        data = self._read_data_file()

        entry = {"executor_index": executor_index}
        if color is not None:
            entry["color"] = color
        if short_label is not None:
            entry["short_label"] = short_label
        if long_label is not None:
            entry["long_label"] = long_label
        else:
            entry["long_label"] = short_label


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

    def append_cc_to_json(self, cc, note, device_id):
        data = self._read_data_file()

        if device_id == 1:
            data["cc_fader_index_dictionary_device1"][str(cc)] = note
        elif device_id == 2:
            data["cc_fader_index_dictionary_device2"][str(cc)] = note

        data["cc_fader_index_dictionary_device1"] = dict(
            sorted(data["cc_fader_index_dictionary_device1"].items(), key=lambda x: int(x[0]))
        )
        data["cc_fader_index_dictionary_device2"] = dict(
            sorted(data["cc_fader_index_dictionary_device2"].items(), key=lambda x: int(x[0]))
        )

        self._write_data_file(data)

    def set_default_devices(self, device1_input="", device1_output="", device2_input="", device2_output=""):
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

    def set_dot2_settings(self, host, password):
        """Changes the console address and password, and saves them in the current profile."""
        self.host = host
        self.plaintext_password = password

        data = self._read_data_file()
        data["default_ip_address"] = host
        data["dot2_password"] = password
        self._write_data_file(data)

    def toggle_config_mode(self):
        self.config_mode = not self.config_mode
        # Keeps the Tools > Config Mode checkmark right when F2 is used (setChecked does not re-trigger the action)
        self.gui_instance.menu["tools"]["config_mode"].setChecked(bool(self.config_mode))

        if self.config_mode:
            self.flash_color(2, 5)
        else:
            self._pending_color_link = None  # Leaving config mode abandons a link waiting for its color
            self.flash_color(2, 21)

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
        backup_directory_path = os.path.join(base_dir, "../backups")
        backup_filepath = os.path.join(backup_directory_path, f"data_backup_{timestamp}.json")

        os.makedirs(backup_directory_path, exist_ok=True)
        shutil.copy2(self.DATA_FILEPATH, backup_filepath)

    def link_executor_note(self, note, device_id):
        """
        Config mode, step 1: asks the executor (for unmapped pads) and the labels.
        Normal pads then wait for a color to be pressed on the palette (step 2,
        see _finish_color_pick) without blocking the window. Special buttons are
        saved right away.
        """
        self._link_in_progress = True
        try:
            executor_index = self._ask_executor_index(note, device_id)
            if executor_index is None:
                return
            short_label, long_label = self.ask_labels()
        finally:
            self._link_in_progress = False

        link = {"note": note, "device_id": device_id, "executor_index": executor_index,
                "short_label": short_label, "long_label": long_label}

        if note in self.NORMAL_BUTTON_NOTES:
            self._start_color_pick(link)
        elif note in self.SPECIAL_BUTTON_NOTES or note == self.SHIFT_KEY:
            self._save_link(link, color=1)

    def _ask_executor_index(self, note, device_id):
        """Executor already mapped to the pad, otherwise asks the user. None when cancelled."""
        note_dictionary = self._note_dictionaries_by_device()[device_id]
        if str(note) in note_dictionary:
            return note_dictionary[str(note)]["executor_index"]

        executor_id = input_prompts.ask_number("Please input the id of the executor",
                                               minimum=1, parent=self.gui_instance)
        return None if executor_id is None else executor_id - 1  # The dot2 counts executors from 0

    def _start_color_pick(self, link):
        """Shows the color palette on the pads and the GUI; the next pad pressed picks the color."""
        self._pending_color_link = link
        self.show_controller_color_palette()
        self.show_color_gui_palette()

    def _finish_color_pick(self, pressed_note, pressed_device_id):
        """Pressing a palette pad picks its color, any other button means "no color"."""
        link = self._pending_color_link
        self._pending_color_link = None

        if pressed_note in self.NORMAL_BUTTON_NOTES and pressed_note < len(self.BUTTON_COLORS_DEVICE1):
            palette = self.BUTTON_COLORS_DEVICE1 if pressed_device_id == 1 else self.BUTTON_COLORS_DEVICE2
            color = palette[pressed_note]
        else:
            color = -1
        self._save_link(link, color=color)

    def _save_link(self, link, color):
        """Writes the link to the profile and refreshes the pads, labels and blinking."""
        self.append_note_to_json(link["note"], link["executor_index"], device_id=link["device_id"], color=color,
                                 short_label=link["short_label"], long_label=link["long_label"])
        if link["short_label"] is not None:
            self.set_button_label(button_id=link["note"], device_id=link["device_id"],
                                  short_label=link["short_label"], long_label=link["long_label"])
        self.load_json()
        self.initiate_executor_note_dictionary()
        self.update_colors()

    def get_fader_index_from_cc(self, cc, device_id):
        if device_id == 1 and str(cc) in self.cc_fader_index_dictionary_device1.keys():
            return self.cc_fader_index_dictionary_device1[str(cc)]
        elif device_id == 2 and str(cc) in self.cc_fader_index_dictionary_device2.keys():
            return self.cc_fader_index_dictionary_device2[str(cc)]

    def _config_mode_fader_touched(self, cc, device_id):
        """
        A fader sends a stream of messages while it moves. Only the first message
        of a movement opens the prompt. The rest of that movement, and any message
        arriving within FADER_SETTLE_SECONDS after the prompt closes, is ignored.
        """
        if cc not in self.FADER_CONTROLS:
            return
        fader = (device_id, cc)
        now = time.monotonic()
        last_touch = self._fader_last_config_touch.get(fader)
        self._fader_last_config_touch[fader] = now
        if last_touch is not None and now - last_touch < self.FADER_SETTLE_SECONDS:
            return  # Same movement still going on

        self.link_cc_note(cc, device_id)
        # The settle delay starts when the prompt closes, the user may still be holding the fader
        self._fader_last_config_touch[fader] = time.monotonic()

    def link_cc_note(self, cc, device_id):
        """Config mode: asks which executor the fader controls and saves it in the profile."""
        current_index = self.get_fader_index_from_cc(cc, device_id)
        fader_number = cc - self.FIRST_FADER_CONTROL + 1

        self._link_in_progress = True  # Drops the messages the fader keeps sending while the prompt is open
        try:
            executor_id = input_prompts.ask_number(
                f"Fader {fader_number} of controller {device_id}: please input the id of the executor",
                minimum=1, default=None if current_index is None else current_index + 1,
                parent=self.gui_instance,
            )
        finally:
            self._link_in_progress = False
        if executor_id is None:
            return

        # Same convention as the pads: the user types the executor id, the dot2 counts from 0
        self.append_cc_to_json(cc=cc, note=executor_id - 1, device_id=device_id)
        self.load_json()
        self.initiate_last_value_dictionary()

    def get_hex_color_from_note(self, note):
        return self.NOTE_COLOR_MAP.get(int(note), None)

# =================================================================
#                            MIDI
# =================================================================

    # ---- Port bookkeeping (device 1 and 2 have separate attributes) ----

    def _get_device_ports(self, device_id):
        if device_id == 1:
            return self.midi_inport_device1, self.midi_outport_device1
        return self.midi_inport_device2, self.midi_outport_device2

    def _set_device_ports(self, device_id, inport, outport):
        if device_id == 1:
            self.midi_inport_device1, self.midi_outport_device1 = inport, outport
        else:
            self.midi_inport_device2, self.midi_outport_device2 = inport, outport

    def _get_default_port_names(self, device_id):
        if device_id == 1:
            return self.default_midi_inport_device1, self.default_midi_outport_device1
        return self.default_midi_inport_device2, self.default_midi_outport_device2

    def _set_default_port_names(self, device_id, input_name, output_name):
        if device_id == 1:
            self.default_midi_inport_device1, self.default_midi_outport_device1 = input_name, output_name
        else:
            self.default_midi_inport_device2, self.default_midi_outport_device2 = input_name, output_name

    def get_open_port_names(self, device_id):
        """Names of the MIDI ports currently open for a controller ("" when not open)."""
        inport, outport = self._get_device_ports(device_id)
        return (inport.name if inport is not None else "",
                outport.name if outport is not None else "")

    def _persist_default_ports(self):
        """Saves the current default port names in the profile."""
        self.set_default_devices(
            device1_input=self.default_midi_inport_device1,
            device2_input=self.default_midi_inport_device2,
            device1_output=self.default_midi_outport_device1,
            device2_output=self.default_midi_outport_device2,
        )

    def _sync_defaults_with_open_ports(self):
        """
        After switching profile, the ports already open stay in use and become
        the defaults of the new profile, so the next startup reuses them.
        """
        any_port_open = False
        for device_id in self.DEVICE_IDS:
            input_name, output_name = self.get_open_port_names(device_id)
            if input_name and output_name:
                self._set_default_port_names(device_id, input_name, output_name)
                any_port_open = True
        if any_port_open:
            self._persist_default_ports()

    # ---- Opening ports ----

    def _open_device_ports(self, device_id, input_name, output_name):
        """Closes the ports open for the controller, opens the given ones and makes them the defaults."""
        for port in self._get_device_ports(device_id):
            if port is not None:
                port.close()
        self._set_device_ports(device_id, None, None)

        inport = mido.open_input(input_name)
        outport = mido.open_output(output_name)
        self._set_device_ports(device_id, inport, outport)
        self._set_default_port_names(device_id, input_name, output_name)

    def select_midi_ports(self, parent=None):
        """
        Opens the saved ports of both controllers. When a saved port is not
        available (first run, controller unplugged...) the user picks one in a
        dialog, which can be cancelled to run without that controller.
        """
        available_inputs = mido.get_input_names()
        available_outputs = mido.get_output_names()

        for device_id in self.DEVICE_IDS:
            input_name, output_name = self._get_default_port_names(device_id)
            if input_name in available_inputs and output_name in available_outputs:
                self._open_device_ports(device_id, input_name, output_name)
            else:
                self.choose_ports_for_device(device_id, parent=parent, available_inputs=available_inputs,
                                             available_outputs=available_outputs, persist=False)

            # A port taken by the first controller is not offered to the second one
            opened_input, opened_output = self.get_open_port_names(device_id)
            if opened_input in available_inputs:
                available_inputs.remove(opened_input)
            if opened_output in available_outputs:
                available_outputs.remove(opened_output)

        self._persist_default_ports()
        print(
            f"Midi Device IN 1: {self.midi_inport_device1}\n"
            f"Midi Device IN 2: {self.midi_inport_device2}\n"
            f"MIDI Device OUT 1: {self.midi_outport_device1}\n"
            f"MIDI Device OUT 2: {self.midi_outport_device2}\n"
        )

    def choose_ports_for_device(self, device_id, parent=None, available_inputs=None,
                                available_outputs=None, persist=True):
        """
        Shows the port selection dialog for one controller, then opens the
        chosen ports and saves them as defaults. Returns False when cancelled.
        """
        if available_inputs is None:
            available_inputs = mido.get_input_names()
        if available_outputs is None:
            available_outputs = mido.get_output_names()

        current_input, current_output = self.get_open_port_names(device_id)
        if not current_input:
            current_input, current_output = self._get_default_port_names(device_id)

        choice = MidiPortDialog.ask_ports(device_id, available_inputs, available_outputs,
                                          current_input, current_output, parent=parent)
        if choice is None:
            return False

        input_name, output_name = choice
        self._open_device_ports(device_id, input_name, output_name)
        if persist:
            self._persist_default_ports()
        return True

    def flash_color(self, duration, color):
        """Lights every pad with color for duration seconds, then restores the colors. Does not block the GUI."""
        self.set_all_pads(velocity=color, channel=11)
        QTimer.singleShot(int(duration * 1000), self.update_colors)

    def set_all_pads(self, velocity=0, channel=None):
        channel = self.default_brightness_level if channel is None else channel
        for pad in self.NORMAL_BUTTON_NOTES:
            self.send_midi_message(midi_message_type="note_on", channel=channel, note=pad, velocity=velocity)

    def send_midi_message(self, midi_message_type, channel, note, velocity, device_id=3):
        """Sends a note message to device 1, 2 or both (device_id=3). Controllers that are not open are skipped."""
        midi_message = mido.Message(
            type=str(midi_message_type), channel=int(channel), note=int(note), velocity=int(velocity)
        )
        for outport in self._outports_for(device_id):
            if outport is not None:
                outport.send(midi_message)

    def _outports_for(self, device_id):
        if device_id == 1:
            return (self.midi_outport_device1,)
        if device_id == 2:
            return (self.midi_outport_device2,)
        return (self.midi_outport_device1, self.midi_outport_device2)

    def show_controller_color_palette(self):
        self.turn_off_pad()
        for pad in range(len(self.BUTTON_COLORS_DEVICE1)):
            color = self.BUTTON_COLORS_DEVICE1[pad]
            self.send_midi_message(
                midi_message_type='note_on',
                channel=self.default_brightness_level,
                note=pad,
                velocity=color,
                device_id=1
            )

        for pad in range(len(self.BUTTON_COLORS_DEVICE2)):
            color = self.BUTTON_COLORS_DEVICE2[pad]
            self.send_midi_message(
                midi_message_type='note_on',
                channel=self.default_brightness_level,
                note=pad,
                velocity=color,
                device_id=2
            )

        for pad in self.SPECIAL_BUTTON_NOTES:
            self.send_midi_message(
                midi_message_type='note_on',
                channel=0,
                note=pad,
                velocity=0,
                device_id=3
            )

    def turn_off_pad(self):
        self.set_all_pads(0, 6)

        for pad in self.SPECIAL_BUTTON_NOTES:
            self.send_midi_message(midi_message_type='note_on', channel=0, note=pad, velocity=0)

    def update_colors(self):
        self.update_controller_colors()
        self.update_gui_button_colors()

    def update_controller_colors(self):
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
        if self.dot2_ws is not None:
            self.dot2_ws.poll_exec_state()

    def dot2_logo(self):
        self.set_all_pads(109, 6)
        self.set_colors((8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 23, 28, 37, 38, 47, 51, 55, 60, 61, 62), 3, 2)
        self.set_colors((8, 11, 13, 14, 15, 16, 19, 22, 24, 25, 26, 27, 30, 32, 35, 38, 40, 43, 45, 46, 47), 3, 1)


    def control_change_handler(self, cc, value, device_id):
        fader_index = self.get_fader_index_from_cc(cc, device_id)
        self.set_gui_fader_value(fader_id=cc, device_id=device_id, value=value)
        value = round(value/127, 2) # Dot2 takes a 0-1 float, not a 0-127 int like the gui and midi
        last_value_dict = self.fader_last_value_dictionary_device1 if device_id == 1 else self.fader_last_value_dictionary_device2
        last_fader_value = last_value_dict[str(cc)]

        if last_fader_value != value:
            self.dot2_ws.send_playback_fader(fader_index=fader_index, fader_value=value)
            last_value_dict[str(cc)] = value

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

        if old_exec_states == current_running_execs:
            return  # No need to continue if they're the same

        # Symmetric difference: only keep the executors whose state changed
        old_current_symmetry = old_exec_states ^ current_running_execs

        for executor in old_current_symmetry:
            turned_on = executor in current_running_execs
            # Executors running on the console but mapped to no pad are simply ignored
            for note, device_id in self.executor_note_dictionary.get(executor, []):
                self.toggle_blink_note(note, device_id, turned_on)

        self.executor_states = current_running_execs
        self.temporary_exec_states = set()

    def periodic_playback_poll(self):
        while True:
            time.sleep(self.PERIODIC_PLAYBACK_INTERVAL)
            self.dot2_ws.poll_exec_state()

    def imitate_midi_message(self, device_id, type, channel, note=None, velocity=None, cc=None, value=None):
        if type == "control_change":
            midi_message = mido.Message(type=type, channel=int(channel), control=int(cc), value=int(value))
        elif type == "note_on" or type == "note_off":
            midi_message = mido.Message(type=type, channel=int(channel), note=int(note), velocity=int(velocity))
        else:
            return
        self.note_loop(midi_message, device_id)

    def fader_button_handler(self, cc, device_id, pressed):
        executor_index = self.get_fader_index_from_cc(cc, device_id)
        if executor_index is None:
            return  # Fader not bound to an executor yet
        self.dot2_ws.send_playback_click(executor_index=executor_index, button_id=1, pressed=pressed)

    def note_loop(self, message, device_id):
        # Config mode: while the prompts are open every message is dropped (the prompts are modal,
        # but MIDI keeps being polled), and while the palette is shown only the next press counts.
        if self._link_in_progress:
            return
        if self._pending_color_link is not None:
            if message.type == "note_on":
                self._finish_color_pick(message.note, device_id)
            return

        if message.type == "control_change":
            if self.config_mode:
                self._config_mode_fader_touched(message.control, device_id)
                return

            cc_note_dict = (
                self.cc_fader_index_dictionary_device1 if device_id == 1
                else self.cc_fader_index_dictionary_device2
            )

            if str(message.control) in cc_note_dict:
                self.control_change_handler(cc=message.control, value=message.value, device_id=device_id)

        elif message.type == "note_on" or message.type == "note_off":
            note = message.note
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
    # TODO gui button state

# =================================================================
#                         Dot2 connection
# =================================================================

    def setup_dot2_handler(self):
        """Creates the websocket handler (without connecting) and registers the playback callback."""
        self.dot2_ws = Dot2WebSocketHandler(
            host=self.host,
            password=self.plaintext_password,
            heartbeat_step=self.HEARTBEAT_STEP,
            debug=True,
        )
        self.dot2_ws.on("playbacks", self.handle_playbacks)

    def start_dot2_connection(self):
        """Starts connecting to the console in the background; follow it with dot2_connection_status()."""
        self.dot2_ws.connect()

    def restart_dot2_connection(self):
        """Drops the current connection (if any) and connects again with the current host and password."""
        self.dot2_ws.disconnect()
        self.dot2_ws.update_credentials(host=self.host, password=self.plaintext_password)
        self.dot2_ws.connect()

    def dot2_connection_status(self):
        """See Dot2WebSocketHandler.connection_status()."""
        return self.dot2_ws.connection_status()

    def dot2_settings_changed(self):
        """True when the host or password in use differ from the websocket's (ex: another profile was loaded)."""
        return (self.dot2_ws.HOST != self.host
                or self.dot2_ws.PLAINTEXT_PASSWORD != self.plaintext_password)

# =================================================================
#                      Setup / Run / Lifecycle
# =================================================================

    def setup(self, profile_path, parent_widget=None):
        """
        Loads the profile, opens the MIDI ports (asking the user when a saved
        port is missing), shows the logo on the pads and prepares the dot2
        handler. The connection itself is started with start_dot2_connection().
        """
        self.load_profile(profile_path)
        self.select_midi_ports(parent=parent_widget)
        self.dot2_logo()
        QTimer.singleShot(self.LOGO_DURATION_MS, self.update_colors)

        self.setup_dot2_handler()
        self._register_hotkeys()
        self._start_playback_poll_thread()

    def _start_playback_poll_thread(self):
        self._playback_poll_thread = threading.Thread(
            target=self.periodic_playback_poll, daemon=True
        )
        self._playback_poll_thread.start()

    def _register_hotkeys(self):
        """
        Global hotkeys. The keyboard library calls them from its own thread, so
        each one is forwarded to the GUI thread, where widgets and dialogs are safe to use.
        """
        self._hotkey_dispatcher = GuiThreadDispatcher()
        on_gui_thread = self._hotkey_dispatcher.wrap
        keyboard.add_hotkey("F1", on_gui_thread(self.invert_devices))
        keyboard.add_hotkey("F2", on_gui_thread(self.toggle_config_mode))
        keyboard.add_hotkey("F11", on_gui_thread(self.restore_last_backup))
        keyboard.add_hotkey("F12", on_gui_thread(self.remove_color_from_data))

    def shutdown(self):
        """Closes the dot2 connection, turns the pads off and closes the MIDI ports. Called when the app quits."""
        if self.dot2_ws is not None:
            self.dot2_ws.disconnect()
        self.turn_off_pad()
        for device_id in self.DEVICE_IDS:
            for port in self._get_device_ports(device_id):
                if port is not None:
                    port.close()
            self._set_device_ports(device_id, None, None)

    def poll(self):
        """Polls the open controllers for messages and handles them"""
        for device_id in self.DEVICE_IDS:
            inport, _ = self._get_device_ports(device_id)
            if inport is None:
                continue
            for msg in inport.iter_pending():
                self.note_loop(msg, device_id=device_id)