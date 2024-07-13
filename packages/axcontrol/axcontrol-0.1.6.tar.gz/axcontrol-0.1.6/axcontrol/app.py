import signal
import sys
import tkinter as tk
from axcontrol.gui.app import create_gui
from axcontrol.automation import init_control_finder
from axcontrol.code_generator import CodeGenerator
from axcontrol.listeners import InputListener


def signal_handler(signal, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    root = tk.Tk()
    root.title("AxControl App")
    root.resizable(True, True)

    code_generator = CodeGenerator()
    gui = create_gui(root)
    control_finder_manager = init_control_finder(root, gui.overlay, code_generator)
    listener = InputListener(control_finder_manager)
    gui.set_input_listener(listener)

    root.mainloop()


if __name__ == "__main__":
    main()
