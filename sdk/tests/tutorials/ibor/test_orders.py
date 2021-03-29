import unittest
import uuid
import lusid
import lusid.models as models
from lusid import *
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

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    @lusid_feature("F4")
    def test_upsert_simple_order(self):
        """Test makes a request for a single order."""

        test_scope = "Orders-SimpleUpsert-TestScope"
        # Create unique order id
        order = self.get_guid()
        # Create ResourceId for order

        # Construct order arguments
        instrument_identifiers = {TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]}
        order_id = models.ResourceId(test_scope, order)
        portfolio_id = ResourceId(test_scope, "OrdersTestPortfolio")
        # The key:This takes the format {domain}/{scope}/{code}, value: Lusid property value'
        properties = {f"Order/{test_scope}/TIF": PerpetualProperty(f"Order/{test_scope}/TIF", PropertyValue("GTC")),
                      f"Order/{test_scope}/OrderBook":
                          PerpetualProperty(f"Order/{test_scope}/OrderBook", PropertyValue("UK Test Orders")),
                      f"Order/{test_scope}/PortfolioManager":
                          PerpetualProperty(f"Order/{test_scope}/PortfolioManager", PropertyValue("F Bar")),
                      f"Order/{test_scope}/Account":
                          PerpetualProperty(f"Order/{test_scope}/Account", PropertyValue("J Wilson")),
                      f"Order/{test_scope}/Strategy":
                          PerpetualProperty(f"Order/{test_scope}/Strategy", PropertyValue("RiskArb"))}

        order_book_id = ResourceId(test_scope, "OrdersTestBook")
        quantity = 100
        # Construct request
        order_request = OrderRequest(properties=properties,
                                     instrument_identifiers=instrument_identifiers,
                                     quantity=quantity, side='buy',
                                     order_book_id=order_book_id,
                                     portfolio_id=portfolio_id, id=order_id)

        order_req = OrderSetRequest(order_requests=[order_request])

        upsert_result = self.orders_api.upsert_orders(order_set_request=order_req)

        assert len(upsert_result.values) == 1
        assert upsert_result.values[0].to_dict()['id']['code'] == order
        assert upsert_result.values[0].to_dict()['lusid_instrument_id'] == self.instrument_ids[0]
        assert upsert_result.values[0].to_dict()['quantity'] == 100
        assert upsert_result.values[0].to_dict()['properties'][f"Order/{test_scope}/TIF"]['key'] == f"Order/{test_scope}/TIF"


if __name__ == '__main__':
    unittest.main()
