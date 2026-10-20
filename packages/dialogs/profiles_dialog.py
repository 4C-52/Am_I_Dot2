"""
ProfilesDialog: choose the folder holding the profiles (it becomes the default
location of the New/Open file dialogs), pick one of its profiles from a
dropdown, and create, rename or delete profiles of that folder.

Create, rename and delete act on the disk immediately, even if the dialog is
then cancelled. When the loaded profile is renamed, current_profile_path gives
its new path so the caller can follow it.
"""

from PySide6.QtWidgets import (QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFormLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from packages.dialogs.input_prompts import ask_text, confirm_destructive_action, show_warning
from packages.profile_manager import (ProfileError, create_named_profile, delete_profile, is_same_file,
                                      list_profiles, profile_display_name, rename_profile)

NO_PROFILE_TEXT = 'No profile found in this folder. Click "New..." to create one.'
HINT_TEXT_STYLE = "color: gray;"
LOADED_SUFFIX = "  (loaded)"
DIALOG_TITLE = "Profiles"


class ProfilesDialog(QDialog):
    def __init__(self, profiles_folder, current_profile_path=None, base_profile=None, parent=None):
        """
        current_profile_path : profile loaded in the app (marked in the list, cannot be deleted)
        base_profile         : profile data whose console/MIDI settings new profiles copy
        """
        super().__init__(parent)
        self.setWindowTitle(DIALOG_TITLE)
        self.setModal(True)
        self.setMinimumWidth(560)

        self.current_profile_path = current_profile_path
        self._base_profile = base_profile

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
        form.addRow("", self._build_profile_buttons())
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

    def _build_profile_buttons(self):
        """New / Rename / Delete row under the dropdown."""
        self.new_button = QPushButton("New...", self)
        self.new_button.setToolTip("Create a blank profile in the profiles folder")
        self.new_button.clicked.connect(self._on_new_clicked)

        self.rename_button = QPushButton("Rename...", self)
        self.rename_button.setToolTip("Rename the selected profile")
        self.rename_button.clicked.connect(self._on_rename_clicked)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setToolTip("Move the selected profile to the recycle bin")
        self.delete_button.clicked.connect(self._on_delete_clicked)

        row = QHBoxLayout()
        row.addWidget(self.new_button)
        row.addWidget(self.rename_button)
        row.addWidget(self.delete_button)
        row.addStretch(1)
        return row

    # ---- Folder and list ----

    def _on_browse_clicked(self, *_):
        folder = QFileDialog.getExistingDirectory(self, "Select the profiles folder", self.selected_folder)
        if folder:
            self.folder_edit.setText(folder)
            self._refresh_profile_list()

    def _refresh_profile_list(self, select_path=None):
        """Fills the dropdown with the profiles of the folder, pre-selecting select_path when it is one of them."""
        self.profile_combo.clear()
        for path in list_profiles(self.selected_folder):
            label = profile_display_name(path)
            if self._is_loaded_profile(path):
                label += LOADED_SUFFIX
            self.profile_combo.addItem(label, path)
            if is_same_file(path, select_path):
                self.profile_combo.setCurrentIndex(self.profile_combo.count() - 1)

        has_profiles = self.profile_combo.count() > 0
        self.profile_combo.setEnabled(has_profiles)
        self.rename_button.setEnabled(has_profiles)
        self.delete_button.setEnabled(has_profiles)
        self.no_profile_label.setVisible(not has_profiles)

    def _is_loaded_profile(self, path):
        return is_same_file(path, self.current_profile_path)

    # ---- New / Rename / Delete ----

    def _on_new_clicked(self, *_):
        name = ask_text("Name of the new profile:", title=DIALOG_TITLE, parent=self)
        if name is None:
            return
        try:
            path = create_named_profile(self.selected_folder, name, base_profile=self._base_profile)
        except ProfileError as error:
            show_warning(str(error), title=DIALOG_TITLE, parent=self)
            return
        self._refresh_profile_list(select_path=path)

    def _on_rename_clicked(self, *_):
        path = self.selected_profile_path
        old_name = profile_display_name(path)
        new_name = ask_text(f'New name for "{old_name}":', title=DIALOG_TITLE, default=old_name, parent=self)
        if new_name is None or new_name.strip() == old_name:
            return
        try:
            new_path = rename_profile(path, new_name)
        except ProfileError as error:
            show_warning(str(error), title=DIALOG_TITLE, parent=self)
            return

        if self._is_loaded_profile(path):
            self.current_profile_path = new_path  # The app keeps using the profile under its new name
        self._refresh_profile_list(select_path=new_path)

    def _on_delete_clicked(self, *_):
        path = self.selected_profile_path
        name = profile_display_name(path)
        if self._is_loaded_profile(path):
            show_warning(f'"{name}" is the profile in use. Load another profile before deleting this one.',
                         title=DIALOG_TITLE, parent=self)
            return

        confirmed = confirm_destructive_action(
            f'Delete the profile "{name}"?\n\n'
            "It is moved to the recycle bin when your system has one, otherwise it is deleted for good.",
            title="Delete profile", parent=self, final_prompt=f'The profile "{name}" will be deleted.',
        )
        if not confirmed:
            return
        try:
            delete_profile(path)
        except ProfileError as error:
            show_warning(str(error), title=DIALOG_TITLE, parent=self)
            return
        self._refresh_profile_list(select_path=self.current_profile_path)

    # ---- Results ----

    @property
    def selected_folder(self):
        return self.folder_edit.text()

    @property
    def selected_profile_path(self):
        """Path of the profile chosen in the dropdown, or None when the folder has no profile."""
        return self.profile_combo.currentData()
