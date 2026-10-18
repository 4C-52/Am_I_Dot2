"""
PreferencesDialog: dot2 connection settings (password shown in clear text with
its MD5 hash, IP address with validation) and the MIDI ports of both
controllers.

The two controller buttons act immediately through the controller: the chosen
ports are opened and saved as soon as the user confirms them. The password and
IP address are only read by the caller once the dialog is accepted.
"""

from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
                               QLabel, QLineEdit, QPushButton, QVBoxLayout)

from packages.error_handler import show_error
from packages.utils import is_valid_ipv4, md5_hex

INVALID_IP_TEXT = "Please type a valid IP address (xxx.xxx.xxx.xxx, each number between 0 and 255)."
ERROR_TEXT_STYLE = "color: red;"
NOT_OPEN_TEXT = "not connected"
DEVICE_IDS = (1, 2)


class PreferencesDialog(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Preferences")
        self.setModal(True)
        self.setMinimumWidth(600)

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self
        )
        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self._build_dot2_group())
        layout.addWidget(self._build_midi_group())
        layout.addWidget(self._buttons)

        self._refresh_md5_label()
        self._refresh_ip_validity()
        self._refresh_port_labels()

    # ---- Building the window ----

    def _build_dot2_group(self):
        group = QGroupBox("Dot2 connection", self)
        form = QFormLayout(group)

        self.password_edit = QLineEdit(self.controller.plaintext_password, group)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)  # Always readable, on purpose
        self.password_edit.textChanged.connect(self._refresh_md5_label)

        self.md5_label = QLabel(group)
        self.md5_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.ip_edit = QLineEdit(self.controller.host, group)
        self.ip_edit.setPlaceholderText("192.168.0.12")
        self.ip_edit.textChanged.connect(self._refresh_ip_validity)

        self.ip_error_label = QLabel(INVALID_IP_TEXT, group)
        self.ip_error_label.setStyleSheet(ERROR_TEXT_STYLE)
        self.ip_error_label.setWordWrap(True)

        form.addRow("Dot2 password:", self.password_edit)
        form.addRow("MD5 password:", self.md5_label)
        form.addRow("IP address:", self.ip_edit)
        form.addRow("", self.ip_error_label)
        return group

    def _build_midi_group(self):
        group = QGroupBox("MIDI controllers", self)
        grid = QGridLayout(group)
        self.port_labels = {}
        for row, device_id in enumerate(DEVICE_IDS):
            select_button = QPushButton(f"Controller {device_id}", group)
            select_button.setToolTip(
                f"Select the MIDI input and output of controller {device_id} (Wing-{device_id})"
            )
            select_button.clicked.connect(partial(self._on_controller_button_clicked, device_id=device_id))
            ports_label = QLabel(group)
            grid.addWidget(select_button, row, 0)
            grid.addWidget(ports_label, row, 1)
            self.port_labels[device_id] = ports_label
        grid.setColumnStretch(1, 1)
        return group

    # ---- Live feedback ----

    def _refresh_md5_label(self, *_):
        self.md5_label.setText(md5_hex(self.password))

    def _refresh_ip_validity(self, *_):
        """Shows the red hint and blocks OK while the IP address is not valid."""
        valid = is_valid_ipv4(self.ip_address)
        self.ip_error_label.setVisible(not valid)
        self._buttons.button(QDialogButtonBox.StandardButton.Ok).setEnabled(valid)

    def _refresh_port_labels(self):
        for device_id, label in self.port_labels.items():
            input_name, output_name = self.controller.get_open_port_names(device_id)
            label.setText(f"In:  {input_name or NOT_OPEN_TEXT}\nOut: {output_name or NOT_OPEN_TEXT}")

    def _on_controller_button_clicked(self, device_id):
        try:
            self.controller.choose_ports_for_device(device_id, parent=self)
        except Exception as error:  # rtmidi raises various exception types when a port cannot be opened
            show_error(f"The MIDI ports of controller {device_id} could not be opened:\n{error}",
                       title="MIDI error", parent=self)
        self._refresh_port_labels()

    # ---- Results ----

    @property
    def password(self):
        return self.password_edit.text()

    @property
    def ip_address(self):
        return self.ip_edit.text().strip()
