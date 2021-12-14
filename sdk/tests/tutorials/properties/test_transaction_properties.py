# import general python packages
import unittest
import json
from datetime import datetime
import pytz
import logging

# import lusid specific packages
import lusid
import lusid.models as models
from lusid import ApiException
from utilities import InstrumentLoader, IdGenerator
from utilities import TestDataUtilities
from utilities.id_generator_utilities import delete_entities


class TransactionProperty(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # setup logging configuration
        cls.root_logger = logging.getLogger(__name__)
        cls.root_logger.setLevel(logging.INFO)
        
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        # set test scope and code
        cls.scope = "TransactionProperty"
        cls.code = "TransactionTaxDetail"
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        delete_entities(cls.id_generator)

    def create_transaction_property(self):
        # Details of the property
        property_definition = models.CreatePropertyDefinitionRequest(
            domain="Transaction",
            scope=self.scope,
            code=self.code,
            display_name=self.code,
            data_type_id=lusid.ResourceId(scope="system", code="string"),
        )

        # create property definition
        try:
            self.property_definitions_api.create_property_definition(
                create_property_definition_request=property_definition
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                self.root_logger.info(
                    f"Property {property_definition.domain}/{property_definition.scope}/{property_definition.code} already exists"
                )
        finally:
            self.id_generator.add_scope_and_code("property_definition", property_definition.scope,
                                                 property_definition.code, ["Transaction"])

    def create_portfolio(self):
        # Details of new portfolio to be created
        effective_date = datetime(2020, 12, 1, 0, 0, tzinfo=pytz.utc)
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code=self.code,
            display_name=self.code,
            base_currency="GBP",
            created=effective_date,
        )

        # create portfolio
        try:
            self.transaction_portfolios_api.create_portfolio(
                scope=self.scope,
                create_transaction_portfolio_request=create_portfolio_request,
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PortfolioWithIdAlreadyExists":
                self.root_logger.info(
                    f"Portfolio {create_portfolio_request.code} already exists"
                )
        finally:
            self.id_generator.add_scope_and_code("portfolio", self.scope, self.code)

    def create_txn_with_property(self, instrument_id, property_value):
        # setup the transaction
        effective_date = datetime(2020, 12, 1, 0, 0, tzinfo=pytz.utc)
        txn = models.TransactionRequest(
            transaction_id="TXN001",
            type="Buy",
            instrument_identifiers={"Instrument/default/Figi": instrument_id},
            transaction_date=effective_date,
            settlement_date=effective_date,
            units=1000,
            transaction_price=models.TransactionPrice(price=100, type="Price"),
            total_consideration=models.CurrencyAndAmount(amount=1, currency="GBP"),
            exchange_rate=1,
            transaction_currency="GBP",
            properties={
                f"Transaction/{self.scope}/{self.code}": lusid.PerpetualProperty(
                    key=f"Transaction/{self.scope}/{self.code}",
                    value=lusid.PropertyValue(label_value=property_value),
                )
            },
        )

        return self.transaction_portfolios_api.upsert_transactions(
            scope=self.scope, code=self.code, transaction_request=[txn]
        )

    def get_transaction(self, scope, code):
        return self.transaction_portfolios_api.get_transactions(scope=scope, code=code)

    def test_transaction_property(self):
        # Value for our property
        transaction_tax_data = {"Tax": 1.0, "Rate": 0.01, "Schedule": "A"}
        # Convert property to string representation
        transaction_tax_string = json.dumps(transaction_tax_data)

        # Setup property and portfolio
        self.create_transaction_property()
        self.create_portfolio()

        # Setup transaction with txn tax details as the property value
        response = self.create_txn_with_property("BBG00KTDTF73", transaction_tax_string)
        self.assertIsNotNone(response)

        # Get transaction with property
        txn_response = self.get_transaction(scope=self.scope, code=self.code)
        self.assertIsNotNone(txn_response)

        # Parse property value from transaction and assert is equal to original string object
        queried_property_string = (
            txn_response.values[0]
                .properties[f"Transaction/{self.scope}/{self.code}"]
                .value.label_value
        )
        self.assertIsNotNone(queried_property_string)
        self.assertEqual(queried_property_string, transaction_tax_string)

        # Test individual key-value pairs against original data
        queried_property_dict = json.loads(queried_property_string)
        self.assertEqual(transaction_tax_data["Tax"], queried_property_dict["Tax"])
        self.assertEqual(transaction_tax_data["Rate"], queried_property_dict["Rate"])
        self.assertEqual(
            transaction_tax_data["Schedule"], queried_property_dict["Schedule"]
        )


if __name__ == "__main__":
    unittest.main()
