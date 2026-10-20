# Configuring Am I Dot2

This guide explains how to bind dot2 executors to the pads, buttons and faders of your APC mini mk2, and how to give pads a color and a label.

Everything is saved in the **profile** that is currently open, as soon as you confirm each step. Read [Managing profiles](MANAGING_PROFILES.md) to choose where profiles live.

---

## Contents

- [Before you start](#before-you-start)
- [The controller layout](#the-controller-layout)
- [Config Mode](#config-mode)
- [Binding a pad](#binding-a-pad)
- [Binding a special button](#binding-a-special-button)
- [Binding a fader](#binding-a-fader)
- [Changing colors and labels](#changing-colors-and-labels)
- [Changing or removing a binding](#changing-or-removing-a-binding)
- [Removing all colors and restoring a backup](#removing-all-colors-and-restoring-a-backup)
- [Tips for a clean layout](#tips-for-a-clean-layout)
- [Troubleshooting](#troubleshooting)

---

## Before you start

1. The app is connected to the console: the status bar says **"Connected to the dot2"**. See the [first setup](../README.md#first-setup) if it does not.
2. The right profile is open: its name is in the window title. Create a new one with **Settings > Profiles > New...** if this is a new show.
3. Your executors already exist on the console. Am I Dot2 triggers executors, it does not create them.

### Finding an executor's number

On the console, hold the **MA** key and hover over the executor. The console shows its number. That number is what Am I Dot2 asks for.

---

## The controller layout

The window shows each controller exactly like the real one, so you can configure with the mouse or with the hardware.

| Part | What it does in Am I Dot2 | Color |
|---|---|---|
| **8×8 pad grid** | Triggers its executor | Any of the 128 palette colors |
| **Row of buttons under the grid** | Triggers its executor | Fixed (red LED) |
| **Column of buttons right of the grid** | Triggers its executor | Fixed (green LED) |
| **Shift button** | Triggers its executor | Fixed |
| **9 faders** (the last one is the master fader) | Moves its executor's fader | No LED |

In the window, each fader also has a **button under it**. It presses the button of the executor bound to that fader.

Controller 1 is **Wing-1**, controller 2 is **Wing-2**. Each has its own bindings, so pad 1 on Wing-1 and pad 1 on Wing-2 can trigger different executors.

---

## Config Mode

All binding happens in **Config Mode**. Turn it on with **Tools > Config Mode**, or press **F2**.

- Turning it **on** flashes every pad **red** for two seconds.
- Turning it **off** flashes every pad **green** for two seconds.
- The **Tools > Config Mode** checkmark shows whether it is on.

While Config Mode is on, pads and faders **do not trigger anything on the console**. Pressing them starts a binding instead.

Config Mode stays on until you turn it off, so you can bind a whole page in one go.

> ⚠️ Turn Config Mode off before the show. Otherwise every pad press opens a prompt instead of firing the executor.

---

## Binding a pad

Bind one pad of the 8×8 grid:

1. Turn on **Config Mode**.
2. **Press the pad**, on the controller or in the window.
3. **Type the executor number** and click **OK**. This step is skipped when the pad is already bound.
4. **Type a short label**, for example `Wash`. It is printed on the pad in the window. Click **Cancel** if you want no label.
5. **Type a long label**, for example `Blue wash on the stage`. It appears when the mouse rests on the pad. Leave it empty to reuse the short label.
6. **Pick a color.** Both controllers and the window now show the palette:
   - controller 1 shows colors 0 to 63,
   - controller 2 shows colors 64 to 127.

   **Press the pad that has the color you want**, on either controller or in the window. To leave the pad dark, press any button outside the 8×8 grid instead.
7. The pads go back to normal and the binding is saved.

While a prompt or the palette is open, other pad presses and fader moves are ignored, so a stray touch cannot bind the wrong thing.

---

## Binding a special button

The buttons under the grid, the buttons right of the grid and the Shift button work the same way, without the color step:

1. Turn on **Config Mode**.
2. Press the button.
3. Type the executor number, then the short and long labels.

Their LEDs have a fixed color. They light up when bound and blink while their executor runs.

---

## Binding a fader

1. Turn on **Config Mode**.
2. **Move the fader**, on the controller or in the window. A prompt opens, for example **"Fader 3 of controller 1"**.
3. **Type the executor number** and click **OK**.

A fader sends many messages while it moves, but one movement opens only **one** prompt. Everything the fader sends while the prompt is open is ignored. After the prompt closes, the fader is also ignored until it has been **still for one second**, so you can let go calmly.

To change a fader's executor, let it rest for a second, then move it again. The prompt opens with the current executor already filled in. **Cancel** keeps the current binding.

Once Config Mode is off, the fader drives its executor's fader on the console.

---

## Changing colors and labels

Press an already bound pad in Config Mode. The app keeps its executor and asks again for the labels and the color.

---

## Changing or removing a binding

Changing the **executor** of an already bound pad, or **unbinding** a pad or fader, cannot be done from the app yet. Edit the profile file instead:

1. Close Am I Dot2, or be ready to reopen the profile afterwards.
2. Make a copy of the profile file first.
3. Open the profile (a `.json` file) in a text editor such as Notepad.
4. Find the pad under `note_executor_dictionary_device1` (Wing-1) or `note_executor_dictionary_device2` (Wing-2). Pads are listed by number, `"0"` being the bottom-left pad of the grid.

```json
"note_executor_dictionary_device1": {
  "0": {
    "executor_index": 213,
    "color": 3,
    "short_label": "Wash",
    "long_label": "Blue wash on the stage"
  },
```

- To **change the executor**, change `executor_index`. It is the console's executor number **minus 1**: executor 214 is written `213`.
- To **unbind the pad**, delete its whole block, from `"0": {` to the matching `},`. Watch the commas: the last block of a list has none after it.
- Faders are under `cc_fader_index_dictionary_device1` and `..._device2`, as `"fader number": executor_index`. The first fader is `"48"`, the master fader is `"56"`.

5. Save the file, then reopen it with **File > Open** (opening the same profile again reloads it).

If you make a typing mistake, the app refuses the file and lists what is wrong, so nothing is lost. Fix the file, or go back to your copy.

---

## Removing all colors and restoring a backup

| Key | What it does |
|---|---|
| **F12** | Makes a backup of the current profile, then removes the color of every pad. The bindings and labels stay. Asks twice before doing it. |
| **F11** | Copies the most recent backup over the current profile. Asks twice before doing it. |

> ⚠️ **F11 restores the most recent backup, whichever profile it came from.** If you pressed F12 on another profile since, F11 brings back that other profile's content. See [Managing profiles](MANAGING_PROFILES.md#the-built-in-backups) before relying on it.

---

## Tips for a clean layout

- **Mirror the console.** Bind pads in the same order as the executors on the console, so the layout makes sense to anyone running the show.
- **Use color families.** For example, blue for washes, yellow for specials, red for effects. You can tell groups apart in the dark.
- **Keep short labels short.** The pads in the window are small; three to eight characters read best. Put the details in the long label.
- **Bind the master fader** to the executor you use most as a grand master.
- **Save a copy of the profile** once the layout is done (see [Managing profiles](MANAGING_PROFILES.md)).

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Pressing a pad does nothing in Config Mode | A prompt or the color palette is still open, possibly behind another window. Finish or cancel it first. |
| The prompt asks for an executor I already typed | That pad was not bound yet, or the profile was reopened from an older copy. |
| The pad stays dark after binding | No color was picked: a button outside the grid was pressed during the color step. Press the pad again in Config Mode and pick a color. |
| A fader asks for its executor again and again | It is moved in short bursts with pauses longer than one second. Move it in one go, or leave Config Mode once it is bound. |
| The pad does not blink when its executor runs | Check the connection in the status bar. Blinking needs the console connection. |
| Nothing happens on the console after binding | Config Mode is still on. Turn it off. |
