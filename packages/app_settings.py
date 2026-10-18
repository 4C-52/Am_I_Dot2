"""
AppSettings: the few settings that belong to the application itself rather
than to a profile (which folder holds the profiles, which profile was opened
last).

They are stored in the user's configuration folder, outside the application
folder, so they survive when a new version of the app replaces the old one.
"""

import json
import os

from PySide6.QtCore import QStandardPaths

from packages.app_info import APP_NAME

SETTINGS_FILENAME = "settings.json"
PROFILES_SUBFOLDER = "profiles"


def default_settings_folder():
    """Per-user configuration folder: ~/.config/Am_I_Dot2 on Linux, AppData/Local/Am_I_Dot2 on Windows."""
    base = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.GenericConfigLocation)
    return os.path.join(base, APP_NAME)


def default_profiles_folder():
    """Visible per-user folder for the profiles: ~/Documents/Am_I_Dot2/profiles."""
    documents = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)
    return os.path.join(documents, APP_NAME, PROFILES_SUBFOLDER)


class AppSettings:
    def __init__(self, settings_folder=None):
        self.settings_folder = settings_folder or default_settings_folder()
        self.profiles_folder = default_profiles_folder()
        self.last_profile_path = None

    @property
    def settings_filepath(self):
        return os.path.join(self.settings_folder, SETTINGS_FILENAME)

    def load(self):
        """Reads the settings file if it exists. A missing or broken file simply keeps the defaults."""
        try:
            with open(self.settings_filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            return self

        if not isinstance(data, dict):
            return self
        if _is_non_empty_string(data.get("profiles_folder")):
            self.profiles_folder = data["profiles_folder"]
        if _is_non_empty_string(data.get("last_profile_path")):
            self.last_profile_path = data["last_profile_path"]
        return self

    def save(self):
        """Writes the settings file, creating its folder when needed. Raises OSError when the folder is not writable."""
        os.makedirs(self.settings_folder, exist_ok=True)
        with open(self.settings_filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    def to_dict(self):
        return {
            "profiles_folder": self.profiles_folder,
            "last_profile_path": self.last_profile_path,
        }


def _is_non_empty_string(value):
    return isinstance(value, str) and value != ""
