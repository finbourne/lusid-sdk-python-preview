import unittest
import pytz
import lusid
import lusid.models as models
from datetime import datetime
#from utilities import TestDataUtilities


class ComplexInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        api_client = TestDataUtilities.api_client()
        cls.instruments_api = lusid.InstrumentsApi(api_client)

    # Define a function to upsert instrument
    def upsert_otc_to_lusid(self, instrument, name, lusid_id):
        response = self.instruments_api.upsert_instruments(
            request_body={
                lusid_id: models.InstrumentDefinition(
                    name=name,
                    identifiers={
                        "ClientInternal": models.InstrumentIdValue(value=lusid_id)
                    },
                    definition=instrument,
                )
            }
        )
        # Check for failures with response
        self.assertEqual(len(response.values), 1, response.failed)

    def query_otc_from_lusid(self, lusid_id):
        return self.instruments_api.get_instruments(
            identifier_type="ClientInternal", request_body=[lusid_id]
        )

    # Create an FX-Forward (that then upsert to LUSID)
    def test_create_fx_forward(self):
        fx_forward = lusid.FxForward(
            dom_amount=-1,
            fgn_amount=109,
            dom_ccy="USD",
            fgn_ccy="JPY",
            start_date=datetime(2020, 2, 7, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2020, 9, 18, 00, tzinfo=pytz.utc),
            instrument_type="FxForward",
        )

        # Assert instrument was created
        self.assertIsNotNone(fx_forward)

        # Upsert to LUSID with unique ID and
        unique_id = "id-fxfwd-2"
        self.upsert_otc_to_lusid(fx_forward, "some-name-for-this-fxforward", unique_id)

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertIsNotNone(response)
        self.assertGreater(len(response.values), 0, "Response.values = 0")
        saved_fx_forward = response.values[unique_id].instrument_definition

        self.assertEqual(
            saved_fx_forward.instrument_type, lusid.InstrumentType.FXFORWARD
        )
        self.assertEqual(saved_fx_forward.dom_amount, fx_forward.dom_amount)
        self.assertEqual(saved_fx_forward.fgn_amount, fx_forward.fgn_amount)
        self.assertEqual(saved_fx_forward.dom_ccy, fx_forward.dom_ccy)
        self.assertEqual(saved_fx_forward.fgn_ccy, fx_forward.fgn_ccy)

    def test_create_fx_option(self):
        fx_option = lusid.FxOption(
            strike=100,
            dom_ccy="USD",
            fgn_ccy="JPY",
            start_date=datetime(2020, 2, 7, 00, tzinfo=pytz.utc),
            option_maturity_date=datetime(2020, 12, 18, 00, tzinfo=pytz.utc),
            option_settlement_date=datetime(2020, 12, 21, 00, tzinfo=pytz.utc),
            is_call_not_put=True,
            is_delivery_not_cash=True,
            instrument_type="FxOption",
        )

        # Assert instrument was created
        self.assertIsNotNone(fx_option)

        # Upsert to LUSID with unique ID and
        unique_id = "id-fxopt-1"
        self.upsert_otc_to_lusid(fx_option, "some-name-for-this-fxoption", unique_id)

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertIsNotNone(response)
        self.assertGreater(len(response.values), 0, "Response.values = 0")
        saved_fx_option = response.values[unique_id].instrument_definition

        self.assertEqual(saved_fx_option.instrument_type, lusid.InstrumentType.FXOPTION)
        self.assertEqual(saved_fx_option.dom_ccy, fx_option.dom_ccy)
        self.assertEqual(saved_fx_option.fgn_ccy, fx_option.fgn_ccy)
        self.assertEqual(saved_fx_option.start_date, fx_option.start_date)
        self.assertEqual(
            saved_fx_option.option_maturity_date, fx_option.option_maturity_date
        )
        self.assertEqual(
            saved_fx_option.option_settlement_date, fx_option.option_settlement_date
        )
        self.assertEqual(saved_fx_option.is_call_not_put, fx_option.is_call_not_put)
        self.assertEqual(
            saved_fx_option.is_delivery_not_cash, fx_option.is_delivery_not_cash
        )

        # to be inserted here
    def test_create_term_deposit(self):

        term_deposit = lusid.TermDeposit(
            startDate=datetime(2020, 2, 5, 00, tzinfo=pytz.utc),
            maturityDate=datetime(2020, 2, 8, 00, tzinfo=pytz.utc),
            contractSize=1000000,
            flowConvention=lusid.FlowConventions(
                scope=None,
                code=None,
                currency="GBP",
                paymentFrequency="6M",
                rollConvention="MF",
                dayCountConvention="Act365",
                paymentCalendars=[],
                resetCalendars=[],
                settleDays=1,
                resetDays=0
                ),
            rate=0.03,
            instrument_type="TermDeposit"
        )

        # Assert instrument was created
        self.assertIsNotNone(term_deposit)


