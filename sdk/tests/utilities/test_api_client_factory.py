import json
import os
import unittest
from collections import UserString
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from lusid import ApiConfigurationLoader, ScopesApi, ResourceListOfScopeDefinition
from lusid.utilities import ApiClientFactory, format_proxy_schema
from utilities import TokenUtilities as tu, CredentialsSource


class UnknownApi:
    pass


class UnknownImpl:
    pass


class RefreshingToken(UserString):

    def __init__(self):
        token_data = {"expires": datetime.now(), "current_access_token": ""}

        def get_token():
            token_data["current_access_token"] = None
            return token_data["current_access_token"]

        self.access_token = get_token

    def __getattribute__(self, name):
        token = object.__getattribute__(self, "access_token")()
        if name == "data":
            return token
        return token.__getattribute__(name)


class ApiFactory(unittest.TestCase):
    def validate_api(self, api):
        result = api.list_scopes()
        self.assertIsNotNone(result)
        self.assertGreater(len(result.values), 0)

    def test_get_unknown_api_throws_exception(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        with self.assertRaises(TypeError) as error:
            factory.build(UnknownApi)
        self.assertEqual(error.exception.args[0], "unknown api: UnknownApi")

    def test_get_unknown_type_throws_exception(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        with self.assertRaises(TypeError) as error:
            factory.build(UnknownImpl)
        self.assertEqual(error.exception.args[0], "unknown api: UnknownImpl")

    def test_get_api_with_token(self):
        token, _ = tu.get_okta_tokens(CredentialsSource.secrets_path())
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

        factory = ApiClientFactory(
            token=token, api_url=config.api_url, app_name=config.app_name
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

        response = api.list_scopes()

        self.assertIsInstance(response, ResourceListOfScopeDefinition)

    def test_get_api_with_none_token(self):

        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())
        factory = ApiClientFactory(
            token=None,
            api_url=config.api_url,
            app_name=config.app_name,
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

        response = api.list_scopes()

        self.assertIsInstance(response, ResourceListOfScopeDefinition)

    def test_get_api_with_str_none_token(self):

        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())
        factory = ApiClientFactory(
            token=RefreshingToken(),
            api_url=config.api_url,
            app_name=config.app_name,
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

        response = api.list_scopes()

        self.assertIsInstance(response, ResourceListOfScopeDefinition)

    def test_get_api_with_token_url_as_env_var(self):
        token, _ = tu.get_okta_tokens(CredentialsSource.secrets_path())
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

        os.environ["FBN_LUSID_API_URL"] = config.api_url

        factory = ApiClientFactory(token=token, app_name=config.app_name)
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

        response = api.list_scopes()

        self.assertIsInstance(response, ResourceListOfScopeDefinition)

    def test_get_api_with_configuration(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_info(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)

        with self.assertRaises(ValueError) as error:
            api.list_scopes(call_info="invalid param")

        self.assertEqual(error.exception.args[0], "call_info value must be a lambda")

    def test_get_info_with_invalid_param_throws_error(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        result = api.list_scopes(call_info=lambda r: print(r))

        self.assertIsNotNone(result)

    def test_init_from_value(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        scopes_api = ScopesApi(factory.build(ScopesApi))
        result = scopes_api.list_scopes()

        self.assertGreater(len(result.values), 0)

    def test_wrapped_method(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )

        wrapped_scopes_api = factory.build(ScopesApi)
        portfolio = ScopesApi(wrapped_scopes_api.api_client)

        self.assertEqual(portfolio.__doc__, wrapped_scopes_api.__doc__)
        self.assertEqual(portfolio.__module__, wrapped_scopes_api.__module__)
        self.assertDictEqual(portfolio.__dict__, wrapped_scopes_api.__dict__)

    def test_get_api_with_proxy(self):
        proxy_credentials = Path(__file__).parent.parent.joinpath('secrets.proxy.json')

        factory = ApiClientFactory(api_secrets_filename=proxy_credentials)

        scopes_api = ScopesApi(factory.build(ScopesApi))
        result = scopes_api.list_scopes()

        self.assertGreater(len(result.values), 0)

    def test_get_api_with_proxy_using_env_vars(self):

        proxy_credentials = Path(__file__).parent.parent.joinpath('secrets.proxy.json')

        if os.path.isfile(proxy_credentials):
            with open(proxy_credentials, "r") as secrets_file:
                config = json.load(secrets_file)

                proxies = format_proxy_schema(config["proxy"]["proxyAddress"], config["proxy"]["username"], config["proxy"]["password"])

                env_vars = {
                    "FBN_TOKEN_URL": config["api"].get("tokenUrl", None),
                    "FBN_USERNAME": config["api"].get("username", None),
                    "FBN_PASSWORD": config["api"].get("password", None),
                    "FBN_CLIENT_ID": config["api"].get("clientId", None),
                    "FBN_CLIENT_SECRET": config["api"].get("clientSecret", None),
                    "FBN_LUSID_API_URL": config["api"].get("apiUrl", None),
                    "FBN_APP_NAME": config["api"].get("applicationName", None),
                    "HTTPS_PROXY": proxies["https"]
                }

        else:
            env_vars = {
                "FBN_TOKEN_URL": os.getenv("FBN_TOKEN_URL"),
                "FBN_USERNAME": os.getenv("FBN_USERNAME"),
                "FBN_PASSWORD": os.getenv("FBN_PASSWORD"),
                "FBN_CLIENT_ID": os.getenv("FBN_CLIENT_ID"),
                "FBN_CLIENT_SECRET": os.getenv("FBN_CLIENT_SECRET"),
                "FBN_LUSID_API_URL": os.getenv("FBN_LUSID_API_URL"),
                "FBN_APP_NAME": os.getenv("FBN_APP_NAME"),
                "HTTPS_PROXY": os.getenv("HTTPS_PROXY")
            }

        if None in env_vars.values():
            assert False, "Source test configuration missing values from both secrets file and environment variables"

        with patch.dict('os.environ', env_vars):
            factory = ApiClientFactory()

            scopes_api = ScopesApi(factory.build(ScopesApi))
            result = scopes_api.list_scopes()

            self.assertGreater(len(result.values), 0)
