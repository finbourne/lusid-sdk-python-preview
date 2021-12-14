import unittest
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature

from lusid import ApiException
from utilities import InstrumentLoader, IdGenerator
from utilities import TestDataUtilities


class Valuation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.recipes_api = lusid.ConfigurationRecipeApi(api_client)
        cls.aggregation_api = lusid.AggregationApi(api_client)
        cls.quotes_api = lusid.QuotesApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        for entity, scope, code in cls.id_generator.pop_scope_and_codes():
            try:
                if entity == "portfolio":
                    cls.portfolios_api.delete_portfolio(scope, code)
                elif entity == "recipe":
                    cls.recipes_api.delete_configuration_recipe(scope, code)
            except ApiException as ex:
                print(ex)

    @lusid_feature("F20")
    def test_portfolio_aggregation(self):

        effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)
        self.id_generator.add_scope_and_code("portfolio", TestDataUtilities.tutorials_scope, portfolio_code)

        transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=100,
                                                               price=101,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[1],
                                                               units=100,
                                                               price=102,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[2],
                                                               units=100,
                                                               price=103,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn")
        ]

        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transaction_request=transactions)

        prices = [
            (self.instrument_ids[0], 100),
            (self.instrument_ids[1], 200),
            (self.instrument_ids[2], 300)
        ]

        requests = [
            models.UpsertQuoteRequest(
                quote_id=models.QuoteId(
                    models.QuoteSeriesId(
                        provider="DataScope",
                        instrument_id=price[0],
                        instrument_id_type="LusidInstrumentId",
                        quote_type="Price",
                        field="mid"
                    ),
                    effective_at=effective_date
                ),
                metric_value=models.MetricValue(
                    value=price[1],
                    unit="GBP"
                )
            )
            for price in prices
        ]

        self.quotes_api.upsert_quotes(TestDataUtilities.tutorials_scope,
                                      request_body={"quote" + str(request_number): requests[request_number]
                                              for request_number in range(len(requests))})

        recipe_scope = 'cs-tutorials'
        recipe_code = 'quotes_recipe'

        self.id_generator.add_scope_and_code("recipe", recipe_scope, recipe_code)

        demo_recipe = models.ConfigurationRecipe(
            scope=recipe_scope,
            code=recipe_code,
            market=models.MarketContext(
                market_rules=[],
                suppliers=models.MarketContextSuppliers(
                    equity='DataScope'
                ),
                options=models.MarketOptions(
                    default_supplier='DataScope',
                    default_instrument_code_type='LusidInstrumentId',
                    default_scope=TestDataUtilities.tutorials_scope)
            )
        )
        upsert_recipe_request = models.UpsertRecipeRequest(demo_recipe)
        self.recipes_api.upsert_configuration_recipe(upsert_recipe_request)

        valuation_request = models.ValuationRequest(
            recipe_id=models.ResourceId(scope=recipe_scope,code=recipe_code),
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum")
            ],
            group_by=["Instrument/default/Name"],
            portfolio_entity_ids = [
                models.PortfolioEntityId(scope = TestDataUtilities.tutorials_scope, code = portfolio_code)
            ],
            valuation_schedule=models.ValuationSchedule(effective_at=effective_date)
        )

        #   do the aggregation
        aggregation = self.aggregation_api.get_valuation(valuation_request=valuation_request)

        for item in aggregation.data:
            print("\t{}\t{}\t{}".format(item["Instrument/default/Name"], item["Proportion(Holding/default/PV)"],
                                        item["Sum(Holding/default/PV)"]))

        # Asserts
        self.assertEqual(len(aggregation.data),3)
        self.assertEqual(aggregation.data[0]["Sum(Holding/default/PV)"], 10000)
        self.assertEqual(aggregation.data[1]["Sum(Holding/default/PV)"], 20000)
        self.assertEqual(aggregation.data[2]["Sum(Holding/default/PV)"], 30000)
