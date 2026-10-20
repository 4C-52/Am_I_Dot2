"""
Everything about profile files: the JSON files holding the pad/fader mapping
of one show, along with the dot2 and MIDI settings.

This module knows the expected format (validation), creates blank profiles,
and lists the profiles of a folder. It never touches the controllers or the
GUI; MidiController.load_profile() does that.
"""

import copy
import json
import os

from PySide6.QtCore import QFile

PROFILE_EXTENSION = ".json"
PROFILE_FILE_FILTER = "Am I Dot2 profile (*.json)"
DEFAULT_PROFILE_FILENAME = "default.json"
NEW_PROFILE_FILENAME = "new_profile.json"
MAX_PROBLEMS_SHOWN = 8

# Characters and names Windows refuses in file names (also refused elsewhere so profiles stay portable)
INVALID_NAME_CHARACTERS = '<>:"/\\|?*'
RESERVED_WINDOWS_NAMES = {"CON", "PRN", "AUX", "NUL",
                          *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}

# Top-level fields of a profile and the python type(s) each one must have.
TOP_LEVEL_FIELDS = {
    "default_brightness_level": int,
    "default_blink_channel": int,
    "default_ip_address": str,
    "dot2_password": str,
    "config_mode": (int, bool),
    "DEFAULT_MIDI_INPORT_DEVICE1": str,
    "DEFAULT_MIDI_OUTPORT_DEVICE1": str,
    "DEFAULT_MIDI_INPORT_DEVICE2": str,
    "DEFAULT_MIDI_OUTPORT_DEVICE2": str,
    "note_executor_dictionary_device1": dict,
    "note_executor_dictionary_device2": dict,
    "cc_fader_index_dictionary_device1": dict,
    "cc_fader_index_dictionary_device2": dict,
}
NOTE_DICTIONARY_FIELDS = ("note_executor_dictionary_device1", "note_executor_dictionary_device2")
CC_DICTIONARY_FIELDS = ("cc_fader_index_dictionary_device1", "cc_fader_index_dictionary_device2")

# Fields describing the setup (console, controllers) rather than the show.
# They are copied from the current profile when a new one is created.
SETUP_FIELDS = (
    "default_brightness_level",
    "default_blink_channel",
    "default_ip_address",
    "dot2_password",
    "DEFAULT_MIDI_INPORT_DEVICE1",
    "DEFAULT_MIDI_OUTPORT_DEVICE1",
    "DEFAULT_MIDI_INPORT_DEVICE2",
    "DEFAULT_MIDI_OUTPORT_DEVICE2",
)

BLANK_PROFILE = {
    "default_brightness_level": 6,
    "default_blink_channel": 10,
    "default_ip_address": "10.0.0.50",
    "dot2_password": "1",
    "config_mode": 0,
    "DEFAULT_MIDI_INPORT_DEVICE1": "",
    "DEFAULT_MIDI_OUTPORT_DEVICE1": "",
    "DEFAULT_MIDI_INPORT_DEVICE2": "",
    "DEFAULT_MIDI_OUTPORT_DEVICE2": "",
    "note_executor_dictionary_device1": {},
    "note_executor_dictionary_device2": {},
    "cc_fader_index_dictionary_device1": {},
    "cc_fader_index_dictionary_device2": {},
}


class ProfileError(Exception):
    """Raised when a profile file cannot be read or does not have the expected format."""


# =================================================================
#                           Validation
# =================================================================

def validate_profile_data(data):
    """Returns a list of human readable problems. An empty list means the profile is valid."""
    if not isinstance(data, dict):
        return ["The file does not contain a JSON object."]

    problems = []
    for field, expected_type in TOP_LEVEL_FIELDS.items():
        if field not in data:
            problems.append(f'Missing field "{field}".')
        elif not _is_instance(data[field], expected_type):
            problems.append(f'Field "{field}" has the wrong type.')
    if problems:
        return problems  # No point in checking the content of missing dictionaries

    for field in NOTE_DICTIONARY_FIELDS:
        problems += _validate_note_dictionary(field, data[field])
    for field in CC_DICTIONARY_FIELDS:
        problems += _validate_cc_dictionary(field, data[field])
    return problems


def _validate_note_dictionary(field, note_dictionary):
    """Checks {"note": {"executor_index": int, "color": int, "short_label"?: str, "long_label"?: str}}."""
    problems = []
    for note, entry in note_dictionary.items():
        if not _is_number_string(note):
            problems.append(f'"{field}": key "{note}" is not a MIDI note number.')
            continue
        if not isinstance(entry, dict):
            problems.append(f'"{field}": note {note} is not an object.')
            continue
        if not _is_instance(entry.get("executor_index"), int):
            problems.append(f'"{field}": note {note} is missing a numeric "executor_index".')
        if not _is_instance(entry.get("color"), int):
            problems.append(f'"{field}": note {note} is missing a numeric "color".')
        for label in ("short_label", "long_label"):
            if entry.get(label) is not None and not isinstance(entry[label], str):
                problems.append(f'"{field}": note {note} has a non-text "{label}".')
    return problems


def _validate_cc_dictionary(field, cc_dictionary):
    """Checks {"control_change": executor_index}."""
    problems = []
    for cc, executor_index in cc_dictionary.items():
        if not _is_number_string(cc):
            problems.append(f'"{field}": key "{cc}" is not a MIDI control change number.')
        elif not _is_instance(executor_index, int):
            problems.append(f'"{field}": control change {cc} must map to a numeric executor index.')
    return problems


