import unittest
import uuid
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class GroupPortfolios(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolio_group_api = lusid.PortfolioGroupsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)


    @lusid_feature("F8-1")
    def test_create_portfolio_group(self):
        # set up the portfolio group
        guid = str(uuid.uuid4())

        request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(guid),
            display_name="portfolio_group-{0}".format(guid),
            values=[],
        )

        # create the portfolio group in LUSID in the specified scope
        result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=request
        )

        # assertions
        self.assertEqual(result.id.code, request.code)

    @lusid_feature("F8-2")
    def test_add_portfolio_to_group(self):
        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # create portfolio
        # set up the portfolio
        portfolio_request = models.CreateTransactionPortfolioRequest(
            display_name="portfolio-{0}".format(guid),
            code="id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        # create the portfolio in LUSID in the specified scope
        portfolio_result = self.transaction_portfolios_api.create_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_transaction_portfolio_request=portfolio_request
        )

        # create portfolio group
        portfolio_group_request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(guid),
            display_name="portfolio_group-{0}".format(guid),
            values=[],
            created=effective_date
        )

        # create the portfolio group in LUSID in the specified scope
        portfolio_group_result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=portfolio_group_request
        )

        # add transactions portfolio to group
        add_portfolio_request = self.portfolio_group_api.add_portfolio_to_group(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_result.id.code,
            resource_id=models.ResourceId(
                scope=TestDataUtilities.tutorials_scope,
                code=portfolio_result.id.code
            ),
            effective_at=effective_date
        )

        # assertions - if the first portfolio in this group has the same code as our portfolio we created, it worked.
        self.assertEqual(add_portfolio_request.portfolios[0].code, portfolio_request.code)

    @lusid_feature("F8-3")
    def test_add_sub_group_to_group(self):

        guid = str(uuid.uuid4())
        sub_guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # set up a portfolio group
        portfolio_group_request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(guid),
            display_name="portfolio_group-{0}".format(guid),
            values=[],
            created=effective_date
        )

        # create the portfolio group in LUSID in the specified scope
        portfolio_group_result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=portfolio_group_request
        )

        # set up the sub portfolio group
        sub_portfolio_group_request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(sub_guid),
            display_name="portfolio_group-{0}".format(sub_guid),
            values=[],
            created=effective_date
        )

        # create the sub portfolio group in LUSID in the specified scope
        sub_portfolio_group_result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=sub_portfolio_group_request
        )

        # create sub portfolio group
        add_subgroup_to_group = self.portfolio_group_api.add_sub_group_to_group(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_request.code,
            resource_id=models.ResourceId(
                scope=TestDataUtilities.tutorials_scope,
                code=sub_portfolio_group_request.code
            ),
            effective_at=effective_date
        )

        # assertions
        self.assertEqual(add_subgroup_to_group.sub_groups[0].code,sub_portfolio_group_request.code)

    @lusid_feature("F8-4")
    def test_delete_portfolio_from_group(self):

        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # create a portfolio and add it to the group
        # create portfolio
        # set up the portfolio
        portfolio_request = models.CreateTransactionPortfolioRequest(
            display_name="portfolio-{0}".format(guid),
            code="id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        # create the portfolio in LUSID in the specified scope
        portfolio_result = self.transaction_portfolios_api.create_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_transaction_portfolio_request=portfolio_request
        )

        # create portfolio group
        portfolio_group_request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(guid),
            display_name="portfolio_group-{0}".format(guid),
            values=[],
            created=effective_date
        )

        # create the portfolio group in LUSID in the specified scope
        portfolio_group_result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=portfolio_group_request
        )

        # add transactions portfolio to group
        add_portfolio_request = self.portfolio_group_api.add_portfolio_to_group(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_result.id.code,
            resource_id=models.ResourceId(
                scope=TestDataUtilities.tutorials_scope,
                code=portfolio_result.id.code
            ),
            effective_at=effective_date
        )

        # remove the portfolio from our group
        delete_portfolio_result = self.portfolio_group_api.delete_portfolio_from_group(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_request.code,
            portfolio_scope=TestDataUtilities.tutorials_scope,
            portfolio_code=portfolio_result.id.code,
            effective_at=effective_date
        )

        # assertions - we check if our list of portfolios equals an empty list
        self.assertEqual(delete_portfolio_result.portfolios, [])

    @lusid_feature("F8-5")
    def test_upsert_group_properties(self):
        # set up the portfolio group
        guid = str(uuid.uuid4())
        property_name = "managerId-{0}".format(guid)

        portfolio_group_request = models.CreatePortfolioGroupRequest(
            code="portfolio_group-{}".format(guid),
            display_name="portfolio_group-{0}".format(guid),
            values=[],
        )

        # create the portfolio group in LUSID in the specified scope
        portfolio_group_result = self.portfolio_group_api.create_portfolio_group(
            scope=TestDataUtilities.tutorials_scope,
            create_portfolio_group_request=portfolio_group_request
        )

        # create the property
        property_definition = models.CreatePropertyDefinitionRequest(
            domain="PortfolioGroup",
            scope=TestDataUtilities.tutorials_scope,
            life_time="Perpetual",
            code=property_name,
            value_required=False,
            display_name="Manager Id",
            data_type_id=models.ResourceId("System","string")
        )

        property_definition_result = self.property_definitions_api.create_property_definition(
            create_property_definition_request=property_definition
        )

        # upsert the properties
        property_value = models.PropertyValue("A Manager")
        upsert_properties_result = self.portfolio_group_api.upsert_group_properties(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_request.code,
            request_body={property_definition_result.key: models.PerpetualProperty(property_definition_result.key, property_value)}
        )

        # get the properties
        properties_result = self.portfolio_group_api.get_group_properties(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_group_request.code
        ).properties

        label_property = properties_result[property_definition_result.key]

        self.assertEqual(label_property.value.label_value, property_value.label_value)

