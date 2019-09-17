import unittest

import lusid
import lusid.models
from lusid.utilities.api_client_builder import ApiClientBuilder
from lusid.exceptions import ApiException
from utilities.credentials_source import CredentialsSource
from utilities.test_data_utilities import TestDataUtilities


class CorporateActions(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.corporate_actions_sources_api = lusid.CorporateActionSourcesApi(api_client)

    def test_list_corporate_action_sources(self):
        sources = self.corporate_actions_sources_api.list_corporate_action_sources()
        self.assertGreater(len(sources.values), 0)
        for source in sources.values:
            print(f"{source.id.scope}\t:\t{source.id.code}")

    @unittest.skip("Not Implemented")
    def test_list_corporate_actions_for_one_day(self):
        sources = self.corporate_actions_sources_api.get_corporate_actions(
            scope="UK_High_Growth_Equities_Fund_a4fb",
            code="UK_High_Growth_Equities_Fund_base_fund_corporate_action_source"
        )
