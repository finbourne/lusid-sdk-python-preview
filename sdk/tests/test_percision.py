import unittest
from datetime import datetime

import pytz
import uuid

import lusid
import lusid.models as models
from lusidfeature import lusid_feature

from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.instrument_loader import InstrumentLoader
from utilities.test_data_utilities import TestDataUtilities
from utilities.credentials_source import CredentialsSource


class Properties(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        # cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        # cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

        # instrument_loader = InstrumentLoader(cls.instruments_api)
        # cls.instrument_ids = instrument_loader.load_instruments()

        # cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    def test_get_portfolio(self):
        portfolio = self.portfolios_api.get_portfolio("test-precision", "ABC",
                                                      property_keys = ["Portfolio/test-precision/noquotes"])


        print(portfolio)