# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.82
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


class GroupOfMarketDataKeyRules(object):
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
        'market_data_key_rule_group_operation': 'str',
        'market_rules': 'list[MarketDataKeyRule]'
    }

    attribute_map = {
        'market_data_key_rule_group_operation': 'marketDataKeyRuleGroupOperation',
        'market_rules': 'marketRules'
    }

    required_map = {
        'market_data_key_rule_group_operation': 'required',
        'market_rules': 'required'
    }

    def __init__(self, market_data_key_rule_group_operation=None, market_rules=None, local_vars_configuration=None):  # noqa: E501
        """GroupOfMarketDataKeyRules - a model defined in OpenAPI"
        
        :param market_data_key_rule_group_operation:  The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum] (required)
        :type market_data_key_rule_group_operation: str
        :param market_rules:  The rules that should be grouped together in market data resolution. (required)
        :type market_rules: list[lusid.MarketDataKeyRule]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._market_data_key_rule_group_operation = None
        self._market_rules = None
        self.discriminator = None

        self.market_data_key_rule_group_operation = market_data_key_rule_group_operation
        self.market_rules = market_rules

    @property
    def market_data_key_rule_group_operation(self):
        """Gets the market_data_key_rule_group_operation of this GroupOfMarketDataKeyRules.  # noqa: E501

        The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum]  # noqa: E501

        :return: The market_data_key_rule_group_operation of this GroupOfMarketDataKeyRules.  # noqa: E501
        :rtype: str
        """
        return self._market_data_key_rule_group_operation

    @market_data_key_rule_group_operation.setter
    def market_data_key_rule_group_operation(self, market_data_key_rule_group_operation):
        """Sets the market_data_key_rule_group_operation of this GroupOfMarketDataKeyRules.

        The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum]  # noqa: E501

        :param market_data_key_rule_group_operation: The market_data_key_rule_group_operation of this GroupOfMarketDataKeyRules.  # noqa: E501
        :type market_data_key_rule_group_operation: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_key_rule_group_operation is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_key_rule_group_operation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                market_data_key_rule_group_operation is not None and len(market_data_key_rule_group_operation) < 1):
            raise ValueError("Invalid value for `market_data_key_rule_group_operation`, length must be greater than or equal to `1`")  # noqa: E501

        self._market_data_key_rule_group_operation = market_data_key_rule_group_operation

    @property
    def market_rules(self):
        """Gets the market_rules of this GroupOfMarketDataKeyRules.  # noqa: E501

        The rules that should be grouped together in market data resolution.  # noqa: E501

        :return: The market_rules of this GroupOfMarketDataKeyRules.  # noqa: E501
        :rtype: list[lusid.MarketDataKeyRule]
        """
        return self._market_rules

    @market_rules.setter
    def market_rules(self, market_rules):
        """Sets the market_rules of this GroupOfMarketDataKeyRules.

        The rules that should be grouped together in market data resolution.  # noqa: E501

        :param market_rules: The market_rules of this GroupOfMarketDataKeyRules.  # noqa: E501
        :type market_rules: list[lusid.MarketDataKeyRule]
        """
        if self.local_vars_configuration.client_side_validation and market_rules is None:  # noqa: E501
            raise ValueError("Invalid value for `market_rules`, must not be `None`")  # noqa: E501

        self._market_rules = market_rules

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
        if not isinstance(other, GroupOfMarketDataKeyRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupOfMarketDataKeyRules):
            return True

        return self.to_dict() != other.to_dict()
