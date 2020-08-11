from urllib.request import pathname2url

import requests

from .refreshing_token import RefreshingToken


class ClientCredentialsFlowProvider:

    def __init__(self, configuration, okta_response_handler):
        """
        :param ApiConfiguration configuration: The configuration to use
        :param typing.callable okta_response_handler: An optional function to handle the Okta response
        """
        self.configuration = configuration
        self.okta_response_handler = okta_response_handler

    def get_auth_token(self):
        """
        Get an authentication token

        :return: RefreshingToken api_token: A refreshing API token
        """

        # Encode credentials that may contain special characters
        encoded_password = pathname2url(self.configuration.password)
        encoded_client_id = pathname2url(self.configuration.client_id)
        encoded_client_secret = pathname2url(self.configuration.client_secret)

        # Prepare our authentication request
        token_request_body = f"grant_type=password&username={self.configuration.username}" \
                             f"&password={encoded_password}&scope=openid client groups offline_access" \
                             f"&client_id={encoded_client_id}&client_secret={encoded_client_secret}"

        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # extra request args
        kwargs = {"headers": headers}

        if self.configuration.proxy_config is not None:
            kwargs["proxies"] = self.configuration.proxy_config.format_proxy_schema()

        # use certificate if supplied
        if self.configuration.certificate_filename is not None:
            kwargs["verify"] = self.configuration.certificate_filename

        # make request to Okta to get an authentication token
        okta_response = requests.post(self.configuration.token_url, data=token_request_body, **kwargs)

        if self.okta_response_handler is not None:
            self.okta_response_handler(okta_response)

        # Ensure that we have a 200 response code
        if okta_response.status_code != 200:
            raise ValueError(okta_response.json())

        # convert the json encoded response to be able to extract the token values
        okta_json = okta_response.json()

        # Retrieve our api token from the authentication response
        api_token = RefreshingToken(token_url=self.configuration.token_url,
                                    client_id=encoded_client_id,
                                    client_secret=encoded_client_secret,
                                    initial_access_token=okta_json["access_token"],
                                    initial_token_expiry=okta_json["expires_in"],
                                    refresh_token=okta_json["refresh_token"],
                                    proxies=kwargs.get("proxies", None),
                                    certificate_filename=kwargs.get("verify", None))

        return api_token
