import unittest
from datetime import datetime
import pytz
import uuid

import lusid
import lusid.models as models
from utilities import PortfolioLoader
from utilities import TestDataUtilities


class EdiTmRecipes(unittest.TestCase):
    """This is an example of a recipe for running valuations with EDI
    and TraderMade market data, that can be added automatically to a
    LUSID environment upon request. When using automated market data
    services, valuation can be carried out by simply providing a recipe
    that points to these sources as shown below."""

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

        # Setup test parameters
        cls.effective_date = datetime(2021, 1, 21, tzinfo=pytz.utc)

        # Setup test data from utilities
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        # Setup test portfolios
        cls.portfolio_scope = TestDataUtilities.tutorials_scope
        cls.gbp_portfolio_code = cls.test_data_utilities.create_transaction_portfolio(
            TestDataUtilities.tutorials_scope
        )
        cls.xccy_portfolio_code = cls.test_data_utilities.create_transaction_portfolio(
            TestDataUtilities.tutorials_scope
        )

        # Load transactions to test portfolio
        portfolio_loader = PortfolioLoader(
            cls.transaction_portfolios_api, cls.instruments_api
        )
        portfolio_loader.setup_gbp_portfolio(
            cls.portfolio_scope, cls.gbp_portfolio_code, cls.effective_date
        )
        portfolio_loader.setup_xccy_portfolio(
            cls.portfolio_scope, cls.xccy_portfolio_code, cls.effective_date
        )

        # Setup scopes for recipe tests
        cls.recipe_scope = "TestEdi"
        cls.recipe_code = "EdiQuotes"

        # Set market data scope for quotes and recipes
        cls.market_data_provider = "Edi"
        cls.market_data_scope = "Test-" + str(uuid.uuid4())

    @classmethod
    def tearDownClass(cls):
        portfolio_codes = [
            cls.gbp_portfolio_code,
            cls.xccy_portfolio_code,
        ]

        # Delete portfolio once tests are concluded
        for code in portfolio_codes:
            cls.portfolios_api.delete_portfolio(TestDataUtilities.tutorials_scope, code)

    def create_configuration_recipe(
        self, recipe_scope, recipe_code
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that can be used inline or upserted,
        using market data key rules to infer EDI close prices for instruments
        using FIGIs or LUIDs as look-up identifiers for equities, and TraderMade
        FX rates. These can be setup based on client request, and would allow for
        pricing without the need to upsert quotes separately
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :param str default_id: The default identifier used for looking up quotes
        :return: ConfigurationRecipe
        """

        return models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            market=models.MarketContext(
                market_rules=[
                    models.MarketDataKeyRule(
                        key="Equity.Figi.*",
                        supplier="Edi",
                        data_scope="EDI",
                        quote_type="Price",
                        field="close",
                        quote_interval="1D.0D",
                        price_source="EOD price file",
                    ),
                    models.MarketDataKeyRule(
                        key="Equity.LusidInstrumentId.*",
                        supplier="Edi",
                        data_scope="EDI",
                        quote_type="Price",
                        field="close",
                        quote_interval="1D.0D",
                        price_source="EOD price file",
                    ),
                    models.MarketDataKeyRule(
                        key="Fx.CurrencyPair.*",
                        supplier="TraderMade",
                        data_scope="TraderMadeFxData",
                        quote_type="Price",
                        field="close",
                        quote_interval="1D.0D",
                        price_source="",
                    ),
                ],
                suppliers=models.MarketContextSuppliers(
                    equity=self.market_data_provider
                ),
                options=models.MarketOptions(
                    default_supplier=self.market_data_provider,
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
        self, portfolio_scope, portfolio_code, recipe_scope=None, recipe_code=None
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
                    scope=portfolio_scope,
                    code=portfolio_code,
                    portfolio_entity_type="SinglePortfolio",
                )
            ],
            valuation_schedule=models.ValuationSchedule(
                effective_from=self.effective_date, effective_at=self.effective_date
            ),
        )

    def test_edi_base_recipe(self):
        """
        Tests that valuation for a recipe using EDI equity quotes.
        These are updated in LUSID upon client request, and will not require a
        separate API call to upsert quotes/market data.
        """

        # Upsert recipe
        recipe = self.create_configuration_recipe(self.recipe_scope, self.recipe_code)
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Valuation/PvInPortfolioCcy)"

        # Create valuation request
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.gbp_portfolio_code,
            self.recipe_scope,
            self.recipe_code,
        )

        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request,
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][valuation_key], 242.1)
        self.assertEqual(valuation.data[1][valuation_key], 8158.0)
        self.assertEqual(valuation.data[2][valuation_key], 1840.5)

    def test_trader_made_base_recipe(self):
        """
        Tests that valuation/valuation for a recipe using TraderMade FX quotes,
        by valuing a cross-currency portfolio using GBP quotes.
        These are updated in LUSID upon client request, and will not require a
        separate API call to upsert quotes/market data.
        """

        # Upsert recipe
        recipe = self.create_configuration_recipe(self.recipe_scope, self.recipe_code)
        self.upsert_recipe_request(recipe)

        # Set valuation result key
        valuation_key = "Sum(Valuation/PvInPortfolioCcy)"

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.xccy_portfolio_code,
            self.recipe_scope,
            self.recipe_code,
        )

        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request,
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][valuation_key], 242.1)
        self.assertEqual(valuation.data[1][valuation_key], 8158.0)
        self.assertEqual(valuation.data[2][valuation_key], 1840.5)


if __name__ == "__main__":
    unittest.main()
