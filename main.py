"""Entry point: builds the main window and the MidiController, then starts the Qt event loop."""
import os
import shutil
import sys
from functools import partial

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from packages import profile_manager
from packages.app_info import (APP_NAME, BUNDLED_PROFILE_PATH, CONFIGURING_AM_I_DOT2_URL,
                               GITHUB_PAGE_URL, MANAGE_PROFILES_URL, open_in_browser)
from packages.app_settings import AppSettings
from packages.dialogs.connection_error_dialog import ask_retry_connection
from packages.dialogs.preferences_dialog import PreferencesDialog
from packages.dialogs.profiles_dialog import ProfilesDialog
from packages.error_handler import install_global_exception_hook, show_error
from packages.gui_main_window import Ui_MainWindow
from packages.midi_controller import MidiController
from packages.profile_manager import (DEFAULT_PROFILE_FILENAME, NEW_PROFILE_FILENAME,
                                      PROFILE_FILE_FILTER, ProfileError, profile_display_name)
from packages.version_checker import VersionChecker, show_update_dialog
from packages.web_socket_handler import STATUS_CONNECTED, STATUS_CONNECTING

POLLING_INTERVAL = 10  # Interval between midi polls in milliseconds
DOT2_CONNECTION_TIMEOUT_MS = 5000  # How long to wait for the console before offering to retry
DOT2_CONNECTION_POLL_MS = 250  # How often the connection progress is checked
STATUS_MESSAGE_MS = 5000  # How long temporary messages stay in the status bar

#TODO:
# Create an animation for toggled buttons in GUI
# Feedback from Dot2 for fader value
# Fix select_color for UI
# Make GUI to send commands
# Make device to use the GUI
# Make GUi for every window, like playbacks, groups, commands...

