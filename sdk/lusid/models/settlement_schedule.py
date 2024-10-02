# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.236
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


class SettlementSchedule(object):
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
        'trade_id': 'str',
        'settlement_date': 'datetime',
        'units': 'float'
    }

    attribute_map = {
        'trade_id': 'tradeId',
        'settlement_date': 'settlementDate',
        'units': 'units'
    }

    required_map = {
        'trade_id': 'optional',
        'settlement_date': 'optional',
        'units': 'optional'
    }

    def __init__(self, trade_id=None, settlement_date=None, units=None, local_vars_configuration=None):  # noqa: E501
        """SettlementSchedule - a model defined in OpenAPI"
        
        :param trade_id: 
        :type trade_id: str
        :param settlement_date: 
        :type settlement_date: datetime
        :param units: 
        :type units: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._trade_id = None
        self._settlement_date = None
        self._units = None
        self.discriminator = None

        self.trade_id = trade_id
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if units is not None:
            self.units = units

    @property
    def trade_id(self):
        """Gets the trade_id of this SettlementSchedule.  # noqa: E501


        :return: The trade_id of this SettlementSchedule.  # noqa: E501
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this SettlementSchedule.


        :param trade_id: The trade_id of this SettlementSchedule.  # noqa: E501
        :type trade_id: str
        """

        self._trade_id = trade_id

    @property
    def settlement_date(self):
        """Gets the settlement_date of this SettlementSchedule.  # noqa: E501


        :return: The settlement_date of this SettlementSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this SettlementSchedule.


        :param settlement_date: The settlement_date of this SettlementSchedule.  # noqa: E501
        :type settlement_date: datetime
        """

        self._settlement_date = settlement_date

    @property
    def units(self):
        """Gets the units of this SettlementSchedule.  # noqa: E501


        :return: The units of this SettlementSchedule.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this SettlementSchedule.


        :param units: The units of this SettlementSchedule.  # noqa: E501
        :type units: float
        """

        self._units = units

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
        if not isinstance(other, SettlementSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettlementSchedule):
            return True

        return self.to_dict() != other.to_dict()
