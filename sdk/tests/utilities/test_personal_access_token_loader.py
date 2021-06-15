import unittest
from pathlib import Path
from lusid.utilities.personal_access_token import PersonalAccessTokenLoader


class PersonalAccessTokenLoaderTest(unittest.TestCase):
    """
    These test ensure that the PersonalAccessTokenLoader works as expected
    """

    @classmethod
    def setUpClass(cls):
        cls.config_keys_path = Path(__file__).parent.parent.parent.joinpath('lusid/utilities/config_keys.json')

    def test_access_token_is_returned(self):
        pat = PersonalAccessTokenLoader(self.config_keys_path).pat
        self.assertIsNotNone(pat)
