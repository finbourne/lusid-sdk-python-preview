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

    def create_aggregation_request(
        self, inline_recipe
    ) -> lusid.models.AggregationRequest:
        """
        Creates an aggregation request that aggregates valuation results based on
        provided inline recipe or recipe identifiers when using an upserted one
        :param ConfigurationRecipe inline_recipe: A configured recipe to be used inline
        :return: AggregationRequest
        """

        return models.AggregationRequest(
            inline_recipe=inline_recipe,
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum"),
            ],
            group_by=["Instrument/default/Name"],
            effective_at=self.effective_date,
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
        Creates a configuration recipe that can be used inline or upserted,
        and sets the default lookup identifier for quotes
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

    def test_raises_exception_when_instrument_id_not_updated(self) -> None:
        """
        Tests that aggregation/valuation raises an 'MarketResolverFailure' exception
        when quotes and transactions are loaded using different identifiers. This only
        occurs when the identifiers (in this case 'Isin') have not been added to the
        instruments used in valuation
        """
        # Upsert quotes specifying the quote identifier
        quotes_response = self.upsert_quotes(instrument_id="Isin")
        self.assertEqual(len(quotes_response.failed), 0)
        # Set default look-up id for quotes
        in_line_recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, default_id="Isin"
        )

        # Call aggregation with recipe identifiers
        aggregation_request = self.create_aggregation_request(in_line_recipe)

        with self.assertRaises(Exception) as context:
            # Complete aggregation
            self.aggregation_api.get_aggregation(
                scope=TestDataUtilities.tutorials_scope,
                code=self.portfolio_code,
                aggregation_request=aggregation_request,
            )
            # Check that 'MarketResolverFailure' exception raised
            self.assertEqual(
                json.loads(context.exception.body)["name"], "MarketResolverFailure"
            )

    def test_differing_quote_and_transaction_instrument_ids(self) -> None:
        """
        Tests that aggregation/valuation for when quotes uploaded using a different
        identifier than transactions. LUSID will seek to match by unique identifiers,
        provided these are mapped in 'instruments'. This market data reconciliation
        issue can be solved by adding the quote identifiers to the instruments
        """

        quotes_response = self.upsert_quotes(instrument_id="Isin")
        self.assertEqual(len(quotes_response.failed), 0)

        in_line_recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, default_id="Isin"
        )

        # Instrument FIGIs from the upserted quotes
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
        valuation_key = "Sum(Holding/default/PV)"

        # Call aggregation with recipe identifiers
        aggregation_request = self.create_aggregation_request(in_line_recipe)

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
