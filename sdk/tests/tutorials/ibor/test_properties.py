import unittest
from datetime import datetime

import pytz
from lusidfeature import lusid_feature

import lusid
import lusid.models as models
from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities import IdGenerator
from utilities.credentials_source import CredentialsSource
from utilities.id_generator_utilities import delete_entities
from utilities.instrument_loader import InstrumentLoader
from utilities.test_data_utilities import TestDataUtilities


class Properties(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build()

        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        delete_entities(cls.id_generator)

    @lusid_feature("F1-5")
    def test_create_portfolio_with_label_property(self):
        # Details of property to be created
        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)

        _, scope, property_code, _ = self.id_generator.generate_scope_and_code(
            "property_definition",
            scope=TestDataUtilities.tutorials_scope,
            code_prefix="fund-style-",
            annotations=["Portfolio"]
        )

        label_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=scope,
            code=property_code,
            display_name=property_code,
            life_time="Perpetual",
            value_required=False,
            data_type_id=models.resource_id.ResourceId(scope="system", code="string")
        )

        # create property definition
        label_property_definition_request = self.property_definitions_api.create_property_definition(
            label_property_definition)

        # create property values
        property_value = models.PropertyValue(label_value="Active")

        _, scope, portfolio_code = self.id_generator.generate_scope_and_code(
            "portfolio",
            scope=TestDataUtilities.tutorials_scope,
            code_prefix="portfolio-"
        )

        # Details of new portfolio to be created
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code=portfolio_code,
            display_name=portfolio_code,
            base_currency="GBP",
            created=effective_date,
            properties={
                label_property_definition_request.key: models.PerpetualProperty(
                    key=label_property_definition_request.key,
                    value=property_value
                )
            }
        )

        # create portfolio
        portfolio_request = self.transaction_portfolios_api.create_portfolio(scope=TestDataUtilities.tutorials_scope,
                                                                             create_transaction_portfolio_request=create_portfolio_request)

        # get properties for assertions
        portfolio_properties = self.portfolios_api.get_portfolio_properties(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_request.id.code).properties

        label_property = portfolio_properties[label_property_definition_request.key]

        # Perform assertions on keys, codes and values
        self.assertEqual(list(portfolio_properties.keys())[0], label_property_definition_request.key)
        self.assertEqual(portfolio_request.id.code, create_portfolio_request.code)
        self.assertEqual(label_property.value.label_value, property_value.label_value)

    @lusid_feature("F1-6")
    def test_create_portfolio_with_metric_property(self):

        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)

        _, scope, property_code, _ = self.id_generator.generate_scope_and_code(
            "property_definition",
            scope=TestDataUtilities.tutorials_scope,
            code_prefix="fund-NAV-",
            annotations=["Portfolio"]
        )

        # details of property to be created
        metric_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=scope,
            code=property_code,
            display_name="fund NAV",
            life_time="Perpetual",
            value_required=False,
            data_type_id=models.resource_id.ResourceId(scope="system", code="currencyAndAmount")
        )

        # create property definitions
        metric_property_definition_result = self.property_definitions_api.create_property_definition(metric_property_definition)

        # create the property values
        metric_property_value_request = models.PropertyValue(metric_value=models.MetricValue(value=1100000, unit="GBP"))
        # metric_property_value_request = models.PropertyValue(label_value="Active")

        # Details of the new portfolio to be created, created here with the minimum set of mandatory fields

        _, scope, portfolio_code = self.id_generator.generate_scope_and_code(
            "portfolio",
            scope=TestDataUtilities.tutorials_scope,
            code_prefix="portfolio-"
        )

        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code=portfolio_code,
            display_name=portfolio_code,
            base_currency="GBP",
            created=effective_date,
            properties={
                metric_property_definition_result.key: models.PerpetualProperty(
                    key=metric_property_definition_result.key,
                    value=metric_property_value_request
                )
            }
        )

        # Create portfolio
        portfolio_result = self.transaction_portfolios_api.create_portfolio(scope=TestDataUtilities.tutorials_scope,
                                                                            create_transaction_portfolio_request=create_portfolio_request)
        portfolio_properties = self.portfolios_api.get_portfolio_properties(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_result.id.code).properties
        metric_property = portfolio_properties[metric_property_definition_result.key]

        # Perform assertions on codes, keys, values and units
        self.assertEqual(portfolio_result.id.code, create_portfolio_request.code)
        self.assertEqual(list(portfolio_properties.keys())[0], metric_property_definition_result.key)
        self.assertEqual(metric_property.value.metric_value.value, metric_property_value_request.metric_value.value)
        self.assertEqual(metric_property.value.metric_value.unit, metric_property_value_request.metric_value.unit)

