import unittest
from axcontrol.automation import checks


class TestScreensizeChecks(unittest.TestCase):
    def test_get_screen_size(self):
        (height, width) = checks.get_screen_size()
        assert isinstance(height, int)
        assert isinstance(width, int)

    def test_screen_size_big_enough(self):
        (height, width) = checks.get_screen_size()
        with self.assertRaises(RuntimeError) as _:
            checks.check_screen_size_big_enough((height + 1, width + 1))
        assert checks.check_screen_size_big_enough((height - 1, width - 1))
