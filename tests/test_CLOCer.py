from unittest import TestCase
from clocer.CLOCer import CLOCer


class TestCLOCer(TestCase):
    def test_run(self):
        CLOCer.run("https://github.com/ISNTI0/Windows_SeleniumJar")
