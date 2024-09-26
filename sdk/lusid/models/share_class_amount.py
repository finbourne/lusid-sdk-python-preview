# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.230
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


class ShareClassAmount(object):
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
        'fund_currency_amount': 'float',
        'share_class_currency_amount': 'float'
    }

    attribute_map = {
        'fund_currency_amount': 'fundCurrencyAmount',
        'share_class_currency_amount': 'shareClassCurrencyAmount'
    }

    required_map = {
        'fund_currency_amount': 'optional',
        'share_class_currency_amount': 'optional'
    }

    def __init__(self, fund_currency_amount=None, share_class_currency_amount=None, local_vars_configuration=None):  # noqa: E501
        """ShareClassAmount - a model defined in OpenAPI"
        
        :param fund_currency_amount:  The value of the amount in the fund currency.
        :type fund_currency_amount: float
        :param share_class_currency_amount:  The value of the amount in the share class currency.
        :type share_class_currency_amount: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fund_currency_amount = None
        self._share_class_currency_amount = None
        self.discriminator = None

        if fund_currency_amount is not None:
            self.fund_currency_amount = fund_currency_amount
        if share_class_currency_amount is not None:
            self.share_class_currency_amount = share_class_currency_amount

    @property
    def fund_currency_amount(self):
        """Gets the fund_currency_amount of this ShareClassAmount.  # noqa: E501

        The value of the amount in the fund currency.  # noqa: E501

        :return: The fund_currency_amount of this ShareClassAmount.  # noqa: E501
        :rtype: float
        """
        return self._fund_currency_amount

    @fund_currency_amount.setter
    def fund_currency_amount(self, fund_currency_amount):
        """Sets the fund_currency_amount of this ShareClassAmount.

        The value of the amount in the fund currency.  # noqa: E501

        :param fund_currency_amount: The fund_currency_amount of this ShareClassAmount.  # noqa: E501
        :type fund_currency_amount: float
        """

        self._fund_currency_amount = fund_currency_amount

    @property
    def share_class_currency_amount(self):
        """Gets the share_class_currency_amount of this ShareClassAmount.  # noqa: E501

        The value of the amount in the share class currency.  # noqa: E501

        :return: The share_class_currency_amount of this ShareClassAmount.  # noqa: E501
        :rtype: float
        """
        return self._share_class_currency_amount

    @share_class_currency_amount.setter
    def share_class_currency_amount(self, share_class_currency_amount):
        """Sets the share_class_currency_amount of this ShareClassAmount.

        The value of the amount in the share class currency.  # noqa: E501

        :param share_class_currency_amount: The share_class_currency_amount of this ShareClassAmount.  # noqa: E501
        :type share_class_currency_amount: float
        """

        self._share_class_currency_amount = share_class_currency_amount

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
        if not isinstance(other, ShareClassAmount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareClassAmount):
            return True

        return self.to_dict() != other.to_dict()
