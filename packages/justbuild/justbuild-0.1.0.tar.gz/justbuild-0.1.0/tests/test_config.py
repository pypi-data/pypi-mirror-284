import unittest

from quantready import __name__ as name
from quantready.config import Config


class TestConfig(unittest.TestCase):
    def test_configclass(self):
        config = Config()
        self.assertIsInstance(config, Config, msg="config is not a Config")
        self.assertEqual(config.name, name)


if __name__ == "__main__":
    unittest.main()
