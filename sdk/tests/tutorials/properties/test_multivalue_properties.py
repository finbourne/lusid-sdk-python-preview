import unittest
import json
import logging
import pytz
from datetime import datetime

import lusid
import lusid.models as models
from lusid import ApiException
from utilities import TestDataUtilities, IdGenerator


class MultiLabelPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        logging.basicConfig(level=logging.INFO)

        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        for item in cls.id_generator.pop_scope_and_codes():
            entity = item[0]
            scope = item[1]
            code = item[2]
            try:
                if entity == "portfolio":
                    cls.portfolios_api.delete_portfolio(scope, code)
                elif entity == "property_definition":
                    domain = item[3]
                    cls.property_definitions_api.delete_property_definition(domain, scope, code)
            except ApiException as ex:
                print(ex)

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
        finally:
            self.id_generator.add_scope_and_code("property_definition", multi_value_property_definition.scope,
                                                 multi_value_property_definition.code, ["Portfolio"])

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
        finally:
            self.id_generator.add_scope_and_code("portfolio", scope, portfolio_code)

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
