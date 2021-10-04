import unittest
from datetime import datetime
from decimal import Decimal

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
        cls.portfolios_api = lusid.PortfoliosApi(api_client)


    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    def test_get_portfolio(self):
        portfolio = self.portfolios_api.get_portfolio("test-precision", "ABC",
                                                      property_keys = ["Portfolio/test-precision/noquotes"])

        print(portfolio)

        # self.assertEqual(Decimal('0.1234567891011121314151617182'), portfolio.properties['Portfolio/test-precision/noquotes'].value.metric_value.value)

