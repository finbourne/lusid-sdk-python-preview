import unittest
from time import sleep

from lusid.utilities import ApiConfigurationLoader
from lusid.utilities import RefreshingToken
from utilities import CredentialsSource
from utilities import TokenUtilities as tu


class TokenRefresh(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

    def test_get_token(self):
        original_token, refresh_token = tu.get_okta_tokens()

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        self.assertIsNotNone(refreshed_token)
        self.assertEqual(original_token, refreshed_token)

    def test_refreshed_token_when_expired(self):
        original_token, refresh_token = tu.get_okta_tokens()

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=1,  # 1s expiry
                                          refresh_token=refresh_token,
                                          expiry_offset=3599)  # set to 1s expiry

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertNotEqual(first_value, refreshed_token)

    def test_token_when_not_expired_does_not_refresh(self):
        original_token, refresh_token = tu.get_okta_tokens()

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertEqual(first_value, refreshed_token)

    def test_can_make_header(self):
        original_token, refresh_token = tu.get_okta_tokens()

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        header = "Bearer " + refreshed_token

        self.assertIsNotNone(header)