def _is_instance(value, expected_type):
    """isinstance() that does not accept booleans where plain integers are expected."""
    if isinstance(value, bool) and expected_type is int:
        return False
    return isinstance(value, expected_type)


def _is_number_string(text):
    return isinstance(text, str) and text.lstrip("-").isdigit()


# =================================================================
#                           Reading / writing
# =================================================================

def read_profile(path):
    """Reads and validates a profile file. Raises ProfileError with a readable message on failure."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except OSError as error:
        raise ProfileError(f"The file could not be read:\n{error}") from error
    except ValueError as error:
        raise ProfileError(f"The file is not valid JSON:\n{error}") from error

    problems = validate_profile_data(data)
    if problems:
        raise ProfileError("The file is not an Am I Dot2 profile:\n" + _format_problems(problems))
    return data


def check_profile_file(path):
    """Returns None when the file is a valid profile, otherwise the error message."""
    try:
        read_profile(path)
    except ProfileError as error:
        return str(error)
    return None


def write_profile(path, data):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def blank_profile_data(base_profile=None):
    """
    A new profile with no pad or fader mapped. When base_profile is given, its
    setup fields (console address, password, MIDI ports, brightness...) are kept
    so the user does not have to configure them again.
    """
    data = copy.deepcopy(BLANK_PROFILE)
    if base_profile:
        for field in SETUP_FIELDS:
            if field in base_profile:
                data[field] = base_profile[field]
    return data


def create_blank_profile(path, base_profile=None):
    """Writes a blank profile to path and returns its data."""
    data = blank_profile_data(base_profile)
    write_profile(path, data)
    return data


# =================================================================
#                           Folders and names
# =================================================================

def list_profiles(folder):
    """Sorted paths of the profile files found in the folder (empty when the folder does not exist)."""
    if not folder or not os.path.isdir(folder):
        return []
    names = sorted(name for name in os.listdir(folder) if name.lower().endswith(PROFILE_EXTENSION))
    return [os.path.join(folder, name) for name in names]


def ensure_profile_extension(path):
    return path if path.lower().endswith(PROFILE_EXTENSION) else path + PROFILE_EXTENSION


def unique_profile_path(folder, filename):
    """folder/filename, with _2, _3... appended to the name until no such file exists."""
    base, extension = os.path.splitext(filename)
    candidate = os.path.join(folder, filename)
    counter = 2
    while os.path.exists(candidate):
        candidate = os.path.join(folder, f"{base}_{counter}{extension}")
        counter += 1
    return candidate


def profile_display_name(path):
    """"C:/profiles/my_show.json" -> "my_show"."""
    return os.path.splitext(os.path.basename(path))[0]


def is_same_file(path_a, path_b):
    if not path_a or not path_b:
        return False
    return os.path.normcase(os.path.abspath(path_a)) == os.path.normcase(os.path.abspath(path_b))


def profile_path_for_name(folder, name):
    """
    folder/<name>.json for a name typed by the user ("My show" or "My show.json").
    Raises ProfileError when the name cannot be used as a file name.
    """
    name = name.strip()
    if name.lower().endswith(PROFILE_EXTENSION):
        name = name[:-len(PROFILE_EXTENSION)].strip()

    if not name:
        raise ProfileError("The profile name cannot be empty.")
    invalid = sorted({character for character in name if character in INVALID_NAME_CHARACTERS or ord(character) < 32})
    if invalid:
        raise ProfileError("The profile name cannot contain these characters: " + " ".join(invalid))
    if name.endswith("."):
        raise ProfileError("The profile name cannot end with a dot.")
    if name.upper() in RESERVED_WINDOWS_NAMES:
        raise ProfileError(f'"{name}" is reserved by Windows, please choose another name.')
    return os.path.join(folder, name + PROFILE_EXTENSION)


# =================================================================
#                     Create / rename / delete
# =================================================================

def create_named_profile(folder, name, base_profile=None):
    """Creates a blank profile called name in folder and returns its path. Never overwrites a file."""
    path = profile_path_for_name(folder, name)
    if os.path.exists(path):
        raise ProfileError(f'A profile called "{profile_display_name(path)}" already exists in this folder.')
    try:
        create_blank_profile(path, base_profile)
    except OSError as error:
        raise ProfileError(f"The profile could not be created:\n{error}") from error
    return path


def rename_profile(path, new_name):
    """Renames the profile file (it stays in its folder) and returns its new path. Never overwrites a file."""
    new_path = profile_path_for_name(os.path.dirname(path), new_name)
    # A file with that name blocks the rename, unless it is this very file (case-only rename on Windows)
    if os.path.exists(new_path) and not is_same_file(path, new_path):
        raise ProfileError(f'A profile called "{profile_display_name(new_path)}" already exists in this folder.')
    try:
        os.rename(path, new_path)
    except OSError as error:
        raise ProfileError(f"The profile could not be renamed:\n{error}") from error
    return new_path


def delete_profile(path):
    """
    Moves the profile to the recycle bin, or deletes it for good when the
    system has no recycle bin. Returns True when it went to the recycle bin.
    """
    if QFile.moveToTrash(path):
        return True
    try:
        os.remove(path)
    except OSError as error:
        raise ProfileError(f"The profile could not be deleted:\n{error}") from error
    return False


def _format_problems(problems):
    lines = [f"- {problem}" for problem in problems[:MAX_PROBLEMS_SHOWN]]
    hidden = len(problems) - MAX_PROBLEMS_SHOWN
    if hidden > 0:
        lines.append(f"- ... and {hidden} more problem(s)")
    return "\n".join(lines)
