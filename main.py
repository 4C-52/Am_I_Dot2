"""Entry point: sets up the MidiController and starts the main loop."""

from midi_controller import MidiController


def main():
    controller = MidiController()
    controller.setup()
    controller.run()


if __name__ == "__main__":
    main()