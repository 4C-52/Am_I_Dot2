"""
GuiThreadDispatcher: runs a function in the Qt GUI thread, whichever thread
asks for it.

The global hotkeys (keyboard library) call their callbacks from their own
background thread. Qt widgets and dialogs may only be touched from the GUI
thread, otherwise the app can crash at random. Wrapping each hotkey callback
with dispatcher.wrap() queues the call into the GUI thread instead.
"""

from PySide6.QtCore import QObject, Qt, Signal, Slot


class GuiThreadDispatcher(QObject):
    """Must be created in the GUI thread (the thread it lives in is the one that runs the calls)."""

    _call_requested = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Queued: the function runs later, in this object's thread, never in the caller's thread
        self._call_requested.connect(self._run, Qt.ConnectionType.QueuedConnection)

    def call(self, function):
        """Schedules function() to run in the GUI thread. Safe to call from any thread."""
        self._call_requested.emit(function)

    def wrap(self, function):
        """Returns a callback that, when called from any thread, runs function() in the GUI thread."""
        return lambda: self.call(function)

    @Slot(object)
    def _run(self, function):
        function()
