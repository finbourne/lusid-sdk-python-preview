import json
import os

from .api_configuration import ApiConfiguration
from .proxy_config import ProxyConfig


class ApiConfigurationLoader:

    @staticmethod
    def load(api_secrets_filename=None):
        """
        :param api_secrets_filename: name of api configuration file
        :return: populated ApiConfiguration
        """

        token_url_env_key = "FBN_TOKEN_URL"
        lusid_url_env_key = "FBN_LUSID_API_URL"
        username_env_key = "FBN_USERNAME"
        password_env_key = "FBN_PASSWORD"
        client_id_env_key = "FBN_CLIENT_ID"
        client_secret_env_key = "FBN_CLIENT_SECRET"
        app_name_env_key = "FBN_APP_NAME"
        proxy_address = "FBN_PROXY_ADDRESS"
        proxy_port = "FBN_PROXY_PORT"
        proxy_username = "FBN_PROXY_USERNAME"
        proxy_password = "FBN_PROXY_PASSWORD"

        token_url_config_key = "tokenUrl"
        lusid_url_config_key = "apiUrl"
        username_config_key = "username"
        password_config_key = "password"
        client_id_config_key = "clientId"
        client_secret_config_key = "clientSecret"
        app_name_config_key = "applicationName"
        proxy_key = "proxy"
        proxy_address_key = "proxyAddress"
        proxy_username_key = "username"
        proxy_password_key = "password"

        def vars_from_env():
            # Load our configuration details from the environment variables
            return {
                "token_url": os.getenv(token_url_env_key, None),
                "api_url": os.getenv(lusid_url_env_key, None),
                "username": os.getenv(username_env_key, None),
                "password": os.getenv(password_env_key, None),
                "client_id": os.getenv(client_id_env_key, None),
                "client_secret": os.getenv(client_secret_env_key, None),
                "app_name": os.getenv(app_name_env_key, "")
            }

        config_values = vars_from_env()
        missing = {k: v for k, v in config_values.items() if v is None}
        missing.pop("app_name", None)

        # If any of the environmental variables are missing use a local secrets file
        if len(missing) > 0:

            if api_secrets_filename is None:
                var_to_env = {
                    "token_url": token_url_env_key,
                    "api_url": lusid_url_env_key,
                    "username": username_env_key,
                    "password": password_env_key,
                    "client_id": client_id_env_key,
                    "client_secret": client_secret_env_key
                }

                raise ValueError(f"Path to secrets file not specified and missing the following environment variables: {','.join([var_to_env[k] for k in missing.keys()])}")

            with open(api_secrets_filename, "r") as secrets:
                config = json.load(secrets)

            config_values = {
                "token_url": config["api"].get(token_url_config_key, None),
                "username": config["api"].get(username_config_key, None),
                "password": config["api"].get(password_config_key, None),
                "client_id": config["api"].get(client_id_config_key, None),
                "client_secret": config["api"].get(client_secret_config_key, None),
                "api_url": config["api"].get(lusid_url_config_key, None),
                "app_name": config["api"].get(app_name_config_key, "")
            }

            missing_config = {k: v for k, v in config_values.items() if v is None}
            missing_config.pop("app_name", None)

            if len(missing_config) > 0:
                var_to_config = {
                    "token_url": token_url_config_key,
                    "api_url": lusid_url_config_key,
                    "username": username_config_key,
                    "password": password_config_key,
                    "client_id": client_id_config_key,
                    "client_secret": client_secret_config_key
                }

                raise ValueError(f"Trying to load config from secrets file but missing: {','.join([var_to_config[k] for k in missing_config.keys()])}")

            #  proxy config
            if proxy_key in config:
                proxy_values = {
                    "address": config[proxy_key].get(proxy_address_key, None),
                    "username": config[proxy_key].get(proxy_username_key, None),
                    "password": config[proxy_key].get(proxy_password_key, None),
                }
                config_values["proxy_config"] = ProxyConfig(**proxy_values)

        return ApiConfiguration(**config_values)
