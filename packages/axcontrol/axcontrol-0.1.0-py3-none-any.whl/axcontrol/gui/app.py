import threading
import time
import tkinter as tk
from tkinter import ttk
from axcontrol.utils.clipboard import copy_to_clipboard
from axcontrol.gui.overlay import SimpleOverlay


class GUI:
    def __init__(self, root):
        self.root = root
        self.input_listener = None

        self._overlay_thread_stop_event = threading.Event()
        self.overlay = SimpleOverlay(self._overlay_thread_stop_event)
        self._overlay_thread = threading.Thread(target=self.overlay.run, daemon=True)

        self._create_widgets()

    def set_input_listener(self, input_listener):
        self.input_listener = input_listener

    def _start_overlay_thread(self):
        self._overlay_thread.start()

    def _stop_overlay_thread(self):
        self._overlay_thread_stop_event.set()

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create the "Start Detection" button
        self.start_button = ttk.Button(
            main_frame, text="Start Detection", command=self.start_detection
        )
        self.start_button.grid(column=0, row=0, pady=(0, 10))

        # Create the "Stop Detection" button
        self.stop_button = ttk.Button(
            main_frame,
            text="Stop Detection",
            command=self.stop_detection,
            state=tk.DISABLED,
        )
        self.stop_button.grid(column=1, row=0, pady=(0, 10))

        # Create the text field
        text_var = tk.StringVar(value="foo")
        text_field = ttk.Entry(main_frame, textvariable=text_var)
        text_field.grid(column=0, row=1, sticky=(tk.E, tk.W))

        # Create the "Copy" button
        self.copy_button = ttk.Button(
            main_frame, text="Copy", command=lambda: copy_to_clipboard(text_var.get())
        )
        self.copy_button.grid(column=1, row=1, padx=(5, 0))

        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=0)
        main_frame.rowconfigure(0, weight=0)
        main_frame.rowconfigure(1, weight=0)

    def start_detection(self):
        self.input_listener.start()
        self._overlay_thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_detection(self):
        self.input_listener.stop()
        self._stop_overlay_thread()
        while self._overlay_thread.is_alive():
            time.sleep(0.01)  # wait for thread to stop
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)


def create_gui(root) -> GUI:
    return GUI(root)
