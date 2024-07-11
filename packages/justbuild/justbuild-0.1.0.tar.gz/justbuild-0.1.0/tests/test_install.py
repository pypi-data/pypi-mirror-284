import unittest
from subprocess import run


class TestInstall(unittest.TestCase):
    def test_library_installed(self):
        import quantready

        self.assertIsNotNone(quantready)

    def test_module(self):
        run(["python", "-m", "quantready", "--help"])

    def test_consolescript(self):
        run(["quantready", "--help"])
