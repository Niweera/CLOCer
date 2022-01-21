from unittest import TestCase
from clocer.CLOCer import CLOCer
import json
from os.path import exists, abspath, join, dirname, realpath
from unittest.mock import patch
from clocer.CustomExceptions import CLOCerError


class TestCLOCer(TestCase):
    def test_setup(self):
        CLOCer.setup()

    def test_setup_fail(self):
        actual_error_msg = "Mock error occurred"
        with patch.object(CLOCer, "setup", return_value=None) as get_mock:
            with self.assertRaises(CLOCerError):
                get_mock.side_effect = CLOCerError(actual_error_msg)
                CLOCer.setup()

    def test_run(self):
        url = "https://github.com/Niweera/cpu-meter"
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
