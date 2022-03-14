import unittest

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import BaseValuationUtilities


class MultiSourceRecipe(BaseValuationUtilities):
    """This is an example of using recipes to manage multiple
    market data sources, using a 'MarketDataRule'. These rules
    can be passed as a list, where the sources will be prioritised
    in order, allowing for waterfall logic when resolving market data.
    Multiple price sources can exist under a given market data provider.
    """

    @lusid_feature("F11-7")
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
        # Upsert quotes and recipe
        quotes_response = self.upsert_quotes()
        self.assertEqual(len(quotes_response.failed), 0)
        recipe = self.create_configuration_recipe(self.recipe_scope, self.recipe_code)
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


if __name__ == "__main__":
    unittest.main()
