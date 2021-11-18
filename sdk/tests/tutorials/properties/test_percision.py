import unittest
from decimal import Decimal
import lusid
from lusid.utilities.api_client_factory import ApiClientFactory
from numpy import float64
from numpy import float32




class PrecisionTest(unittest.TestCase):
    """This tests an optional flag in the api_client that allows users to return float values as Python Decimals."""

    @classmethod
    def setUpClass(cls):
        api_client_decimal= ApiClientFactory(flag_to_use_decimal=True).api_client
        api_factory_float = ApiClientFactory(flag_to_use_decimal=False).api_client

        cls.portfolios_api_decimal = lusid.PortfoliosApi(api_client_decimal)
        cls.portfolios_api_float = lusid.PortfoliosApi(api_factory_float)
        cls.transactions_portfolio_api = lusid.TransactionPortfoliosApi(api_client_decimal)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client_decimal)


    def test_create_portfolio_with_property(self):

        data_type_id = lusid.models.ResourceId("system", "number")

        #   property definition
        property_definition = lusid.models.CreatePropertyDefinitionRequest(
            domain = "Portfolio",
            scope = "test-precision",
            code = "decimal_value",
            value_required = False,
            display_name = "Precision property",
            life_time = "Perpetual",
            data_type_id = data_type_id
        )

        #   create the property definition
        property_definition_result = self.property_definitions_api.create_property_definition(
            create_property_definition_request = property_definition)

        #  property value
        property_value = "0.12345678910111213"
        property_value = float(property_value)
        portfolio_property = lusid.models.ModelProperty(key = property_definition_result.key,
                                                        value = lusid.models.PropertyValue(metric_value = lusid.models.MetricValue(value=property_value)))

        #  details of the portfolio to be created
        request = lusid.models.CreateTransactionPortfolioRequest(display_name = "Decimal Port",
                                                                 code = "ABCD",
                                                                 base_currency = "GBP",

                                                                  # set the property value when creating the portfolio
                                                                 properties = {
                                                                 property_definition_result.key: portfolio_property})

        # create the portfolio
        portfolio = self.transactions_portfolio_api.create_portfolio(
            scope = "test-precision",
            create_transaction_portfolio_request = request)

        portfolio_code = portfolio.id.code
        self.assertEqual(portfolio_code, request.code)



    def test_precision(self):
        portfolio = self.portfolios_api_decimal.get_portfolio(scope = "test-precision",code= "ABCD",
                                                      property_keys = ["Portfolio/test-precision/decimal_value"])


        self.assertTrue(type(portfolio.properties['Portfolio/test-precision/decimal_value'].value.metric_value.value)== Decimal)
        self.assertEqual(Decimal('0.12345678910111213'), portfolio.properties['Portfolio/test-precision/decimal_value'].value.metric_value.value)
        print(portfolio.properties['Portfolio/test-precision/decimal_value'].value.metric_value.value)

    def test_float(self):
        portfolio = self.portfolios_api_float.get_portfolio("test-precision", "ABCD", property_keys = ["Portfolio/test-precision/decimal_value"])
        print(type(portfolio.properties['Portfolio/test-precision/decimal_value'].value.metric_value.value))


    def test_tear_down(self):

        self.portfolios_api_float.delete_portfolio(scope="test-precision", code="ABCD")
        self.property_definitions_api.delete_property_definition(domain="Portfolio", scope="test-precision", code="decimal_value")
        print("portfolio delted")





