Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python notebook for OTC derivatives - Copying from C# SDK

import unittest
import lusid
import datetime
from utilities import TestDataUtilities

class ComplexInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        api_client = TestDataUtilities.api_client()
        cls.instruments_api = lusid.InstrumentsApi(api_client)

    # Define a function to upsert instrument
    def upsert_otc_to_lusid(self, instrument, name, lusid_id):
        response = self.instruments_api.upsert_instruments(request_body = {instrument : models.InstrumentDefinition(
            name = name, 
            identifiers = {lusid_id : models.InstrumentIdValue(value = lusid_id)}
                )
            }
        )
    # Check for failures with response 
        self.assertEqual(len(response.values), 1, response.failed)

    def query_otc_from_lusid(self, lusid_id):
        self.instruments_api.get_instruments(identifier_type= 'lusid_id', identifier = lusid_id)

    # Create an FX-Forward (that can be then upserted into LUSID)
    usdJpyFxRate = 109
    def test_create_fx_forward(self):
        fx_forward = lusid.FxForward(
            dom_amount = -1, 
            fgn_amount = usdJpyFxRate, 
            dom_ccy = 'USD', 
            fgn_ccy = 'JPY',
            start_date = datetime(2020, 2, 7, 00),
            maturity_date = datetime(2020, 9, 18, 00),
            instrument_type = 'FXFORWARD'
        )

        # Assert that it was created
        self.assertIsNotNone(fx_forward)

        # Upsert to LUSID with unique ID and 
        uniqueId = 'id-fxfwd-1'  
        self.upsert_otc_to_lusid(fx_forward, "some-name-for-this-fxforward", uniqueId)

        # Can now query from LUSID and run tests
        saved_fx_forward = self.query_otc_from_lusid(uniqueId)
        self.assertIsNotNone(saved_fx_forward)
        self.assertEqual(saved_fx_forward.instrument_type, lusid.InstrumentType.FXFORWARD)
        self.assertEqual(saved_fx_forward.dom_amount, fx_forward.dom_amount)
        self.assertEqual(saved_fx_forward.fgn_amount, fx_forward.fgn_amount)
        self.assertEqual(saved_fx_forward.dom_ccy, fx_forward.dom_ccy)
        self.assertEqual(saved_fx_forward.fgn_ccy, fx_forward.fgn_ccy)