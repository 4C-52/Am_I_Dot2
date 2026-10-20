# Managing profiles

A **profile** is one file holding everything Am I Dot2 needs for a show:

- which executor each pad, button and fader triggers,
- the color and labels of each pad,
- the console's IP address and Web Remote password,
- the MIDI ports of both controllers,
- the pad brightness and blink style.

Profiles are plain `.json` files. You can copy, rename, back up and email them like any other file.

---

## Contents

- [Where profiles are stored](#where-profiles-are-stored)
- [Creating, opening, renaming and deleting](#creating-opening-renaming-and-deleting)
- [What a profile remembers](#what-a-profile-remembers)
- [Good practice](#good-practice)
- [Backing up your profiles](#backing-up-your-profiles)
- [The built-in backups](#the-built-in-backups)
- [Moving to another computer](#moving-to-another-computer)
- [When a profile cannot be opened](#when-a-profile-cannot-be-opened)
- [Profile file reference](#profile-file-reference)

---

## Where profiles are stored

By default, profiles live in:

| System | Profiles folder |
|---|---|
| Windows | `Documents\Am_I_Dot2\profiles` |
| Linux / macOS | `~/Documents/Am_I_Dot2/profiles` |

On the very first start, the app creates `default.json` there.

To use another folder, open **Settings > Profiles**, click **Browse...**, choose the folder and click **OK**. That folder then becomes the one **File > New** and **File > Open** start in.

The app also keeps a small settings file, separate from the profiles, with the profiles folder and the last profile you opened:

| System | Settings file |
|---|---|
| Windows | `%LOCALAPPDATA%\Am_I_Dot2\settings.json` |
| Linux | `~/.config/Am_I_Dot2/settings.json` |

Both are outside the app folder, so **updating the app never touches your profiles**.

---

## Creating, opening, renaming and deleting

Everything is in **Settings > Profiles**:

| Button | What it does |
|---|---|
| **Browse...** | Chooses the profiles folder |
| **Profile** list | Lists the profiles of that folder. Pick one and click **OK** to load it. The loaded profile is marked **(loaded)** |
| **New...** | Creates a blank profile in the profiles folder |
| **Rename...** | Renames the selected profile. Renaming the loaded profile is fine, the app follows it |
| **Delete** | Moves the selected profile to the recycle bin, after asking twice. The loaded profile cannot be deleted: load another one first |

New, Rename and Delete act on the disk **immediately**. Clicking **Cancel** afterwards does not undo them.

You can also use:

- **File > New** to create a profile anywhere you like, with the file explorer,
- **File > Open** to open a profile from anywhere, for example from a USB stick.

When the app starts, it reopens the last profile you used.

---

## What a profile remembers

| Saved in the profile | Changed with |
|---|---|
| Pad, button and fader bindings, colors and labels | Config Mode, see [Configuring Am I Dot2](CONFIGURING_AM_I_DOT2.md) |
| Console IP address and Web Remote password | **Settings > Preferences** |
| MIDI ports of controller 1 and controller 2 | **Settings > Preferences** |
| Pad brightness and blink style | Editing the file, see the [reference](#profile-file-reference) |

Two things are worth knowing:

- **Preferences only change the loaded profile.** If you change the console's IP address, your other profiles keep their own. Loading another profile connects with that profile's address and password.
- **A new profile starts with the current setup.** It copies the console address, password, MIDI ports, brightness and blink style of the loaded profile, with no bindings. When you switch profiles, the controllers that are already open stay in use and are saved into the profile you loaded.

---

## Good practice

### Give profiles a dedicated, easy-to-reach folder

Keep **all** your profiles in **one** folder that you can find in a hurry, and never mix them with other files.

- The default `Documents\Am_I_Dot2\profiles` is a good choice.
- If you already organize your shows in a folder, for example `Documents\Shows`, make a `Profiles` subfolder there and choose it with **Browse...**.
- Pin the folder to **Quick access** in the Windows file explorer, so it is one click away.
- Avoid the Desktop, the Downloads folder and the app folder itself. The app folder is replaced on every update.

### Name profiles clearly

A good name tells you the show, the venue and when, at a glance:

```
2026-11-14_Bal-de-promo_Salle-des-fetes.json
Theatre-Municipal_Generic-rig.json
Concert-Jazz_Repetition.json
```

- Put the **date first** (year-month-day) if you do many one-off shows: the list then sorts in order.
- Use the same name as the dot2 show file, so you always know which profile goes with which show.
- Letters, numbers, spaces, dashes and underscores are safe. The app refuses characters Windows does not allow, like `/` or `?`.

### Keep a copy before big changes

Before reworking a profile, copy it in the file explorer, for example `My show.json` to `My show - before rework.json`. If the new layout does not work out, open the copy.

### One profile per rig, not per day

If you play the same venue with the same rig often, keep one profile for it and reuse it, rather than creating a new one every time.

### Do not share your password by accident

The Web Remote password is stored **in clear text** in the profile. Before sending a profile to someone else or posting it online, remove it from `dot2_password` or change it.

---

## Backing up your profiles

A profile represents hours of work. Losing it right before a show is the classic disaster. Pick at least one of these:

- **Use a synced folder (recommended).** Put the profiles folder inside OneDrive, Dropbox or Google Drive, then choose it in **Settings > Profiles > Browse...**. Every change is copied to the cloud automatically. Avoid working on the same profile from two computers at the same time.
- **Copy to a USB stick before each show.** Copy the whole profiles folder. If the show computer dies, any other computer with Am I Dot2 can open the profile from the stick with **File > Open**.
- **Keep a dated archive.** After a show, copy the folder to an archive, for example `Archives\2026-11-14 profiles`. You can always come back to the exact state of a past show.

Whatever you choose, **test a backup now and then**: open a copied profile with **File > Open** and check that the pads come up right.

---

## The built-in backups

Pressing **F12** (remove all pad colors) first saves a backup of the loaded profile. **F11** restores the most recent of these backups into the loaded profile.

They are stored in a `backups` folder **next to** the profiles folder: with the default location, that is `Documents\Am_I_Dot2\backups`. They are named after the date and time, for example `data_backup_2026-10-21_14h05.json`.

> ⚠️ These backups are **not** a backup strategy:
>
> - they are only made when you press F12,
> - **F11 restores the most recent backup, whichever profile it came from**. If you pressed F12 on profile A and then on profile B, pressing F11 on profile A copies B's content into it.
>
> Use them to undo an F12, right away and on the same profile. For anything else, use the copies described above.

To restore an older backup by hand, copy it from the `backups` folder into the profiles folder, give it a clear name, and open it with **File > Open**.

---

## Moving to another computer

1. Install Am I Dot2 on the new computer.
2. Copy your profiles into its profiles folder, or choose the folder where you copied them with **Settings > Profiles > Browse...**.
3. Open the profile.
4. MIDI port names often differ between computers. If the saved ports are not found, the app asks you to choose them. You can also choose them in **Settings > Preferences**.
5. If the console has another IP address on this network, change it in **Settings > Preferences**.

---

## When a profile cannot be opened

The app checks every profile before loading it. If the file is damaged or is not an Am I Dot2 profile, it shows what is wrong and **keeps the current profile loaded**. Nothing is lost.

This usually happens after editing a file by hand: a missing comma, a missing quote, or a number written as text. Fix the line the message points to, or go back to your copy.

If the last used profile cannot be opened at startup, the app creates a blank profile instead and tells you where it is. Your broken file is left untouched so you can fix it.

---

## Profile file reference

You never need to edit a profile by hand for normal use. This reference is for advanced settings and for fixing files.

| Field | Meaning |
|---|---|
| `default_ip_address` | Console IP address |
| `dot2_password` | Web Remote password, in clear text |
| `DEFAULT_MIDI_INPORT_DEVICE1`, `DEFAULT_MIDI_OUTPORT_DEVICE1` | MIDI input and output of controller 1 |
| `DEFAULT_MIDI_INPORT_DEVICE2`, `DEFAULT_MIDI_OUTPORT_DEVICE2` | MIDI input and output of controller 2 |
| `default_brightness_level` | Brightness of lit pads, see below. Default `6` |
| `default_blink_channel` | How pads of running executors flash, see below. Default `10` |
| `config_mode` | Leave at `0` |
| `note_executor_dictionary_device1`, `..._device2` | Pad and button bindings of each controller, see [Configuring Am I Dot2](CONFIGURING_AM_I_DOT2.md#changing-or-removing-a-binding) |
| `cc_fader_index_dictionary_device1`, `..._device2` | Fader bindings of each controller |

The two LED settings use the APC mini mk2's own LED modes:

| Value | LED behavior |
|---|---|
| `0` to `6` | Steady, from dimmest (`0`) to full brightness (`6`) |
| `7` to `10` | Pulsing, from fastest (`7`) to slowest (`10`) |
| `11` to `15` | Blinking, from fastest (`11`) to slowest (`15`) |

`default_brightness_level` should stay between `0` and `6`. `default_blink_channel` can be any value from `7` to `15`.

After editing, save the file and reopen it with **File > Open**.
