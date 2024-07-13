import ctypes


def get_screen_size() -> tuple[int, int]:
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def check_screen_size_big_enough(min: tuple[int, int]) -> bool | None:
    size = get_screen_size()
    if min[0] > size[0] or min[1] > size[1]:
        raise RuntimeError(f"Screen size needs to be at least {min[0]}x{min[1]}")
    return True
