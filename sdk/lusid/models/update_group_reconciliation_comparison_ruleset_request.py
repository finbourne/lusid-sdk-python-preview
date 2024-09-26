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


class UpdateGroupReconciliationComparisonRulesetRequest(object):
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
        'display_name': 'str',
        'reconciliation_type': 'str',
        'core_attribute_rules': 'list[GroupReconciliationCoreAttributeRule]',
        'aggregate_attribute_rules': 'list[GroupReconciliationAggregateAttributeRule]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'reconciliation_type': 'reconciliationType',
        'core_attribute_rules': 'coreAttributeRules',
        'aggregate_attribute_rules': 'aggregateAttributeRules'
    }

    required_map = {
        'display_name': 'required',
        'reconciliation_type': 'required',
        'core_attribute_rules': 'required',
        'aggregate_attribute_rules': 'required'
    }

    def __init__(self, display_name=None, reconciliation_type=None, core_attribute_rules=None, aggregate_attribute_rules=None, local_vars_configuration=None):  # noqa: E501
        """UpdateGroupReconciliationComparisonRulesetRequest - a model defined in OpenAPI"
        
        :param display_name:  The name of the ruleset (required)
        :type display_name: str
        :param reconciliation_type:  The type of reconciliation to perform. \"Holding\" | \"Transaction\" | \"Valuation\" (required)
        :type reconciliation_type: str
        :param core_attribute_rules:  The core comparison rules (required)
        :type core_attribute_rules: list[lusid.GroupReconciliationCoreAttributeRule]
        :param aggregate_attribute_rules:  The aggregate comparison rules (required)
        :type aggregate_attribute_rules: list[lusid.GroupReconciliationAggregateAttributeRule]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._reconciliation_type = None
        self._core_attribute_rules = None
        self._aggregate_attribute_rules = None
        self.discriminator = None

        self.display_name = display_name
        self.reconciliation_type = reconciliation_type
        self.core_attribute_rules = core_attribute_rules
        self.aggregate_attribute_rules = aggregate_attribute_rules

    @property
    def display_name(self):
        """Gets the display_name of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501

        The name of the ruleset  # noqa: E501

        :return: The display_name of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateGroupReconciliationComparisonRulesetRequest.

        The name of the ruleset  # noqa: E501

        :param display_name: The display_name of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 256):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def reconciliation_type(self):
        """Gets the reconciliation_type of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501

        The type of reconciliation to perform. \"Holding\" | \"Transaction\" | \"Valuation\"  # noqa: E501

        :return: The reconciliation_type of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :rtype: str
        """
        return self._reconciliation_type

    @reconciliation_type.setter
    def reconciliation_type(self, reconciliation_type):
        """Sets the reconciliation_type of this UpdateGroupReconciliationComparisonRulesetRequest.

        The type of reconciliation to perform. \"Holding\" | \"Transaction\" | \"Valuation\"  # noqa: E501

        :param reconciliation_type: The reconciliation_type of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :type reconciliation_type: str
        """
        if self.local_vars_configuration.client_side_validation and reconciliation_type is None:  # noqa: E501
            raise ValueError("Invalid value for `reconciliation_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reconciliation_type is not None and len(reconciliation_type) < 1):
            raise ValueError("Invalid value for `reconciliation_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._reconciliation_type = reconciliation_type

    @property
    def core_attribute_rules(self):
        """Gets the core_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501

        The core comparison rules  # noqa: E501

        :return: The core_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :rtype: list[lusid.GroupReconciliationCoreAttributeRule]
        """
        return self._core_attribute_rules

    @core_attribute_rules.setter
    def core_attribute_rules(self, core_attribute_rules):
        """Sets the core_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.

        The core comparison rules  # noqa: E501

        :param core_attribute_rules: The core_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :type core_attribute_rules: list[lusid.GroupReconciliationCoreAttributeRule]
        """
        if self.local_vars_configuration.client_side_validation and core_attribute_rules is None:  # noqa: E501
            raise ValueError("Invalid value for `core_attribute_rules`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                core_attribute_rules is not None and len(core_attribute_rules) < 1):
            raise ValueError("Invalid value for `core_attribute_rules`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._core_attribute_rules = core_attribute_rules

    @property
    def aggregate_attribute_rules(self):
        """Gets the aggregate_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501

        The aggregate comparison rules  # noqa: E501

        :return: The aggregate_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :rtype: list[lusid.GroupReconciliationAggregateAttributeRule]
        """
        return self._aggregate_attribute_rules

    @aggregate_attribute_rules.setter
    def aggregate_attribute_rules(self, aggregate_attribute_rules):
        """Sets the aggregate_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.

        The aggregate comparison rules  # noqa: E501

        :param aggregate_attribute_rules: The aggregate_attribute_rules of this UpdateGroupReconciliationComparisonRulesetRequest.  # noqa: E501
        :type aggregate_attribute_rules: list[lusid.GroupReconciliationAggregateAttributeRule]
        """
        if self.local_vars_configuration.client_side_validation and aggregate_attribute_rules is None:  # noqa: E501
            raise ValueError("Invalid value for `aggregate_attribute_rules`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                aggregate_attribute_rules is not None and len(aggregate_attribute_rules) < 1):
            raise ValueError("Invalid value for `aggregate_attribute_rules`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._aggregate_attribute_rules = aggregate_attribute_rules

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
        if not isinstance(other, UpdateGroupReconciliationComparisonRulesetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGroupReconciliationComparisonRulesetRequest):
            return True

        return self.to_dict() != other.to_dict()
