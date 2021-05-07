import unittest
from datetime import datetime
import pytz
import uuid

import lusid
import lusid.models as models
from utilities import TestDataUtilities
from utilities import PortfolioLoader


class CurrencySubUnitRecipe(unittest.TestCase):
    """ "This is an example of running valuation with prices quoted
    in currency subunits, a typical example will be GBp/GBx where a
    valuation may be carried out in GBP. In order for LUSID to carry out
    the fx transformation, the key parameter is 'attempt_to_infer_missing_fx'
    which needs to set to 'True' in the ConfigurationRecipe's pricing options
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
        cls.recipe_scope = "TestQuoteInterval"
        cls.recipe_code = "SimpleQuotes"

        # Set market data scope for quotes and recipes
        cls.market_data_provider = "Lusid"
        cls.market_data_scope = "Test-" + str(uuid.uuid4())

        # Setup test portfolio
        cls.portfolio_scope = TestDataUtilities.tutorials_scope
        cls.portfolio_code = cls.test_data_utilities.create_transaction_portfolio(
            TestDataUtilities.tutorials_scope
        )

        # Load GBP transactions to test portfolio
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
        self, recipe_scope, recipe_code, infer_fx_rate
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that infers fx_rates when required,
        this can be used to have the valuation request look for inverse fx
        quotes or currency sub-units such as GBp/GBx. A key distinction in
        valuation, is the use of the metric/key that will ensure valuation
        is returned in either the domestic or portfolio currency, these
        are 'Valuation/Pv' and 'Valuation/PvInPortfolioCcy' respectively.
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :param bool infer_fx_rate: looks up fx_rate from quote store when set to 'True'
        :return: ConfigurationRecipe
        """

        return models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            market=models.MarketContext(
                market_rules=[
                    models.MarketDataKeyRule(
                        key="Equity.Figi.*",
                        supplier="Lusid",
                        data_scope=self.market_data_scope,
                        quote_type="Price",
                        field="mid",
                        quote_interval="1D.0D",
                    ),
                ],
                suppliers=models.MarketContextSuppliers(
                    equity=self.market_data_provider
                ),
                options=models.MarketOptions(
                    default_supplier=self.market_data_provider,
                    default_instrument_code_type="Figi",
                    default_scope=self.market_data_scope,
                    attempt_to_infer_missing_fx=infer_fx_rate,
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

    def upsert_quotes(self, quotes_date) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param datetime quotes_date: The date of the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("BBG000BF46Y8", 10000),
            ("BBG000PQKVN8", 20000),
            ("BBG000FD8G46", 30000),
        ]

        requests = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider="Lusid",
                        instrument_id=price[0],
                        instrument_id_type="Figi",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=quotes_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBp"),
            )
            for price in prices
        ]

        return self.quotes_api.upsert_quotes(
            scope=self.market_data_scope,
            request_body={
                "quote" + str(request_number): requests[request_number]
                for request_number in range(len(requests))
            },
        )

    def test_currency_subunit(self):
        """
        Tests that a recipe including an 'infer_fx_rate' boolean reconciles
        market data when quotes provided in currency subunits such as GBp/GBx.
        LUSID will look to translate the quotes back to the portfolio base currency,
        based on prices in the quotes store
        :return: None
        """

        # Upsert quotes with a timedelta of 2 days against out valuation date
        quotes_response = self.upsert_quotes(self.effective_date)
        self.assertEqual(len(quotes_response.failed), 0)

        # Upsert recipe with fx inference set to True
        recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, infer_fx_rate=True
        )
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Valuation/PvInPortfolioCcy)"

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.recipe_scope, self.recipe_code
        )

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
