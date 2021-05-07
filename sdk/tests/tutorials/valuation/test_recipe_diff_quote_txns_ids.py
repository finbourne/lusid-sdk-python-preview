import unittest
import json
from datetime import datetime
import pytz
import uuid

import lusid
import lusid.models as models
from utilities import PortfolioLoader
from utilities import TestDataUtilities


class IdentifiersRecipe(unittest.TestCase):
    """This is an example recipe showing handling of differing
    identifiers in valuation. When using a different identifier
    when setting transactions to the ones used for market data
    in the quotes store, the valuation engine can resolve the
    two provided both are stored on the instrument level. When
    only one is stored in the instruments master, valuation will
    return a 'MarketResolverFailure', which can be solved by
    adding the missing identifier to the instrument.
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

        # Setup test parameters
        cls.effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        # Setup test data from utilities
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

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

        # Setup scopes for recipe tests
        cls.recipe_scope = "TestIdentifiers"
        cls.recipe_code = "SimpleQuotes"

        # Set market data scope to be used with quotes and recipes
        cls.market_data_provider = "Lusid"
        cls.market_data_scope = "Test-" + str(uuid.uuid4())

    @classmethod
    def tearDownClass(cls):
        # Delete portfolio once tests are concluded
        cls.portfolios_api.delete_portfolio(
            TestDataUtilities.tutorials_scope, cls.portfolio_code
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

    def upsert_quotes(self, instrument_id) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param str instrument_id: The identifier used in the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("GB0008847096", 100),
            ("GB00B1CRLC47", 200),
            ("BMG4593F1389", 300),
        ]

        requests = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider=self.market_data_provider,
                        instrument_id=price[0],
                        instrument_id_type=instrument_id,
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=self.effective_date,
                ),
                metric_value=models.MetricValue(value=price[1], unit="GBP"),
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

    def create_configuration_recipe(
        self, recipe_scope, recipe_code, default_id
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that sets the default lookup identifier
        used for reconciling quotes. In cases where transactions are booked using
        different identifiers than those used in upserting quotes, LUSID will try
        and reconcile these, provided both identifiers are stored on the instruments.
        valuation request have
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :param str default_id: The default identifier used for looking up quotes
        :return: ConfigurationRecipe
        """

        return models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            # Specify the market context around which pricing data to use
            market=models.MarketContext(
                # Set the pricing data defaults for identifiers, scope and provider
                options=models.MarketOptions(
                    default_supplier=self.market_data_provider,
                    default_instrument_code_type=default_id,
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

    def test_raises_exception_when_instrument_id_not_updated(self) -> None:
        """
        Tests that valuation raises a 'MarketResolverFailure' exception when quotes and
        transactions are loaded using different identifiers. This only occurs when the
        identifiers (in this case 'Isin') have not been added to the instruments used
        in the valuation request, i.e. instruments need updating to resolve quotes.
        """
        # Upsert quotes specifying the quote identifier
        quotes_response = self.upsert_quotes(instrument_id="Isin")
        self.assertEqual(len(quotes_response.failed), 0)

        # Create and upsert recipe, setting a default look-up id for quotes
        recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, default_id="Isin"
        )
        self.upsert_recipe_request(recipe)

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.recipe_scope, self.recipe_code
        )

        with self.assertRaises(Exception) as context:
            # Complete aggregation
            self.aggregation_api.get_valuation(
                valuation_request=valuation_request,
            )
            # Check that 'MarketResolverFailure' exception raised
            self.assertEqual(
                json.loads(context.exception.body)["name"], "MarketResolverFailure"
            )

    def test_differing_quote_and_transaction_instrument_ids(self) -> None:
        """
        Tests that valuation works when quotes uploaded using different identifiers
        than the ones used in booking transactions. LUSID will seek to match quotes
        to instruments using the provided identifiers, which will act as a bridge to
        the identifiers used in valuation. Such a market data reconciliation issue
        can be solved by adding the quote identifiers to the instruments.
        """

        quotes_response = self.upsert_quotes(instrument_id="Isin")
        self.assertEqual(len(quotes_response.failed), 0)

        # Create and upsert recipe, setting a default look-up id for quotes
        recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, default_id="Isin"
        )
        self.upsert_recipe_request(recipe)

        # Instrument ISINs from the upserted quotes
        prices = [
            ("GB0008847096", 100),
            ("GB00B1CRLC47", 200),
            ("BMG4593F1389", 300),
        ]
        # Instrument IDs as upserted originally using the InstrumentLoader()
        instruments = [
            ("BBG000BF46Y8", "TESCO PLC"),
            ("BBG000PQKVN8", "MONDI PLC"),
            ("BBG000FD8G46", "HISCOX LTD"),
        ]

        # Create an upsert instrument request including the ISINs
        update_instrument_request = {
            id[0]: models.InstrumentDefinition(
                name=id[1],
                identifiers={
                    "Figi": models.InstrumentIdValue(value=id[0]),
                    "Isin": models.InstrumentIdValue(value=prices[i][0]),
                },
            )
            for i, id in enumerate(instruments)
        }

        # Upsert instruments with ISINs to update the instrument identifiers
        response = self.instruments_api.upsert_instruments(update_instrument_request)
        assert len(response.failed) == 0

        # Set valuation result key
        valuation_key = "Sum(Valuation/PvInPortfolioCcy)"

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.recipe_scope, self.recipe_code
        )

        # Complete valuation
        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][valuation_key], 10000)
        self.assertEqual(valuation.data[1][valuation_key], 20000)
        self.assertEqual(valuation.data[2][valuation_key], 30000)
