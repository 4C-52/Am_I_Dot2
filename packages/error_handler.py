"""
Central error reporting.

- show_error(): tells the user something went wrong, always with the same
  "contact the developer" hint.
- install_global_exception_hook(): any exception nobody caught (main thread,
  Qt slots, worker threads) ends up in that same message box instead of
  silently killing the app or only printing in a console nobody reads.
"""

import sys
import threading
import traceback

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication, QMessageBox

CONTACT_DEVELOPER_HINT = "If the problem persists, please contact the developer."
DEFAULT_TITLE = "Am I Dot2 - Error"
UNEXPECTED_ERROR_CONTEXT = "An unexpected error occurred"


def show_error(message, title=DEFAULT_TITLE, details=None, parent=None):
    """
    Blocking error box showing the message, the contact-the-developer hint and
    an optional expandable "details" text (for example a traceback).
    """
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Icon.Critical)
    box.setWindowTitle(title)
    box.setText(f"{message}\n\n{CONTACT_DEVELOPER_HINT}")
    if details:
        box.setDetailedText(details)
    box.setStandardButtons(QMessageBox.StandardButton.Ok)
    box.exec()


def format_exception(exc_type, exc_value, exc_traceback):
    return "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))


class _ErrorRelay(QObject):
    """Lives in the GUI thread so that any thread can request an error box safely through a signal."""

    error_occurred = Signal(str, str, str)  # message, title, details

    def __init__(self):
        super().__init__()
        self.error_occurred.connect(self._show)

    @staticmethod
    def _show(message, title, details):
        show_error(message, title=title, details=details)


_relay = None


def install_global_exception_hook():
    """
    Routes uncaught exceptions to show_error(). Must be called from the GUI
    thread once the QApplication exists.
    """
    global _relay
    _relay = _ErrorRelay()
    sys.excepthook = _handle_uncaught_exception
    threading.excepthook = _handle_thread_exception


def report_exception(exc_type, exc_value, exc_traceback, context=UNEXPECTED_ERROR_CONTEXT):
    """Prints the traceback to the console and shows it to the user. Safe to call from any thread."""
    details = format_exception(exc_type, exc_value, exc_traceback)
    if sys.stderr is not None:  # Windowed builds (no console) have no stderr at all
        sys.stderr.write(details)

    message = f"{context}:\n{exc_type.__name__}: {exc_value}"
    if _relay is not None and QApplication.instance() is not None:
        _relay.error_occurred.emit(message, DEFAULT_TITLE, details)


def _handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    report_exception(exc_type, exc_value, exc_traceback)


def _handle_thread_exception(args):
    if args.exc_type is SystemExit:
        return
    thread_name = args.thread.name if args.thread is not None else "unknown"
    report_exception(
        args.exc_type, args.exc_value, args.exc_traceback,
        context=f'{UNEXPECTED_ERROR_CONTEXT} in thread "{thread_name}"',
    )
