"""
Temporary message box helper built on PySide6.

show_message_box() blocks until the user answers, then returns the name of the
button that was pressed, or None if the window was dismissed any other way
(close button, Escape, Alt-F4...). Either way the window is closed on return.
"""

from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QPushButton, QVBoxLayout)

import sys

DEFAULT_BUTTON = "Ok"  # Used when no button list is given, returns None


class _MessageBox(QDialog):
    """Modal dialog showing a message and one button per entry of button_list."""

    def __init__(self, title, message, button_list, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(260)

        self.clicked_button = None  # Stays None unless a button is pressed

        label = QLabel(str(message), self)
        label.setWordWrap(True)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        for name in button_list:
            button = QPushButton(str(name), self)
            button.setAutoDefault(False)
            button.clicked.connect(partial(self._on_button_clicked, name))
            button_layout.addWidget(button)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addSpacing(10)
        layout.addLayout(button_layout)

    def _on_button_clicked(self, name):
        """Remember which button was pressed, then close the window."""
        self.clicked_button = name
        self.accept()


def show_message_box(title, message, button_list=None):
    """Show a modal message box and wait for the user to answer it.

    title       : window title of the message box
    message     : text shown as the message body
    button_list : list of button names, ex: ["Yes", "No"].
                  If omitted or empty, a single "Ok" button is shown.

    Returns the name of the pressed button, or None if the window was closed
    without pressing one. The default "Ok" button also returns None.
    """
    # Only create a QApplication when running outside of the GUI (ex: tests)
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    has_custom_buttons = bool(button_list)
    buttons = list(button_list) if has_custom_buttons else [DEFAULT_BUTTON]

    dialog = _MessageBox(title, message, buttons)
    dialog.resize(dialog.sizeHint())
    dialog.exec()
    clicked_button = dialog.clicked_button
    dialog.deleteLater()

    return clicked_button if has_custom_buttons else None


if __name__ == "__main__":
    print(show_message_box("Am I Dot2", "No button list, this returns None."))
    print(show_message_box("Am I Dot2", "Overwrite the current profile?",
                           ["Overwrite", "Keep both", "Cancel"]))
