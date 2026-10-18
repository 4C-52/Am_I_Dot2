"""Dialog shown when the dot2 console cannot be reached, with a button to retry."""

from PySide6.QtWidgets import QMessageBox

RETRY_TEXT = "Retry"
CONTINUE_TEXT = "Continue without the console"

# Keyed by Dot2WebSocketHandler.connection_status() values.
STATUS_EXPLANATIONS = {
    "login_failed": "The console refused the login, so the remote password is probably wrong.",
    "unreachable": "Nothing answered at this address: the connection was refused or dropped.",
    "connecting": "The console did not answer within {timeout} seconds.",
}
DEFAULT_EXPLANATION = "The connection could not be established."


def describe_connection_failure(status, timeout_seconds):
    return STATUS_EXPLANATIONS.get(status, DEFAULT_EXPLANATION).format(timeout=timeout_seconds)


def ask_retry_connection(host, status, timeout_seconds, parent=None):
    """
    Explains why the dot2 could not be reached and what usually causes it.
    Returns True when the user wants to retry, False to keep working offline.
    """
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Icon.Warning)
    box.setWindowTitle("Cannot connect to the dot2")
    box.setText(f"Am I Dot2 could not connect to the dot2 console at {host}.")
    box.setInformativeText(
        f"What happened: {describe_connection_failure(status, timeout_seconds)}\n\n"
        "This usually happens when:\n"
        "• the console (or dot2 onPC) is off, or not on the same network as this computer,\n"
        f"• the IP address set in Settings > Preferences ({host}) is not the console's,\n"
        "• the Web Remote is disabled on the console (Setup > Global Settings),\n"
        "• the remote password set in Settings > Preferences does not match the console's.\n\n"
        "Without a connection, the pads will not trigger anything on the console and the "
        "running executors will not blink."
    )
    retry_button = box.addButton(RETRY_TEXT, QMessageBox.ButtonRole.AcceptRole)
    box.addButton(CONTINUE_TEXT, QMessageBox.ButtonRole.RejectRole)
    box.setDefaultButton(retry_button)
    box.exec()
    return box.clickedButton() is retry_button
