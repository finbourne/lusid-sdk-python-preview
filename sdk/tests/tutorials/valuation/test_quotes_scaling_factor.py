import unittest
from datetime import datetime
import pytz

import lusid
import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class ScalingFactor(unittest.TestCase):
    """This is an example of using the scale_factor in an
    upsert_quotes request, which is applicable to instruments
    where the price requires scaling, such as bonds. For a bond
    with quotes as a percentage of par of 100, adding this value
    as the scaling factor will account for the transformation when
    running a valuation
    """

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

        # Setup scopes for recipe tests
        cls.recipe_scope = "TestIdentifiers"
        cls.recipe_code = "SimpleQuotes"

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
                price=1,
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

    def upsert_quotes(self, scale_factor) -> None:
        """
        Upserts quotes using a scaling factor paramater, that can be
        used to for non-standard quotes such as bond prices that are
        quotes as percentage as par (i.e. 'scaling_factor=100').
        :param float scale_factor: scale factor for non-standard quotes
        :return: None
        """
        # Add prices as a percentage of par
        prices = [
            (self.instrument_ids[0], 100),
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
                    effective_at=self.effective_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBP"),
                # Set a scaling factor for the par value
                scale_factor=scale_factor,
            )
            for price in prices
        ]

        self.quotes_api.upsert_quotes(
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

    def create_valuation_request(
        self, recipe_scope=None, recipe_code=None
    ) -> lusid.models.ValuationRequest:
        """
        Creates a valuation request that can be used to return results based on
        an upserted recipe for the selected portfolio. The selected key in this
        example will return valuation in the portfolio currency (see 'Valuation/PV'
        for results in domestic currency). Additionally, the 'op' parameter will
        allow for use of arithmetic operators on a given metric. For more info on
        the set of available metrics, see the 'get_queryable_keys()' call under
        LUSID API docs, part of the Aggregation endpoint.
        :param str recipe_scope: The scope for an already upserted recipe
        :param str recipe_code: The code for an already upserted recipe
        :return: ValuationRequest
        """

        recipe_id = models.ResourceId(scope=recipe_scope, code=recipe_code)

        return models.ValuationRequest(
            recipe_id=recipe_id,
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Valuation/PV", "Proportion"),
                models.AggregateSpec("Valuation/PV", "Sum"),
            ],
            group_by=["Instrument/default/Name"],
            portfolio_entity_ids=[
                models.PortfolioEntityId(
                    scope=TestDataUtilities.tutorials_scope,
                    code=self.portfolio_code,
                    portfolio_entity_type="SinglePortfolio",
                )
            ],
            valuation_schedule=models.ValuationSchedule(
                effective_from=self.effective_date, effective_at=self.effective_date
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

    def test_par_scaled_valuation(self) -> None:
        """
        Valuation test for a simple instrument using quotes upserted with a
        scale_factor of 100, this would typically be applicable to bonds or
        other instruments where the par amount is other than 1.
        """

        # Upsert quotes with scale_factor of 100
        self.upsert_quotes(100)

        # Upsert recipe
        recipe = self.create_configuration_recipe(self.recipe_scope, self.recipe_code)
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Valuation/PV)"

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.recipe_scope, self.recipe_code
        )

        # Complete valuation
        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request
        )

        # Asserts
        self.assertEqual(len(valuation.data), 1)
        self.assertEqual(valuation.data[0][valuation_key], 100)


if __name__ == "__main__":
    unittest.main()
