import uiautomation as auto
from axcontrol.automation.control_finder import ControlFinder


class ControlFinderManager:
    def __init__(self, root, overlay, code_generator):
        self.root = root
        self.overlay = overlay
        self.code_generator = code_generator
        self.previous_control = None

    def find_and_highlight_control(self):
        control = auto.ControlFromCursor()
        if not ControlFinder.properties_match(control, self.previous_control):
            if getattr(control, "BoundingRectangle", False):
                rect = control.BoundingRectangle
                self.overlay.draw_rect(
                    rect.left, rect.top, rect.right, rect.bottom, "red"
                )
                self.previous_control = control

            path = ControlFinder.find_fastest_path(auto.GetRootControl(), control)
            if path != "Target control not found":
                control = ControlFinder.find_control_from_path(path)
                if getattr(control, "BoundingRectangle", False):
                    rect = control.BoundingRectangle
                    self.overlay.draw_rect(
                        rect.left, rect.top, rect.right, rect.bottom, "green"
                    )
                    self.previous_control = control
                    self.code_generator.set_verified_control_path(path)
        self.root.after(100, self.find_and_highlight_control)

    def generate_code(self, event_type, x, y):
        self.code_generator.write_template(event_type, x, y)
