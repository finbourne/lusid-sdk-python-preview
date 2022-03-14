import unittest

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import TestDataUtilities, BaseValuationUtilities


class ScalingFactor(BaseValuationUtilities):
    """This is an example of using the scale_factor in an
    upsert_quotes request, which is applicable to instruments
    where the price requires scaling, such as bonds. For a bond
    with quotes as a percentage of par of 100, adding this value
    as the scaling factor will account for the transformation when
    running a valuation
    """

    @lusid_feature("F14-5")
    def upsert_quotes(self, scale_factor) -> None:
        """
        Upserts quotes using a scaling factor parameter, that can be
        used to for non-standard quotes such as bond prices that are
        quotes as percentage as par (i.e. 'scaling_factor=100').
        :param float scale_factor: scale factor for non-standard quotes
        :return: None
        """
        # Add prices as a percentage of par
        prices = [
            ("BBG00Y271826", 100),
            ("BBG005D5KGM0", 200),
            ("BBG000DPM932", 300)
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
                    default_instrument_code_type="Figi",
                    default_scope=TestDataUtilities.tutorials_scope,
                ),
            ),
        )

    @lusid_feature("F10-7")
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
        self.assertEqual(valuation.data[0][self.valuation_portfolio_key], 100)


if __name__ == "__main__":
    unittest.main()
