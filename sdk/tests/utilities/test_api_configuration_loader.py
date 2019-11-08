import json
import os
import unittest
from pathlib import Path
from unittest.mock import patch

from lusid import ApiConfigurationLoader
from utilities import CredentialsSource


class ApiConfigurationLoaderTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.credentials = CredentialsSource.secrets_path()

        if os.path.isfile(cls.credentials):
            with open(cls.credentials, "r") as secrets_file:
                cls.secrets = json.load(secrets_file)

                cls.env_vars = {
                    "FBN_TOKEN_URL": cls.secrets["api"].get("tokenUrl", None),
                    "FBN_USERNAME": cls.secrets["api"].get("username", None),
                    "FBN_PASSWORD": cls.secrets["api"].get("password", None),
                    "FBN_CLIENT_ID": cls.secrets["api"].get("clientId", None),
                    "FBN_CLIENT_SECRET": cls.secrets["api"].get("clientSecret", None),
                    "FBN_LUSID_API_URL": cls.secrets["api"].get("apiUrl", None),
                    "FBN_APP_NAME": cls.secrets["api"].get("applicationName", None)
                }

        else:
            cls.env_vars = {
                "FBN_TOKEN_URL": os.getenv("FBN_TOKEN_URL"),
                "FBN_USERNAME": os.getenv("FBN_USERNAME"),
                "FBN_PASSWORD": os.getenv("FBN_PASSWORD"),
                "FBN_CLIENT_ID": os.getenv("FBN_CLIENT_ID"),
                "FBN_CLIENT_SECRET": os.getenv("FBN_CLIENT_SECRET"),
                "FBN_LUSID_API_URL": os.getenv("FBN_LUSID_API_URL"),
                "FBN_APP_NAME": os.getenv("FBN_APP_NAME")
            }

        if None in cls.env_vars.values():
            assert False, "Source test configuration missing values from both secrets file and environment variables"

    def assert_config_file_values(self, config):
        # use assertTrue to avoid leaking details when assertion fails
        self.assertTrue(config.token_url == self.secrets["api"]["tokenUrl"])
        self.assertTrue(config.username == self.secrets["api"]["username"])
        self.assertTrue(config.password == self.secrets["api"]["password"])
        self.assertTrue(config.client_id == self.secrets["api"]["clientId"])
        self.assertTrue(config.client_secret == self.secrets["api"]["clientSecret"])
        self.assertTrue(config.api_url == self.secrets["api"]["apiUrl"])
        self.assertTrue(config.app_name == self.secrets["api"].get("applicationName", ""))

    def test_load_from_environment_vars(self):
        with patch.dict('os.environ', self.env_vars):
            config = ApiConfigurationLoader.load()

            # use assertTrue to avoid leaking details when assertion fails
            self.assertTrue(config.token_url == self.env_vars["FBN_TOKEN_URL"])
            self.assertTrue(config.username == self.env_vars["FBN_USERNAME"])
            self.assertTrue(config.password == self.env_vars["FBN_PASSWORD"])
            self.assertTrue(config.client_id == self.env_vars["FBN_CLIENT_ID"])
            self.assertTrue(config.client_secret == self.env_vars["FBN_CLIENT_SECRET"])
            self.assertTrue(config.api_url == self.env_vars["FBN_LUSID_API_URL"])
            self.assertTrue(config.app_name == self.env_vars["FBN_APP_NAME"])

    def test_load_from_config_file(self):

        if not os.path.isfile(self.credentials):
            self.skipTest(f"missing secrets file: {CredentialsSource.secrets_path()}")

        config = ApiConfigurationLoader.load(self.credentials)
        self.assert_config_file_values(config)

    def test_missing_from_config_file_throws(self):

        secrets = Path(__file__).parent.parent.joinpath('secrets.missing.json')

        if not os.path.isfile(secrets):
            self.skipTest(f"missing secrets file: {secrets}")

        with self.assertRaises(ValueError) as ex, patch.dict('os.environ', clear=True):
            ApiConfigurationLoader.load(secrets)

        self.assertEqual(ex.exception.args[0], "Trying to load config from secrets file but missing: username,password")

    def test_missing_env_vars_uses_config_file(self):

        if not os.path.isfile(self.credentials):
            self.skipTest(f"missing secrets file: {CredentialsSource.secrets_path()}")

        env_vars = self.env_vars
        env_vars.pop("FBN_TOKEN_URL")

        with patch.dict('os.environ', self.env_vars):
            config = ApiConfigurationLoader.load(self.credentials)
            self.assert_config_file_values(config)

    def test_no_config_throws(self):

        with self.assertRaises(ValueError) as ex, patch.dict('os.environ', clear=True):
            ApiConfigurationLoader.load()

        self.assertEqual(ex.exception.args[0],
                         'Path to secrets file not specified and missing the following environment variables: FBN_TOKEN_URL,FBN_LUSID_API_URL,FBN_USERNAME,FBN_PASSWORD,FBN_CLIENT_ID,FBN_CLIENT_SECRET')
