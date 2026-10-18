"""
MidiPortDialog: lets the user pick the MIDI input and the MIDI output of one
controller from two columns of radio buttons.

Used by the Preferences window, and at startup when a saved port is not
available anymore (first run, controller unplugged, port renamed...).
"""

from PySide6.QtWidgets import (QButtonGroup, QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout,
                               QLabel, QRadioButton, QVBoxLayout)

PORT_NAME_PROPERTY = "port_name"
NO_PORT_TEXT = "No MIDI {kind} found"


class MidiPortDialog(QDialog):
    def __init__(self, device_id, available_inputs, available_outputs,
                 current_input="", current_output="", parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Controller {device_id} - MIDI ports")
        self.setModal(True)
        self.setMinimumWidth(520)

        self._input_group = QButtonGroup(self)
        self._output_group = QButtonGroup(self)

        title = QLabel(f"Select the MIDI input and output of controller {device_id} (Wing-{device_id}).", self)
        title.setWordWrap(True)

        columns = QHBoxLayout()
        columns.addWidget(self._build_port_column("Input", available_inputs, current_input, self._input_group))
        columns.addWidget(self._build_port_column("Output", available_outputs, current_output, self._output_group))

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self
        )
        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addLayout(columns)
        layout.addWidget(self._buttons)

        self._input_group.buttonClicked.connect(self._refresh_ok_button)
        self._output_group.buttonClicked.connect(self._refresh_ok_button)
        self._refresh_ok_button()

    # ---- Building the window ----

    def _build_port_column(self, kind, port_names, current_name, group):
        """A group box with one radio button per port name; the current port is pre-selected."""
        box = QGroupBox(kind, self)
        column = QVBoxLayout(box)
        if not port_names:
            column.addWidget(QLabel(NO_PORT_TEXT.format(kind=kind.lower()), box))
        for name in port_names:
            radio = QRadioButton(name, box)
            radio.setProperty(PORT_NAME_PROPERTY, name)  # text() may hide "&" characters, the property never does
            radio.setChecked(name == current_name)
            group.addButton(radio)
            column.addWidget(radio)
        column.addStretch(1)
        return box

    def _refresh_ok_button(self, *_):
        """OK is only possible once both an input and an output are selected."""
        both_selected = self.selected_input is not None and self.selected_output is not None
        self._buttons.button(QDialogButtonBox.StandardButton.Ok).setEnabled(both_selected)

    # ---- Results ----

    @property
    def selected_input(self):
        return self._checked_port_name(self._input_group)

    @property
    def selected_output(self):
        return self._checked_port_name(self._output_group)

    @staticmethod
    def _checked_port_name(group):
        button = group.checkedButton()
        return button.property(PORT_NAME_PROPERTY) if button is not None else None

    @classmethod
    def ask_ports(cls, device_id, available_inputs, available_outputs,
                  current_input="", current_output="", parent=None):
        """Shows the dialog and returns (input_name, output_name), or None if the user cancelled."""
        dialog = cls(device_id, available_inputs, available_outputs, current_input, current_output, parent)
        accepted = bool(dialog.exec())
        result = (dialog.selected_input, dialog.selected_output) if accepted else None
        dialog.deleteLater()
        return result
