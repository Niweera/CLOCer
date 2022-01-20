from unittest import TestCase
from clocer.Configure import Configure


class TestConfigure(TestCase):
    def test_check_cloc(self):
        Configure.check_cloc()
