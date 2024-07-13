import unittest
from axcontrol.automation.control_finder import ControlFinder
from mocked_control_tree import (
    create_control,
    create_control_tree,
    test_control_tree,
    test_control_tree_with_children_of_same_type,
)


class TestFindFastestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_nt = test_control_tree
        return super().setUp()

    def test_find_last_element(self):
        target = create_control(
            {
                "ControlTypeName": "TextControl",
                "Name": "Status",
                "AutomationId": "StatusTextId",
                "ClassName": "TextClass",
                "Children": [],
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘StatusBar{N:Status Bar;A:StatusBarId;C:StatusBarClass;I:0;}➘Text{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path

    def test_find_sibling(self):
        target = create_control(
            {
                "ControlTypeName": "ButtonControl",
                "Name": "Open",
                "AutomationId": "OpenButtonId",
                "ClassName": "ButtonClass",
                "Children": [],
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘ToolBar{N:Tool Bar;A:ToolBarId;C:ToolBarClass;I:0;}➘Button{N:Open;A:OpenButtonId;C:ButtonClass;I:1;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path

    def test_find_nothing(self):
        target = create_control(
            {
                "ControlTypeName": "NotExistingControl",
                "Name": "Pictures",
                "AutomationId": "PicturesFolderId",
                "ClassName": "TreeItemClass",
                "Children": [],
            }
        )
        expected_path = "Target control not found"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path

    def test_find_nested_controltype(self):
        """by design a path to nested controls can only return the path to the deepest matching control"""
        target = create_control(
            {
                "ControlTypeName": "NestedTextControl",
                "Name": "Status",
                "AutomationId": "StatusTextId",
                "ClassName": "TextClass",
                "Children": [],
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        expected_path_too_short = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        diff_path = "➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}➘NestedText{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert expected_path.replace(expected_path_too_short, "", 1) == diff_path
        assert path == expected_path

    def test_find_single_child_control(self):
        target = create_control(
            {
                "ControlTypeName": "TextControl",
                "Name": "Status",
                "AutomationId": "StatusTextId",
                "ClassName": "TextClass",
                "Children": [],
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘StatusBar{N:Status Bar;A:StatusBarId;C:StatusBarClass;I:0;}➘Text{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path

    def test_find_minimal_child_control(self):
        target = create_control(
            {
                "ControlTypeName": "ImageControl",
                "Name": None,
                "AutomationId": None,
                "ClassName": None,
                "Children": None,
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘Pane{N:Main Content;A:MainContentId;C:PaneClass;I:0;}➘Edit{N:Text Editor;A:TextEditorId;C:EditClass;I:0;}➘Image{I:0;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path

    def test_find_with_parantheses(self):
        target = create_control(
            {
                "ControlTypeName": "RegressionControl",
                "Name": "Etwas mit „Mit Farbe füllen“ zum test",
                "AutomationId": "StatusTextId",
                "ClassName": "TextClass",
                "Children": [],
            }
        )
        expected_path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘Regression{N:Etwas mit „Mit Farbe füllen“ zum test;A:StatusTextId;C:TextClass;I:0;}"
        path = ControlFinder.find_fastest_path(self.test_data_nt, target)
        assert path == expected_path


class TestFindControlFromPath(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_nt = test_control_tree
        return super().setUp()

    def test_find_control(self):
        control_tree = create_control_tree(
            {
                "ControlTypeName": "TextControl",
                "Name": "Status",
                "AutomationId": "StatusTextId",
                "ClassName": "TextClass",
                "Children": [],
            }
        )
        path = "Text{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        control = ControlFinder.find_control_from_path(
            path=path, root_control=control_tree
        )
        assert control.Name == "Status"

    def test_find_last_element(self):
        control_tree = create_control_tree(
            {
                "ControlTypeName": "WindowControl",
                "Name": "Main Window",
                "AutomationId": "MainWindowId",
                "ClassName": "WindowClass",
                "Children": [
                    {
                        "ControlTypeName": "TextControl",
                        "Name": "Status",
                        "AutomationId": "StatusTextId",
                        "ClassName": "TextClass",
                        "Children": [],
                    }
                ],
            }
        )
        path = "Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘Text{N:Status;A:StatusTextId;C:TextClass;I:0;}"
        control = ControlFinder.find_control_from_path(
            path=path, root_control=control_tree
        )
        assert control.Name == "Status"

    def test_find_minimal_element(self):
        path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘Pane{N:Main Content;A:MainContentId;C:PaneClass;I:0;}➘Edit{N:Text Editor;A:TextEditorId;C:EditClass;I:0;}➘Image{I:0;}"
        control = ControlFinder.find_control_from_path(
            path=path, root_control=self.test_data_nt
        )
        assert control.ControlTypeName == "ImageControl"

    def test_find_with_parantheses(self):
        path = "Desktop{N:Desktop;A:Desktop;C:DesktopClass;I:0;}➘Window{N:Main Window;A:MainWindowId;C:WindowClass;I:0;}➘Regression{N:Etwas mit „Mit Farbe füllen“ zum test;A:StatusTextId;C:TextClass;I:0;}"
        control = ControlFinder.find_control_from_path(
            path=path, root_control=self.test_data_nt
        )
        assert control.Name == "Etwas mit „Mit Farbe füllen“ zum test"


class TestGetNthOfType(unittest.TestCase):
    def test_get_nth_child_of_type(self):
        control = ControlFinder.get_nth_child_of_type(
            test_control_tree_with_children_of_same_type, "TreeItemControl", 1
        )
        assert control.Name == "Documents"


# manual timeit timing tests

# import uiautomation as auto
# import timeit
# from axcontrol.automation.control_finder import ControlFinder


# def run():
#     for i in range(5):
#         desktop_icon_path = "Pane{C:WorkerW;I:3;}➘Pane{C:SHELLDLL_DefView;I:0;}➘List{A:1;C:SysListView32;I:0;}➘ListItem{N:FortiClient VPN;I:2;}"
#         path_user = "Pane{N:FortiClient - Zero Trust Fabric Agent;C:Chrome_WidgetWin_1;I:2;}➘Document{N:FortiClient -- Zero Trust Fabric Agent;A:10312640;C:Chrome_RenderWidgetHostHWND;I:0;}➘Group{I:0;}➘Group{A:app;I:0;}➘Group{I:2;}➘Group{A:vpn;I:0;}➘Group{A:vpn-disconnected;I:0;}➘Group{A:vpn-connection-info;I:1;}➘Group{A:vpn-username-container;I:1;}➘Edit{N:Benutzername;A:vpn-username;I:0;}"
#         path_pass = "Pane{N:FortiClient - Zero Trust Fabric Agent;C:Chrome_WidgetWin_1;I:2;}➘Document{N:FortiClient -- Zero Trust Fabric Agent;A:10312640;C:Chrome_RenderWidgetHostHWND;I:0;}➘Group{I:0;}➘Group{A:app;I:0;}➘Group{I:2;}➘Group{A:vpn;I:0;}➘Group{A:vpn-disconnected;I:0;}➘Group{A:vpn-connection-info;I:1;}➘Group{I:2;}➘Group{I:0;}➘Edit{N:Passwort;A:vpn-password;I:0;}"
#         path_close = "Pane{N:FortiClient - Zero Trust Fabric Agent;C:Chrome_WidgetWin_1;I:2;}➘TitleBar{I:0;}➘Button{N:Schließen;I:2;}"
#         ControlFinder.find_control_from_path(desktop_icon_path).DoubleClick()
#         ControlFinder.find_control_from_path(path_user).GetValuePattern().SetValue(
#             "this is a vpn username1"
#         )
#         ControlFinder.find_control_from_path(path_pass).GetValuePattern().SetValue(
#             "12345678"
#         )
#         ControlFinder.find_control_from_path(path_close).Click()


# timeit.timeit(
#     "run()",
#     globals=globals(),
#     number=1,
# )
# 30.591993000009097
# 29.627071099821478
# 29.819780700141564

# import uiautomation as auto
# import timeit


# def run():
#     for i in range(5):
#         auto.ListItemControl(Name='FortiClient VPN').DoubleClick()
#         auto.EditControl(Name="Benutzername").GetValuePattern().SetValue(
#             "this is a vpn username2"
#         )
#         auto.EditControl(Name="Passwort").GetValuePattern().SetValue("12345678")
#         auto.ButtonControl(Name="Schließen").Click()


# timeit.timeit(
#     "run()",
#     globals=globals(),
#     number=1,
# )
# # # 37.05387669999618
# # # 36.37181310006417
