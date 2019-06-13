import unittest
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.credentials_source import CredentialsSource
from utilities.instrument_loader import InstrumentLoader
from utilities.test_data_utilities import TestDataUtilities


class Valuation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.analytic_stores_api = lusid.AnalyticsStoresApi(api_client)
        cls.aggregation_api = lusid.AggregationApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    def test_portfolio_aggregation(self):

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

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
                                                            transactions=transactions)

        analytic_stores = self.analytic_stores_api.list_analytic_stores()
        store = next(
            filter(lambda s: s.date == effective_date and s.scope == TestDataUtilities.tutorials_scope,
                   analytic_stores.values), None)

        if store is None:
            #   create an analytic store
            analytic_store_request = models.CreateAnalyticStoreRequest(scope=TestDataUtilities.tutorials_scope,
                                                                       date=effective_date)

            self.analytic_stores_api.create_analytic_store(request=analytic_store_request)

        prices = [
            models.InstrumentAnalytic(self.instrument_ids[0], 100),
            models.InstrumentAnalytic(self.instrument_ids[1], 200),
            models.InstrumentAnalytic(self.instrument_ids[2], 300)
        ]

        #   add prices
        self.analytic_stores_api.set_analytics(scope=TestDataUtilities.tutorials_scope,
                                               year=effective_date.year,
                                               month=effective_date.month,
                                               day=effective_date.day,
                                               data=prices)

        aggregation_request = models.AggregationRequest(
            recipe_id=models.ResourceId(TestDataUtilities.tutorials_scope, "default"),
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum")
            ],
            group_by=["Instrument/default/Name"],
            effective_at=effective_date
        )

        #   do the aggregation
        aggregation = self.aggregation_api.get_aggregation_by_portfolio(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code,
                                                                        request=aggregation_request)

        for item in aggregation.data:
            print("\t{}\t{}\t{}".format(item["Instrument/default/Name"], item["Proportion(Holding/default/PV)"],
                                        item["Sum(Holding/default/PV)"]))
