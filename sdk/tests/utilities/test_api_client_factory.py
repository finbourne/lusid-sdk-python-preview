import unittest

from lusid.models import ResourceListOfPortfolio
from lusid import ApiConfigurationLoader, PortfoliosApi
from lusid.utilities import ApiClientFactory
from utilities import TokenUtilities as tu, CredentialsSource
import os


class UnknownApi:
    pass


class UnknownImpl:
    pass


class ApiFactory(unittest.TestCase):

    def validate_api(self, api):
        result = api.list_portfolios(limit=10)
        self.assertIsNotNone(result)
        self.assertGreater(len(result.values), 0)

    def test_get_unknown_api_throws_exception(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        with self.assertRaises(TypeError) as error:
            factory.build(UnknownApi)
        self.assertEqual(error.exception.args[0], "unknown api: UnknownApi")

    def test_get_unknown_type_throws_exception(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        with self.assertRaises(TypeError) as error:
            factory.build(UnknownImpl)
        self.assertEqual(error.exception.args[0], "unknown api: UnknownImpl")

    def test_get_api_with_token(self):
        token, _ = tu.get_okta_tokens()
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

        factory = ApiClientFactory(token=token, api_url=config.api_url, app_name=config.app_name)
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)
        self.validate_api(api)

        response = api.list_portfolios()

        self.assertIsInstance(response, ResourceListOfPortfolio)

    def test_get_api_with_none_token(self):

        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())
        factory = ApiClientFactory(token=None, api_url=config.api_url, app_name=config.app_name, api_secrets_filename=CredentialsSource.secrets_path())
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)
        self.validate_api(api)

        response = api.list_portfolios()

        self.assertIsInstance(response, ResourceListOfPortfolio)

    def test_get_api_with_token_url_as_env_var(self):
        token, _ = tu.get_okta_tokens()
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

        os.environ["FBN_LUSID_API_URL"] = config.api_url

        factory = ApiClientFactory(token=token, app_name=config.app_name)
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)
        self.validate_api(api)

        response = api.list_portfolios()

        self.assertIsInstance(response, ResourceListOfPortfolio)

    def test_get_api_with_configuration(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)
        self.validate_api(api)

    def test_get_api_with_info(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)

        with self.assertRaises(ValueError) as error:
            api.list_portfolios(limit=10, call_info="invalid param")

        self.assertEqual(error.exception.args[0], "call_info value must be a lambda")

    def test_get_info_with_invalid_param_throws_error(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        api = factory.build(PortfoliosApi)

        self.assertIsInstance(api, PortfoliosApi)
        result = api.list_portfolios(limit=10, call_info=lambda r: print(r))

        self.assertIsNotNone(result)

    def test_init_from_value(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        portfolios = PortfoliosApi(factory.build(PortfoliosApi))
        result = portfolios.list_portfolios(limit=10)

        self.assertGreater(len(result.values), 0)

    def test_wrapped_method(self):
        factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())

        wrapped_portfolio = factory.build(PortfoliosApi)
        portfolio = PortfoliosApi(wrapped_portfolio.api_client)

        self.assertEqual(portfolio.__doc__, wrapped_portfolio.__doc__)
        self.assertEqual(portfolio.__module__, wrapped_portfolio.__module__)
        self.assertDictEqual(portfolio.__dict__, wrapped_portfolio.__dict__)


