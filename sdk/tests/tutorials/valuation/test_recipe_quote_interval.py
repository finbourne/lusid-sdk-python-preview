import unittest
from datetime import datetime
from datetime import timedelta
import json

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import BaseValuationUtilities


class QuoteIntervalRecipe(BaseValuationUtilities):
    """This is an example of using recipes to resolve market data
    using a quote interval, which allows the valuation engine to
    resolve data for a broader time window. For example, setting the
    window to '5D.0D' will look back 5 days from the provided valuation
    date and use the first price that matches the criteria.
    """

    def create_configuration_recipe(
        self, recipe_scope, recipe_code, quote_interval
    ) -> lusid.models.ConfigurationRecipe:
        """
        Creates a configuration recipe that can be used inline or upserted,
        using a 'quote_interval' to look back for pricing data in the quotes
        store when missing for the selected valuation date. The interval is
        specified as a dot separated string with a start and end period, e.g.
        5D.0D to look back 5D starting today (0 days ago).
        :param str recipe_scope: The scope for the configuration recipe
        :param str recipe_code: The code of the the configuration recipe
        :param str quote_interval: The look back interval for quotes data
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
                        quote_interval=quote_interval,
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


    def upsert_quotes(self, quotes_date) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param datetime quotes_date: The date of the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("BBG000BF46Y8", 100),
            ("BBG000PQKVN8", 200),
            ("BBG000FD8G46", 300),
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

    @lusid_feature ("F11-1")
    def test_quote_interval(self):
        """
        Tests that a recipe including a 'quote_interval' parameter
        reconciles market data when not within the selected valuation
        date or time-interval. LUSID will look back for prices in the quotes
        store based on the specified interval in the 'MarketDataKeyRule'
        :return: None
        """

        # Upsert quotes with a timedelta of 2 days against out valuation date
        quotes_response = self.upsert_quotes(self.effective_date - timedelta(days=2))
        self.assertEqual(len(quotes_response.failed), 0)

        # Upsert recipe with '2D' quote interval to increase valuation window
        recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, "2D.0D"
        )
        self.upsert_recipe_request(recipe)

        # Create valuation request
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.portfolio_code,
            self.recipe_scope,
            self.recipe_code,
        )

        valuation = self.aggregation_api.get_valuation(
            valuation_request=valuation_request,
        )

        # Asserts
        self.assertEqual(len(valuation.data), 3)
        self.assertEqual(valuation.data[0][self.valuation_portfolio_key], 10000)
        self.assertEqual(valuation.data[1][self.valuation_portfolio_key], 20000)
        self.assertEqual(valuation.data[2][self.valuation_portfolio_key], 30000)

    def test_error_raised_outside_quote_interval(self):
        """
        Tests that a recipe including a 'quote_interval' parameter
        reconciles market data when not within the selected valuation
        date or time-interval. LUSID will look back for prices in the quotes
        store based on the specified interval in the 'MarketDataKeyRule'
        :return: None
        """
        # Upsert quotes with a timedelta of 2 days against out valuation date
        quotes_response = self.upsert_quotes(self.effective_date - timedelta(days=2))
        self.assertEqual(len(quotes_response.failed), 0)

        # Upsert recipe with '0D' quote interval which is the default value
        recipe = self.create_configuration_recipe(
            self.recipe_scope, self.recipe_code, "0D.0D"
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


if __name__ == "__main__":
    unittest.main()
