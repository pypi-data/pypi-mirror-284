import subprocess
import uiautomation as auto
from typing import Set, Tuple


class AppLauncher:
    @staticmethod
    def get_window_control_set() -> Set[auto.WindowControl]:
        return set(
            [
                c
                for c in auto.GetRootControl().GetChildren()
                if c.ControlType == auto.ControlType.WindowControl
            ]
        )

    @staticmethod
    def get_control_identifier(control: auto.WindowControl) -> Tuple[str, str]:
        return (control.AutomationId, control.Name)

    @staticmethod
    def get_difference(
        existing_controls: Set[auto.WindowControl],
        new_controls: Set[auto.WindowControl],
    ) -> auto.WindowControl:
        existing_ids = {
            AppLauncher.get_control_identifier(control) for control in existing_controls
        }
        new_ids = {
            AppLauncher.get_control_identifier(control) for control in new_controls
        }

        difference = new_ids - existing_ids
        diff_controls = [
            control
            for control in new_controls
            if AppLauncher.get_control_identifier(control) in difference
        ]

        assert (
            len(diff_controls) == 1
        ), f"Expected exactly one new control, but found {len(diff_controls)}"

        return diff_controls[0]

    @staticmethod
    def launch_application(path: str) -> auto.WindowControl:
        existing_controls = AppLauncher.get_window_control_set()
        subprocess.Popen(path)
        new_controls = AppLauncher.get_window_control_set()

        while len(existing_controls) >= len(new_controls):
            new_controls = AppLauncher.get_window_control_set()

        return AppLauncher.get_difference(existing_controls, new_controls)
