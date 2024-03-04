# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.105
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


class CleardownModuleRule(object):
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
        'rule_id': 'str',
        'general_ledger_account_code': 'str',
        'rule_filter': 'str'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'general_ledger_account_code': 'generalLedgerAccountCode',
        'rule_filter': 'ruleFilter'
    }

    required_map = {
        'rule_id': 'required',
        'general_ledger_account_code': 'required',
        'rule_filter': 'required'
    }

    def __init__(self, rule_id=None, general_ledger_account_code=None, rule_filter=None, local_vars_configuration=None):  # noqa: E501
        """CleardownModuleRule - a model defined in OpenAPI"
        
        :param rule_id:  The identifier for the Cleardown Rule. (required)
        :type rule_id: str
        :param general_ledger_account_code:  The account to post the residual P&L to. (required)
        :type general_ledger_account_code: str
        :param rule_filter:  The filter syntax for the Cleardown Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. (required)
        :type rule_filter: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_id = None
        self._general_ledger_account_code = None
        self._rule_filter = None
        self.discriminator = None

        self.rule_id = rule_id
        self.general_ledger_account_code = general_ledger_account_code
        self.rule_filter = rule_filter

    @property
    def rule_id(self):
        """Gets the rule_id of this CleardownModuleRule.  # noqa: E501

        The identifier for the Cleardown Rule.  # noqa: E501

        :return: The rule_id of this CleardownModuleRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CleardownModuleRule.

        The identifier for the Cleardown Rule.  # noqa: E501

        :param rule_id: The rule_id of this CleardownModuleRule.  # noqa: E501
        :type rule_id: str
        """
        if self.local_vars_configuration.client_side_validation and rule_id is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_id is not None and len(rule_id) > 64):
            raise ValueError("Invalid value for `rule_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_id is not None and len(rule_id) < 1):
            raise ValueError("Invalid value for `rule_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', rule_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `rule_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def general_ledger_account_code(self):
        """Gets the general_ledger_account_code of this CleardownModuleRule.  # noqa: E501

        The account to post the residual P&L to.  # noqa: E501

        :return: The general_ledger_account_code of this CleardownModuleRule.  # noqa: E501
        :rtype: str
        """
        return self._general_ledger_account_code

    @general_ledger_account_code.setter
    def general_ledger_account_code(self, general_ledger_account_code):
        """Sets the general_ledger_account_code of this CleardownModuleRule.

        The account to post the residual P&L to.  # noqa: E501

        :param general_ledger_account_code: The general_ledger_account_code of this CleardownModuleRule.  # noqa: E501
        :type general_ledger_account_code: str
        """
        if self.local_vars_configuration.client_side_validation and general_ledger_account_code is None:  # noqa: E501
            raise ValueError("Invalid value for `general_ledger_account_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_account_code is not None and len(general_ledger_account_code) > 512):
            raise ValueError("Invalid value for `general_ledger_account_code`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_account_code is not None and len(general_ledger_account_code) < 1):
            raise ValueError("Invalid value for `general_ledger_account_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_account_code is not None and not re.search(r'^[\s\S]*$', general_ledger_account_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `general_ledger_account_code`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._general_ledger_account_code = general_ledger_account_code

    @property
    def rule_filter(self):
        """Gets the rule_filter of this CleardownModuleRule.  # noqa: E501

        The filter syntax for the Cleardown Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax.  # noqa: E501

        :return: The rule_filter of this CleardownModuleRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_filter

    @rule_filter.setter
    def rule_filter(self, rule_filter):
        """Sets the rule_filter of this CleardownModuleRule.

        The filter syntax for the Cleardown Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax.  # noqa: E501

        :param rule_filter: The rule_filter of this CleardownModuleRule.  # noqa: E501
        :type rule_filter: str
        """
        if self.local_vars_configuration.client_side_validation and rule_filter is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_filter`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_filter is not None and len(rule_filter) > 16384):
            raise ValueError("Invalid value for `rule_filter`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_filter is not None and len(rule_filter) < 1):
            raise ValueError("Invalid value for `rule_filter`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_filter is not None and not re.search(r'^[\s\S]*$', rule_filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `rule_filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._rule_filter = rule_filter

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
        if not isinstance(other, CleardownModuleRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CleardownModuleRule):
            return True

        return self.to_dict() != other.to_dict()
