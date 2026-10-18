"""
Checks GitHub for a newer release of the app.

The check runs in a background thread so the GUI never waits for the network.
Any problem (no internet, GitHub down, no release published yet) is silently
ignored: a missing update notice is better than an error at every startup.
"""

import json
import re
import threading
import urllib.request

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from packages.app_info import (APP_NAME, APP_VERSION, GITHUB_LATEST_RELEASE_API_URL,
                               GITHUB_RELEASES_URL, open_in_browser)

REQUEST_TIMEOUT_SECONDS = 5
VERSION_PATTERN = re.compile(r"v?(\d+(?:\.\d+)*)", re.IGNORECASE)


# =================================================================
#                      Version numbers
# =================================================================

def parse_version(text):
    """"v1.2.3" or "1.2.3-beta" -> (1, 2, 3). Anything unparsable -> ()."""
    match = VERSION_PATTERN.match((text or "").strip())
    if not match:
        return ()
    return tuple(int(part) for part in match.group(1).split("."))


def is_newer_version(candidate, current):
    """True when candidate is strictly greater than current ("1.10.0" > "1.9.2")."""
    candidate_parts = parse_version(candidate)
    current_parts = parse_version(current)
    if not candidate_parts or not current_parts:
        return False
    length = max(len(candidate_parts), len(current_parts))
    return _pad(candidate_parts, length) > _pad(current_parts, length)


def _pad(parts, length):
    return parts + (0,) * (length - len(parts))


# =================================================================
#                      GitHub lookup
# =================================================================

def fetch_latest_release(timeout=REQUEST_TIMEOUT_SECONDS):
    """Asks GitHub for the latest release. Returns (version_tag, release_url) or None when unavailable."""
    request = urllib.request.Request(
        GITHUB_LATEST_RELEASE_API_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": f"{APP_NAME}/{APP_VERSION}"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.load(response)
    except Exception:  # Network down, 404 when no release exists yet, bad JSON...
        return None

    tag = data.get("tag_name") if isinstance(data, dict) else None
    if not tag:
        return None
    return tag, data.get("html_url") or GITHUB_RELEASES_URL


class VersionChecker(QObject):
    """Emits update_available(latest_version, release_url) in the GUI thread when a newer release exists."""

    update_available = Signal(str, str)

    def check_in_background(self):
        threading.Thread(target=self._check, name="version-check", daemon=True).start()

    def _check(self):
        release = fetch_latest_release()
        if release is None:
            return
        latest_version, release_url = release
        if is_newer_version(latest_version, APP_VERSION):
            self.update_available.emit(latest_version, release_url)


# =================================================================
#                      Dialog
# =================================================================

def show_update_dialog(latest_version, release_url, parent=None):
    """Tells the user a newer version exists and offers to open its download page."""
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Icon.Information)
    box.setWindowTitle("Update available")
    box.setText(
        f"A new version of Am I Dot2 is available: {latest_version}\n"
        f"You are using version {APP_VERSION}."
    )
    box.setInformativeText(
        "Your profiles and settings are stored outside of the application folder, "
        "so they will still be there after updating."
    )
    go_button = box.addButton("Go to the release page", QMessageBox.ButtonRole.AcceptRole)
    box.addButton("Update later", QMessageBox.ButtonRole.RejectRole)
    box.setDefaultButton(go_button)
    box.exec()

    if box.clickedButton() is go_button:
        open_in_browser(release_url)
