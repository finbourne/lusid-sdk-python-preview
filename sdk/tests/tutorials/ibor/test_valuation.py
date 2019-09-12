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
        cls.aggregation_api = lusid.AggregationApi(api_client)
        cls.quotes_api = lusid.QuotesApi(api_client)
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

        prices = [
            models.InstrumentAnalytic(self.instrument_ids[0], 100),
            models.InstrumentAnalytic(self.instrument_ids[1], 200),
            models.InstrumentAnalytic(self.instrument_ids[2], 300)
        ]

        requests = []
        for ii in range(3):
            requests.append(
                models.UpsertQuoteRequest(
                    quote_id=models.QuoteId(
                        models.QuoteSeriesId(
                            provider="DataScope",
                            instrument_id=self.instrument_ids[ii],
                            instrument_id_type="LusidInstrumentId",
                            quote_type="Price",
                            field="mid"
                        ),
                        effective_at=effective_date
                    ),
                    metric_value=models.MetricValue(
                        value=prices[ii].value,
                        unit="GBP"
                    )
                )
            )

        # for request_number in range(len(requests)):
        quotes_result = self.quotes_api.upsert_quotes(TestDataUtilities.tutorials_scope,
                                                      quotes={"quote" + str(request_number): requests[request_number]
                                                              for request_number in range(len(requests))})

        inline_recipe = models.ConfigurationRecipe(
            code='quotes_recipe',
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

        aggregation_request = models.AggregationRequest(
            inline_recipe=inline_recipe,
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

        # Asserts
        assert len(aggregation.data) == 3
        assert aggregation.data[0]["Sum(Holding/default/PV)"] == 10000
        assert aggregation.data[1]["Sum(Holding/default/PV)"] == 20000
        assert aggregation.data[2]["Sum(Holding/default/PV)"] == 30000
