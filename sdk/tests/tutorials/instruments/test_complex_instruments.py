import unittest
import pytz
import lusid
from lusidfeature import lusid_feature
import lusid.models as models
from datetime import datetime
from utilities import TestDataUtilities


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

    @lusid_feature("F37")
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

    @lusid_feature("F42")
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

    @lusid_feature("F43")
    def test_create_bond(self):

        bond = models.Bond(
            start_date=datetime(2020, 1, 1, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2030, 1, 1, 00, tzinfo=pytz.utc),
            dom_ccy="GBP",
            principal=1000,
            coupon_rate=0.05,
            flow_conventions=models.FlowConventions(
                # coupon payment currency
                currency="GBP",
                # semi-annual coupon payments
                payment_frequency="6M",
                # modified following rolling convention (other options : ModifiedPrevious, NoAdjustment, EndOfMonth,...)
                roll_convention="ModifiedFollowing",
                # using an Actual/365 day count convention (other options : Act360, ActAct, ...)
                day_count_convention="Actual365",
                # no holiday calendar supplied - empty list
                payment_calendars=[],
                reset_calendars=[],
                settle_days=2,
                reset_days=2,
            ),
            identifiers={"clientInternal": "id-bond-1"},
            instrument_type="Bond",
        )

        # Assert instrument was created
        self.assertIsNotNone(bond)

        # Upsert to LUSID with unique ID and
        unique_id = "id-bond-1"
        self.upsert_otc_to_lusid(bond, "some-name-for-this-bond", unique_id)

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertIsNotNone(response)
        self.assertGreater(len(response.values), 0, "Response.values = 0")

        saved_bond = response.values[unique_id].instrument_definition

        self.assertEqual(saved_bond.instrument_type, lusid.InstrumentType.BOND)
        self.assertEqual(saved_bond.start_date, bond.start_date)
        self.assertEqual(saved_bond.maturity_date, bond.maturity_date)
        self.assertEqual(saved_bond.dom_ccy, bond.dom_ccy)
        self.assertEqual(saved_bond.principal, bond.principal)
        self.assertEqual(saved_bond.coupon_rate, bond.coupon_rate)
        self.assertEqual(
            saved_bond.flow_conventions.currency, bond.flow_conventions.currency
        )
        self.assertEqual(
            saved_bond.flow_conventions.day_count_convention,
            bond.flow_conventions.day_count_convention,
        )
        self.assertEqual(
            saved_bond.flow_conventions.payment_calendars,
            bond.flow_conventions.payment_calendars,
        )
        self.assertEqual(
            saved_bond.flow_conventions.reset_calendars,
            bond.flow_conventions.reset_calendars,
        )
        self.assertEqual(
            saved_bond.flow_conventions.payment_frequency,
            bond.flow_conventions.payment_frequency,
        )
        self.assertEqual(
            saved_bond.flow_conventions.reset_days, bond.flow_conventions.reset_days
        )
        self.assertEqual(
            saved_bond.flow_conventions.settle_days, bond.flow_conventions.settle_days
        )
        self.assertEqual(
            saved_bond.flow_conventions.roll_convention,
            bond.flow_conventions.roll_convention,
        )

    @lusid_feature("F38")
    def test_create_interest_rate_swap(self):

        # Create the flow convention for each leg + one for the index
        flow_convention_fixed = models.FlowConventions(
            currency="EUR",
            payment_frequency="6M",
            day_count_convention="Actual365",
            roll_convention="ModifiedFollowing",
            payment_calendars=[],
            reset_calendars=[],
            settle_days=2,
            reset_days=0,
        )
        flow_convention_float = models.FlowConventions(
            currency="EUR",
            payment_frequency="6M",
            day_count_convention="Act360",
            roll_convention="ModifiedFollowing",
            payment_calendars=[],
            reset_calendars=[],
            settle_days=2,
            reset_days=0,
        )

        float_leg_idx_conv = models.IndexConvention(
            currency="EUR",
            code="EURIBOR",
            payment_tenor="6M",
            fixing_reference="EUR6M",
            publication_day_lag=0,
            day_count_convention="Act360",
        )

        # create the leg definitions
        float_leg_definition = models.LegDefinition(
            rate_or_spread=0,
            index_convention=float_leg_idx_conv,
            pay_receive="Receive",
            conventions=flow_convention_float,
            stub_type="Both",
            notional_exchange_type="None",
        )

        fixed_leg_definition = models.LegDefinition(
            rate_or_spread=0.01,
            pay_receive="Pay",
            conventions=flow_convention_fixed,
            stub_type="Both",
            notional_exchange_type="None",
        )

        # create the fixed and floating legs
        fixed_leg = models.FixedLeg(
            start_date=datetime(2019, 10, 1, 0, 0, tzinfo=pytz.utc),
            maturity_date=datetime(2029, 10, 1, 0, 0, tzinfo=pytz.utc),
            notional=10000000,
            leg_definition=fixed_leg_definition,
            instrument_type="FixedLeg",
        )

        floating_leg = models.FloatingLeg(
            start_date=datetime(2019, 10, 1, 0, 0, tzinfo=pytz.utc),
            maturity_date=datetime(2029, 10, 1, 0, 0, tzinfo=pytz.utc),
            notional=10000000,
            leg_definition=float_leg_definition,
            instrument_type="FloatingLeg",
        )

        irs_legs = [fixed_leg, floating_leg]

        # create the swap
        interest_rate_swap_definition = models.InterestRateSwap(
            start_date=datetime(2019, 10, 1, 0, 0, tzinfo=pytz.utc),
            maturity_date=datetime(2029, 10, 1, 0, 0, tzinfo=pytz.utc),
            legs=irs_legs,
            instrument_type="InterestRateSwap",
        )

        # Assert instrument was created
        self.assertIsNotNone(interest_rate_swap_definition)

        # Upsert to LUSID with unique ID and
        unique_id = "id-interest-rate-swap-1"
        self.upsert_otc_to_lusid(
            interest_rate_swap_definition, "some-name-for-this-irs", unique_id
        )

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertIsNotNone(response)
        self.assertGreater(len(response.values), 0, "Response.values = 0")

        saved_irs = response.values[unique_id].instrument_definition
        saved_fixed_leg = saved_irs.legs[0]
        saved_floating_leg = saved_irs.legs[1]

        # Check instrument base details
        self.assertEqual(
            saved_irs.instrument_type, lusid.InstrumentType.INTERESTRATESWAP
        )
        self.assertEqual(saved_irs.start_date, interest_rate_swap_definition.start_date)
        self.assertEqual(
            saved_irs.maturity_date, interest_rate_swap_definition.maturity_date
        )

        # Check leg details
        self.assertEqual(saved_fixed_leg.notional, fixed_leg.notional)
        self.assertEqual(saved_fixed_leg.start_date, fixed_leg.start_date)
        self.assertEqual(saved_fixed_leg.maturity_date, fixed_leg.maturity_date)
        self.assertEqual(saved_fixed_leg.instrument_type, fixed_leg.instrument_type)
        self.assertEqual(
            saved_fixed_leg.leg_definition.pay_receive,
            fixed_leg.leg_definition.pay_receive,
        )
        self.assertEqual(
            saved_fixed_leg.leg_definition.rate_or_spread,
            fixed_leg.leg_definition.rate_or_spread,
        )
        self.assertEqual(
            saved_fixed_leg.leg_definition.stub_type, fixed_leg.leg_definition.stub_type
        )

        # Check leg details
        self.assertEqual(saved_floating_leg.notional, floating_leg.notional)
        self.assertEqual(saved_floating_leg.start_date, floating_leg.start_date)
        self.assertEqual(saved_floating_leg.maturity_date, floating_leg.maturity_date)
        self.assertEqual(
            saved_floating_leg.instrument_type, floating_leg.instrument_type
        )
        self.assertEqual(
            saved_floating_leg.leg_definition.pay_receive,
            floating_leg.leg_definition.pay_receive,
        )
        self.assertEqual(
            saved_floating_leg.leg_definition.rate_or_spread,
            floating_leg.leg_definition.rate_or_spread,
        )
        self.assertEqual(
            saved_floating_leg.leg_definition.stub_type,
            floating_leg.leg_definition.stub_type,
        )

        # Check flow conventions
        saved_float_convention = saved_floating_leg.leg_definition.conventions
        self.assertEqual(
            saved_float_convention.currency, flow_convention_float.currency
        )
        self.assertEqual(
            saved_float_convention.day_count_convention,
            flow_convention_float.day_count_convention,
        )
        self.assertEqual(
            saved_float_convention.payment_calendars,
            flow_convention_float.payment_calendars,
        )
        self.assertEqual(
            saved_float_convention.reset_calendars,
            flow_convention_float.reset_calendars,
        )
        self.assertEqual(
            saved_float_convention.payment_frequency,
            flow_convention_float.payment_frequency,
        )
        self.assertEqual(
            saved_float_convention.reset_days, flow_convention_float.reset_days
        )
        self.assertEqual(
            saved_float_convention.settle_days, flow_convention_float.settle_days
        )
        self.assertEqual(
            saved_float_convention.roll_convention,
            flow_convention_float.roll_convention,
        )

        saved_fixed_convention = saved_fixed_leg.leg_definition.conventions
        self.assertEqual(
            saved_fixed_convention.currency, flow_convention_float.currency
        )
        self.assertEqual(
            saved_fixed_convention.day_count_convention,
            flow_convention_fixed.day_count_convention,
        )
        self.assertEqual(
            saved_fixed_convention.payment_calendars,
            flow_convention_fixed.payment_calendars,
        )
        self.assertEqual(
            saved_fixed_convention.reset_calendars,
            flow_convention_fixed.reset_calendars,
        )
        self.assertEqual(
            saved_fixed_convention.payment_frequency,
            flow_convention_fixed.payment_frequency,
        )
        self.assertEqual(
            saved_fixed_convention.reset_days, flow_convention_fixed.reset_days
        )
        self.assertEqual(
            saved_fixed_convention.settle_days, flow_convention_fixed.settle_days
        )
        self.assertEqual(
            saved_fixed_convention.roll_convention,
            flow_convention_fixed.roll_convention,
        )

        # Check Index convention
        saved_idx_convention = saved_floating_leg.leg_definition.index_convention
        self.assertEqual(saved_idx_convention.code, float_leg_idx_conv.code)
        self.assertEqual(saved_idx_convention.currency, float_leg_idx_conv.currency)
        self.assertEqual(
            saved_idx_convention.day_count_convention,
            float_leg_idx_conv.day_count_convention,
        )
        self.assertEqual(
            saved_idx_convention.fixing_reference, float_leg_idx_conv.fixing_reference
        )
        self.assertEqual(
            saved_idx_convention.payment_tenor, float_leg_idx_conv.payment_tenor
        )
        self.assertEqual(
            saved_idx_convention.publication_day_lag,
            float_leg_idx_conv.publication_day_lag,
        )

    @lusid_feature("F44")
    def test_create_future(self):
        fut_contract_details = lusid.FuturesContractDetails(
            dom_ccy="USD",
            contract_code="CL",
            contract_month="F",
            contract_size=42000,
            convention="Act365",
            country="US",
            description="Crude Oil Nymex future Jan21",
            exchange_code="NYM",
            exchange_name="NYM",
            ticker_step=0.01,
            unit_value=4.2,
        )

        future_definition = lusid.Future(
            start_date=datetime(2020, 9, 11, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2020, 12, 31, 00, tzinfo=pytz.utc),
            identifiers={},
            contract_details=fut_contract_details,
            contracts=1,
            ref_spot_price=100,
            underlying=lusid.ExoticInstrument(
                lusid.InstrumentDefinitionFormat("custom", "custom", "0.0.0"),
                content="{}",
                instrument_type="ExoticInstrument",
            ),
            instrument_type="Future",
        )

        # Assert instrument was created
        self.assertIsNotNone(future_definition)

        # Upsert to LUSID with unique ID and
        unique_id = "id-future-2"
        self.upsert_otc_to_lusid(
            future_definition, "some-name-for-this-future", unique_id
        )

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertGreater(len(response.values), 0, "Response.values = 0")

        saved_future = response.values[unique_id].instrument_definition

        self.assertEqual(saved_future.instrument_type, lusid.InstrumentType.FUTURE)
        self.assertEqual(saved_future.start_date, future_definition.start_date)
        self.assertEqual(saved_future.maturity_date, future_definition.maturity_date)
        self.assertEqual(saved_future.ref_spot_price, future_definition.ref_spot_price)
        self.assertEqual(saved_future.contracts, future_definition.contracts)
        self.assertEqual(
            saved_future.contract_details.description,
            future_definition.contract_details.description,
        )
        self.assertEqual(
            saved_future.contract_details.contract_month,
            future_definition.contract_details.contract_month,
        )
        self.assertEqual(
            saved_future.underlying.instrument_type,
            future_definition.underlying.instrument_type,
        )
        self.assertEqual(
            saved_future.underlying.instrument_type,
            lusid.InstrumentType.EXOTICINSTRUMENT,
        )
