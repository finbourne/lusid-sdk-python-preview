import unittest
import pytz
import lusid
import lusid.models as models
from datetime import datetime
from utilities import TestDataUtilities


class ComplexInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client factory
        api_client_factory = TestDataUtilities.api_client_factory()
        cls.instruments_api = api_client_factory.build(lusid.InstrumentsApi)

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

    def test_create_term_deposit(self):

        term_deposit = models.TermDeposit(
            start_date=datetime(2020, 2, 5, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2020, 2, 8, 00, tzinfo=pytz.utc),
            contract_size=1000000,
            flow_convention=models.FlowConventions(
                scope=None,
                code=None,
                currency="GBP",
                payment_frequency="6M",
                roll_convention="MF",
                day_count_convention="Act365",
                payment_calendars=[],
                reset_calendars=[],
                settle_days=1,
                reset_days=0
                ),
            rate=0.03,
            instrument_type="TermDeposit"
        )

        request_id = "upsert_request_001"
        term_deposit_identifier = "TermDepositInstrument"
        upsert_term_deposit = self.instruments_api.upsert_instruments(request_body={
        request_id: models.InstrumentDefinition(
            name="Term Deposit Example",
            identifiers={"ClientInternal": models.InstrumentIdValue(term_deposit_identifier)},
            definition=term_deposit
        )
    })
        # Assert instrument was created
        self.assertIsNotNone(upsert_term_deposit.values[request_id].instrument_definition)
        self.assertIsNotNone(upsert_term_deposit.values[request_id].lusid_instrument_id)

        # Remove the test instrument
        self.instruments_api.delete_instrument("ClientInternal",term_deposit_identifier)

    def test_create_zero_coupon_bond(self):

        zero_coupon_bond = models.Bond(
            start_date=datetime(2020, 2, 7, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2020, 9, 18, 00, tzinfo=pytz.utc),
            dom_ccy="GBP",
            principal=100000,
            coupon_rate=0,
            flow_conventions=models.FlowConventions(
                scope=None,
                code=None,
                currency="GBP",
                payment_frequency="0Invalid",
                roll_convention="None",
                day_count_convention="Invalid",
                payment_calendars=[],
                reset_calendars=[],
                settle_days=2,
                reset_days=2
                ),
            identifiers={},
            instrument_type="Bond"
        )

        request_id = "upsert_request_001"
        zero_coupon_bond_identifier = "ZeroCouponBondInstrument"
        upsert_zero_coupon_bond = self.instruments_api.upsert_instruments(request_body={
            request_id: models.InstrumentDefinition(
                name="Zero Coupon Bond Example",
                identifiers={"ClientInternal": models.InstrumentIdValue(zero_coupon_bond_identifier)},
                definition=zero_coupon_bond
            )
        })
        # Assert instrument was created
        self.assertIsNotNone(upsert_zero_coupon_bond.values[request_id].instrument_definition)
        self.assertIsNotNone(upsert_zero_coupon_bond.values[request_id].lusid_instrument_id)

        # Remove the test instrument
        self.instruments_api.delete_instrument("ClientInternal", zero_coupon_bond_identifier)

