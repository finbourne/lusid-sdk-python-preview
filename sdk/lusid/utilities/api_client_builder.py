from urllib.request import pathname2url

import requests
from urllib3 import make_headers

import lusid
from .proxy_config import format_proxy_schema
from .api_configuration_loader import ApiConfigurationLoader
from .refreshing_token import RefreshingToken


class ApiClientBuilder:

    @staticmethod
    def build(api_secrets_filename=None, okta_response_handler=None, api_configuration=None):
        """
        :param api_secrets_filename: name api configuration file
        :param api_configuration: populated ApiConfiguration, if supplied this is used in preference to api_secrets_filename
        :param okta_response_handler: optional function to handle Okta response
        :return: ApiClient correctly configured with credentials and host
        """

        # Load the configuration
        configuration = api_configuration if api_configuration is not None else ApiConfigurationLoader().load(
            api_secrets_filename)

        encoded_password = pathname2url(configuration.password)
        encoded_client_id = pathname2url(configuration.client_id)
        encoded_client_secret = pathname2url(configuration.client_secret)

        # Prepare our authentication request
        token_request_body = f"grant_type=password&username={configuration.username}" \
                             f"&password={encoded_password}&scope=openid client groups offline_access" \
                             f"&client_id={encoded_client_id}&client_secret={encoded_client_secret}"
        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # extra request args
        kwargs = {"headers": headers}

        # use proxy if supplied
        proxy_config = configuration.proxy_config
        if proxy_config is not None:
            kwargs["proxies"] = format_proxy_schema(proxy_config.address, proxy_config.username, proxy_config.password)

        # use certificate if supplied
        if configuration.certificate_filename is not None:
            kwargs["verify"] = configuration.certificate_filename

        # make request to Okta to get an authentication token
        okta_response = requests.post(configuration.token_url, data=token_request_body, **kwargs)

        if okta_response_handler is not None:
            okta_response_handler(okta_response)

        # Ensure that we have a 200 response code
        if okta_response.status_code != 200:
            raise ValueError(okta_response.json())

        # convert the json encoded response to be able to extract the token values
        okta_json = okta_response.json()

        # Retrieve our api token from the authentication response
        api_token = RefreshingToken(token_url=configuration.token_url,
                                    client_id=encoded_client_id,
                                    client_secret=encoded_client_secret,
                                    initial_access_token=okta_json["access_token"],
                                    initial_token_expiry=okta_json["expires_in"],
                                    refresh_token=okta_json["refresh_token"])

        # Initialise our API client using our token so that we can include it in all future requests
        config = lusid.Configuration()
        config.access_token = api_token
        config.host = configuration.api_url

        # set the cert
        config.ssl_ca_cert = configuration.certificate_filename

        # set the proxy for LUSID if needed
        if configuration.proxy_config is not None:
            config.proxy = configuration.proxy_config.address
            if proxy_config.username is not None and proxy_config.password is not None:
                config.proxy_headers = make_headers(proxy_basic_auth=f"{proxy_config.username}:{proxy_config.password}")

        return lusid.ApiClient(config, header_name="X-LUSID-Application", header_value=configuration.app_name)
