class ApiConfiguration:

    def __init__(self, token_url, api_url, username, password, client_id, client_secret, app_name,
                 certificate_filename=None, proxy_config=None):
        """
        :param token_url:
        :param api_url:
        :param username:
        :param password:
        :param client_id:
        :param client_secret:
        :param app_name:
        :param str certificate_filename: (optional) Name of the certificate file (.pem, .cer or .crt)
        :param proxy_config:
        """
        self.__token_url = token_url
        self.__api_url = api_url
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__app_name = app_name
        self.__certificate_filename = certificate_filename
        self.__proxy_config = proxy_config

    @property
    def token_url(self):
        return self.__token_url

    @token_url.setter
    def token_url(self, value):
        self.__token_url = value

    @property
    def api_url(self):
        return self.__api_url

    @api_url.setter
    def api_url(self, value):
        self.__api_url = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value):
        self.__client_secret = value

    @property
    def app_name(self):
        return self.__app_name

    @app_name.setter
    def app_name(self, value):
        self.__app_name = value

    @property
    def certificate_filename(self):
        return self.__certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, value):
        self.__certificate_filename = value

    @property
    def proxy_config(self):
        return self.__proxy_config

    @proxy_config.setter
    def proxy_config(self, value):
        self.__proxy_config = value
