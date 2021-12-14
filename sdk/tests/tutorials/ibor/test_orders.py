import unittest
import uuid
import lusid
import lusid.models as models
from lusid import OrderRequest, ApiException
from lusid import OrderSetRequest
from lusid import PerpetualProperty
from lusid import PropertyValue
from lusid import ResourceId
from lusidfeature import lusid_feature
from utilities import InstrumentLoader, IdGenerator
from utilities import TestDataUtilities
import json


class Orders(unittest.TestCase):
    tests_scope = {'simple-upsert': 'Orders-SimpleUpsert-TestScope'}
    test_codes = ['TIF', 'OrderBook', 'PortfolioManager', 'Account', 'Strategy']

    @staticmethod
    def load_properties(properties_api, id_generator, scopes, codes):
        for scope in scopes:
            for code in codes:
                try:
                    properties_api.create_property_definition(
                        create_property_definition_request=models.CreatePropertyDefinitionRequest(
                            domain="Order",
                            scope=scope,
                            code=code,
                            display_name=code,
                            constraint_style="Property",
                            data_type_id=lusid.ResourceId(scope="system", code="string"),
                        )
                    )
                except lusid.ApiException as e:
                    if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                        pass  # ignore if the property definition exists
                finally:
                    id_generator.add_scope_and_code("property_definition", scope, code)

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

        cls.orders_api = lusid.OrdersApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.properties_api = lusid.PropertyDefinitionsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)

        cls.instrument_ids = instrument_loader.load_instruments()
        cls.load_properties(
            properties_api=cls.properties_api,
            id_generator=cls.id_generator,
            scopes=cls.tests_scope.values(),
            codes=cls.test_codes
        )

    @classmethod
    def tearDownClass(cls):
        for entity, scope, code in cls.id_generator.pop_scope_and_codes():
            try:
                if entity == "property_definition":
                    cls.properties_api.delete_property_definition("Order", scope, code)
                elif entity == "order":
                    cls.orders_api.delete_order(scope, code)
            except ApiException as ex:
                print(ex)

    @lusid_feature("F4")
    def test_upsert_simple_order(self):
        """Makes a request for a single order."""

        # Construct order arguments
        instrument_identifiers = {TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]}
        _, orders_scope, order_id = self.id_generator.generate_scope_and_code("order",
                                                                              scope=self.tests_scope['simple-upsert'])

        # Create ResourceId for order
        order_resource_id = models.ResourceId(orders_scope, order_id)
        portfolio_id = ResourceId(orders_scope, "OrdersTestPortfolio")
        properties = {f"Order/{orders_scope}/TIF": PerpetualProperty(f"Order/{orders_scope}/TIF", PropertyValue("GTC")),
                      f"Order/{orders_scope}/OrderBook":
                          PerpetualProperty(f"Order/{orders_scope}/OrderBook", PropertyValue("UK Test Orders")),
                      f"Order/{orders_scope}/PortfolioManager":
                          PerpetualProperty(f"Order/{orders_scope}/PortfolioManager", PropertyValue("F Bar")),
                      f"Order/{orders_scope}/Account":
                          PerpetualProperty(f"Order/{orders_scope}/Account", PropertyValue("J Wilson")),
                      f"Order/{orders_scope}/Strategy":
                          PerpetualProperty(f"Order/{orders_scope}/Strategy", PropertyValue("RiskArb"))}

        quantity = 100
        # Construct request
        order_request = OrderRequest(properties=properties,
                                     instrument_identifiers=instrument_identifiers,
                                     quantity=quantity, side='buy',
                                     portfolio_id=portfolio_id, id=order_resource_id)

        order_set_request = OrderSetRequest(order_requests=[order_request])

        upsert_result = self.orders_api.upsert_orders(order_set_request=order_set_request)

        self.assertEqual(len(upsert_result.values), 1)
        response = upsert_result.values[0].to_dict()
        self.assertEqual(response['id']['code'], order_id)
        self.assertEqual(response['lusid_instrument_id'], self.instrument_ids[0])
        self.assertEqual(response['quantity'], 100)
        self.assertEqual(response['properties'][f"Order/{orders_scope}/TIF"]['key'], f"Order/{orders_scope}/TIF")
