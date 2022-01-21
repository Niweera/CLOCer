from unittest import TestCase
from clocer.Configure import Configure
from clocer.CustomExceptions import ConfigureError
from os.path import exists, abspath, join, dirname, realpath


class TestConfigure(TestCase):
    def test_check_cloc(self):
        try:
            Configure.check_cloc()
        except ConfigureError:
            self.fail("Configure.check_cloc() raised ConfigureError")

    def test_setup_output(self):
        Configure.setup_output()
        output_path: str = abspath(
            join(dirname(dirname(realpath(__file__))), "clocer", "output")
        )
        self.assertTrue(exists(output_path))
