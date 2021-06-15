from fbnsdkutilities import ApiClientFactoryBase
import lusid

class ApiClientFactory(ApiClientFactoryBase):
    """
    The ApiClientFactory is responsible for providing the ability to create any of the LUSID APIs using the provided
    credentials. It will use the same ApiClient across all of the APIs.

    """
    def __init__(self, **kwargs):
        """
        Iniitalise an ApiClientFactory by passing the token, api_url and app_name, or by
        passing in the api_secrets_filename

        :param str token: Bearer token used to initialise the API
        :param str api_secrets_filename: Name of secrets file (including full path)
        :param str api_url: LUSID API url
        :param str app_name: Application name (optional)
        :param str certificate_filename: Name of the certificate file (.pem, .cer or .crt)
        :param str proxy_url: The url of the proxy to use including the port e.g. http://myproxy.com:8888
        :param str proxy_username: The username for the proxy to use
        :param str proxy_password: The password for the proxy to use
        :param str correlation_id: Correlation id for all calls made from the returned LUSID API instances
        :param bool tcp_keep_alive: A flag for controlling if the API client uses TCP keep-alive probes
        """

        super().__init__(lusid, **kwargs)
