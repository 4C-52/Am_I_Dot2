# Developer documentation

How Am I Dot2 is built, how its parts talk to each other, and how to change, build and release it.

User documentation lives in the [README](../README.md), [Configuring Am I Dot2](CONFIGURING_AM_I_DOT2.md) and [Managing profiles](MANAGING_PROFILES.md).

---

## Contents

- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [Project layout](#project-layout)
- [Architecture](#architecture)
- [Threads](#threads)
- [MIDI flow and Config Mode](#midi-flow-and-config-mode)
- [The dot2 Web Remote protocol](#the-dot2-web-remote-protocol)
- [Executor feedback (blinking)](#executor-feedback-blinking)
- [Profiles and settings](#profiles-and-settings)
- [The GUI](#the-gui)
- [Errors and messages](#errors-and-messages)
- [Testing](#testing)
- [Building](#building)
- [Releasing](#releasing)
- [Code conventions](#code-conventions)
- [Gotchas](#gotchas)

---

## Tech stack

| Purpose | Library |
|---|---|
| GUI | [PySide6](https://doc.qt.io/qtforpython-6/) (Qt 6) |
| MIDI | [mido](https://mido.readthedocs.io/) with the [python-rtmidi](https://pypi.org/project/python-rtmidi/) backend |
| Console connection | [websocket-client](https://pypi.org/project/websocket-client/) |
| Global hotkeys | [keyboard](https://pypi.org/project/keyboard/) |
| Packaging | [PyInstaller](https://pyinstaller.org/) |

Exact versions are pinned in `requirements.txt`. Build tools are in `requirements-build.txt`.

---

## Getting started

```bash
git clone https://github.com/4C-52/Am_I_Dot2.git
cd Am_I_Dot2
python -m venv .venv
# Windows: .venv\Scripts\activate      Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

On Linux the `keyboard` library needs root, so run `sudo .venv/bin/python main.py`. Running as root leaves root-owned `__pycache__` folders behind. Delete them, or run `python -B`, if later non-root runs complain.

Without a console, the app still starts: it offers to retry the connection, or to continue without it.

---

## Project layout

```
Am_I_Dot2/
├── main.py                      MainApp: main window, menus, profiles, connection follow-up
├── resources_rc.py              GENERATED from gui/resources.qrc (icons)
├── requirements.txt             Runtime dependencies
├── requirements-build.txt       + PyInstaller and Pillow
├── data/data.json               Starter profile copied into the profiles folder on first run
├── gui/
│   ├── am_i_dot2_V2.ui          Qt Designer file of the main window (the one in use)
│   ├── am_i_dot2_V1.ui          Previous version, kept for reference
│   └── resources.qrc            Icon list for pyside6-rcc
├── media/                       Logo, README gif, menu icons
├── docs/                        This documentation
└── packages/
    ├── app_info.py              App name, version, GitHub links, open_in_browser()
    ├── app_settings.py          AppSettings: profiles folder + last profile (user config folder)
    ├── profile_manager.py       Profile validation, create/rename/delete, folders and names
    ├── midi_controller.py       MidiController: MIDI ports, pad colors, bindings, Config Mode
    ├── web_socket_handler.py    Dot2WebSocketHandler: dot2 Web Remote protocol
    ├── error_handler.py         show_error() and the global exception hook
    ├── version_checker.py       GitHub release check and update dialog
    ├── gui_thread.py            GuiThreadDispatcher: run a function on the GUI thread
    ├── utils.py                 md5_hex(), is_valid_ipv4()
    ├── message_box.py           Standalone custom message box helper (not used by the app yet)
    ├── gui_main_window.py       GENERATED from gui/am_i_dot2_V2.ui
    └── dialogs/
        ├── preferences_dialog.py      Settings > Preferences
        ├── midi_port_dialog.py        MIDI input/output picker for one controller
        ├── profiles_dialog.py         Settings > Profiles
        ├── connection_error_dialog.py "Cannot connect to the dot2" + Retry
        └── input_prompts.py           Text/number prompts, two-step destructive confirmation
```

---

## Architecture

```
            ┌──────────────── MainApp (main.py) ─────────────────┐
            │ window, menus, profiles, preferences, connection   │
            └───────┬─────────────────────────────▲──────────────┘
      GUI pad/fader │ imitate_midi_message()      │ set_button_color(), set_button_label(),
                    ▼                             │ set_fader_value(), clear_all_buttons()...
            ┌──────────────── MidiController ────────────────────┐
APC mini ──►│ poll() ─► note_loop() ─► bindings / Config Mode    │──► APC mini (LED colors)
  mk2       │ profile data, colors, blinking                     │
            └───────┬─────────────────────────────▲──────────────┘
                    │ send_playback_click()       │ "playbacks" callback
                    │ send_playback_fader()       │ ─► handle_playbacks()
                    ▼                             │
            ┌──────────── Dot2WebSocketHandler ──────────────────┐
            │ login, heartbeat, requests, callback dispatch      │◄──► dot2 Web Remote
            └────────────────────────────────────────────────────┘
```

- **`MainApp`** owns the window and everything the user clicks. It creates the `MidiController` and hands it a reference to itself (`send_gui_instance`), so the controller can update the on-screen pads.
- **`MidiController`** is the core. It holds the loaded profile in memory, opens the MIDI ports, turns MIDI messages into console commands, drives the pad LEDs, and runs Config Mode. It writes to the profile file whenever a binding changes.
- **`Dot2WebSocketHandler`** knows nothing about MIDI. It speaks the dot2 protocol and calls registered callbacks when messages arrive.
- **`profile_manager`** is pure file logic (validation, naming, create/rename/delete). It never touches the GUI or the controllers.
- **Dialogs** are built in code, not in Qt Designer. Each one returns its result through properties read after `exec()`.

### Startup sequence

1. `main()` creates the `QApplication` and installs the global exception hook.
2. `MainApp.__init__` builds the UI, then loads `AppSettings`.
3. `_resolve_startup_profile()` picks the last profile, else `default.json` in the profiles folder. That file is seeded from `data/data.json` on first run. An invalid file is replaced by a blank profile and reported.
4. `MidiController.setup()` loads the profile, opens the MIDI ports (asking when a saved port is missing), shows the dot2 logo on the pads for two seconds, creates the websocket handler, registers hotkeys, and starts the playback poll thread.
5. The window is shown, then `MainApp.start()` starts the console connection and the update check.

---

## Threads

| Thread | Created by | What runs there |
|---|---|---|
| **GUI thread** | Qt | Everything in the window, the MIDI poll (`QTimer`, every 10 ms), the connection follow-up timer, all dialogs |
| **Websocket** | `Dot2WebSocketHandler.connect()` | `run_forever()` and every callback, including `handle_playbacks()` |
| **Heartbeat** | `Dot2WebSocketHandler.connect()` | Sends `{"session": id}` every 10 s |
| **Playback poll** | `MidiController.setup()` | Asks the console for executor states every 3 s |
| **Hotkeys** | the `keyboard` library | F1, F2, F11, F12 callbacks, immediately forwarded to the GUI thread |
| **Version check** | `VersionChecker.check_in_background()` | One GitHub request at startup |

**The one rule: Qt widgets and dialogs may only be touched from the GUI thread.** Breaking it causes random crashes that are hard to reproduce. Use one of these:

- a Qt **signal** emitted from the worker thread, as `VersionChecker.update_available` does,
- `GuiThreadDispatcher.call(function)` or `.wrap(function)`, as the hotkeys do,
- **polling from a `QTimer`**, as the connection follow-up does with `connection_status()`.

`handle_playbacks()` runs on the websocket thread but only sends MIDI, which is why it does not need any of this.

---

## MIDI flow and Config Mode

Physical messages and on-screen clicks go through the same path:

- `MidiController.poll()` reads pending messages from both inputs and passes each to `note_loop(message, device_id)`.
- On-screen pads and faders call `imitate_midi_message()`, which builds a `mido.Message` and calls `note_loop()` too.

In `note_loop()`:

| Message | Normal mode | Config Mode |
|---|---|---|
| `note_on` / `note_off` on a bound pad | `send_playback_click()` with `pressed = velocity == 127`, then a state poll | `note_on` starts `link_executor_note()` |
| `control_change` on a bound fader | `control_change_handler()`: scales 0-127 to 0-1 and sends it if changed | `_config_mode_fader_touched()` |

### Config Mode state

Config Mode must never block the GUI thread, because the MIDI poll and the window both run there. Three pieces of state make it work:

- **`_link_in_progress`** is `True` while a modal prompt is open. A modal dialog runs a nested event loop, so the MIDI poll keeps firing. `note_loop()` drops every message while this flag is set, which also prevents re-entrant prompts.
- **`_pending_color_link`** holds a pad binding waiting for its color. The palette is shown, and the next `note_on` from either controller or the window resolves it in `_finish_color_pick()`. Leaving Config Mode or loading a profile clears it.
- **`_fader_last_config_touch`** maps `(device_id, cc)` to the time of the last message from that fader. A fader sends a stream of messages while it moves, so only a message arriving after `FADER_SETTLE_SECONDS` of silence opens a prompt. The timer restarts when the prompt closes.

### Note numbers

| Notes / CC | Control | Constant |
|---|---|---|
| 0-63 | 8×8 grid, 0 is bottom-left | `NORMAL_BUTTON_NOTES` |
| 100-107 | Buttons under the grid (red LEDs) | `SPECIAL_BUTTON_NOTES` |
| 112-119 | Buttons right of the grid (green LEDs) | `SPECIAL_BUTTON_NOTES` |
| 122 | Shift | `SHIFT_KEY` |
| CC 48-56 | Faders, 56 is the master | `FADER_CONTROLS` |

Pad LEDs are set with a `note_on` whose **velocity is the color** (0-127, see `NOTE_COLOR_MAP` for the RGB equivalents used on screen). The **MIDI channel is the LED mode**: 0-6 steady brightness, 7-10 pulsing, 11-15 blinking. Special buttons only use channel 0 with velocity 0 (off), 1 (on) or 2 (blink).

---

## The dot2 Web Remote protocol

All of it lives in `web_socket_handler.py`. The protocol is not officially documented. This is what the handler does:

1. Connect to `ws://<host>/?ma=1` with the header `Origin: http://<host>`.
2. The console sends `{"status": "server ready"}`. Answer `{"session": 0}`.
3. The console sends a session id. If `forceLogin` is set, send a `login` request with user `remote` and the **MD5 hex** of the password.
4. The console answers `{"responseType": "login", "result": true}` (or `false`).
5. Send `{"session": <id>}` every 10 s to keep the session alive.

| Request | Used by | Purpose |
|---|---|---|
| `playbacks_userInput` with `buttonId`, `pressed`, `released` | `send_playback_click()` | Press or release an executor button |
| `playbacks_userInput` with `faderValue` (0-1) | `send_playback_fader()` | Move an executor fader |
| `playbacks` | `poll_exec_state()` | Ask which executors are running |

Every request carries `"session"`. Responses are dispatched to callbacks registered with `on(key, callback)` (persistent) or `once(key, callback)` (one shot). The key matches either a key of the JSON message or its `responseType` value.

`connection_status()` returns `connected`, `login_failed`, `unreachable` (refused or dropped) or `connecting`. The GUI polls it rather than receiving callbacks, see [Threads](#threads).

Reconnecting creates a new `WebSocketApp`. Callbacks from the previous one are ignored through `_is_current(ws)`, and each connection has its own heartbeat stop event, so a late callback from an old socket cannot corrupt the new state.

---

## Executor feedback (blinking)

The console cannot return every executor in one request, so `poll_exec_state()` sends **two**: B-wing executors first, then F-wing. F-wing answers carry `"responseSubType": 2`, which is how the two are told apart.

`handle_playbacks()` therefore receives each poll in two halves:

1. The B-wing half is stored in `temporary_exec_states`.
2. The F-wing half is merged with it, giving the full set of running executors.
3. The **symmetric difference** with the previous set gives the executors that changed. Only their pads are updated, through `toggle_blink_note()`.

`executor_note_dictionary` is the reverse lookup used here: `executor_index -> [[note, device_id], ...]`. Rebuild it with `initiate_executor_note_dictionary()` whenever bindings change.

---

## Profiles and settings

### Profile files

A profile is a JSON file validated by `profile_manager.validate_profile_data()` before anything is loaded. `load_profile()` raises `ProfileError` with a readable list of problems, and leaves the current state untouched when the file is invalid.

`executor_index` is **0-based**: the user types the console's executor number and the app stores it minus 1. The same convention applies to pads and faders.

To **add a field** to the profile format:

1. Add it to `TOP_LEVEL_FIELDS` (expected type) and `BLANK_PROFILE` (default) in `profile_manager.py`.
2. If it describes the setup rather than the show, add it to `SETUP_FIELDS` so new profiles inherit it.
3. Read it in `MidiController._apply_profile_data()`.
4. Existing profiles will now fail validation because the field is missing. Either make validation accept its absence, or migrate old files when reading them. Do not ship a change that silently breaks users' profiles.

`MidiController` reads and writes the file with `_read_data_file()` / `_write_data_file()`. Writes are read-modify-write of the whole file.

### App settings

`AppSettings` stores the profiles folder and the last profile in the user configuration folder (`QStandardPaths.GenericConfigLocation` + `Am_I_Dot2`). A missing or broken settings file silently falls back to defaults.

User data never lives in the app folder, which is replaced on every update.

---

## The GUI

### Generated files: never edit by hand

| Source | Generated file | Command |
|---|---|---|
| `gui/am_i_dot2_V2.ui` | `packages/gui_main_window.py` | `pyside6-uic gui/am_i_dot2_V2.ui -o packages/gui_main_window.py` |
| `gui/resources.qrc` | `resources_rc.py` | `pyside6-rcc gui/resources.qrc -o resources_rc.py` |

Change the `.ui` in Qt Designer, then regenerate. Any manual edit to a generated file is lost on the next regeneration. Use the `pyside6-uic` matching the PySide6 version in `requirements.txt`.

### Widget names

| Widgets | Wing-1 | Wing-2 |
|---|---|---|
| Pads and buttons | `button<note>_4` | `button<note>_6` |
| Faders | `fader<cc>_4` | `fader<cc>_6` |
| Fader buttons | `pushButton_fader<cc>_4` | `pushButton_fader<cc>_6` |
| Wing containers | `wing_1` | `wing_2` |

`MainApp.__init__` maps them into dictionaries keyed by note or CC: `wing1_buttons`, `wing2_faders`, and so on. Keep these names when editing the `.ui`, or update the dictionaries.

### Pad colors

A pad's permanent color is stored as the Qt property `bg_color` and applied as a stylesheet. Temporary colors, like the palette, change the stylesheet only, and `restore_permanent_button_color()` puts the property back. After changing a stylesheet, call `_repolish()` so Qt re-applies it.

### Adding a menu action

1. Add the action in Qt Designer and regenerate.
2. Add it to `self.menu` in `MainApp.__init__` under its menu, for example `"tools": {"my_action": self.ui.actionMyAction}`.
3. Map it to a method in `_build_menu_actions()`, for example `("tools", "my_action"): self.do_something`.

Actions not listed in `_build_menu_actions()` do nothing. Currently that is Refresh Profile, Contact Help and the Wing Enabled toggles.

---

## Errors and messages

| Situation | Use |
|---|---|
| A bug or an unexpected failure | `error_handler.show_error()`: adds "contact the developer" and optional technical details |
| A mistake the user can fix (bad name, file in use...) | `input_prompts.show_warning()` |
| Information | `input_prompts.show_info()` |
| Destructive action | `input_prompts.confirm_destructive_action()`: Yes/No, then typing `CONFIRM` |
| Asking for text or a number | `input_prompts.ask_text()` / `ask_number()`, which return `None` when cancelled |

Uncaught exceptions on any thread reach `install_global_exception_hook()`, which shows them in a `show_error()` box on the GUI thread. In windowed builds `sys.stderr` is `None`, so never write to it unguarded.

---

## Testing

There is no automated test suite yet. Changes so far have been checked with throwaway scripts that run the real app without hardware:

- set `QT_QPA_PLATFORM=offscreen` so no window appears,
- put fake `mido`, `keyboard` and `websocket` modules into `sys.modules` **before** importing `main`,
- replace blocking dialogs (`QInputDialog.getText`, `MidiPortDialog.ask_ports`, `ask_retry_connection`...) with functions returning scripted answers,
- create `MainApp(settings=AppSettings(settings_folder=<temp dir>))` with a temporary profiles folder, so real user data is never touched.

```python
import os, sys, types, tempfile
os.environ["QT_QPA_PLATFORM"] = "offscreen"

class FakePort:
    def __init__(self, name): self.name, self.pending = name, []
    def send(self, message): pass
    def iter_pending(self):
        while self.pending: yield self.pending.pop(0)
    def close(self): pass

fake_mido = types.ModuleType("mido")
fake_mido.get_input_names = fake_mido.get_output_names = lambda: ["a"]
fake_mido.open_input = fake_mido.open_output = FakePort
fake_mido.Message = lambda **kw: types.SimpleNamespace(**kw)
sys.modules["mido"] = fake_mido
# ... same idea for "keyboard" (add_hotkey) and "websocket" (WebSocketApp)

from PySide6.QtWidgets import QApplication
app = QApplication([])
import main
from packages.app_settings import AppSettings
from packages.dialogs import midi_port_dialog
midi_port_dialog.MidiPortDialog.ask_ports = classmethod(lambda cls, *a, **k: ("a", "a"))

settings = AppSettings(settings_folder=tempfile.mkdtemp())
settings.profiles_folder = tempfile.mkdtemp()
window = main.MainApp(settings=settings)
```

Turning these scripts into a `pytest` suite would be a valuable contribution.

Always test the real thing too: a cold start with both controllers, a console connection, a pad press, and a blinking executor.

---

## Building

PyInstaller cannot cross-compile: **build the Windows version on Windows**. From the project folder, in PowerShell:

```powershell
py -m venv .venv-build
.venv-build\Scripts\Activate.ps1
pip install -r requirements-build.txt
pyinstaller main.py --name Am_I_Dot2 --windowed --onedir --noconfirm --clean --icon media/gui_icons/ma_logo.png --add-data "data/data.json;data" --hidden-import mido.backends.rtmidi
```

The app is in `dist\Am_I_Dot2\`. Zip and ship **the whole folder**.

| Option | Why |
|---|---|
| `--windowed` | No console window. `sys.stdout` and `sys.stderr` are `None` in this mode |
| `--onedir` | Starts faster and is flagged less by antivirus software than `--onefile` |
| `--hidden-import mido.backends.rtmidi` | mido imports its backend dynamically, PyInstaller cannot see it |
| `--add-data "data/data.json;data"` | Starter profile for first runs. Drop it to make new users start blank. **It ships whatever is in `data/data.json`**, including the console IP and password |
| `--icon ...png` | Pillow converts it to `.ico` |

If `pip` tries to compile `python-rtmidi` from source, there is no prebuilt package for that Python version yet. Use the previous Python version for the build.

---

## Releasing

1. Set `APP_VERSION` in `packages/app_info.py`, for example `"1.0.1"` or `"1.1.0-beta"`.
2. Commit, then build on Windows.
3. Create a GitHub release with the tag `v` + version, for example `v1.0.1`, and attach the zip.

How the update checker reads versions (`version_checker.py`):

- It asks GitHub for the **latest release**, which ignores drafts and releases marked **pre-release**. Leave "pre-release" unticked on betas that existing users should be told about.
- Versions compare number by number: `1.10.0` is newer than `1.9.2`, and `1.0` equals `1.0.0`.
- Anything after the numbers marks a pre-release, which ranks below the same final version: `1.0.0` is newer than `1.0.0-beta`.
- Two pre-releases with the same numbers are **equal**. Give each beta its own number.
- If the tag is newer than `APP_VERSION` inside a build, every user of that build sees "update available" at each start. Always bump `APP_VERSION` before building a release.

Network errors are ignored on purpose: no internet must never mean an error at startup.

---

## Code conventions

- **Small helpers over long functions.** If a block needs a comment to explain what it does, it probably wants to be a named function.
- **New file rather than a longer one** when a feature is self-contained. Dialogs go in `packages/dialogs/`.
- **Section banners** in long files:

  ```python
  # =================================================================
  #                          Section name
  # =================================================================
  ```

- **Signals are connected with `functools.partial` and keyword arguments**, for example `partial(self._on_button_pressed, note=note, device_id=1)`.
- **Constants** are `UPPER_CASE` at module or class level, with a comment giving the unit (`# in milliseconds`).
- **Docstrings explain why**, not only what, especially for anything thread-related or timing-related.
- **Blocking work never runs on the GUI thread.** Use timers, threads plus signals, or state machines like Config Mode.

---

## Gotchas

| Gotcha | Explanation |
|---|---|
| **Resizing after `hide()`** | Qt recalculates layouts later. Defer the resize with `QTimer.singleShot(0, ...)`, then `activate()` **both** the central layout and the window's own layout (`self.layout()`), otherwise `resize()` is clamped to the old minimum size. See `MainApp._shrink_to_content()` |
| **Maximum window size** | A maximum size on the main window greys out the maximize button on Windows. Leave it unset in Qt Designer |
| **Modal dialogs and the MIDI poll** | `exec()` runs a nested event loop, so `poll()` keeps running while a dialog is open. Guard state with flags like `_link_in_progress` |
| **`load_json()` vs `load_profile()`** | `load_json()` re-reads the current file and keeps the runtime `config_mode`. `load_profile()` validates and fully switches profile |
| **`config_mode` in the file** | It is read on profile load but never written. Leave it at `0` |
| **MIDI ports on Windows** | Only one program can open a port. Opening fails if dot2 onPC or another tool uses it |
| **`keyboard` on Linux** | Needs root. Its hotkeys are global, they fire even when the window is not focused |
| **F11 restore** | Restores the most recent `data_backup_*.json` in `<profiles folder>/../backups`, whichever profile it came from |
| **Two GUI toolkits** | Only Qt is used. Do not reintroduce tkinter dialogs: they do not mix with the Qt event loop |
