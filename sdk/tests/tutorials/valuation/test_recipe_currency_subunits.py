import unittest
from datetime import datetime

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import BaseValuationUtilities


class CurrencySubUnitValuation(BaseValuationUtilities):
    """ "This is an example of running valuation with prices quoted
    in currency subunits, a typical example will be GBp/GBx where a
    valuation may be carried out in GBP. In order for LUSID to carry out
    the fx transformation, the key parameter is 'attempt_to_infer_missing_fx'
    which needs to set to 'True' in the ConfigurationRecipe's pricing options
    """

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

    @lusid_feature("F14-6")
    def upsert_quotes(self, quotes_date) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param datetime quotes_date: The date of the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("BBG00Y271826", 10000),
            ("BBG005D5KGM0", 20000),
            ("BBG000DPM932", 30000),
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
