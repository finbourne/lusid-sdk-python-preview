import unittest
from datetime import datetime
from parameterized import parameterized

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Valuation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a configured API client
        api_client = TestDataUtilities.api_client()

        # Setup required LUSID APIs
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.aggregation_api = lusid.AggregationApi(api_client)
        cls.quotes_api = lusid.QuotesApi(api_client)
        cls.recipes_api = lusid.ConfigurationRecipeApi(api_client)
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
            TestDataUtilities.tutorials_scope, cls.portfolio_code
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

    def create_aggregation_request(
        self, inline_recipe=None, recipe_scope=None, recipe_code=None
    ) -> lusid.models.AggregationRequest:
        """
        Creates an aggregation request that aggregates valuation results based on
        provided inline recipe or recipe identifiers when using an upserted one
        :param ConfigurationRecipe inline_recipe: A configured recipe to be used inline
        :param str recipe_scope: The scope for an already upserted recipe
        :param str recipe_code: The code for an already upserted recipe
        :return: AggregationRequest
        """

        if recipe_scope:
            in_line_recipe = self.create_configuration_recipe(recipe_scope, recipe_code)
            self.upsert_recipe_request(in_line_recipe)
            recipe_id = models.ResourceId(scope=recipe_scope, code=recipe_code)
        else:
            recipe_id = None

        return models.AggregationRequest(
            recipe_id=recipe_id,
            inline_recipe=inline_recipe,
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum"),
            ],
            group_by=["Instrument/default/Name"],
            effective_at=self.effective_date,
        )

    @lusid_feature("F20")
    @parameterized.expand(
        [
            [
                "Test valuation with an aggregation request containing a recipe inline",
                create_configuration_recipe("self", "TestRecipes", "SimpleQuotes"),
                None,
                None,
            ],
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
        # Set valuation result key
        valuation_key = "Sum(Holding/default/PV)"

        # Call aggregation with recipe identifiers
        aggregation_request = self.create_aggregation_request(
            in_line_recipe, recipe_scope, recipe_code
        )

        # Complete aggregation
        aggregation = self.aggregation_api.get_aggregation(
            scope=TestDataUtilities.tutorials_scope,
            code=self.portfolio_code,
            aggregation_request=aggregation_request,
        )

        # Asserts
        self.assertEqual(len(aggregation.data), 3)
        self.assertEqual(aggregation.data[0][valuation_key], 10000)
        self.assertEqual(aggregation.data[1][valuation_key], 20000)
        self.assertEqual(aggregation.data[2][valuation_key], 30000)
