# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.582
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


class UnderlyingLeg(object):
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
        'pay_receive': 'str',
        'underlying': 'LusidInstrument'
    }

    attribute_map = {
        'pay_receive': 'payReceive',
        'underlying': 'underlying'
    }

    required_map = {
        'pay_receive': 'required',
        'underlying': 'required'
    }

    def __init__(self, pay_receive=None, underlying=None, local_vars_configuration=None):  # noqa: E501
        """UnderlyingLeg - a model defined in OpenAPI"
        
        :param pay_receive:  Either Pay or Receive stating direction of the underlying in the swap.    Supported string (enumeration) values are: [Pay, Receive]. (required)
        :type pay_receive: str
        :param underlying:  (required)
        :type underlying: lusid.LusidInstrument

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pay_receive = None
        self._underlying = None
        self.discriminator = None

        self.pay_receive = pay_receive
        self.underlying = underlying

    @property
    def pay_receive(self):
        """Gets the pay_receive of this UnderlyingLeg.  # noqa: E501

        Either Pay or Receive stating direction of the underlying in the swap.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :return: The pay_receive of this UnderlyingLeg.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this UnderlyingLeg.

        Either Pay or Receive stating direction of the underlying in the swap.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :param pay_receive: The pay_receive of this UnderlyingLeg.  # noqa: E501
        :type pay_receive: str
        """
        if self.local_vars_configuration.client_side_validation and pay_receive is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_receive`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) < 1):
            raise ValueError("Invalid value for `pay_receive`, length must be greater than or equal to `1`")  # noqa: E501

        self._pay_receive = pay_receive

    @property
    def underlying(self):
        """Gets the underlying of this UnderlyingLeg.  # noqa: E501


        :return: The underlying of this UnderlyingLeg.  # noqa: E501
        :rtype: lusid.LusidInstrument
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this UnderlyingLeg.


        :param underlying: The underlying of this UnderlyingLeg.  # noqa: E501
        :type underlying: lusid.LusidInstrument
        """
        if self.local_vars_configuration.client_side_validation and underlying is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying`, must not be `None`")  # noqa: E501

        self._underlying = underlying

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
        if not isinstance(other, UnderlyingLeg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnderlyingLeg):
            return True

        return self.to_dict() != other.to_dict()
