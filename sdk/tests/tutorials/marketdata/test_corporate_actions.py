import unittest

import lusid
import lusid.models as models
from features.lusid_feature import lusid_feature
from lusid.utilities.api_client_builder import ApiClientBuilder
from lusid.exceptions import ApiException
from utilities.credentials_source import CredentialsSource
from utilities.test_data_utilities import TestDataUtilities
import uuid


class CorporateActions(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.corporate_actions_sources_api = lusid.CorporateActionSourcesApi(api_client)

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    @lusid_feature("F33")
    def test_list_corporate_action_sources(self):
        uuid = self.get_guid()
        request = models.CreateCorporateActionSourceRequest(
            scope=TestDataUtilities.tutorials_scope,
            code=f"test-corp-action-code-{uuid}",
            display_name=f"test-corp-action-{uuid}"
        )
        self.corporate_actions_sources_api.create_corporate_action_source(request)
        sources = self.corporate_actions_sources_api.list_corporate_action_sources()
        self.assertGreater(len(sources.values), 0)

    @unittest.skip("Not Implemented")
    def test_list_corporate_actions_for_one_day(self):
        uuid = self.get_guid()
        request = models.CreateCorporateActionSourceRequest(
            scope=TestDataUtilities.tutorials_scope,
            code=f"test-corp-action-code-{uuid}",
            display_name=f"test-corp-action-{uuid}"
        )
        self.corporate_actions_sources_api.create_corporate_action_source(request)
        sources = self.corporate_actions_sources_api.get_corporate_actions(
            scope=f"test-corp-action-code-{uuid}",
            code=f"test-corp-action-code-{uuid}"
        )
