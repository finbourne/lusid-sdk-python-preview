import unittest
import json

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import BaseValuationUtilities


class EdiTmRecipes(BaseValuationUtilities):
    """This is an example of a recipe for running valuations with EDI
    and TraderMade market data, that can be added automatically to a
    LUSID environment upon request. When using automated market data
    services, valuation can be carried out by simply providing a recipe
    that points to these sources as shown below."""

    @lusid_feature("F11-5")
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

    def test_edi_base_recipe(self):
        """
        Tests that valuation for a recipe using EDI equity quotes.
        These are updated in LUSID upon client request, and will not require a
        separate API call to upsert quotes/market data.
        """

        #     # Setup scopes for recipe tests
        self.recipe_code = "EdiQuotes"
        self.recipe_scope = "TestEdi"

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

        # Test recipe queries EDI quotes
        with self.assertRaises(Exception) as context:
            # Complete aggregation
            self.aggregation_api.get_valuation(
                valuation_request=valuation_request,
            )
            # Check that 'MarketResolverFailure' exception raised
            self.assertEqual(
                json.loads(context.exception.body)["name"], "MarketResolverFailure"
            )

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

        # Call valuation with recipe identifiers
        valuation_request = self.create_valuation_request(
            self.portfolio_scope,
            self.xccy_portfolio_code,
            self.recipe_scope,
            self.recipe_code,
        )

        # Test recipe queries TM quotes
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
