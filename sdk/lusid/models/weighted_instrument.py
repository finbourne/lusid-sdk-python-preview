# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2942
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class WeightedInstrument(object):
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
        'quantity': 'float',
        'holding_identifier': 'str',
        'instrument': 'LusidInstrument'
    }

    attribute_map = {
        'quantity': 'quantity',
        'holding_identifier': 'holdingIdentifier',
        'instrument': 'instrument'
    }

    required_map = {
        'quantity': 'optional',
        'holding_identifier': 'optional',
        'instrument': 'optional'
    }

    def __init__(self, quantity=None, holding_identifier=None, instrument=None):  # noqa: E501
        """
        WeightedInstrument - a model defined in OpenAPI

        :param quantity:  The quantity of the instrument that is owned.
        :type quantity: float
        :param holding_identifier:  Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments.
        :type holding_identifier: str
        :param instrument: 
        :type instrument: lusid.LusidInstrument

        """  # noqa: E501

        self._quantity = None
        self._holding_identifier = None
        self._instrument = None
        self.discriminator = None

        if quantity is not None:
            self.quantity = quantity
        self.holding_identifier = holding_identifier
        if instrument is not None:
            self.instrument = instrument

    @property
    def quantity(self):
        """Gets the quantity of this WeightedInstrument.  # noqa: E501

        The quantity of the instrument that is owned.  # noqa: E501

        :return: The quantity of this WeightedInstrument.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this WeightedInstrument.

        The quantity of the instrument that is owned.  # noqa: E501

        :param quantity: The quantity of this WeightedInstrument.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def holding_identifier(self):
        """Gets the holding_identifier of this WeightedInstrument.  # noqa: E501

        Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments.  # noqa: E501

        :return: The holding_identifier of this WeightedInstrument.  # noqa: E501
        :rtype: str
        """
        return self._holding_identifier

    @holding_identifier.setter
    def holding_identifier(self, holding_identifier):
        """Sets the holding_identifier of this WeightedInstrument.

        Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments.  # noqa: E501

        :param holding_identifier: The holding_identifier of this WeightedInstrument.  # noqa: E501
        :type: str
        """

        self._holding_identifier = holding_identifier

    @property
    def instrument(self):
        """Gets the instrument of this WeightedInstrument.  # noqa: E501


        :return: The instrument of this WeightedInstrument.  # noqa: E501
        :rtype: LusidInstrument
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this WeightedInstrument.


        :param instrument: The instrument of this WeightedInstrument.  # noqa: E501
        :type: LusidInstrument
        """

        self._instrument = instrument

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
        if not isinstance(other, WeightedInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
