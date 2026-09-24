"""Entry point: sets up the MidiController and starts the main loop."""

from packages.midi_controller_handler import MidiControllerHandler
import sys
import re
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from packages.gui import Ui_MainWindow
from PySide6.QtCore import QTimer

POLLING_INTERVAL = 10  # Interval between midi polls in milliseconds

#TODO:
# 1. [DONE] Initiate button callbacks
# 2.        Make a function to handle fader buttons in midi controller and web socket handler
# 3. [DONE] Handle label changes for buttons (Short name: the one on the button, long name: the one in the tooltip, if no long name provided set it the same as short name)
# 4. [DONE] Handle background color changes for buttons
# 5.        Create an animation for toggled buttons in GUI
# 6. [DONE] Make a set_value function for GUI faders so that when physical faders are moved they move too
# 7.        Feedback from Dot2 for fader value
# 8. [DONE] Save label and color data
# 9. [DONE] Load label and color data
# 10.       Fix select_color for UI
# 11.       Have a black outline for text
# 12.       Make GUI to send commands
# 13.       Make device to use the GUI
# 14.       Make GUi for every window, like playbacks, groups, commands...
#TODO:

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.wing1_buttons = {0: self.ui.button0, 1: self.ui.button1, 2: self.ui.button2, 3: self.ui.button3, 4: self.ui.button4, 5: self.ui.button5, 6: self.ui.button6, 7: self.ui.button7, 8: self.ui.button8, 9: self.ui.button9, 10: self.ui.button10, 11: self.ui.button11, 12: self.ui.button12, 13: self.ui.button13, 14: self.ui.button14, 15: self.ui.button15, 16: self.ui.button16, 17: self.ui.button17, 18: self.ui.button18, 19: self.ui.button19, 20: self.ui.button20, 21: self.ui.button21, 22: self.ui.button22, 23: self.ui.button23, 24: self.ui.button24, 25: self.ui.button25, 26: self.ui.button26, 27: self.ui.button27, 28: self.ui.button28, 29: self.ui.button29, 30: self.ui.button30, 31: self.ui.button31, 32: self.ui.button32, 33: self.ui.button33, 34: self.ui.button34, 35: self.ui.button35, 36: self.ui.button36, 37: self.ui.button37, 38: self.ui.button38, 39: self.ui.button39, 40: self.ui.button40, 41: self.ui.button41, 42: self.ui.button42, 43: self.ui.button43, 44: self.ui.button44, 45: self.ui.button45, 46: self.ui.button46, 47: self.ui.button47, 48: self.ui.button48, 49: self.ui.button49, 50: self.ui.button50, 51: self.ui.button51, 52: self.ui.button52, 53: self.ui.button53, 54: self.ui.button54, 55: self.ui.button55, 56: self.ui.button56, 57: self.ui.button57, 58: self.ui.button58, 59: self.ui.button59, 60: self.ui.button60, 61: self.ui.button61, 62: self.ui.button62, 63: self.ui.button63, 100: self.ui.button100, 101: self.ui.button101, 102: self.ui.button102, 103: self.ui.button103, 104: self.ui.button104, 105: self.ui.button105, 106: self.ui.button106, 107: self.ui.button107, 112: self.ui.button112, 113: self.ui.button113, 114: self.ui.button114, 115: self.ui.button115, 116: self.ui.button116, 117: self.ui.button117, 118: self.ui.button118, 119: self.ui.button119, 122: self.ui.button122}
        self.wing2_buttons = {0: self.ui.button0_2, 1: self.ui.button1_2, 2: self.ui.button2_2, 3: self.ui.button3_2, 4: self.ui.button4_2, 5: self.ui.button5_2, 6: self.ui.button6_2, 7: self.ui.button7_2, 8: self.ui.button8_2, 9: self.ui.button9_2, 10: self.ui.button10_2, 11: self.ui.button11_2, 12: self.ui.button12_2, 13: self.ui.button13_2, 14: self.ui.button14_2, 15: self.ui.button15_2, 16: self.ui.button16_2, 17: self.ui.button17_2, 18: self.ui.button18_2, 19: self.ui.button19_2, 20: self.ui.button20_2, 21: self.ui.button21_2, 22: self.ui.button22_2, 23: self.ui.button23_2, 24: self.ui.button24_2, 25: self.ui.button25_2, 26: self.ui.button26_2, 27: self.ui.button27_2, 28: self.ui.button28_2, 29: self.ui.button29_2, 30: self.ui.button30_2, 31: self.ui.button31_2, 32: self.ui.button32_2, 33: self.ui.button33_2, 34: self.ui.button34_2, 35: self.ui.button35_2, 36: self.ui.button36_2, 37: self.ui.button37_2, 38: self.ui.button38_2, 39: self.ui.button39_2, 40: self.ui.button40_2, 41: self.ui.button41_2, 42: self.ui.button42_2, 43: self.ui.button43_2, 44: self.ui.button44_2, 45: self.ui.button45_2, 46: self.ui.button46_2, 47: self.ui.button47_2, 48: self.ui.button48_2, 49: self.ui.button49_2, 50: self.ui.button50_2, 51: self.ui.button51_2, 52: self.ui.button52_2, 53: self.ui.button53_2, 54: self.ui.button54_2, 55: self.ui.button55_2, 56: self.ui.button56_2, 57: self.ui.button57_2, 58: self.ui.button58_2, 59: self.ui.button59_2, 60: self.ui.button60_2, 61: self.ui.button61_2, 62: self.ui.button62_2, 63: self.ui.button63_2, 100: self.ui.button100_2, 101: self.ui.button101_2, 102: self.ui.button102_2, 103: self.ui.button103_2, 104: self.ui.button104_2, 105: self.ui.button105_2, 106: self.ui.button106_2, 107: self.ui.button107_2, 112: self.ui.button112_2, 113: self.ui.button113_2, 114: self.ui.button114_2, 115: self.ui.button115_2, 116: self.ui.button116_2, 117: self.ui.button117_2, 118: self.ui.button118_2, 119: self.ui.button119_2, 122: self.ui.button122_2}
        self.wing1_faders = {48: self.ui.fader48, 49: self.ui.fader49, 50: self.ui.fader50, 51: self.ui.fader51, 52: self.ui.fader52, 53: self.ui.fader53, 54: self.ui.fader54, 55: self.ui.fader55, 56: self.ui.fader56}
        self.wing2_faders = {48: self.ui.fader48_2, 49: self.ui.fader49_2, 50: self.ui.fader50_2, 51: self.ui.fader51_2, 52: self.ui.fader52_2, 53: self.ui.fader53_2, 54: self.ui.fader54_2, 55: self.ui.fader55_2, 56: self.ui.fader56_2}
        self.wing1_fader_buttons = {48: self.ui.pushButton_fader48, 49: self.ui.pushButton_fader49, 50: self.ui.pushButton_fader50, 51: self.ui.pushButton_fader51, 52: self.ui.pushButton_fader52, 53: self.ui.pushButton_fader53, 54: self.ui.pushButton_fader54, 55: self.ui.pushButton_fader55, 56: self.ui.pushButton_fader56}
        self.wing2_fader_buttons = {48: self.ui.pushButton_fader48_2, 49: self.ui.pushButton_fader49_2, 50: self.ui.pushButton_fader50_2, 51: self.ui.pushButton_fader51_2, 52: self.ui.pushButton_fader52_2, 53: self.ui.pushButton_fader53_2, 54: self.ui.pushButton_fader54_2, 55: self.ui.pushButton_fader55_2, 56: self.ui.pushButton_fader56_2}

        self.handler = MidiControllerHandler(gui_instances=[self, self])
        self.handler.setup()

        self.assign_callbacks()

        self.midi_timer = QTimer()
        self.midi_timer.timeout.connect(self.handler.poll)
        self.midi_timer.start(POLLING_INTERVAL)

    # =================================================================
    #                          Tools/Utils
    # =================================================================

    def invert_hex_color(self, hex_color: str) -> str:
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

    def get_button_background_color(self, button):
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

    # =================================================================
    #                          Callbacks
    # =================================================================

    def assign_callbacks(self):
        # Button callback assignment
        for note, btn in self.wing1_buttons.items():
            btn.pressed.connect(partial(self._on_button_pressed,
                                        note=note, device_id=1))
            btn.released.connect(partial(self._on_button_released,
                                         note=note, device_id=1))

        for note, btn in self.wing2_buttons.items():
            btn.pressed.connect(partial(self._on_button_pressed,
                                        note=note, device_id=2))
            btn.released.connect(partial(self._on_button_released,
                                         note=note, device_id=2))

        # Fader Button callback assignment
        # TODO: THIS IS NOT DONE YET!!!!!!!
        """for cc, fbtn in self.wing1_fader_buttons.items():
            fbtn.pressed.connect(partial(self.controller. ...))
            fbtn.released.connect(partial(self.controller. ...))
        for cc, fbtn in self.wing2_fader_buttons.items():
            fbtn.pressed.connect(partial(self.controller. ...))
            fbtn.released.connect(partial(self.controller. ...))"""
        # TODO: THIS IS NOT DONE YET!!!!!!!

        # Fader callback assignment
        for cc, fader in self.wing1_faders.items():
            fader.valueChanged.connect(partial(self._on_fader_changed, cc=cc, device_id=1))

        for cc, fader in self.wing2_faders.items():
            fader.valueChanged.connect(partial(self._on_fader_changed, cc=cc, device_id=2))

    def _on_fader_changed(self, value, cc, device_id):
        self.handler.imitate_midi_message(
            type="control_change", channel=0, cc=cc, value=value, device_id=device_id)

    def _on_button_pressed(self, note, device_id):
        self.handler.imitate_midi_message(
            type="note_on", channel=0, note=note, velocity=127, device_id=device_id)

    def _on_button_released(self, note, device_id):
        self.handler.imitate_midi_message(
            type="note_off", channel=0, note=note, velocity=0, device_id=device_id)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()