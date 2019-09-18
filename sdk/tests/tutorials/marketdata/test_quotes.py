import unittest
from datetime import datetime, timedelta

import pytz as pytz

import lusid
import lusid.models as models
from utilities import TestDataUtilities


class Quotes(unittest.TestCase):
    quotes_api = None

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.quotes_api = lusid.QuotesApi(api_client)

    def test_add_quote(self):

        request = models.UpsertQuoteRequest(
            quote_id=models.QuoteId(
                models.QuoteSeriesId(
                    provider="DataScope",
                    instrument_id="BBG000B9XRY4",
                    instrument_id_type="Figi",
                    quote_type="Price",
                    field="mid"
                ),
                effective_at = datetime(2019, 4, 15, tzinfo=pytz.utc)
            ),
            metric_value=models.MetricValue(
                value=199.23,
                unit="USD"
            )
        )

        self.quotes_api.upsert_quotes(TestDataUtilities.tutorials_scope, quotes={"quote1": request})

    def test_get_quote_for_instrument_for_single_day(self):

        quote_series_id = models.QuoteSeriesId(
            provider="DataScope",
            instrument_id="BBG000B9XRY4",
            instrument_id_type="Figi",
            quote_type="Price",
            field="mid"
        )

        effective_date = datetime(2019, 4, 15, tzinfo=pytz.utc)

        # get the close quote for AAPL on 15-Apr-19
        quote_response = self.quotes_api.get_quotes(
            scope=TestDataUtilities.tutorials_scope,
            effective_at=effective_date,
            quote_ids={"quote1": quote_series_id}
        )

        self.assertEqual(len(quote_response.values), 1)

        quote = quote_response.values["quote1"]

        self.assertEqual(quote.metric_value.value, 199.23)

    def test_get_timeseries_quotes(self):

        start_date = datetime(2019, 4, 15, tzinfo=pytz.utc)
        date_range = [start_date - timedelta(days=x) for x in range(0, 30)]

        quote_id = models.QuoteSeriesId(
            provider="DataScope",
            price_source="USDRC",
            instrument_id="BBG000B9XRY4",
            instrument_id_type="Figi",
            quote_type="Price",
            field="mid"
        )

        # get the quotes for each day in the date range
        quote_responses = [
            self.quotes_api.get_quotes(
                scope=TestDataUtilities.tutorials_scope,
                effective_at=d,
                quote_ids={"quote1": quote_id}
            )
            for d in date_range
        ]

        self.assertEqual(len(quote_responses), 30)
