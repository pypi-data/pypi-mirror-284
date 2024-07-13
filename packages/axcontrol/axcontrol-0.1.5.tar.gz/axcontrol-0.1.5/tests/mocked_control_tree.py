from dataclasses import dataclass, field
from typing import List, Optional

test_data = {
    "ControlTypeName": "DesktopControl",
    "Name": "Desktop",
    "AutomationId": "Desktop",
    "ClassName": "DesktopClass",
    "Children": [
        {
            "ControlTypeName": "WindowControl",
            "Name": "Main Window",
            "AutomationId": "MainWindowId",
            "ClassName": "WindowClass",
            "Children": [
                {
                    "ControlTypeName": "MenuBarControl",
                    "Name": "Menu Bar",
                    "AutomationId": "MenuBarId",
                    "ClassName": "MenuBarClass",
                    "Children": [
                        {
                            "ControlTypeName": "MenuItemControl",
                            "Name": "File",
                            "AutomationId": "FileMenuId",
                            "ClassName": "MenuItemClass",
                            "Children": [],
                        },
                        {
                            "ControlTypeName": "MenuItemControl",
                            "Name": "Edit",
                            "AutomationId": "EditMenuId",
                            "ClassName": "MenuItemClass",
                            "Children": [],
                        },
                    ],
                },
                {
                    "ControlTypeName": "ToolBarControl",
                    "Name": "Tool Bar",
                    "AutomationId": "ToolBarId",
                    "ClassName": "ToolBarClass",
                    "Children": [
                        {
                            "ControlTypeName": "ButtonControl",
                            "Name": "New",
                            "AutomationId": "NewButtonId",
                            "ClassName": "ButtonClass",
                            "Children": [],
                        },
                        {
                            "ControlTypeName": "ButtonControl",
                            "Name": "Open",
                            "AutomationId": "OpenButtonId",
                            "ClassName": "ButtonClass",
                            "Children": [],
                        },
                    ],
                },
                {
                    "ControlTypeName": "PaneControl",
                    "Name": "Main Content",
                    "AutomationId": "MainContentId",
                    "ClassName": "PaneClass",
                    "Children": [
                        {
                            "ControlTypeName": "EditControl",
                            "Name": "Text Editor",
                            "AutomationId": "TextEditorId",
                            "ClassName": "EditClass",
                            "Children": [
                                {
                                    "ControlTypeName": "ImageControl",
                                    "Name": None,
                                    "AutomationId": None,
                                    "ClassName": None,
                                    "Children": None,
                                }
                            ],
                        },
                        {
                            "ControlTypeName": "TreeViewControl",
                            "Name": "File Explorer",
                            "AutomationId": "FileExplorerTreeId",
                            "ClassName": "TreeViewClass",
                            "Children": [
                                {
                                    "ControlTypeName": "TreeItemControl",
                                    "Name": "Documents",
                                    "AutomationId": "DocumentsFolderId",
                                    "ClassName": "TreeItemClass",
                                    "Children": [],
                                },
                                {
                                    "ControlTypeName": "TreeItemControl",
                                    "Name": "Pictures",
                                    "AutomationId": "PicturesFolderId",
                                    "ClassName": "TreeItemClass",
                                    "Children": [],
                                },
                            ],
                        },
                    ],
                },
                {
                    "ControlTypeName": "StatusBarControl",
                    "Name": "Status Bar",
                    "AutomationId": "StatusBarId",
                    "ClassName": "StatusBarClass",
                    "Children": [
                        {
                            "ControlTypeName": "TextControl",
                            "Name": "Status",
                            "AutomationId": "StatusTextId",
                            "ClassName": "TextClass",
                            "Children": [],
                        }
                    ],
                },
                {
                    "ControlTypeName": "NestedTextControl",
                    "Name": "Status",
                    "AutomationId": "StatusTextId",
                    "ClassName": "TextClass",
                    "Children": [
                        {
                            "ControlTypeName": "NestedTextControl",
                            "Name": "Status",
                            "AutomationId": "StatusTextId",
                            "ClassName": "TextClass",
                            "Children": [
                                {
                                    "ControlTypeName": "NestedTextControl",
                                    "Name": "Status",
                                    "AutomationId": "StatusTextId",
                                    "ClassName": "TextClass",
                                    "Children": [],
                                }
                            ],
                        }
                    ],
                },
                {
                    "ControlTypeName": "RegressionControl",
                    "Name": "Etwas mit „Mit Farbe füllen“ zum test",
                    "AutomationId": "StatusTextId",
                    "ClassName": "TextClass",
                    "Children": [],
                },
            ],
        }
    ],
}


@dataclass
class Control:
    ControlTypeName: Optional[str]
    Name: Optional[str]
    AutomationId: Optional[str]
    ClassName: Optional[str]
    Children: List["Control"] = field(default_factory=list)
    Parent: Optional["Control"] = None

    def add_child(self, child: "Control"):
        self.Children.append(child)
        child.Parent = self

    def GetChildren(self):
        return self.Children if self.Children else []

    def GetFirstChildControl(self):
        return self.Children[0] if self.Children else None

    def GetNextSiblingControl(self):
        # todo: implement a proper method for mocked tree
        return self.Parent.Children[0] if self.Parent.Children else None

    def GetParentControl(self):
        return self.Parent

    def Exists(self, timeout=0, interval=0):
        # For testing purposes, always return True
        return True

    def __getattr__(self, name):
        if name.endswith("Control"):
            return lambda **kwargs: self._find_control(name, **kwargs)
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def _find_control(self, control_type, **kwargs):
        for child in self.Children:
            if child.ControlTypeName == control_type:
                if all(
                    self._match_property(child, key, value)
                    for key, value in kwargs.items()
                ):
                    return child
        return False

    @staticmethod
    def _match_property(control, key, value):
        if key == "searchDepth":
            return True  # Ignore searchDepth for testing purposes
        if hasattr(control, key):
            if callable(value):
                return value(getattr(control, key))
            return getattr(control, key) == value
        return False


def create_control(data: dict) -> Control:
    control = Control(
        ControlTypeName=data.get("ControlTypeName", None),
        Name=data.get("Name", None),
        AutomationId=data.get("AutomationId", None),
        ClassName=data.get("ClassName", None),
    )
    for child_data in data.get("Children") or []:
        child = create_control(child_data)
        control.add_child(child)
    return control


def create_control_tree(data: dict) -> Control:
    control = Control(
        ControlTypeName="MockedRootControl",
        Name="MockedRoot",
        AutomationId="MockedRoot",
        ClassName="MockedRootControlClass",
        Children=[create_control(data=data)],
    )
    return control


test_control_tree = create_control_tree(test_data)

test_control_tree_with_children_of_same_type = create_control(
    {
        "ControlTypeName": "TreeViewControl",
        "Name": "File Explorer",
        "AutomationId": "FileExplorerTreeId",
        "ClassName": "TreeViewClass",
        "Children": [
            {
                "ControlTypeName": "TreeItemControl",
                "Name": "Documents",
                "AutomationId": "DocumentsFolderId",
                "ClassName": "TreeItemClass",
                "Children": [],
            },
            {
                "ControlTypeName": "TreeItemControl",
                "Name": "Documents",
                "AutomationId": "DocumentsFolderId",
                "ClassName": "TreeItemClass",
                "Children": [],
            },
            {
                "ControlTypeName": "TreeItemControl",
                "Name": "Documents",
                "AutomationId": "DocumentsFolderId",
                "ClassName": "TreeItemClass",
                "Children": [],
            },
        ],
    }
)
