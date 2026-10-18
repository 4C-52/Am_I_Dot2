"""
Static information about the application: name, version, and the web links
used by the Help menu and the update checker.

Bump APP_VERSION every time a new GitHub release is published, and give the
release a tag with the same number (version "1.2.0" <-> tag "v1.2.0").
"""

from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

APP_NAME = "Am_I_Dot2"
APP_VERSION = "0.1.0"

GITHUB_OWNER = "4C-52"
GITHUB_REPOSITORY = "Am_I_Dot2"
GITHUB_PAGE_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPOSITORY}"
GITHUB_RELEASES_URL = f"{GITHUB_PAGE_URL}/releases"
GITHUB_LATEST_RELEASE_API_URL = (
    f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPOSITORY}/releases/latest"
)

# Help menu links. Each menu action has its own constant so they can be changed independently.
CONFIGURING_AM_I_DOT2_URL = f"{GITHUB_PAGE_URL}/blob/master/README.md"
MANAGE_PROFILES_URL = f"{GITHUB_PAGE_URL}/blob/master/README.md"

# Folder containing main.py, whatever the folder the app is launched from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Profile shipped with the source code, used to seed a fresh installation.
BUNDLED_PROFILE_PATH = PROJECT_ROOT / "data" / "data.json"


def open_in_browser(url):
    """Opens the url in the user's default web browser. Returns True on success."""
    return QDesktopServices.openUrl(QUrl(url))
