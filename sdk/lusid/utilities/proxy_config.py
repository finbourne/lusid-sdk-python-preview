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


def format_proxy_schema(address, username, password):

    proxy_url = address
    if username is not None and password is not None:
        index = address.index("://")

        proxy_url = f"{address[0:index + 3]}{username}:{password}@{address[index + 3:]}"

    return {
        "http": proxy_url,
        "https": proxy_url
    }
