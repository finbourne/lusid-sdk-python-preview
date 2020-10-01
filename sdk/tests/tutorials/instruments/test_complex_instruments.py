import unittest

import pytz

import lusid
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
        response = self.instruments_api.upsert_instruments(request_body={lusid_id: models.InstrumentDefinition(
            name=name,
            identifiers={'ClientInternal': models.InstrumentIdValue(value=lusid_id)},
            definition=instrument
        )
        }
        )
        # Check for failures with response
        self.assertEqual(len(response.values), 1, response.failed)

    def query_otc_from_lusid(self, lusid_id):
        return self.instruments_api.get_instruments(identifier_type='ClientInternal',
                                                    request_body=[lusid_id]
                                                    )

    # Create an FX-Forward (that then upsert to LUSID)
    def test_create_fx_forward(self):
        fx_forward = lusid.FxForward(
            dom_amount=-1,
            fgn_amount=109,
            dom_ccy='USD',
            fgn_ccy='JPY',
            start_date=datetime(2020, 2, 7, 00, tzinfo=pytz.utc),
            maturity_date=datetime(2020, 9, 18, 00, tzinfo=pytz.utc),
            instrument_type='FxForward'
        )

        # Assert that it was created
        self.assertIsNotNone(fx_forward)

        # Upsert to LUSID with unique ID and 
        unique_id = 'id-fxfwd-2'
        self.upsert_otc_to_lusid(fx_forward, "some-name-for-this-fxforward", unique_id)

        # Can now query from LUSID and run tests
        response = self.query_otc_from_lusid(unique_id)
        self.assertIsNotNone(response)
        self.assertGreater(len(response.values), 0, 'Response.values = 0')
        saved_fx_forward = response.values[unique_id].instrument_definition

        self.assertEqual(saved_fx_forward.instrument_type, lusid.InstrumentType.FXFORWARD)
        self.assertEqual(saved_fx_forward.dom_amount, fx_forward.dom_amount)
        self.assertEqual(saved_fx_forward.fgn_amount, fx_forward.fgn_amount)
        self.assertEqual(saved_fx_forward.dom_ccy, fx_forward.dom_ccy)
        self.assertEqual(saved_fx_forward.fgn_ccy, fx_forward.fgn_ccy)
