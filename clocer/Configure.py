import logging
import subprocess
from os import mkdir
from os.path import exists, abspath, join, dirname, realpath

from clocer.CustomExceptions import ConfigureError


class Configure:
    """
    Class to setup CLOC software package
    """

    @staticmethod
    def check_cloc():
        try:
            output = subprocess.check_output("cloc --version", shell=True)
            logging.info(
                "CLOC is in PATH (version: " + output.decode("UTF-8").strip("\n") + ")"
            )
            return
        except subprocess.CalledProcessError:
            try:
                logging.info("Now installing CLOC")
                result = subprocess.run(
                    ["sudo", "apt", "install", "cloc", "-y"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                if result.returncode == 0:
                    logging.info("Successfully installed CLOC")
                else:
                    raise Exception("Error occurred in installing CLOC")
            except Exception as e:
                raise ConfigureError(e)

    @staticmethod
    def setup_output():
        try:
            output_path: str = abspath(join(dirname(realpath(__file__)), "output"))
            if not exists(output_path):
                mkdir(output_path)
        except Exception as e:
            raise ConfigureError(e)
