import unittest
from datetime import datetime
import pytz
import uuid

import lusid
import lusid.models as models
from utilities import PortfolioLoader
from utilities import TestDataUtilities


class MultiSourceRecipe(unittest.TestCase):
    """This is an example of using recipes to manage multiple
    market data sources, using a 'MarketDataRule'. These rules
    can be passed as a list, where the sources will be prioritised
    in order, allowing for waterfall logic when resolving market data.
    Multiple price sources can exist under a given market data provider.
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

        # Setup test data from utilities
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        # Setup test parameters
        cls.effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        # Setup scopes for tests
        cls.recipe_scope = "TestSources"
        cls.recipe_code = "SimpleQuotes"

        # Set market data scope for quotes and recipes
        cls.market_data_provider = "Lusid"
        cls.market_data_scope = "Test-" + str(uuid.uuid4())

        # Setup test portfolio
        cls.portfolio_scope = TestDataUtilities.tutorials_scope
        cls.portfolio_code = cls.test_data_utilities.create_transaction_portfolio(
            TestDataUtilities.tutorials_scope
        )

        # Load transactions to test portfolio
        portfolio_loader = PortfolioLoader(
            cls.transaction_portfolios_api, cls.instruments_api
        )
        portfolio_loader.setup_gbp_portfolio(
            cls.portfolio_scope, cls.portfolio_code, cls.effective_date
        )

    @classmethod
    def tearDownClass(cls):
        # Delete portfolio once tests are concluded
        cls.portfolios_api.delete_portfolio(
            TestDataUtilities.tutorials_scope, cls.portfolio_code
        )

    def create_configuration_recipe(
        self, recipe_scope, recipe_code
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that allows for use of 2 different
        price_sources under a given market_data provider, using a
        'MarketDataKeyRule'. When using the market_rule parameter, LUSID
        will seek to resolve using the first available data from the providers
        specified in the list.
        This example prioritises quotes from supplier 'Client' over 'Lusid'
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :return: ConfigurationRecipe
        """

        return models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            market=models.MarketContext(
                market_rules=[
                    models.MarketDataKeyRule(
                        key="Equity.Figi.*",
                        supplier=self.market_data_provider,
                        data_scope=self.market_data_scope,
                        quote_type="Price",
                        field="mid",
                        quote_interval="1D.0D",
                        price_source="source_1",
                    ),
                    models.MarketDataKeyRule(
                        key="Equity.Figi.*",
                        supplier=self.market_data_provider,
                        data_scope=self.market_data_scope,
                        quote_type="Price",
                        field="mid",
                        quote_interval="1D.0D",
                        price_source="source_2",
                    ),
                ],
                suppliers=models.MarketContextSuppliers(
                    equity=self.market_data_provider
                ),
                options=models.MarketOptions(
                    default_supplier=self.market_data_provider,
                    default_instrument_code_type="Figi",
                    default_scope=self.market_data_scope,
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
                models.AggregateSpec("Valuation/PvInPortfolioCcy", "Proportion"),
                models.AggregateSpec("Valuation/PvInPortfolioCcy", "Sum"),
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

    def upsert_quotes(self) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        using quotes from two separate sources for the same date
        :return: UpsertQuotesResponse
        """

        source_1 = [
            ("BBG000BF46Y8", 100),
        ]

        source_2 = [
            ("BBG000PQKVN8", 200),
            ("BBG000FD8G46", 300),
        ]

        requests_1 = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider=self.market_data_provider,
                        price_source="source_1",
                        instrument_id=price[0],
                        instrument_id_type="Figi",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=self.effective_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBP"),
            )
            for price in source_1
        ]
        requests_2 = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider=self.market_data_provider,
                        price_source="source_2",
                        instrument_id=price[0],
                        instrument_id_type="Figi",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=self.effective_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBP"),
            )
            for price in source_2
        ]

        requests = requests_1 + requests_2

        return self.quotes_api.upsert_quotes(
            scope=self.market_data_scope,
            request_body={
                "quote" + str(request_number): requests[request_number]
                for request_number in range(len(requests))
            },
        )

    def test_waterfall_source(self):

        quotes_response = self.upsert_quotes()
        self.assertEqual(len(quotes_response.failed), 0)

        # Upsert recipe
        recipe_scope = "TestRecipes"
        recipe_code = "SimpleQuotes"
        recipe = self.create_configuration_recipe(recipe_scope, recipe_code)
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Valuation/PvInPortfolioCcy)"

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(recipe_scope, recipe_code)

        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request,
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][valuation_key], 10000)
        self.assertEqual(valuation.data[1][valuation_key], 20000)
        self.assertEqual(valuation.data[2][valuation_key], 30000)


if __name__ == "__main__":
    unittest.main()
