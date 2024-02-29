# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.96
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


class MultiCurrencyAmounts(object):
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
        'local_amount': 'float',
        'base_amount': 'float'
    }

    attribute_map = {
        'local_amount': 'localAmount',
        'base_amount': 'baseAmount'
    }

    required_map = {
        'local_amount': 'required',
        'base_amount': 'required'
    }

    def __init__(self, local_amount=None, base_amount=None, local_vars_configuration=None):  # noqa: E501
        """MultiCurrencyAmounts - a model defined in OpenAPI"
        
        :param local_amount:  (required)
        :type local_amount: float
        :param base_amount:  (required)
        :type base_amount: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._local_amount = None
        self._base_amount = None
        self.discriminator = None

        self.local_amount = local_amount
        self.base_amount = base_amount

    @property
    def local_amount(self):
        """Gets the local_amount of this MultiCurrencyAmounts.  # noqa: E501


        :return: The local_amount of this MultiCurrencyAmounts.  # noqa: E501
        :rtype: float
        """
        return self._local_amount

    @local_amount.setter
    def local_amount(self, local_amount):
        """Sets the local_amount of this MultiCurrencyAmounts.


        :param local_amount: The local_amount of this MultiCurrencyAmounts.  # noqa: E501
        :type local_amount: float
        """
        if self.local_vars_configuration.client_side_validation and local_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `local_amount`, must not be `None`")  # noqa: E501

        self._local_amount = local_amount

    @property
    def base_amount(self):
        """Gets the base_amount of this MultiCurrencyAmounts.  # noqa: E501


        :return: The base_amount of this MultiCurrencyAmounts.  # noqa: E501
        :rtype: float
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """Sets the base_amount of this MultiCurrencyAmounts.


        :param base_amount: The base_amount of this MultiCurrencyAmounts.  # noqa: E501
        :type base_amount: float
        """
        if self.local_vars_configuration.client_side_validation and base_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `base_amount`, must not be `None`")  # noqa: E501

        self._base_amount = base_amount

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
        if not isinstance(other, MultiCurrencyAmounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiCurrencyAmounts):
            return True

        return self.to_dict() != other.to_dict()
