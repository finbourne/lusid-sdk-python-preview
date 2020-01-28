class ProxyConfig:

    def __init__(self, address, username, password):
        self.__address = address
        self.__username = username
        self.__password = password

    @property
    def address(self):
        return self.__address

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password
