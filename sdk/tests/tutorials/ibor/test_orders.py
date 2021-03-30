import unittest
import uuid
import lusid
import lusid.models as models
from lusid import OrderRequest
from lusid import OrderSetRequest
from lusid import PerpetualProperty
from lusid import PropertyValue
from lusid import ResourceId
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Orders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.orders_api = lusid.OrdersApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

    @lusid_feature("F4")
    def test_upsert_simple_order(self):
        """Makes a request for a single order."""

        orders_scope = "Orders-SimpleUpsert-TestScope"
        # Create unique order id
        order_id = str(uuid.uuid4())

        # Construct order arguments
        instrument_identifiers = {TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]}
        ##Create ResourceId for order
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

        order_book_id = ResourceId(orders_scope, "OrdersTestBook")
        quantity = 100
        # Construct request
        order_request = OrderRequest(properties=properties,
                                     instrument_identifiers=instrument_identifiers,
                                     quantity=quantity, side='buy',
                                     order_book_id=order_book_id,
                                     portfolio_id=portfolio_id, id=order_resource_id)

        order_set_request = OrderSetRequest(order_requests=[order_request])

        upsert_result = self.orders_api.upsert_orders(order_set_request=order_set_request)

        self.assertEqual(len(upsert_result.values),1)
        response=upsert_result.values[0].to_dict()
        self.assertEqual(response['id']['code'], order_id)
        self.assertEqual(response['lusid_instrument_id'], self.instrument_ids[0])
        self.assertEqual(response['quantity'], 100)
        self.assertEqual(response['properties'][f"Order/{orders_scope}/TIF"]['key'] , f"Order/{orders_scope}/TIF")