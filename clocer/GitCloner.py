from git import Repo
import shutil
import logging
from os.path import abspath, join, dirname, realpath, exists
from clocer.CustomExceptions import CloneError
from os import mkdir
import requests


class GitCloner:
    """
    Class for cloning GitHub repositories
    """

    @staticmethod
    def clone_repo(url: str) -> None:
        try:
            temp_path: str = abspath(join(dirname(realpath(__file__)), "temp"))
            clone_path: str = abspath(join(temp_path, "clone"))

            if not exists(temp_path):
                mkdir(temp_path)

            if exists(clone_path):
                shutil.rmtree(clone_path)

            response = requests.get(url)
            response.raise_for_status()

            Repo.clone_from(url=url, to_path=clone_path)
            logging.info(f"cloned {url} into {clone_path}")
            return
        except Exception as e:
            raise CloneError(e)

    @staticmethod
    def clean_up():
        try:
            clone_path = abspath(join(dirname(realpath(__file__)), "temp", "clone"))
            if exists(clone_path):
                shutil.rmtree(clone_path)
                logging.info(f"cleaned up in {clone_path}")
        except Exception as e:
            raise CloneError(e)
