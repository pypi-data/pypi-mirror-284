import uiautomation as auto
from enum import Enum


class ScrollDirection(Enum):
    Down = 0
    Up = 1


def scroll_by(
    scroll_bar: auto.ScrollBarControl,
    direction: ScrollDirection = ScrollDirection.Down,
    value: int = 36.5,
) -> bool:
    # ~36.5 height is a single row (non-retina display)
    assert isinstance(
        direction, ScrollDirection
    ), "direction needs to be of type ScrollDirection"
    assert value >= 0, "value hast to be > 0, use direction arg to change direciton"
    sb = scroll_bar.GetRangeValuePattern()
    if sb.IsReadOnly:
        return
    if direction == ScrollDirection.Down:
        if sb.Value == sb.Maximum:
            return False
        if not sb.Value + value > sb.Maximum:
            sb.SetValue(sb.Value + value)
        else:
            sb.SetValue(sb.Maximum)
    else:
        if sb.Value == 0:
            return False
        if not sb.Value - value < 0:
            sb.SetValue(sb.Value - value)
        else:
            sb.SetValue(0)
    return True


def scroll_percent_abs(
    scroll_bar: auto.ScrollBarControl,
    direction: ScrollDirection = ScrollDirection.Down,
    percent: float = None,
) -> bool:  # same api as the other functions for ease of use
    assert isinstance(
        direction, ScrollDirection
    ), "direction needs to be of type ScrollDirection"
    assert percent >= 0.0 and percent <= 1.0, "percent needs to be within 0.0 and 1.0"
    sb = scroll_bar.GetRangeValuePattern()
    if sb.IsReadOnly:
        return
    value = sb.Maximum * percent
    sb.SetValue(value)


def scroll_bar_at_max(scroll_bar: auto.ScrollBarControl) -> bool:
    sb = scroll_bar.GetRangeValuePattern()
    return sb.Value == sb.Maximum


def scroll_percent(
    scroll_bar: auto.ScrollBarControl,
    direction: ScrollDirection = ScrollDirection.Down,
    percent: float = None,
) -> bool:
    assert isinstance(
        direction, ScrollDirection
    ), "direction needs to be of type ScrollDirection"
    assert percent >= 0.0 and percent <= 1.0, "percent needs to be within 0.0 and 1.0"
    sb = scroll_bar.GetRangeValuePattern()
    if sb.IsReadOnly:
        return
    value = sb.Maximum * percent
    if direction == ScrollDirection.Down:
        if sb.Value == sb.Maximum:
            return False
        if not sb.Value + value > sb.Maximum:
            sb.SetValue(sb.Value + value)
        else:
            sb.SetValue(sb.Maximum)
    else:
        if sb.Value == 0:
            return False
        if not sb.Value - value < 0:
            sb.SetValue(sb.Value - value)
        else:
            sb.SetValue(0)
    return True
