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


class RulesInterval(object):
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
        'effective_range': 'DateRange',
        'rules': 'list[AmortisationRule]'
    }

    attribute_map = {
        'effective_range': 'effectiveRange',
        'rules': 'rules'
    }

    required_map = {
        'effective_range': 'required',
        'rules': 'required'
    }

    def __init__(self, effective_range=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """RulesInterval - a model defined in OpenAPI"
        
        :param effective_range:  (required)
        :type effective_range: lusid.DateRange
        :param rules:  The rules of this rule set. (required)
        :type rules: list[lusid.AmortisationRule]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_range = None
        self._rules = None
        self.discriminator = None

        self.effective_range = effective_range
        self.rules = rules

    @property
    def effective_range(self):
        """Gets the effective_range of this RulesInterval.  # noqa: E501


        :return: The effective_range of this RulesInterval.  # noqa: E501
        :rtype: lusid.DateRange
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        """Sets the effective_range of this RulesInterval.


        :param effective_range: The effective_range of this RulesInterval.  # noqa: E501
        :type effective_range: lusid.DateRange
        """
        if self.local_vars_configuration.client_side_validation and effective_range is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_range`, must not be `None`")  # noqa: E501

        self._effective_range = effective_range

    @property
    def rules(self):
        """Gets the rules of this RulesInterval.  # noqa: E501

        The rules of this rule set.  # noqa: E501

        :return: The rules of this RulesInterval.  # noqa: E501
        :rtype: list[lusid.AmortisationRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this RulesInterval.

        The rules of this rule set.  # noqa: E501

        :param rules: The rules of this RulesInterval.  # noqa: E501
        :type rules: list[lusid.AmortisationRule]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rules is not None and len(rules) > 100):
            raise ValueError("Invalid value for `rules`, number of items must be less than or equal to `100`")  # noqa: E501

        self._rules = rules

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
        if not isinstance(other, RulesInterval):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RulesInterval):
            return True

        return self.to_dict() != other.to_dict()
