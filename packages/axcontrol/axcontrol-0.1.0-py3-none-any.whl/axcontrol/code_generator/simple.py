from string import Template


class CodeGenerator:
    def __init__(self, output_file="generated_code.py"):
        self.output_file = output_file
        self.file_initialized = False
        self.verified_control_path = None

    def initialize_file(self):
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(
                "from axcontrol.automation.control_finder import ControlFinder\n\n"
            )
        self.file_initialized = True

    def write_template(self, event_type, x, y):
        if not self.file_initialized:
            self.initialize_file()

        if event_type == "Left-Click":
            template = Template("ControlFinder.find_control_from_path('$path').Click()")
        else:
            template = Template("ControlFinder.find_control_from_path('$path')")

        if self.verified_control_path:
            with open(self.output_file, "a", encoding="utf-8") as file:
                file.write(template.substitute(path=self.verified_control_path) + "\n")

    def set_verified_control_path(self, path):
        self.verified_control_path = path
