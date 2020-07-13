from threading import Lock

from urllib3 import make_headers

from lusid import Configuration, ApiClient
from .api_configuration_loader import ApiConfigurationLoader
from .client_credentials_flow_provider import ClientCredentialsFlowProvider


class ApiClientBuilder:

    __mutex = Lock()
    __okta_responses = {}

    """
    The ApiClientBuilder is responsible for building a lusid.ApiClient. This includes obtaining an access token from
    Okta or using the provided token.

    Any validation on the inputs required to build a lusid.ApiClient is the responsibility of this ApiClientBuilder.
    """

    @staticmethod
    def __check_required_fields(object_to_check, fields):
        """
        This function checks that the provided fields on an object are populated with values other than None

        :param object_to_check: The object to check the fields (a.k.a attributes) of
        :param list[str] fields: The fields to check on the object

        :return: None
        """
        # Check for fields which have a value of None
        missing_fields = [field for field in fields if getattr(object_to_check, field) is None]

        # Raise an error if any fields have a value of None
        if len(missing_fields) > 0:
            raise ValueError(
                f"The fields {str(missing_fields)} on the {object_to_check.__class__.__name__} are set to None, "
                f"please ensure that you have provided them directly, via a secrets file or environment "
                f"variables")

    @classmethod
    def __generate_access_token(cls, configuration, okta_response_handler):
        """
        This function generates an access token by making a call to Okta

        :param ApiConfiguration configuration: The configuration to use
        :param typing.callable okta_response_handler: An optional function to handle the Okta response

        :return: RefreshingToken api_token: A refreshing API token
        """

        try:

            cls.__mutex.acquire()

            # create a simple key by concatentating all the credential values
            token_key = "_".join([x for x in configuration.__dict__.values() if x is not None and isinstance(x, str)])
            api_tokens = cls.__okta_responses.get(token_key)

            # if there isn't a token cached then get a new one from Okta
            if api_tokens is None:

                okta_response = None

                def extract_tokens(response):
                    nonlocal okta_response
                    okta_response = response

                    if okta_response_handler is not None:
                        okta_response_handler(response)

                token_provider = ClientCredentialsFlowProvider(configuration, extract_tokens)
                api_token = token_provider.get_auth_token()

                # cache the token and the corresponding okta response
                cls.__okta_responses[token_key] = (api_token, okta_response)

            else:

                # if a handler is defined, call it with the okta response for the token
                if okta_response_handler is not None:
                    okta_response_handler(api_tokens[1])

                api_token = api_tokens[0]

        finally:
            cls.__mutex.release()

        return api_token


    @classmethod
    def build(cls, api_secrets_filename=None, okta_response_handler=None, api_configuration=None, token=None):
        """
        :param str api_secrets_filename: The full path to the JSON file containing the API credentials and optional proxy details
        :param typing.callable okta_response_handler: An optional function to handle the Okta response
        :param lusid.utilities.ApiConfiguration api_configuration: A pre-populated ApiConfiguration
        :param str token: The pre-populated access token to use instead of asking Okta for a token

        :return: lusid.ApiClient: The configured LUSID ApiClient
        """

        # Load the configuration
        configuration = ApiConfigurationLoader.load(api_secrets_filename)

        # If an api_configuration has been provided override the loaded configuration with any properties that it has
        if api_configuration is not None:
            for key, value in vars(api_configuration).items():
                if value is not None:
                    setattr(configuration, key, value)

        # Use the access token provided if it exists
        if token is not None:
            # Check that there is an api_url available
            cls.__check_required_fields(configuration, ["api_url"])
            api_token = token
        # Otherwise generate an access token from Okta and use a RefreshingToken going forward
        else:
            # Check that all the required fields for generating a token exist
            cls.__check_required_fields(configuration, [
                "api_url",
                "password",
                "username",
                "client_id",
                "client_secret",
                "token_url"])

            # Generate an access token
            api_token = cls.__generate_access_token(
                configuration=configuration,
                okta_response_handler=okta_response_handler
            )

        # Initialise the API client using the token so that it can be included in all future requests
        config = Configuration()
        config.access_token = api_token
        config.host = configuration.api_url

        # Set the certificate from the configuration
        config.ssl_ca_cert = configuration.certificate_filename

        # Set the proxy for LUSID if needed
        if configuration.proxy_config is not None:
            config.proxy = configuration.proxy_config.address
            if configuration.proxy_config.username is not None and configuration.proxy_config.password is not None:
                config.proxy_headers = make_headers(
                    proxy_basic_auth=f"{configuration.proxy_config.username}:{configuration.proxy_config.password}"
                )

        # Create and return the ApiClient
        return ApiClient(
            configuration=config,
            header_name="X-LUSID-Application" if configuration.app_name is not None else None,
            header_value=configuration.app_name)
