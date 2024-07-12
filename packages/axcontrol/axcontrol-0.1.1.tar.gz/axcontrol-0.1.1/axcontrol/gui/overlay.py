import win32gui
import win32con
import win32api
import threading
import time
import queue


class SimpleOverlay:
    def __init__(self, stop_event):
        self.hwnd = None
        self.current_shape = None
        self.lock = threading.Lock()
        self.stop_event = stop_event
        self.running = True
        self.command_queue = queue.Queue()

    def create_window(self):
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.wnd_proc
        wc.lpszClassName = "SimpleOverlayWindow"
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)

        class_atom = win32gui.RegisterClass(wc)

        style = win32con.WS_POPUP | win32con.WS_VISIBLE
        ex_style = (
            win32con.WS_EX_COMPOSITED
            | win32con.WS_EX_LAYERED
            | win32con.WS_EX_TRANSPARENT
            | win32con.WS_EX_TOPMOST
        )

        self.hwnd = win32gui.CreateWindowEx(
            ex_style,
            class_atom,
            "Simple Overlay",
            style,
            0,
            0,
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
            0,
            0,
            0,
            None,
        )

        win32gui.SetLayeredWindowAttributes(
            self.hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY
        )

    def wnd_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_PAINT:
            hdc, paint_struct = win32gui.BeginPaint(hwnd)
            self.draw(hdc)
            win32gui.EndPaint(hwnd, paint_struct)
            return 0
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def draw(self, hdc):
        mem_dc = win32gui.CreateCompatibleDC(hdc)
        bitmap = win32gui.CreateCompatibleBitmap(
            hdc,
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
        )
        old_bitmap = win32gui.SelectObject(mem_dc, bitmap)

        brush = win32gui.CreateSolidBrush(win32api.RGB(0, 0, 0))
        win32gui.FillRect(
            mem_dc,
            (
                0,
                0,
                win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
                win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
            ),
            brush,
        )
        win32gui.DeleteObject(brush)

        with self.lock:
            if self.current_shape:
                left, top, right, bottom, color = self.current_shape
                color_rgb = self.color_to_rgb(color)
                pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(*color_rgb))
                old_pen = win32gui.SelectObject(mem_dc, pen)
                win32gui.SelectObject(
                    mem_dc, win32gui.GetStockObject(win32con.NULL_BRUSH)
                )
                win32gui.Rectangle(mem_dc, left, top, right, bottom)
                win32gui.SelectObject(mem_dc, old_pen)
                win32gui.DeleteObject(pen)

        win32gui.BitBlt(
            hdc,
            0,
            0,
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
            mem_dc,
            0,
            0,
            win32con.SRCCOPY,
        )

        win32gui.SelectObject(mem_dc, old_bitmap)
        win32gui.DeleteObject(bitmap)
        win32gui.DeleteDC(mem_dc)

    def color_to_rgb(self, color):
        colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "purple": (128, 0, 128),
            "cyan": (0, 255, 255),
            "white": (255, 255, 255),
        }
        return colors.get(
            color.lower(), (255, 0, 0)
        )  # Default to red if color not found

    def draw_rect(self, left, top, right, bottom, color):
        self.command_queue.put(("draw", (left, top, right, bottom, color)))

    def clear(self):
        self.command_queue.put(("clear", None))

    def process_commands(self):
        try:
            while True:
                command, args = self.command_queue.get_nowait()
                if command == "draw":
                    with self.lock:
                        self.current_shape = args
                elif command == "clear":
                    with self.lock:
                        self.current_shape = None
                self.redraw()
                self.command_queue.task_done()
        except queue.Empty:
            pass

    def redraw(self):
        if self.hwnd:
            win32gui.InvalidateRect(self.hwnd, None, True)

    def run(self):
        self.create_window()
        while not self.stop_event.is_set():
            self.process_commands()
            win32gui.PumpWaitingMessages()
            time.sleep(0.01)  # Small sleep to reduce CPU usage
        if self.hwnd:
            win32gui.DestroyWindow(self.hwnd)
