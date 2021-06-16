import unittest


from lusid import InstrumentsApi
from lusid.utilities import ApiClientFactory

from utilities import CredentialsSource


class TestApiFactory(unittest.TestCase):

    def test_get_api_with_info(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(InstrumentsApi)

        self.assertIsInstance(api, InstrumentsApi)
        result = api.get_instrument_identifier_types(call_info=lambda r: print(r))

        self.assertIsNotNone(result)
