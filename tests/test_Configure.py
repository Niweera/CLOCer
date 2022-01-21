from unittest import TestCase
from unittest.mock import patch
from clocer.Configure import Configure
from os.path import exists, abspath, join, dirname, realpath
from clocer.CustomExceptions import ConfigureError


class TestConfigure(TestCase):
    def test_check_cloc(self):
        Configure.check_cloc()

    def test_setup_output(self):
        Configure.setup_output()
        output_path: str = abspath(
            join(dirname(dirname(realpath(__file__))), "clocer", "output")
        )
        self.assertTrue(exists(output_path))

    def test_install_cloc(self):
        Configure.install_cloc()

    def test_setup_output_fail(self):
        actual_error_msg = "Mock error occurred"
        with patch.object(Configure, "setup_output", return_value=None) as get_mock:
            with self.assertRaises(ConfigureError):
                get_mock.side_effect = ConfigureError(actual_error_msg)
                Configure.setup_output()
