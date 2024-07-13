import re
from _ctypes import COMError
import uiautomation as auto

SEPARATOR = "➘"


class ControlFinder:
    @staticmethod
    def properties_match(current_control, target_control):
        properties_to_check = ["ControlTypeName", "AutomationId", "Name", "ClassName"]

        for prop in properties_to_check:
            current_value = getattr(current_control, prop, None)
            target_value = getattr(target_control, prop, None)

            # If both controls have this property, they must match
            if current_value is not None and target_value is not None:
                if current_value != target_value:
                    return False
            # If only one control has this property, it's not a match
            elif (current_value is None) != (target_value is None):
                return False

        # If we've made it here, all existing properties match
        return True

    @staticmethod
    def build_control_path(control, index=0, properties: dict = None):
        """
        Build a detailed path string for a control.

        Args:
        control: The control object to build the path for.
        index: The provided index to append to the path (default is 0).
        properties: dict of property names value pairs to include in the path (default is None).

        Returns:
        A string representing the detailed path of the control.
        """
        if properties is None:
            properties = {
                "Name": "N",
                "AutomationId": "A",
                "ClassName": "C",
            }

        # "Control" can be removed and is included back when parsing the string
        child_path = f"{control.ControlTypeName.replace('Control','',1)}{{"

        # property names are shortened and expanded again when parsing the string
        for prop, name in properties.items():
            value = getattr(control, prop, None)
            if value:
                child_path += f"{name}:{value};"

        child_path += f"I:{index};}}"

        return child_path

    @staticmethod
    def find_fastest_path(root_control, target_control):
        # Get the parent of the target control once at the beginning
        target_parent = target_control.GetParentControl()

        def dfs(current_control, path, index_map=None, parent=None):
            if not current_control:
                return None

            if index_map is None:
                index_map = {}

            # Check if the current control matches the target
            if ControlFinder.properties_match(current_control, target_control):
                if target_parent is None or (
                    parent and ControlFinder.properties_match(parent, target_parent)
                ):
                    # Store this path as a potential result, but continue searching
                    result = path
                else:
                    result = None
            else:
                result = None

            # Create a new index map for this level
            level_index_map = {}

            # Recursively search through the children
            for child in current_control.GetChildren():
                try:
                    # Get the control type
                    control_type = child.ControlTypeName
                except COMError:
                    # continue loop on error
                    continue

                # Update the index for this control type at this level
                if control_type not in level_index_map:
                    level_index_map[control_type] = 0
                else:
                    level_index_map[control_type] += 1

                # Build the child path with the index
                child_path = ControlFinder.build_control_path(
                    child, index=level_index_map[control_type]
                )
                new_path = child_path if not path else path + SEPARATOR + child_path

                # Recursive call with the current level's index map and current control as parent
                child_result = dfs(child, new_path, level_index_map, current_control)

                # If a result was found in the child, it's deeper, so prefer it
                if child_result:
                    result = child_result

            return result

        # Start the search from the root control
        result = dfs(root_control, "", None, root_control.GetParentControl())
        return result if result else "Target control not found"

    @staticmethod
    def find_control_from_path(path, root_control=None):
        if root_control is None:
            root_control = auto.GetRootControl()

        current_control = root_control
        control_regex = re.compile(
            r"(\w+)\{(?:N:(.*?);)?(?:A:(.*?);)?(?:C:(.*?);)?(?:I:(\d+);)?\}"
        )
        control_segments = path.split(SEPARATOR)

        for segment in control_segments:
            match = control_regex.match(segment)
            if not match:
                print(f"Invalid segment: {segment}")
                return None
            control_type, name, automation_id, class_name, _ = match.groups()
            control_type += "Control"
            index = int(match.group(5)) if match.group(5) else 0

            # If we only have control type and index, use the get_nth_child_of_type logic
            if control_type and index > 0 and not (name or automation_id or class_name):
                child = ControlFinder.get_nth_child_of_type(
                    current_control, control_type, index
                )
                if not child:
                    print(f"Cannot find {index}-th child of type {control_type}")
                    return None
                current_control = child
                continue

            try:
                control_method = getattr(current_control, control_type)
            except AttributeError:
                print(
                    f"Control type '{control_type}' not found on '{current_control.ControlTypeName}'"
                )
                return None

            search_criteria = {"searchDepth": 1}
            found_automationid_digit = False
            if name:
                search_criteria["Name"] = name
            if automation_id:
                if automation_id.isdigit():
                    found_automationid_digit = True
                else:
                    search_criteria["AutomationId"] = automation_id
            if class_name:
                search_criteria["ClassName"] = class_name

            # Find all matching controls
            current_control = control_method(**search_criteria)
            if found_automationid_digit:
                if not current_control.AutomationId.isdigit():
                    print(
                        f"Cannot find {control_type} with Name='{name}' and AutomationId=isdigit() and ClassName='{class_name}'"
                    )

            if not current_control:
                print(
                    f"Cannot find {control_type} with Name='{name}' and AutomationId='{automation_id}' and ClassName='{class_name}'"
                )
                return None

        return current_control

    @staticmethod
    def get_nth_child_of_type(parent_control, control_type_name, n):
        count = 0
        child = parent_control.GetFirstChildControl()
        while child:
            if child.ControlTypeName == control_type_name:
                if count == n:
                    return child
                count += 1
            child = child.GetNextSiblingControl()
        return None
