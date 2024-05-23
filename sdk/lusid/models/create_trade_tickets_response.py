# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.156
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


class CreateTradeTicketsResponse(object):
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
        'values': 'list[LusidTradeTicket]',
        'failures': 'list[ErrorDetail]'
    }

    attribute_map = {
        'values': 'values',
        'failures': 'failures'
    }

    required_map = {
        'values': 'required',
        'failures': 'required'
    }

    def __init__(self, values=None, failures=None, local_vars_configuration=None):  # noqa: E501
        """CreateTradeTicketsResponse - a model defined in OpenAPI"
        
        :param values:  (required)
        :type values: list[lusid.LusidTradeTicket]
        :param failures:  (required)
        :type failures: list[lusid.ErrorDetail]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._failures = None
        self.discriminator = None

        self.values = values
        self.failures = failures

    @property
    def values(self):
        """Gets the values of this CreateTradeTicketsResponse.  # noqa: E501


        :return: The values of this CreateTradeTicketsResponse.  # noqa: E501
        :rtype: list[lusid.LusidTradeTicket]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CreateTradeTicketsResponse.


        :param values: The values of this CreateTradeTicketsResponse.  # noqa: E501
        :type values: list[lusid.LusidTradeTicket]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def failures(self):
        """Gets the failures of this CreateTradeTicketsResponse.  # noqa: E501


        :return: The failures of this CreateTradeTicketsResponse.  # noqa: E501
        :rtype: list[lusid.ErrorDetail]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this CreateTradeTicketsResponse.


        :param failures: The failures of this CreateTradeTicketsResponse.  # noqa: E501
        :type failures: list[lusid.ErrorDetail]
        """
        if self.local_vars_configuration.client_side_validation and failures is None:  # noqa: E501
            raise ValueError("Invalid value for `failures`, must not be `None`")  # noqa: E501

        self._failures = failures

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
        if not isinstance(other, CreateTradeTicketsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTradeTicketsResponse):
            return True

        return self.to_dict() != other.to_dict()
