import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import TestDataUtilities, BaseValuationUtilities


class Valuation(BaseValuationUtilities):
    """This is an example of conducting a simple valution in LUSID,
    illustrating how to create a portfolio, add transactions and up-
    sert market data for pricing. Finally, a valuation_request is
    carried out on the constructed portfolio
    """

    def upsert_quotes(self) -> models.UpsertQuotesResponse:
        """
        Upserts quotes into LUSID to be used in pricing valuation
        :param str instrument_id: The identifier used in the upserted quotes
        :return: UpsertQuotesResponse
        """

        prices = [
            ("BBG00Y271826", 100),
            ("BBG005D5KGM0", 200),
            ("BBG000DPM932", 300),
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
        Creates a simple configuration recipe that can be upserted and
        and referenced in valuation. Sets a simple lookup based recipe.
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

    def upsert_recipe_request(self, configuration_recipe) -> None:
        """
        Structures a recipe request and upserts it into LUSID
        :param ConfigurationRecipe configuration_recipe: Recipe configuration
        :return: None
        """

        upsert_recipe_request = models.UpsertRecipeRequest(configuration_recipe)
        self.recipes_api.upsert_configuration_recipe(upsert_recipe_request)

    @lusid_feature("F10-1")
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

    def test_valuation(self) -> None:
        """
        General valuation test using an upserted recipe
        """

        # Upsert recipes and quotes
        recipe = self.create_configuration_recipe(self.recipe_scope, self.recipe_code)
        self.upsert_recipe_request(recipe)
        self.upsert_quotes()

        # Create valuation request
        valuation_request = self.create_valuation_request(
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
