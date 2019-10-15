from lusid import ApiClientBuilder
from utilities import CredentialsSource


class TokenUtilities:

    @staticmethod
    def get_okta_tokens():
        original_token = ""
        refresh_token = ""

        def extract_refresh_token(okta_response):
            nonlocal refresh_token
            nonlocal original_token

            okta_json = okta_response.json()
            refresh_token = okta_json["refresh_token"]
            original_token = okta_json["access_token"]

        ApiClientBuilder().build(
            CredentialsSource.secrets_path(),
            extract_refresh_token
        )

        return original_token, refresh_token
