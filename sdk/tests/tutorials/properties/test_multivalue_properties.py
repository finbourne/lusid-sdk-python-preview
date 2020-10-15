# import general python packages
import unittest
import json
import logging
import uuid
import pytz
from datetime import datetime

# import lusid specific packages
import lusid
import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities

# setup logging configuration
logging.basicConfig(level=logging.INFO)


class MultiLabelPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    def test_create_portfolio_with_mv_property(self):
        # Details of property to be created
        uuid = self.get_guid()
        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)
        scope = "MultiValueProperties"
        code = "CallSchedule"
        portfolio_code = f"ud-{uuid}"

        multi_value_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=scope,
            code=code,
            display_name=code,
            constraint_style="Collection",
            data_type_id=lusid.ResourceId(scope="system", code="string"),
        )
        # create portfolio definition
        try:
            # create property definition
            self.property_definitions_api.create_property_definition(
                create_property_definition_request=multi_value_property_definition
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                logging.info(
                    f"Property {multi_value_property_definition.domain}/{multi_value_property_definition.scope}/{multi_value_property_definition.display_name} already exists"
                )

        schedule = [
            '{"date1": "1-jan-2020"}',
            '{"date2": "1-jan-2021"}',
            '{"date3": "1-jan-2022"}',
        ]

        # Details of new portfolio to be created
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code=portfolio_code,
            display_name=f"portfolio-{uuid}",
            base_currency="GBP",
            created=effective_date,
        )

        # create portfolio
        portfolio_request = self.transaction_portfolios_api.create_portfolio(
            scope=scope, create_transaction_portfolio_request=create_portfolio_request
        )

        portfolio_properties_request = self.portfolios_api.upsert_portfolio_properties(
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
            scope=scope, code=portfolio_request.id.code
        ).properties
        label_value_set = portfolio_properties[
            "Portfolio/MultiValueProperties/CallSchedule"
        ].value.label_value_set.values
        self.assertListEqual(label_value_set, schedule)


if __name__ == "__main__":
    unittest.main()
