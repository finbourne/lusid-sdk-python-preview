import unittest

import lusid

from utilities import InstrumentLoader
from utilities import TestDataUtilities

class InstrumentLoaderTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.instrument_loader = InstrumentLoader(cls.instruments_api)

    def test_load_instruments(self):
         # Test luids returned in default case
         luids = self.instrument_loader.load_instruments()
         self.assertEqual(len(luids), 5)

    def test_load_instrument_figis(self):

        # Expected Figis - see utilities.instrument_loader
        expected_figis = [
            "BBG00KTDTF73",
            "BBG00Y271826",
            "BBG00L7XVNP1",
            "BBG005D5KGM0",
            "BBG000DPM932",
        ]

        # Test figis match expected identifiers
        figis = self.instrument_loader.load_instruments(return_luids=False)
        self.assertEqual(len(figis), len(expected_figis))
        self.assertTrue(set(figis).issuperset(set(expected_figis)))
