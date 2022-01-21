import logging
import subprocess
from os.path import abspath, realpath, join, dirname
from platform import system
from clocer.Configure import Configure
from clocer.CustomExceptions import CLOCerError
from clocer.GitCloner import GitCloner


class CLOCer:
    """
    Main Class for CLOCer
    """

    @staticmethod
    def setup():
        try:
            assert system() == "Linux", "CLOCer only supports Linux platforms"
            Configure.check_cloc()
            Configure.setup_output()
            logging.info("CLOCer initiated")
        except Exception as e:
            raise CLOCerError(e)

    @staticmethod
    def run(url):
        try:
            GitCloner.clone_repo(url)

            repo_name = url.replace("https://github.com/", "").replace("/", "_")
            clone_path = abspath(join(dirname(realpath(__file__)), "temp", "clone"))
            output_file = abspath(
                join(dirname(realpath(__file__)), "output", f"{repo_name}.json")
            )

            result = subprocess.run(
                ["cloc", clone_path, "--hide-rate", "--json", f"--out={output_file}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            if result.returncode == 0:
                logging.info("Successfully CLOCered")
                GitCloner.clean_up()
            else:
                raise Exception("Error occurred in CLOCering")
        except Exception as e:
            raise CLOCerError(e)
