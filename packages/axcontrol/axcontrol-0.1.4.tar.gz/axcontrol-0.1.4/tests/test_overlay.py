import threading
import time
import random
import unittest
from axcontrol.gui.overlay import SimpleOverlay


class TestOverlay(unittest.TestCase):
    def setUp(self):
        self.overlay = SimpleOverlay(stop_event=threading.Event())

    def test_color_to_rgb(self):
        self.assertEqual(self.overlay.color_to_rgb("red"), (255, 0, 0))
        self.assertEqual(self.overlay.color_to_rgb("blue"), (0, 0, 255))
        self.assertEqual(
            self.overlay.color_to_rgb("nonexistent"), (255, 0, 0)
        )  # default color

    def test_command_queue(self):
        self.overlay.draw_rect(100, 100, 200, 200, "red")
        self.overlay.clear()
        self.assertEqual(self.overlay.command_queue.qsize(), 2)
        command, args = self.overlay.command_queue.get()
        self.assertEqual(command, "draw")
        self.assertEqual(args, (100, 100, 200, 200, "red"))
        command, args = self.overlay.command_queue.get()
        self.assertEqual(command, "clear")
        self.assertEqual(args, None)


# run this manually
def stress_test_overlay():
    overlay = SimpleOverlay()
    thread = threading.Thread(target=overlay.run)
    thread.start()

    time.sleep(1)  # Wait for window creation

    colors = ["red", "blue", "green", "yellow", "purple", "cyan", "white"]

    print("Starting stress test. Press Ctrl+C to stop.")
    try:
        while True:
            left = random.randint(0, 1000)
            top = random.randint(0, 1000)
            right = left + random.randint(50, 200)
            bottom = top + random.randint(50, 200)
            color = random.choice(colors)
            overlay.draw_rect(left, top, right, bottom, color)
            time.sleep(0.05)  # Adjust this to change the frequency of updates
    except KeyboardInterrupt:
        print("Stress test stopped.")
    finally:
        overlay.stop()
        thread.join()
