import unittest
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Valuation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client factory
        api_client_factory = TestDataUtilities.api_client_factory()

        cls.transaction_portfolios_api = api_client_factory.build(lusid.TransactionPortfoliosApi)
        cls.instruments_api = api_client_factory.build(lusid.InstrumentsApi)
        cls.recipes_api = api_client_factory.build(lusid.ConfigurationRecipeApi)
        cls.aggregation_api = api_client_factory.build(lusid.AggregationApi)
        cls.quotes_api = api_client_factory.build(lusid.QuotesApi)
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    @lusid_feature("F20")
    def test_portfolio_aggregation(self):

        effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

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
