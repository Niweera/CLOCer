import shutil
from unittest import TestCase
from unittest.mock import patch, Mock
from git import Repo
from clocer.CustomExceptions import CloneError
from clocer.GitCloner import GitCloner
from os.path import exists, abspath, join, dirname, realpath


class TestGitCloner(TestCase):
    def setUp(self) -> None:
        self.url = "https://github.com/Niweera/cpu-meter"

    def tearDown(self) -> None:
        GitCloner.clean_up()

    def test_clone_repo(self):
        actual_url = self.url
        GitCloner.clone_repo(actual_url)

        clone_path = abspath(
            join(dirname(dirname(realpath(__file__))), "clocer", "temp", "clone")
        )
        self.assertTrue(exists(clone_path))

        cloned_repo = Repo(clone_path)
        test_url = cloned_repo.remotes[0].config_reader.get("url")
        self.assertEqual(test_url, actual_url)

    def test_clone_repo_fail(self):
        temp_path: str = abspath(
            join(dirname(dirname(realpath(__file__))), "clocer", "temp")
        )
        clone_path: str = abspath(join(temp_path, "clone"))

        with patch("clocer.GitCloner.exists", Mock(return_value=True)):
            if not exists(clone_path):
                with self.assertRaises(CloneError):
                    GitCloner.clone_repo(self.url)

        with patch("clocer.GitCloner.exists", Mock(return_value=False)):
            if exists(temp_path):
                with self.assertRaises(CloneError):
                    GitCloner.clone_repo(self.url)

    def test_clean_up_fail(self):
        with patch("clocer.GitCloner.exists", Mock(return_value=True)), patch.object(
            shutil, "rmtree"
        ) as get_mock, self.assertRaises(CloneError):
            get_mock.side_effect = Exception("Mock error occurred in shutil.rmtree()")
            GitCloner.clean_up()