class MainApp(QMainWindow):
    def __init__(self, settings=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._base_window_title = self.windowTitle()

        self.wing1_buttons = {0: self.ui.button0_4, 1: self.ui.button1_4, 2: self.ui.button2_4, 3: self.ui.button3_4, 4: self.ui.button4_4, 5: self.ui.button5_4, 6: self.ui.button6_4, 7: self.ui.button7_4, 8: self.ui.button8_4, 9: self.ui.button9_4, 10: self.ui.button10_4, 11: self.ui.button11_4, 12: self.ui.button12_4, 13: self.ui.button13_4, 14: self.ui.button14_4, 15: self.ui.button15_4, 16: self.ui.button16_4, 17: self.ui.button17_4, 18: self.ui.button18_4, 19: self.ui.button19_4, 20: self.ui.button20_4, 21: self.ui.button21_4, 22: self.ui.button22_4, 23: self.ui.button23_4, 24: self.ui.button24_4, 25: self.ui.button25_4, 26: self.ui.button26_4, 27: self.ui.button27_4, 28: self.ui.button28_4, 29: self.ui.button29_4, 30: self.ui.button30_4, 31: self.ui.button31_4, 32: self.ui.button32_4, 33: self.ui.button33_4, 34: self.ui.button34_4, 35: self.ui.button35_4, 36: self.ui.button36_4, 37: self.ui.button37_4, 38: self.ui.button38_4, 39: self.ui.button39_4, 40: self.ui.button40_4, 41: self.ui.button41_4, 42: self.ui.button42_4, 43: self.ui.button43_4, 44: self.ui.button44_4, 45: self.ui.button45_4, 46: self.ui.button46_4, 47: self.ui.button47_4, 48: self.ui.button48_4, 49: self.ui.button49_4, 50: self.ui.button50_4, 51: self.ui.button51_4, 52: self.ui.button52_4, 53: self.ui.button53_4, 54: self.ui.button54_4, 55: self.ui.button55_4, 56: self.ui.button56_4, 57: self.ui.button57_4, 58: self.ui.button58_4, 59: self.ui.button59_4, 60: self.ui.button60_4, 61: self.ui.button61_4, 62: self.ui.button62_4, 63: self.ui.button63_4, 100: self.ui.button100_4, 101: self.ui.button101_4, 102: self.ui.button102_4, 103: self.ui.button103_4, 104: self.ui.button104_4, 105: self.ui.button105_4, 106: self.ui.button106_4, 107: self.ui.button107_4, 112: self.ui.button112_4, 113: self.ui.button113_4, 114: self.ui.button114_4, 115: self.ui.button115_4, 116: self.ui.button116_4, 117: self.ui.button117_4, 118: self.ui.button118_4, 119: self.ui.button119_4, 122: self.ui.button122_4}
        self.wing2_buttons = {0: self.ui.button0_6, 1: self.ui.button1_6, 2: self.ui.button2_6, 3: self.ui.button3_6, 4: self.ui.button4_6, 5: self.ui.button5_6, 6: self.ui.button6_6, 7: self.ui.button7_6, 8: self.ui.button8_6, 9: self.ui.button9_6, 10: self.ui.button10_6, 11: self.ui.button11_6, 12: self.ui.button12_6, 13: self.ui.button13_6, 14: self.ui.button14_6, 15: self.ui.button15_6, 16: self.ui.button16_6, 17: self.ui.button17_6, 18: self.ui.button18_6, 19: self.ui.button19_6, 20: self.ui.button20_6, 21: self.ui.button21_6, 22: self.ui.button22_6, 23: self.ui.button23_6, 24: self.ui.button24_6, 25: self.ui.button25_6, 26: self.ui.button26_6, 27: self.ui.button27_6, 28: self.ui.button28_6, 29: self.ui.button29_6, 30: self.ui.button30_6, 31: self.ui.button31_6, 32: self.ui.button32_6, 33: self.ui.button33_6, 34: self.ui.button34_6, 35: self.ui.button35_6, 36: self.ui.button36_6, 37: self.ui.button37_6, 38: self.ui.button38_6, 39: self.ui.button39_6, 40: self.ui.button40_6, 41: self.ui.button41_6, 42: self.ui.button42_6, 43: self.ui.button43_6, 44: self.ui.button44_6, 45: self.ui.button45_6, 46: self.ui.button46_6, 47: self.ui.button47_6, 48: self.ui.button48_6, 49: self.ui.button49_6, 50: self.ui.button50_6, 51: self.ui.button51_6, 52: self.ui.button52_6, 53: self.ui.button53_6, 54: self.ui.button54_6, 55: self.ui.button55_6, 56: self.ui.button56_6, 57: self.ui.button57_6, 58: self.ui.button58_6, 59: self.ui.button59_6, 60: self.ui.button60_6, 61: self.ui.button61_6, 62: self.ui.button62_6, 63: self.ui.button63_6, 100: self.ui.button100_6, 101: self.ui.button101_6, 102: self.ui.button102_6, 103: self.ui.button103_6, 104: self.ui.button104_6, 105: self.ui.button105_6, 106: self.ui.button106_6, 107: self.ui.button107_6, 112: self.ui.button112_6, 113: self.ui.button113_6, 114: self.ui.button114_6, 115: self.ui.button115_6, 116: self.ui.button116_6, 117: self.ui.button117_6, 118: self.ui.button118_6, 119: self.ui.button119_6, 122: self.ui.button122_6}
        self.wing1_faders = {48: self.ui.fader48_4, 49: self.ui.fader49_4, 50: self.ui.fader50_4, 51: self.ui.fader51_4, 52: self.ui.fader52_4, 53: self.ui.fader53_4, 54: self.ui.fader54_4, 55: self.ui.fader55_4, 56: self.ui.fader56_4}
        self.wing2_faders = {48: self.ui.fader48_6, 49: self.ui.fader49_6, 50: self.ui.fader50_6, 51: self.ui.fader51_6, 52: self.ui.fader52_6, 53: self.ui.fader53_6, 54: self.ui.fader54_6, 55: self.ui.fader55_6, 56: self.ui.fader56_6}
        self.wing1_fader_buttons = {48: self.ui.pushButton_fader48_4, 49: self.ui.pushButton_fader49_4, 50: self.ui.pushButton_fader50_4, 51: self.ui.pushButton_fader51_4, 52: self.ui.pushButton_fader52_4, 53: self.ui.pushButton_fader53_4, 54: self.ui.pushButton_fader54_4, 55: self.ui.pushButton_fader55_4, 56: self.ui.pushButton_fader56_4}
        self.wing2_fader_buttons = {48: self.ui.pushButton_fader48_6, 49: self.ui.pushButton_fader49_6, 50: self.ui.pushButton_fader50_6, 51: self.ui.pushButton_fader51_6, 52: self.ui.pushButton_fader52_6, 53: self.ui.pushButton_fader53_6, 54: self.ui.pushButton_fader54_6, 55: self.ui.pushButton_fader55_6, 56: self.ui.pushButton_fader56_6}
        self.menu = {
            "file":{
                "new_file": self.ui.actionNewFile,
                "open_file": self.ui.actionOpenFile,
                "quit_app": self.ui.actionQuitApp
            },
            "wings": {
                "view_wing1": self.ui.actionViewWing1,
                "view_wing2": self.ui.actionViewWing2,
                "toggle_wing1": self.ui.actionWing_1_Enabled,
                "toggle_wing2": self.ui.actionWing_2_Enabled
            },
            "settings": {
                "preferences": self.ui.actionPreferences,
                "profiles": self.ui.actionProfiles
            },
            "tools": {
                "refresh_gui": self.ui.actionRefresh_GUI,
                "refresh_profile": self.ui.actionRefresh_Profile,
                "config_mode": self.ui.actionConfig_Mode
            },
            "help": {
                "github_page": self.ui.actionGithub,
                "configuring_am_i_dot2": self.ui.actionConfiguring_Am_I_Dot_2,
                "manage_profiles": self.ui.actionCreate_a_profile,
                "contact_help": self.ui.actionContact_Help
            }
        }

        # Settings live outside the app folder (see AppSettings) and tell us which profile to open
        self.settings = settings if settings is not None else AppSettings().load()

        self.controller = MidiController()
        self.controller.send_gui_instance(gui_instance=self)
        self.controller.setup(self._resolve_startup_profile(), parent_widget=self)
        self._remember_current_profile()

        self.menu_actions = self._build_menu_actions()
        self.assign_callbacks()
        self.resize_to_maximized()

        self.midi_timer = QTimer()
        self.midi_timer.timeout.connect(self.controller.poll)
        self.midi_timer.start(POLLING_INTERVAL)

        self._dot2_connection_timer = QTimer(self)
        self._dot2_connection_timer.timeout.connect(self._poll_dot2_connection)
        self._dot2_connection_wait_ms = 0

        self.version_checker = VersionChecker()
        self.version_checker.update_available.connect(self._on_update_available)

    def start(self):
        """Background work that should only begin once the window is shown."""
        self.start_dot2_connection()
        self.version_checker.check_in_background()

    # =================================================================
    #                          GUI helpers
    # =================================================================

    @staticmethod
    def invert_hex_color(hex_color: str) -> str:
        """
        Takes a hex color string (e.g. "#RRGGBB" or "RRGGBB")
        and returns the inverted hex color.
        """
        hex_color = hex_color.lstrip("#")

        if len(hex_color) != 6:
            raise ValueError(f"Invalid hex color: {hex_color}")

        r = 255 - int(hex_color[0:2], 16)
        g = 255 - int(hex_color[2:4], 16)
        b = 255 - int(hex_color[4:6], 16)

        return f"#{r:02X}{g:02X}{b:02X}"

    @staticmethod
    def _repolish(widget):
        """Forces Qt to re-apply the stylesheet of a widget after it changed."""
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def _all_buttons(self):
        """(note, button) pairs of both wings."""
        return list(self.wing1_buttons.items()) + list(self.wing2_buttons.items())

    @staticmethod
    def get_button_background_color(button):
        return button.property("bg_color")

    def get_button_instance(self, button_id, device_id):
        return self.wing1_buttons[int(button_id)] if device_id == 1 else self.wing2_buttons[int(button_id)]

    def get_fader_instance(self, fader_id, device_id):
        return self.wing1_faders[int(fader_id)] if device_id == 1 else self.wing2_faders[int(fader_id)]

    def set_fader_value(self, fader_id, device_id, value):
        fader = self.get_fader_instance(fader_id, device_id)
        fader.setValue(value)

    #TODO
    def toggle_button_blink(self):
        pass

    def set_button_label(self, button_id, device_id, short_label, long_label):
        button = self.get_button_instance(button_id, device_id)
        button.setText(short_label)
        button.setToolTip(long_label)
        bg_color = self.get_button_background_color(button)
        if bg_color is not None:
            inverted_color = self.invert_hex_color(bg_color)
            button.setStyleSheet(f"color: {inverted_color}; background-color: {bg_color};")
        if button.toolTipDuration() != 0:
            button.setToolTipDuration(0)

    def set_button_color(self, button_id, device_id, hex_color):
        if hex_color is None:
            return
        button = self.get_button_instance(button_id, device_id)
        button.setStyleSheet(f"background-color: {hex_color};")
        button.setProperty("bg_color", hex_color) # to easily get the color later on
        self._repolish(button)

    def set_temp_button_color(self, button_id, device_id, hex_color):
        if hex_color is None:
            return
        button = self.get_button_instance(button_id, device_id)
        button.setStyleSheet(f"background-color: {hex_color};")
        self._repolish(button)

    def restore_permanent_button_color(self, button_id, device_id):
        button = self.get_button_instance(button_id, device_id)
        hex_color = button.property("bg_color")
        button.setStyleSheet(f"background-color: {hex_color};")
        self._repolish(button)

    def refresh_gui(self):
        for _, button in self._all_buttons():
            self._repolish(button)

    def clear_all_buttons(self):
        """Removes colors, labels and tooltips from every pad of both wings (done before loading another profile)."""
        for note, button in self._all_buttons():
            button.setText(str(note))
            button.setToolTip("")
            button.setProperty("bg_color", None)
            button.setStyleSheet("")
            self._repolish(button)

    def toggle_view_wing(self, wing_id):
        if wing_id == 1:
            if self.wing_shown(wing_id):
                self.ui.wing_1.hide()
            else:
                self.ui.wing_1.show()
        elif wing_id == 2:
            if self.wing_shown(wing_id):
                self.ui.wing_2.hide()
            else:
                self.ui.wing_2.show()
        self.resize_to_smallest_size()

    def wing_shown(self, wing_id):
        # isHidden() and not isVisible(): isVisible() is also False while the whole window is minimized
        return not (self.ui.wing_1 if wing_id == 1 else self.ui.wing_2).isHidden()

    def resize_to_smallest_size(self):
        """
        Shrinks the window around the wings that are still shown. Deferred to the next
        event loop turn because Qt only recalculates the layout after hide()/show() returns;
        resizing right away would still measure the old layout.
        """
        QTimer.singleShot(0, self._shrink_to_content)

    def resize_to_maximized(self):
        """
        Shrinks/Expands the window to fill the screen. Stills shows the taskbar and title bar
        """
        QTimer.singleShot(0, self._set_window_maximized)

    def _set_window_maximized(self):
        self.showMaximized()

    def _shrink_to_content(self):
        if self.isMaximized() or self.isFullScreen():
            self.showNormal()  # A maximized window ignores resize()
        # Both layouts must be recalculated: the window's own layout is what sets the window's
        # minimum size, and resize() never goes below it (it would stay at the two-wing width).
        self.centralWidget().layout().activate()
        self.layout().activate()
        self.resize(self.minimumSizeHint())

    def toggle_check_menu_button(self, menu_id, button_id):
        menu_action = self.menu[menu_id][button_id]
        if menu_action.isCheckable():
            state = menu_action.isChecked()
            menu_action.setChecked(not state)

    def set_blank_gui(self):
        for _, button in self._all_buttons():
            button.setStyleSheet('background-color: "FFFFFF";')
            self._repolish(button)

    def restore_all_permanent_gui_button_colors(self):
        for button in range(len(self.wing1_buttons)-1):
            self.restore_permanent_button_color(button, device_id=1)
            self.restore_permanent_button_color(button, device_id=2)

    # =================================================================
    #                          Profiles
    # =================================================================

    def _resolve_startup_profile(self):
        """
        Path of the profile to load at startup: the last one used if it still
        exists, else the default profile of the profiles folder (created from
        the data.json shipped with the app when there is none yet). An invalid
        file is reported to the user and replaced by a blank profile.
        """
        candidate = self.settings.last_profile_path
        if not (candidate and os.path.isfile(candidate)):
            candidate = self._create_default_profile_if_missing()

        problem = profile_manager.check_profile_file(candidate)
        if problem is None:
            return candidate

        fallback = profile_manager.unique_profile_path(self.settings.profiles_folder, NEW_PROFILE_FILENAME)
        profile_manager.create_blank_profile(fallback)
        show_error(f'The profile "{candidate}" could not be loaded:\n{problem}\n\n'
                   f'A blank profile has been created instead:\n{fallback}',
                   title="Profile error", parent=self)
        return fallback

    def _create_default_profile_if_missing(self):
        """Makes sure <profiles folder>/default.json exists, seeding it from the app's data.json when possible."""
        os.makedirs(self.settings.profiles_folder, exist_ok=True)
        default_path = os.path.join(self.settings.profiles_folder, DEFAULT_PROFILE_FILENAME)
        if os.path.isfile(default_path):
            return default_path

        if BUNDLED_PROFILE_PATH.is_file():
            shutil.copy2(BUNDLED_PROFILE_PATH, default_path)
        else:
            profile_manager.create_blank_profile(default_path)
        return default_path

    def _remember_current_profile(self):
        """Saves the current profile as the one to reopen next time and shows its name in the title bar."""
        path = self.controller.DATA_FILEPATH
        self.settings.last_profile_path = path
        self._save_settings()
        self.setWindowTitle(f"{self._base_window_title} - {profile_display_name(path)}")

    def _save_settings(self):
        try:
            self.settings.save()
        except OSError as error:
            print(f"Warning: the settings could not be saved: {error}")

    def load_profile(self, path):
        """
        Loads a profile into the controllers and the GUI, then remembers it as
        the current one. Returns True on success, False if the file is not a
        valid profile (the user is told, nothing changes).
        """
        try:
            self.controller.load_profile(path)
        except ProfileError as error:
            show_error(f"The profile could not be opened:\n{path}\n\n{error}", title="Profile error", parent=self)
            return False

        self._remember_current_profile()
        self.ui.statusbar.showMessage(f"Profile loaded: {path}", STATUS_MESSAGE_MS)
        if self.controller.dot2_settings_changed():
            self.controller.restart_dot2_connection()
            self._watch_dot2_connection()
        return True

    def open_profile_from_explorer(self):
        """File > Open: picks a profile with the file explorer and loads it."""
        path, _ = QFileDialog.getOpenFileName(
            self, "Open a profile", self.settings.profiles_folder, PROFILE_FILE_FILTER
        )
        if path:
            self.load_profile(path)

    def create_new_profile_from_explorer(self):
        """
        File > New: picks a name with the file explorer, creates a blank profile
        (keeping the current console and MIDI settings) and loads it.
        """
        suggested_path = os.path.join(self.settings.profiles_folder, NEW_PROFILE_FILENAME)
        path, _ = QFileDialog.getSaveFileName(self, "Create a new profile", suggested_path, PROFILE_FILE_FILTER)
        if not path:
            return

        path = profile_manager.ensure_profile_extension(path)
        try:
            profile_manager.create_blank_profile(path, base_profile=self.controller.read_current_profile())
        except (OSError, ValueError) as error:
            show_error(f"The profile could not be created:\n{path}\n\n{error}", title="Profile error", parent=self)
            return
        self.load_profile(path)

    def open_profiles_window(self):
        """
        Settings > Profiles: choose the profiles folder, create/rename/delete profiles,
        and optionally switch to one of them.
        """
        dialog = ProfilesDialog(self.settings.profiles_folder,
                                current_profile_path=self.controller.DATA_FILEPATH,
                                base_profile=self._read_current_profile_or_none(), parent=self)
        accepted = bool(dialog.exec())
        folder, selected_profile = dialog.selected_folder, dialog.selected_profile_path
        loaded_profile_path = dialog.current_profile_path
        dialog.deleteLater()

        # Renames happen on disk right away, so follow them even if the dialog was cancelled
        if not profile_manager.is_same_file(loaded_profile_path, self.controller.DATA_FILEPATH):
            self.controller.DATA_FILEPATH = loaded_profile_path
            self._remember_current_profile()
        if not accepted:
            return

        self.settings.profiles_folder = folder
        self._save_settings()
        if selected_profile and not profile_manager.is_same_file(selected_profile, self.controller.DATA_FILEPATH):
            self.load_profile(selected_profile)

    def _read_current_profile_or_none(self):
        """Current profile data, or None if its file cannot be read (new profiles then use default settings)."""
        try:
            return self.controller.read_current_profile()
        except (OSError, ValueError):
            return None

    # =================================================================
    #                          Preferences
    # =================================================================

    def open_preferences_window(self):
        """Settings > Preferences: dot2 password and IP address, MIDI ports of both controllers."""
        dialog = PreferencesDialog(self.controller, parent=self)
        accepted = bool(dialog.exec())
        password, ip_address = dialog.password, dialog.ip_address
        dialog.deleteLater()
        if not accepted:
            return
        if (ip_address, password) == (self.controller.host, self.controller.plaintext_password):
            return  # Nothing changed, keep the current connection

        try:
            self.controller.set_dot2_settings(host=ip_address, password=password)
        except OSError as error:
            show_error(f"The preferences could not be saved in the profile:\n{error}",
                       title="Preferences error", parent=self)
            return
        self.controller.restart_dot2_connection()
        self._watch_dot2_connection()

    # =================================================================
    #                        Dot2 connection
    # =================================================================

    def start_dot2_connection(self):
        self.controller.start_dot2_connection()
        self._watch_dot2_connection()

    def _watch_dot2_connection(self):
        """Follows the connection progress with a timer, so the GUI never freezes while waiting."""
        self._dot2_connection_wait_ms = 0
        self.ui.statusbar.showMessage(f"Connecting to the dot2 at {self.controller.host}...")
        self._dot2_connection_timer.start(DOT2_CONNECTION_POLL_MS)

    def _poll_dot2_connection(self):
        self._dot2_connection_wait_ms += DOT2_CONNECTION_POLL_MS
        status = self.controller.dot2_connection_status()
        if status == STATUS_CONNECTING and self._dot2_connection_wait_ms < DOT2_CONNECTION_TIMEOUT_MS:
            return  # Still trying, check again later

        self._dot2_connection_timer.stop()
        if status == STATUS_CONNECTED:
            self.ui.statusbar.showMessage(f"Connected to the dot2 at {self.controller.host}")
            return

        self.ui.statusbar.showMessage("Not connected to the dot2")
        retry = ask_retry_connection(self.controller.host, status, DOT2_CONNECTION_TIMEOUT_MS // 1000, parent=self)
        if retry:
            self.controller.restart_dot2_connection()
            self._watch_dot2_connection()

    # =================================================================
    #                          Updates
    # =================================================================

    def _on_update_available(self, latest_version, release_url):
        show_update_dialog(latest_version, release_url, parent=self)

    # =================================================================
    #                          Tools/utils
    # =================================================================

    def exit_app(self):
        """File > Quit: closes the window, which ends the app (see closeEvent)."""
        self.close()

    def closeEvent(self, event):
        """Runs however the window is closed (Quit, window X button, Alt+F4): stops everything cleanly."""
        self.midi_timer.stop()
        self._dot2_connection_timer.stop()
        try:
            self.controller.shutdown()
        except Exception as error:  # An unplugged controller must not prevent quitting
            print(f"Error while shutting down: {error}")
        super().closeEvent(event)

    # =================================================================
    #                          Callbacks
    # =================================================================

    def assign_callbacks(self):
        # Button callback assignment
        for note, btn in self.wing1_buttons.items():
            btn.pressed.connect(partial(self._on_button_pressed, note=note, device_id=1))
            btn.released.connect(partial(self._on_button_released, note=note, device_id=1))
        for note, btn in self.wing2_buttons.items():
            btn.pressed.connect(partial(self._on_button_pressed, note=note, device_id=2))
            btn.released.connect(partial(self._on_button_released, note=note, device_id=2))

        # Fader callback assignment
        for cc, fader in self.wing1_faders.items():
            fader.valueChanged.connect(partial(self._on_fader_changed, cc=cc, device_id=1))
        for cc, fader in self.wing2_faders.items():
            fader.valueChanged.connect(partial(self._on_fader_changed, cc=cc, device_id=2))

        # Fader Button callback assignment
        for cc, fbtn in self.wing1_fader_buttons.items():
            fbtn.pressed.connect(partial(self._on_fader_button_pressed, cc=cc, device_id=1))
            fbtn.released.connect(partial(self._on_fader_button_released, cc=cc, device_id=1))
        for cc, fbtn in self.wing2_fader_buttons.items():
            fbtn.pressed.connect(partial(self._on_fader_button_pressed, cc=cc, device_id=2))
            fbtn.released.connect(partial(self._on_fader_button_released, cc=cc, device_id=2))

        # Menu button callback assignment
        for menu_id, menu_content in self.menu.items():
            for button_id, btn in menu_content.items():
                btn.triggered.connect(partial(self._on_menu_button_triggered, menu_id=menu_id, button_id=button_id))

    def _on_fader_changed(self, value, cc, device_id):
        self.controller.imitate_midi_message(
            type="control_change", channel=0, cc=cc, value=value, device_id=device_id)

    def _on_button_pressed(self, note, device_id):
        self.controller.imitate_midi_message(
            type="note_on", channel=0, note=note, velocity=127, device_id=device_id)

    def _on_button_released(self, note, device_id):
        self.controller.imitate_midi_message(
            type="note_off", channel=0, note=note, velocity=0, device_id=device_id)

    def _on_fader_button_pressed(self, cc, device_id):
        # This does not imitate a midi message because it is not a midi button, it's only GUI side
        self.controller.fader_button_handler(cc=cc, device_id=device_id, pressed=True)

    def _on_fader_button_released(self, cc, device_id):
        # This does not imitate a midi message because it is not a midi button, it's only GUI side
        self.controller.fader_button_handler(cc=cc, device_id=device_id, pressed=False)

    def _build_menu_actions(self):
        """(menu_id, button_id) -> what to do when that menu entry is triggered. Entries not listed here do nothing yet."""
        return {
            ("file", "new_file"): self.create_new_profile_from_explorer,
            ("file", "open_file"): self.open_profile_from_explorer,
            ("file", "quit_app"): self.exit_app,
            ("wings", "view_wing1"): partial(self.toggle_view_wing, wing_id=1),
            ("wings", "view_wing2"): partial(self.toggle_view_wing, wing_id=2),
            ("settings", "preferences"): self.open_preferences_window,
            ("settings", "profiles"): self.open_profiles_window,
            ("tools", "refresh_gui"): self.refresh_gui,
            ("tools", "config_mode"): self.controller.toggle_config_mode,
            ("help", "github_page"): partial(open_in_browser, GITHUB_PAGE_URL),
            ("help", "configuring_am_i_dot2"): partial(open_in_browser, CONFIGURING_AM_I_DOT2_URL),
            ("help", "manage_profiles"): partial(open_in_browser, MANAGE_PROFILES_URL),
        }

    def _on_menu_button_triggered(self, menu_id, button_id):
        action = self.menu_actions.get((menu_id, button_id))
        if action is not None:
            action()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    install_global_exception_hook()

    window = MainApp()
    window.show()
    window.start()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
