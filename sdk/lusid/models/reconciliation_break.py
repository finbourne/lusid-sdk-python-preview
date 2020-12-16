# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2401
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ReconciliationBreak(object):
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
        'instrument_uid': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'left_units': 'float',
        'right_units': 'float',
        'difference_units': 'float',
        'left_cost': 'CurrencyAndAmount',
        'right_cost': 'CurrencyAndAmount',
        'difference_cost': 'CurrencyAndAmount',
        'instrument_properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'instrument_uid': 'instrumentUid',
        'sub_holding_keys': 'subHoldingKeys',
        'left_units': 'leftUnits',
        'right_units': 'rightUnits',
        'difference_units': 'differenceUnits',
        'left_cost': 'leftCost',
        'right_cost': 'rightCost',
        'difference_cost': 'differenceCost',
        'instrument_properties': 'instrumentProperties'
    }

    required_map = {
        'instrument_uid': 'required',
        'sub_holding_keys': 'required',
        'left_units': 'required',
        'right_units': 'required',
        'difference_units': 'required',
        'left_cost': 'required',
        'right_cost': 'required',
        'difference_cost': 'required',
        'instrument_properties': 'required'
    }

    def __init__(self, instrument_uid=None, sub_holding_keys=None, left_units=None, right_units=None, difference_units=None, left_cost=None, right_cost=None, difference_cost=None, instrument_properties=None):  # noqa: E501
        """
        ReconciliationBreak - a model defined in OpenAPI

        :param instrument_uid:  Unique instrument identifier (required)
        :type instrument_uid: str
        :param sub_holding_keys:  Any other properties that comprise the Sub-Holding Key (required)
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param left_units:  Units from the left hand side (required)
        :type left_units: float
        :param right_units:  Units from the right hand side (required)
        :type right_units: float
        :param difference_units:  Difference in units (required)
        :type difference_units: float
        :param left_cost:  (required)
        :type left_cost: lusid.CurrencyAndAmount
        :param right_cost:  (required)
        :type right_cost: lusid.CurrencyAndAmount
        :param difference_cost:  (required)
        :type difference_cost: lusid.CurrencyAndAmount
        :param instrument_properties:  Additional features relating to the instrument (required)
        :type instrument_properties: list[lusid.ModelProperty]

        """  # noqa: E501

        self._instrument_uid = None
        self._sub_holding_keys = None
        self._left_units = None
        self._right_units = None
        self._difference_units = None
        self._left_cost = None
        self._right_cost = None
        self._difference_cost = None
        self._instrument_properties = None
        self.discriminator = None

        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.left_units = left_units
        self.right_units = right_units
        self.difference_units = difference_units
        self.left_cost = left_cost
        self.right_cost = right_cost
        self.difference_cost = difference_cost
        self.instrument_properties = instrument_properties

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this ReconciliationBreak.  # noqa: E501

        Unique instrument identifier  # noqa: E501

        :return: The instrument_uid of this ReconciliationBreak.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this ReconciliationBreak.

        Unique instrument identifier  # noqa: E501

        :param instrument_uid: The instrument_uid of this ReconciliationBreak.  # noqa: E501
        :type: str
        """
        if instrument_uid is None:
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this ReconciliationBreak.  # noqa: E501

        Any other properties that comprise the Sub-Holding Key  # noqa: E501

        :return: The sub_holding_keys of this ReconciliationBreak.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this ReconciliationBreak.

        Any other properties that comprise the Sub-Holding Key  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this ReconciliationBreak.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """
        if sub_holding_keys is None:
            raise ValueError("Invalid value for `sub_holding_keys`, must not be `None`")  # noqa: E501

        self._sub_holding_keys = sub_holding_keys

    @property
    def left_units(self):
        """Gets the left_units of this ReconciliationBreak.  # noqa: E501

        Units from the left hand side  # noqa: E501

        :return: The left_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._left_units

    @left_units.setter
    def left_units(self, left_units):
        """Sets the left_units of this ReconciliationBreak.

        Units from the left hand side  # noqa: E501

        :param left_units: The left_units of this ReconciliationBreak.  # noqa: E501
        :type: float
        """
        if left_units is None:
            raise ValueError("Invalid value for `left_units`, must not be `None`")  # noqa: E501

        self._left_units = left_units

    @property
    def right_units(self):
        """Gets the right_units of this ReconciliationBreak.  # noqa: E501

        Units from the right hand side  # noqa: E501

        :return: The right_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._right_units

    @right_units.setter
    def right_units(self, right_units):
        """Sets the right_units of this ReconciliationBreak.

        Units from the right hand side  # noqa: E501

        :param right_units: The right_units of this ReconciliationBreak.  # noqa: E501
        :type: float
        """
        if right_units is None:
            raise ValueError("Invalid value for `right_units`, must not be `None`")  # noqa: E501

        self._right_units = right_units

    @property
    def difference_units(self):
        """Gets the difference_units of this ReconciliationBreak.  # noqa: E501

        Difference in units  # noqa: E501

        :return: The difference_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._difference_units

    @difference_units.setter
    def difference_units(self, difference_units):
        """Sets the difference_units of this ReconciliationBreak.

        Difference in units  # noqa: E501

        :param difference_units: The difference_units of this ReconciliationBreak.  # noqa: E501
        :type: float
        """
        if difference_units is None:
            raise ValueError("Invalid value for `difference_units`, must not be `None`")  # noqa: E501

        self._difference_units = difference_units

    @property
    def left_cost(self):
        """Gets the left_cost of this ReconciliationBreak.  # noqa: E501


        :return: The left_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._left_cost

    @left_cost.setter
    def left_cost(self, left_cost):
        """Sets the left_cost of this ReconciliationBreak.


        :param left_cost: The left_cost of this ReconciliationBreak.  # noqa: E501
        :type: CurrencyAndAmount
        """
        if left_cost is None:
            raise ValueError("Invalid value for `left_cost`, must not be `None`")  # noqa: E501

        self._left_cost = left_cost

    @property
    def right_cost(self):
        """Gets the right_cost of this ReconciliationBreak.  # noqa: E501


        :return: The right_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._right_cost

    @right_cost.setter
    def right_cost(self, right_cost):
        """Sets the right_cost of this ReconciliationBreak.


        :param right_cost: The right_cost of this ReconciliationBreak.  # noqa: E501
        :type: CurrencyAndAmount
        """
        if right_cost is None:
            raise ValueError("Invalid value for `right_cost`, must not be `None`")  # noqa: E501

        self._right_cost = right_cost

    @property
    def difference_cost(self):
        """Gets the difference_cost of this ReconciliationBreak.  # noqa: E501


        :return: The difference_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._difference_cost

    @difference_cost.setter
    def difference_cost(self, difference_cost):
        """Sets the difference_cost of this ReconciliationBreak.


        :param difference_cost: The difference_cost of this ReconciliationBreak.  # noqa: E501
        :type: CurrencyAndAmount
        """
        if difference_cost is None:
            raise ValueError("Invalid value for `difference_cost`, must not be `None`")  # noqa: E501

        self._difference_cost = difference_cost

    @property
    def instrument_properties(self):
        """Gets the instrument_properties of this ReconciliationBreak.  # noqa: E501

        Additional features relating to the instrument  # noqa: E501

        :return: The instrument_properties of this ReconciliationBreak.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._instrument_properties

    @instrument_properties.setter
    def instrument_properties(self, instrument_properties):
        """Sets the instrument_properties of this ReconciliationBreak.

        Additional features relating to the instrument  # noqa: E501

        :param instrument_properties: The instrument_properties of this ReconciliationBreak.  # noqa: E501
        :type: list[ModelProperty]
        """
        if instrument_properties is None:
            raise ValueError("Invalid value for `instrument_properties`, must not be `None`")  # noqa: E501

        self._instrument_properties = instrument_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReconciliationBreak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
