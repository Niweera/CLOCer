import subprocess
from unittest import TestCase
from unittest.mock import patch, Mock
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

    def test_check_cloc_fail(self):
        with patch.object(subprocess, "check_output") as get_mock:
            get_mock.side_effect = subprocess.CalledProcessError(1, "Mock command")
            Configure.check_cloc()

    def test_install_cloc_fail(self):
        mock = Mock()
        mock.returncode = Mock(return_value=1)

        with patch.object(subprocess, "run") as get_mock:
            get_mock.return_value = mock
            with self.assertRaises(ConfigureError):
                Configure.install_cloc()

    def test_setup_output_fail(self):
        with patch("clocer.Configure.exists", Mock(return_value=False)):
            output_path: str = abspath(
                join(dirname(dirname(realpath(__file__))), "clocer", "output")
            )
            if exists(output_path):
                with self.assertRaises(ConfigureError):
                    Configure.setup_output()
