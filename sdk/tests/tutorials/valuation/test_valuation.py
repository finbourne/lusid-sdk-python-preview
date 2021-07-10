import unittest
from datetime import datetime
from parameterized import parameterized

import pytz

import lusid
import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Valuation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client factory
        api_client_factory = TestDataUtilities.api_client_factory()

        # Setup required LUSID APIs
        cls.transaction_portfolios_api = api_client_factory.build(lusid.TransactionPortfoliosApi)
        cls.portfolios_api = api_client_factory.build(lusid.PortfoliosApi)
        cls.instruments_api = api_client_factory.build(lusid.InstrumentsApi)
        cls.aggregation_api = api_client_factory.build(lusid.AggregationApi)
        cls.quotes_api = api_client_factory.build(lusid.QuotesApi)
        cls.recipes_api = api_client_factory.build(lusid.ConfigurationRecipeApi)
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        # Setup test data from utilities
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        # Set test parameters
        cls.effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)
        cls.portfolio_code = cls.test_data_utilities.create_transaction_portfolio(
            TestDataUtilities.tutorials_scope
        )

        # Setup test portfolio
        cls.setup_portfolio(cls.effective_date, cls.portfolio_code)

    @classmethod
    def tearDownClass(cls):
        # Delete portfolio once tests are concluded
        cls.portfolios_api.delete_portfolio(
            TestDataUtilities.tutorials_scope,
            cls.portfolio_code
        )

    @classmethod
    def setup_portfolio(cls, effective_date, portfolio_code) -> None:
        """
        Sets up instrument, quotes and portfolio data from TestDataUtilities
        :param datetime effective_date: The portfolio creation date
        :param str portfolio_code: The code of the the test portfolio
        :return: None
        """

        transactions = [
            cls.test_data_utilities.build_transaction_request(
                instrument_id=cls.instrument_ids[0],
                units=100,
                price=101,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            cls.test_data_utilities.build_transaction_request(
                instrument_id=cls.instrument_ids[1],
                units=100,
                price=102,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
            cls.test_data_utilities.build_transaction_request(
                instrument_id=cls.instrument_ids[2],
                units=100,
                price=103,
                currency="GBP",
                trade_date=effective_date,
                transaction_type="StockIn",
            ),
        ]

        cls.transaction_portfolios_api.upsert_transactions(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            transaction_request=transactions,
        )

        prices = [
            (cls.instrument_ids[0], 100),
            (cls.instrument_ids[1], 200),
            (cls.instrument_ids[2], 300),
        ]

        requests = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider="Lusid",
                        instrument_id=price[0],
                        instrument_id_type="LusidInstrumentId",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=effective_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBP"),
            )
            for price in prices
        ]

        cls.quotes_api.upsert_quotes(
            TestDataUtilities.tutorials_scope,
            request_body={
                "quote" + str(request_number): requests[request_number]
                for request_number in range(len(requests))
            },
        )

    def create_configuration_recipe(
        self, recipe_scope, recipe_code
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that can be used inline or upserted
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :return: ConfigurationRecipe
        """

        return models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            market=models.MarketContext(
                market_rules=[],
                suppliers=models.MarketContextSuppliers(equity="Lusid"),
                options=models.MarketOptions(
                    default_supplier="Lusid",
                    default_instrument_code_type="LusidInstrumentId",
                    default_scope=TestDataUtilities.tutorials_scope,
                ),
            ),
        )

    def upsert_recipe_request(self, configuration_recipe) -> None:
        """
        Structures a recipe request and upserts it into LUSID
        :param ConfigurationRecipe configuration_recipe: Recipe configuration
        :return: None
        """

        upsert_recipe_request = models.UpsertRecipeRequest(configuration_recipe)
        self.recipes_api.upsert_configuration_recipe(upsert_recipe_request)

    @parameterized.expand(
        [
            [
                "Test valuation with an aggregation request using an already upserted recipe",
                None,
                "TestRecipes",
                "SimpleQuotes",
            ],
        ]
    )
    def test_aggregation(self, _, in_line_recipe, recipe_scope, recipe_code) -> None:
        """
        General valuation/aggregation test
        """
        # create recipe (provides model parameters, locations to use in resolving market data etc.
        # and push it into LUSID. Only needs to happen once each time when updated, or first time run to create.
        recipe = self.create_configuration_recipe(recipe_scope, recipe_code)
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Holding/default/PV)"

        # create valuation request
        valuation_request = models.ValuationRequest(
            recipe_id=models.ResourceId(scope=recipe_scope, code=recipe_code),
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum"),
            ],
            group_by=["Instrument/default/Name"],
            valuation_schedule=models.ValuationSchedule(effective_at=self.effective_date),
            portfolio_entity_ids=[
                models.PortfolioEntityId(
                    scope=TestDataUtilities.tutorials_scope,
                    code=self.portfolio_code)
            ]
        )

        # Complete aggregation
        aggregation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request
        )

        # Asserts
        self.assertEqual(len(aggregation.data), 3)
        self.assertEqual(aggregation.data[0][valuation_key], 10000)
        self.assertEqual(aggregation.data[1][valuation_key], 20000)
        self.assertEqual(aggregation.data[2][valuation_key], 30000)
