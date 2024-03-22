# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.123
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class BlockAndOrdersRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'block_id': 'ResourceId',
        'orders': 'list[BlockedOrderRequest]',
        'block_properties': 'dict(str, PerpetualProperty)',
        'instrument_identifiers': 'dict(str, str)',
        'side': 'str',
        'type': 'str',
        'time_in_force': 'str',
        'date': 'datetime',
        'limit_price': 'CurrencyAndAmount',
        'stop_price': 'CurrencyAndAmount'
    }

    attribute_map = {
        'block_id': 'blockId',
        'orders': 'orders',
        'block_properties': 'blockProperties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'side': 'side',
        'type': 'type',
        'time_in_force': 'timeInForce',
        'date': 'date',
        'limit_price': 'limitPrice',
        'stop_price': 'stopPrice'
    }

    required_map = {
        'block_id': 'required',
        'orders': 'required',
        'block_properties': 'optional',
        'instrument_identifiers': 'required',
        'side': 'required',
        'type': 'optional',
        'time_in_force': 'optional',
        'date': 'optional',
        'limit_price': 'optional',
        'stop_price': 'optional'
    }

    def __init__(self, block_id=None, orders=None, block_properties=None, instrument_identifiers=None, side=None, type=None, time_in_force=None, date=None, limit_price=None, stop_price=None, local_vars_configuration=None):  # noqa: E501
        """BlockAndOrdersRequest - a model defined in OpenAPI"
        
        :param block_id:  (required)
        :type block_id: lusid.ResourceId
        :param orders:  An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block. (required)
        :type orders: list[lusid.BlockedOrderRequest]
        :param block_properties:  Client-defined properties associated with this block.
        :type block_properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param side:  The client's representation of the block's side (buy, sell, short, etc) (required)
        :type side: str
        :param type:  The block order's type (examples: Limit, Market, ...)
        :type type: str
        :param time_in_force:  The block orders' time in force (examples: Day, GoodTilCancel, ...)
        :type time_in_force: str
        :param date:  The date on which the block was made
        :type date: datetime
        :param limit_price: 
        :type limit_price: lusid.CurrencyAndAmount
        :param stop_price: 
        :type stop_price: lusid.CurrencyAndAmount

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._block_id = None
        self._orders = None
        self._block_properties = None
        self._instrument_identifiers = None
        self._side = None
        self._type = None
        self._time_in_force = None
        self._date = None
        self._limit_price = None
        self._stop_price = None
        self.discriminator = None

        self.block_id = block_id
        self.orders = orders
        self.block_properties = block_properties
        self.instrument_identifiers = instrument_identifiers
        self.side = side
        self.type = type
        self.time_in_force = time_in_force
        if date is not None:
            self.date = date
        if limit_price is not None:
            self.limit_price = limit_price
        if stop_price is not None:
            self.stop_price = stop_price

    @property
    def block_id(self):
        """Gets the block_id of this BlockAndOrdersRequest.  # noqa: E501


        :return: The block_id of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this BlockAndOrdersRequest.


        :param block_id: The block_id of this BlockAndOrdersRequest.  # noqa: E501
        :type block_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and block_id is None:  # noqa: E501
            raise ValueError("Invalid value for `block_id`, must not be `None`")  # noqa: E501

        self._block_id = block_id

    @property
    def orders(self):
        """Gets the orders of this BlockAndOrdersRequest.  # noqa: E501

        An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block.  # noqa: E501

        :return: The orders of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: list[lusid.BlockedOrderRequest]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this BlockAndOrdersRequest.

        An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block.  # noqa: E501

        :param orders: The orders of this BlockAndOrdersRequest.  # noqa: E501
        :type orders: list[lusid.BlockedOrderRequest]
        """
        if self.local_vars_configuration.client_side_validation and orders is None:  # noqa: E501
            raise ValueError("Invalid value for `orders`, must not be `None`")  # noqa: E501

        self._orders = orders

    @property
    def block_properties(self):
        """Gets the block_properties of this BlockAndOrdersRequest.  # noqa: E501

        Client-defined properties associated with this block.  # noqa: E501

        :return: The block_properties of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._block_properties

    @block_properties.setter
    def block_properties(self, block_properties):
        """Sets the block_properties of this BlockAndOrdersRequest.

        Client-defined properties associated with this block.  # noqa: E501

        :param block_properties: The block_properties of this BlockAndOrdersRequest.  # noqa: E501
        :type block_properties: dict[str, lusid.PerpetualProperty]
        """

        self._block_properties = block_properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this BlockAndOrdersRequest.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this BlockAndOrdersRequest.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this BlockAndOrdersRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def side(self):
        """Gets the side of this BlockAndOrdersRequest.  # noqa: E501

        The client's representation of the block's side (buy, sell, short, etc)  # noqa: E501

        :return: The side of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this BlockAndOrdersRequest.

        The client's representation of the block's side (buy, sell, short, etc)  # noqa: E501

        :param side: The side of this BlockAndOrdersRequest.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) < 1):
            raise ValueError("Invalid value for `side`, length must be greater than or equal to `1`")  # noqa: E501

        self._side = side

    @property
    def type(self):
        """Gets the type of this BlockAndOrdersRequest.  # noqa: E501

        The block order's type (examples: Limit, Market, ...)  # noqa: E501

        :return: The type of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BlockAndOrdersRequest.

        The block order's type (examples: Limit, Market, ...)  # noqa: E501

        :param type: The type of this BlockAndOrdersRequest.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def time_in_force(self):
        """Gets the time_in_force of this BlockAndOrdersRequest.  # noqa: E501

        The block orders' time in force (examples: Day, GoodTilCancel, ...)  # noqa: E501

        :return: The time_in_force of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this BlockAndOrdersRequest.

        The block orders' time in force (examples: Day, GoodTilCancel, ...)  # noqa: E501

        :param time_in_force: The time_in_force of this BlockAndOrdersRequest.  # noqa: E501
        :type time_in_force: str
        """

        self._time_in_force = time_in_force

    @property
    def date(self):
        """Gets the date of this BlockAndOrdersRequest.  # noqa: E501

        The date on which the block was made  # noqa: E501

        :return: The date of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BlockAndOrdersRequest.

        The date on which the block was made  # noqa: E501

        :param date: The date of this BlockAndOrdersRequest.  # noqa: E501
        :type date: datetime
        """

        self._date = date

    @property
    def limit_price(self):
        """Gets the limit_price of this BlockAndOrdersRequest.  # noqa: E501


        :return: The limit_price of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._limit_price

    @limit_price.setter
    def limit_price(self, limit_price):
        """Sets the limit_price of this BlockAndOrdersRequest.


        :param limit_price: The limit_price of this BlockAndOrdersRequest.  # noqa: E501
        :type limit_price: lusid.CurrencyAndAmount
        """

        self._limit_price = limit_price

    @property
    def stop_price(self):
        """Gets the stop_price of this BlockAndOrdersRequest.  # noqa: E501


        :return: The stop_price of this BlockAndOrdersRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this BlockAndOrdersRequest.


        :param stop_price: The stop_price of this BlockAndOrdersRequest.  # noqa: E501
        :type stop_price: lusid.CurrencyAndAmount
        """

        self._stop_price = stop_price

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BlockAndOrdersRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockAndOrdersRequest):
            return True

        return self.to_dict() != other.to_dict()
