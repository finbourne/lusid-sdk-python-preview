import unittest
from datetime import datetime, timedelta

import pytz as pytz

import lusid
import lusid.models as models
from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.credentials_source import CredentialsSource
from utilities.test_data_utilities import TestDataUtilities


class Quotes(unittest.TestCase):
    quotes_api = None

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.quotes_api = lusid.QuotesApi(api_client)

    def test_add_quote(self):

        request = models.UpsertQuoteRequest(
            quote_id=models.QuoteId(
                provider="DataScope",
                instrument_id="BBG000B9XRY4",
                instrument_id_type="Figi",
                quote_type="Price",
                price_side="Mid"
            ),
            metric_value=models.MetricValue(
                value=199.23,
                unit="USD"
            ),
            effective_at=datetime(2019, 4, 15, tzinfo=pytz.utc)
        )

        self.quotes_api.upsert_quotes(TestDataUtilities.tutorials_scope, quotes=[request])

    def test_get_quote_for_instrument_for_single_day(self):

        quote_id = models.QuoteId(
            provider="DataScope",
            instrument_id="BBG000B9XRY4",
            instrument_id_type="Figi",
            quote_type="Price",
            price_side="Mid"
        )
        effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        # get the close quote for AAPL on 15-Apr-19
        quote_response = self.quotes_api.get_quotes(
            scope=TestDataUtilities.tutorials_scope,
            effective_at=effective_date,
            quote_ids=[quote_id]
        )

        self.assertEqual(len(quote_response.found), 1)

        quote = quote_response.found[0]

        self.assertEqual(quote.metric_value.value, 199.23)

    def test_get_timeseries_quotes(self):

        start_date = datetime(2019, 4, 15, tzinfo=pytz.utc)
        date_range = [start_date - timedelta(days=x) for x in range(0, 30)]

        quote_id = models.QuoteId(
            provider="DataScope",
            instrument_id="BBG000B9XRY4",
            instrument_id_type="Figi",
            quote_type="Price",
            price_side="Mid"
        )

        # get the quotes for each day in the date range
        quote_responses = [
            self.quotes_api.get_quotes(
                scope=TestDataUtilities.tutorials_scope,
                effective_at=d,
                quote_ids=[quote_id]
            )
            for d in date_range
        ]

        self.assertEqual(len(quote_responses), 30)
