from pynput import mouse, keyboard


class InputListener:
    def __init__(self, control_finder_manager):
        self.listener = None
        self.keyboard_listener = None
        self.control_finder_manager = control_finder_manager
        self.ctrl_pressed = False

    def on_move(self, x, y):
        print(f"Pointer moved to {(x, y)}")

    def on_click(self, x, y, button, pressed):
        if pressed and self.ctrl_pressed:
            self.control_finder_manager.generate_code("Left-Click", x, y)

    def on_scroll(self, x, y, dx, dy):
        print(f"Scrolled {dx}, {dy} at {(x, y)}")

    def on_press(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            print("ctrl pressed")
            self.ctrl_pressed = True

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False

    def start(self):
        self.listener = mouse.Listener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll
        )
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()
        self.keyboard_listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
