<p align="center">
  <img src="media/dot2_apc_logo.png" alt="Am I Dot2 logo" width="320">
</p>

# Am I Dot2 ?

**Am I Dot2** turns one or two **Akai APC mini mk2** controllers into a playback surface for an **MA Lighting dot2** console or dot2 onPC.

Normally you would type a MIDI note command into every executor, and the pads would still not tell you what is running. Am I Dot2 talks to the console through its **Web Remote** instead:

- each pad triggers the executor you bind to it, and lights up in the color you choose,
- pads **blink while their executor is running** on the console,
- the faders drive the console's playback faders,
- a window on your computer mirrors both controllers, with labels on the pads, so you can also play the show with the mouse.

Every show gets its own **profile**, so switching from one show to the next takes two clicks.

> ⚠️ Am I Dot2 is in **beta**. Keep a backup of your show file and of your profiles.

---

## Contents

- [What you need](#what-you-need)
- [Installation](#installation)
- [First setup](#first-setup)
- [Everyday use](#everyday-use)
- [Common mistakes](#common-mistakes)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [Known limitations](#known-limitations)
- [More documentation](#more-documentation)

---

## What you need

| | |
|---|---|
| **Controller** | One or two Akai APC mini mk2, connected by USB |
| **Console** | An MA dot2 console, or dot2 onPC |
| **Network** | The computer and the console on the same network (not needed when dot2 onPC runs on the same computer) |
| **Computer** | Windows for the ready-made version. Linux and macOS can run it from the source code |

---

## Installation

### Windows (recommended)

1. Open the [Releases page](https://github.com/4C-52/Am_I_Dot2/releases) and download the Windows zip of the latest version.
2. Extract the zip anywhere, for example in `Documents\Am I Dot2`.
3. Run `Am_I_Dot2.exe` from the extracted folder.

The app is not signed yet, so Windows SmartScreen may show a warning the first time. Click **More info**, then **Run anyway**.

Keep the whole folder together: the `.exe` does not work on its own.

### From the source code (Linux, macOS, Windows)

You need Python 3.10 or newer.

```bash
git clone https://github.com/4C-52/Am_I_Dot2.git
cd Am_I_Dot2
python -m venv .venv
# Windows: .venv\Scripts\activate      Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

> ⚠️ On Linux, the keyboard shortcuts need administrator rights, so start the app with `sudo python main.py`.

> ⚠️ Install `python-rtmidi`, not `rtmidi`. They are different packages and only `python-rtmidi` works. `requirements.txt` already gets the right one.

### Updating

When a new version is out, the app tells you at startup. Download the new zip and replace the old app folder.

Your profiles and settings are stored outside the app folder, so nothing needs to be set up again.

---

## First setup

### 1. Enable the Web Remote on the console

On the dot2, open **Setup > Global Settings**. Turn the **Web Remote** on, set its **password**, and note the console's **IP address**.

![Where to find the Web Remote password and the IP address](media/find_dot2_webremote_password_and_ip.gif)

### 2. Plug in the controllers and start the app

Plug the APC mini mk2 controllers in **before** starting Am I Dot2.

On the first start, the app asks which MIDI ports belong to **controller 1** (Wing-1) and **controller 2** (Wing-2). For each controller, pick the port whose name contains **"Control"**, for both the input and the output.

Only have one controller? Pick it for controller 1 and click **Cancel** for controller 2.

### 3. Enter the console's address and password

Open **Settings > Preferences**:

- **Dot2 password**: the Web Remote password from step 1. The MD5 line under it is filled in automatically.
- **IP address**: the console's IP address from step 1. If dot2 onPC runs on this same computer, try `127.0.0.1`.

Click **OK**. The status bar at the bottom of the window shows **"Connected to the dot2"** when everything is right.

### 4. Create a profile for your show

Open **Settings > Profiles** and click **New...**, or use **File > New**. Name it after your show.

Read [Managing profiles](docs/MANAGING_PROFILES.md) for where to keep them and how to back them up.

### 5. Bind your executors

Turn on **Tools > Config Mode**, press a pad, type the executor number, and pick a color.

[Configuring Am I Dot2](docs/CONFIGURING_AM_I_DOT2.md) explains every step, including faders and labels.

---

## Everyday use

1. Turn on the console and plug in the controllers.
2. Start Am I Dot2. It reopens the last profile you used and connects to the console.
3. Play your show: pads trigger their executors, and the pads of running executors blink.

To switch shows, use **Settings > Profiles** or **File > Open**.

To hide one of the on-screen wings, use the **Wings** menu. The window shrinks to fit.

---

## Common mistakes

| Problem | Likely cause and fix |
|---|---|
| **"Cannot connect to the dot2"** | The console is off, on another network, or its IP address changed. Check **Setup > Global Settings** on the console, then **Settings > Preferences** in the app, and click **Retry**. |
| **The console refuses the login** | The password in **Settings > Preferences** does not match the Web Remote password on the console. Passwords are case-sensitive. |
| **The Web Remote is off** | The app cannot connect even with the right IP address. Enable the Web Remote in **Setup > Global Settings**. |
| **The pads stay dark or the wrong pads react** | The wrong MIDI port was chosen. Pick the port containing **"Control"** in **Settings > Preferences > Controller 1 / Controller 2**. |
| **The two controllers are swapped** | Press **F1** to swap them for this session. To fix it for good, choose the ports again in **Settings > Preferences**. |
| **"The MIDI ports could not be opened"** | Another program is using the controller. On Windows only one program can use a MIDI port at a time: close dot2 onPC's MIDI input for this controller, DAWs, or other controller tools, then try again. |
| **Pads trigger executors twice** | The controller is also set up in the console's own MIDI settings. Remove it there; Am I Dot2 does the job through the Web Remote. |
| **Controller plugged in after starting the app** | The app only looks for controllers at startup and in Preferences. Choose the ports in **Settings > Preferences**, or restart the app. |
| **Pressing a pad asks for an executor number** | Config Mode is on. Turn it off in **Tools > Config Mode**, or press **F2**. |
| **"The profile could not be opened"** | The file is not an Am I Dot2 profile, or it was damaged by hand editing. The message lists what is wrong. See [Managing profiles](docs/MANAGING_PROFILES.md). |
| **The keyboard shortcuts do nothing (Linux)** | The keyboard library needs root on Linux. Start the app with `sudo`. |
| **Windows says the app is unsafe** | The app is not signed yet. Click **More info**, then **Run anyway**. |

Something else? Open an [issue](https://github.com/4C-52/Am_I_Dot2/issues) and include the details shown in the error message.

---

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| **F1** | Swap controller 1 and controller 2 (until the app is closed) |
| **F2** | Turn Config Mode on or off |
| **F11** | Restore the last backup into the current profile (asks twice) |
| **F12** | Remove the colors of every pad (makes a backup first, asks twice) |

> ⚠️ These shortcuts are **global**: they also work when another program has the focus. Avoid pressing them while typing elsewhere.

---

## Known limitations

- Only the APC mini mk2 has been tested.
- Only the first executor page of the console is controlled.
- Fader positions are not read back from the console.
- The executor bound to a pad can only be changed by editing the profile file, see [Configuring Am I Dot2](docs/CONFIGURING_AM_I_DOT2.md#changing-or-removing-a-binding).

---

## More documentation

- [Configuring Am I Dot2](docs/CONFIGURING_AM_I_DOT2.md): binding executors to pads and faders, colors and labels.
- [Managing profiles](docs/MANAGING_PROFILES.md): where to keep profiles, backups and good habits.
- [Developer documentation](docs/DEVELOPER.md): how the code works, building and releasing.

Enjoy! 😊
