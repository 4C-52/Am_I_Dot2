"""
ProfilesDialog: choose the folder holding the profiles (it becomes the default
location of the New/Open file dialogs) and pick one of its profiles from a
dropdown, as an alternative to File > Open.
"""

from PySide6.QtWidgets import (QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFormLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from packages.profile_manager import is_same_file, list_profiles, profile_display_name

NO_PROFILE_TEXT = "No profile found in this folder. Use File > New to create one."
HINT_TEXT_STYLE = "color: gray;"


class ProfilesDialog(QDialog):
    def __init__(self, profiles_folder, current_profile_path=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Profiles")
        self.setModal(True)
        self.setMinimumWidth(560)

        self.folder_edit = QLineEdit(profiles_folder, self)
        self.folder_edit.setReadOnly(True)
        browse_button = QPushButton("Browse...", self)
        browse_button.clicked.connect(self._on_browse_clicked)
        folder_row = QHBoxLayout()
        folder_row.addWidget(self.folder_edit, 1)
        folder_row.addWidget(browse_button)

        self.profile_combo = QComboBox(self)
        self.no_profile_label = QLabel(NO_PROFILE_TEXT, self)
        self.no_profile_label.setStyleSheet(HINT_TEXT_STYLE)
        self.no_profile_label.setWordWrap(True)

        form = QFormLayout()
        form.addRow("Profiles folder:", folder_row)
        form.addRow("Profile:", self.profile_combo)
        form.addRow("", self.no_profile_label)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

        self._refresh_profile_list(select_path=current_profile_path)

    def _on_browse_clicked(self, *_):
        folder = QFileDialog.getExistingDirectory(self, "Select the profiles folder", self.selected_folder)
        if folder:
            self.folder_edit.setText(folder)
            self._refresh_profile_list()

    def _refresh_profile_list(self, select_path=None):
        """Fills the dropdown with the profiles of the folder, pre-selecting select_path when it is one of them."""
        self.profile_combo.clear()
        for path in list_profiles(self.selected_folder):
            self.profile_combo.addItem(profile_display_name(path), path)
            if is_same_file(path, select_path):
                self.profile_combo.setCurrentIndex(self.profile_combo.count() - 1)

        has_profiles = self.profile_combo.count() > 0
        self.profile_combo.setEnabled(has_profiles)
        self.no_profile_label.setVisible(not has_profiles)

    # ---- Results ----

    @property
    def selected_folder(self):
        return self.folder_edit.text()

    @property
    def selected_profile_path(self):
        """Path of the profile chosen in the dropdown, or None when the folder has no profile."""
        return self.profile_combo.currentData()
