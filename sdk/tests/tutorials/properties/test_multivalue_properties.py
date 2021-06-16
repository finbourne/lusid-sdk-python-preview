# import general python packages
import unittest
import json
import logging
import pytz
from datetime import datetime

# import lusid specific packages
import lusid
import lusid.models as models
from utilities import TestDataUtilities

# setup logging configuration
logging.basicConfig(level=logging.INFO)


class MultiLabelPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client factory
        api_client_factory = TestDataUtilities.api_client_factory()
        cls.property_definitions_api = api_client_factory.build(lusid.PropertyDefinitionsApi)
        cls.instruments_api = api_client_factory.build(lusid.InstrumentsApi)
        cls.portfolios_api = api_client_factory.build(lusid.PortfoliosApi)
        cls.transaction_portfolios_api = api_client_factory.build(lusid.TransactionPortfoliosApi)

    def test_create_portfolio_with_mv_property(self):
        # Details of property to be created
        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)
        scope = "MultiValueProperties"
        code = "MorningstarQuarterlyRating"
        portfolio_code = "Portfolio-MVP"

        multi_value_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=scope,
            code=code,
            display_name=code,
            constraint_style="Collection",
            data_type_id=lusid.ResourceId(scope="system", code="string"),
        )

        # create property definition
        try:
            self.property_definitions_api.create_property_definition(
                create_property_definition_request=multi_value_property_definition
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                logging.info(
                    f"Property {multi_value_property_definition.domain}/{multi_value_property_definition.scope}/{multi_value_property_definition.display_name} already exists"
                )

        schedule = [
            '{ "2019-12-31" : "5"}',
            '{ "2020-03-31" : "4"}',
            '{ "2020-06-30" : "3"}',
            '{ "2020-09-30" : "3"}',
        ]

        # Details of new portfolio to be created
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code=portfolio_code,
            display_name=portfolio_code,
            base_currency="GBP",
            created=effective_date,
        )

        # create portfolio
        try:
            self.transaction_portfolios_api.create_portfolio(
                scope=scope,
                create_transaction_portfolio_request=create_portfolio_request,
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PortfolioWithIdAlreadyExists":
                logging.info(
                    f"Portfolio {create_portfolio_request.code} already exists"
                )

        self.portfolios_api.upsert_portfolio_properties(
            scope=scope,
            code=portfolio_code,
            request_body={
                f"Portfolio/{scope}/{code}": models.ModelProperty(
                    key=f"Portfolio/{scope}/{code}",
                    value=models.PropertyValue(
                        label_value_set=models.LabelValueSet(values=schedule)
                    ),
                )
            },
        )

        # get properties for assertions
        portfolio_properties = self.portfolios_api.get_portfolio_properties(
            scope=scope, code=portfolio_code
        ).properties
        label_value_set = portfolio_properties[
            f"Portfolio/MultiValueProperties/{code}"
        ].value.label_value_set.values
        self.assertCountEqual(label_value_set, schedule)


if __name__ == "__main__":
    unittest.main()
