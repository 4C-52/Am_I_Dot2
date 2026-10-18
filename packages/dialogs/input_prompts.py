"""
Small blocking Qt prompts used by config mode and the backup hotkeys.
They replace the old tkinter dialogs so the app only uses one GUI toolkit.

Every function returns None (or False) when the user cancels.
Must be called from the GUI thread.
"""

from PySide6.QtWidgets import QInputDialog, QLineEdit, QMessageBox

DEFAULT_TITLE = "Am I Dot2"
CONFIRM_WORD = "CONFIRM"
MAX_NUMBER = 9999


def ask_text(prompt, title=DEFAULT_TITLE, default="", parent=None):
    """Asks for a line of text. Returns the text (possibly empty) or None when cancelled."""
    text, accepted = QInputDialog.getText(parent, title, prompt, QLineEdit.EchoMode.Normal, default)
    return text if accepted else None


def ask_number(prompt, title=DEFAULT_TITLE, minimum=0, maximum=MAX_NUMBER, default=None, parent=None):
    """Asks for a whole number between minimum and maximum. Returns it, or None when cancelled."""
    start_value = minimum if default is None else default
    value, accepted = QInputDialog.getInt(parent, title, prompt, start_value, minimum, maximum, 1)
    return value if accepted else None


def show_info(message, title=DEFAULT_TITLE, parent=None):
    QMessageBox.information(parent, title, message)


def confirm_destructive_action(warning, title=DEFAULT_TITLE, parent=None):
    """
    Two-step confirmation for actions that overwrite data: a Yes/No question,
    then the user has to type CONFIRM. Returns True only if both steps pass.
    """
    answer = QMessageBox.warning(
        parent, title, warning,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No,
    )
    if answer != QMessageBox.StandardButton.Yes:
        return False

    typed = ask_text(f'Type "{CONFIRM_WORD}" to proceed. Your current file will be LOST.',
                     title=title, parent=parent)
    return typed == CONFIRM_WORD
