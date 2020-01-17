import json
import tempfile
import unittest
from unittest.mock import patch

from lusid.utilities import ApiClientBuilder, ApiConfiguration


class ApiClientBuilderTests(unittest.TestCase):

    def create_temp_config(self):
        """
        Creates a populated config file created in the system temporary folder.
        The file is deleted when the file handle is closed
        :return: open file handle to the created config file
        """
        config = {
            "api": {
                "tokenUrl": "https://test_token_ul",
                "apiUrl": "https://test_api_url",
                "username": "test_username",
                "password": "test_password",
                "clientId": "test_client_id",
                "clientSecret": "test_client_secret",
                "applicationName": "test_app_name"
            }
        }

        # create tmp file with mock details
        tmp_file = tempfile.NamedTemporaryFile(mode="w+")
        config_file = tmp_file.name
        tmp_file.write(json.dumps(config))
        tmp_file.seek(0)

        return tmp_file

    @patch("requests.post")
    def test_build_client_from_file(self, mock_requests):

        with self.create_temp_config() as config_file,patch.dict('os.environ', clear=True):
            
            # mock results
            mock_requests.return_value.status_code = 200
            mock_requests.return_value.json.return_value = {
                "access_token": "mock_access_token",
                "refresh_token": "mock_refresh_token",
                "expires_in": 60
            }

            client = ApiClientBuilder.build(api_secrets_filename=config_file.name)

            self.assertEqual(client.configuration.host, "https://test_api_url")
            self.assertEqual(client.configuration.access_token, "mock_access_token")

    @patch("requests.post")
    def test_build_client_from_values(self, mock_requests):

        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = {
            "access_token": "mock_access_token",
            "refresh_token": "mock_refresh_token",
            "expires_in": 60
        }

        config = ApiConfiguration(
            token_url="https://test_token_ul",
            api_url="https://test_api_url",
            username="test_username",
            password="test_password",
            client_id="test_client_id",
            client_secret="test_client_secret",
            app_name="test_app_name"
        )

        client = ApiClientBuilder.build(api_configuration=config)

        self.assertEqual(client.configuration.host, config.api_url)
        self.assertEqual(client.configuration.access_token, "mock_access_token")

    @patch("requests.post")
    def test_build_client_from_values_in_preference_to_file(self, mock_requests):
        with self.create_temp_config() as config_file:
            # mock results
            mock_requests.return_value.status_code = 200
            mock_requests.return_value.json.return_value = {
                "access_token": "mock_access_token",
                "refresh_token": "mock_refresh_token",
                "expires_in": 60
            }

            config = ApiConfiguration(
                token_url="https://test_token_ul",
                api_url="https://values_api_url",
                username="test_username",
                password="test_password",
                client_id="test_client_id",
                client_secret="test_client_secret",
                app_name="test_app_name"
            )

            client = ApiClientBuilder.build(api_secrets_filename=config_file.name, api_configuration=config)

            self.assertEqual(client.configuration.host, "https://values_api_url")
            self.assertEqual(client.configuration.access_token, "mock_access_token")
