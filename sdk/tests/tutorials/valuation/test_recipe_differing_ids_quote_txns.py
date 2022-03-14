import json

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import BaseValuationUtilities


class IdentifiersValuation(BaseValuationUtilities):
    """This is an example recipe showing handling of differing
    identifiers in valuation. When using a different identifier
    when setting transactions to the ones used for market data
    in the quotes store, the valuation engine can resolve the
    two provided both are stored on the instrument level. When
    only one is stored in the instruments master, valuation will
    return a 'MarketResolverFailure', which can be solved by
    adding the missing identifier to the instrument.
    """

    def upsert_quotes(self, instrument_id) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param str instrument_id: The identifier used in the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("GB00BMH18Q19", 100),
            ("US31959T1025", 200),
            ("GB00B1QH8P22", 300),
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

    @lusid_feature("F10-8")
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

        # Create valuation request
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.portfolio_code,
            self.recipe_scope,
            self.recipe_code,
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
    @lusid_feature("F10-9")
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
            ("GB00BMH18Q19", 100),
            ("US31959T1025", 200),
            ("GB00B1QH8P22", 300),
        ]
        # Instrument IDs as upserted originally using the InstrumentLoader()
        instruments = [
            ("BBG00Y271826", "BYTES TECHNOLOGY GROUP PLC"),
            ("BBG005D5KGM0", "FIRST CITRUS BANCORPORATION"),
            ("BBG000DPM932", "FRASERS GROUP PLC")
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
        self.assertEqual(len(response.failed), 0)

        # Create valuation request
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.portfolio_code,
            self.recipe_scope,
            self.recipe_code,
        )

        # Complete valuation
        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][self.valuation_portfolio_key], 10000)
        self.assertEqual(valuation.data[1][self.valuation_portfolio_key], 20000)
        self.assertEqual(valuation.data[2][self.valuation_portfolio_key], 30000)
