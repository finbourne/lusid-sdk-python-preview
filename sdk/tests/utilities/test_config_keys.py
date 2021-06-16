import unittest

from lusid.utilities import ConfigKeys

from utilities import CredentialsSource


class TestConfigKeys(unittest.TestCase):

    def test_config_keys(self):

        config_keys = ConfigKeys.get()
        self.assertGreater(len(config_keys), 0)
        self.assertDictEqual(ConfigKeys.get(), CredentialsSource.fetch_config_keys())