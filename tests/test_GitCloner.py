from unittest import TestCase
from unittest.mock import patch
from git import Repo
from clocer.CustomExceptions import CloneError
from clocer.GitCloner import GitCloner
from os.path import exists, abspath, join, dirname, realpath


class TestGitCloner(TestCase):
    def tearDown(self) -> None:
        GitCloner.clean_up()

    def test_clone_repo(self):
        actual_url = "https://github.com/Niweera/cpu-meter"
        GitCloner.clone_repo(actual_url)

        clone_path = abspath(
            join(dirname(dirname(realpath(__file__))), "clocer", "temp", "clone")
        )
        self.assertTrue(exists(clone_path))

        cloned_repo = Repo(clone_path)
        test_url = cloned_repo.remotes[0].config_reader.get("url")
        self.assertEqual(test_url, actual_url)

    def test_clean_up_fail(self):
        actual_error_msg = "Mock error occurred"
        with patch.object(GitCloner, "clean_up", return_value=None) as get_mock:
            with self.assertRaises(CloneError):
                get_mock.side_effect = CloneError(actual_error_msg)
                GitCloner.clean_up()
