from unittest import TestCase
from clocer.GitCloner import GitCloner


class TestGitCloner(TestCase):
    def tearDown(self) -> None:
        GitCloner.clean_up()

    def test_clone_repo(self):
        test_url = "https://github.com/nrako/psnode"
        GitCloner.clone_repo(test_url)
        actual_url = GitCloner.check_repo()
        self.assertEqual(test_url, actual_url)
