import subprocess
from unittest import TestCase
from clocer.CLOCer import CLOCer
import json
from os.path import exists, abspath, join, dirname, realpath
from unittest.mock import patch, Mock

from clocer.Configure import Configure
from clocer.CustomExceptions import CLOCerError, ConfigureError


class TestCLOCer(TestCase):
    def setUp(self) -> None:
        self.url = "https://github.com/Niweera/cpu-meter"

    def test_setup(self):
        CLOCer.setup()

    def test_setup_fail(self):
        actual_error_msg = "Mock ConfigureError occurred in Configure.setup_output()"
        with patch.object(Configure, "setup_output", return_value=None) as get_mock:
            get_mock.side_effect = ConfigureError(actual_error_msg)
            with self.assertRaises(CLOCerError):
                CLOCer.setup()

    def test_run(self):
        url = self.url
        repo_name = url.replace("https://github.com/", "").replace("/", "_")

        CLOCer.setup()
        CLOCer.run(url)

        output_path: str = abspath(
            join(
                dirname(dirname(realpath(__file__))),
                "clocer",
                "output",
                f"{repo_name}.json",
            )
        )
        fixture_path: str = abspath(
            join(
                dirname(dirname(realpath(__file__))),
                "tests",
                "fixtures",
                f"{repo_name}.json",
            )
        )

        with open(output_path, "r") as test_file:
            test_result = json.load(test_file)
            test_result.pop("header", None)

        with open(fixture_path, "r") as fixture_file:
            actual_result = json.load(fixture_file)
            actual_result.pop("header", None)

        self.assertTrue(exists(output_path))
        self.assertDictEqual(test_result, actual_result)

    def test_run_fail(self):
        mock = Mock()
        mock.returncode = Mock(return_value=1)
        CLOCer.setup()

        with patch.object(subprocess, "run") as get_mock:
            get_mock.return_value = mock
            with self.assertRaises(CLOCerError):
                CLOCer.run(self.url)
