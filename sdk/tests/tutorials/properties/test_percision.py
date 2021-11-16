import unittest
from decimal import Decimal

import lusid
from lusid.utilities import ApiConfiguration
from lusid.utilities.api_client_builder import ApiClientBuilder



class Precision_test(unittest.TestCase):
    """This tests an optional flag in the api_client that allows users to return float values as Python Decimals."""

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        config = ApiConfiguration(flag_to_use_decimal = True)
        api_client = ApiClientBuilder().build(api_configuration = config)

        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

    def test_flag(self):
        config = ApiConfiguration(flag_to_use_decimal = True)
        self.assertEqual(config.flag_to_use_decimal, True)


    def test_precision(self):
        portfolio = self.portfolios_api.get_portfolio("test-precision", "ABC",
                                                      property_keys = ["Portfolio/test-precision/noquotes"])

        self.assertTrue(type(portfolio.properties['Portfolio/test-precision/noquotes'].value.metric_value.value)== Decimal)
        self.assertEqual(Decimal('0.1234567891011121314151617182'), portfolio.properties['Portfolio/test-precision/noquotes'].value.metric_value.value)
        

