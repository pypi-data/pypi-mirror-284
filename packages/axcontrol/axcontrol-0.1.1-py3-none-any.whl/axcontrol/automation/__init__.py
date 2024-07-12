import uiautomation as auto
from .control_finder_manager import ControlFinderManager


def init_control_finder(root, overlay, code_generator):
    auto.uiautomation.SetGlobalSearchTimeout(0.5)
    control_finder_manager = ControlFinderManager(root, overlay, code_generator)
    root.after(100, control_finder_manager.find_and_highlight_control)
    return control_finder_manager
