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


class StagedModificationStagingRule(object):
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
        'staging_rule_set_id': 'str',
        'rule_id': 'str',
        'required_approvals': 'int',
        'current_user_can_decide': 'bool'
    }

    attribute_map = {
        'staging_rule_set_id': 'stagingRuleSetId',
        'rule_id': 'ruleId',
        'required_approvals': 'requiredApprovals',
        'current_user_can_decide': 'currentUserCanDecide'
    }

    required_map = {
        'staging_rule_set_id': 'optional',
        'rule_id': 'optional',
        'required_approvals': 'optional',
        'current_user_can_decide': 'optional'
    }

    def __init__(self, staging_rule_set_id=None, rule_id=None, required_approvals=None, current_user_can_decide=None, local_vars_configuration=None):  # noqa: E501
        """StagedModificationStagingRule - a model defined in OpenAPI"
        
        :param staging_rule_set_id:  System generated unique id for the staging rule set.
        :type staging_rule_set_id: str
        :param rule_id:  The ID of the staging rule.
        :type rule_id: str
        :param required_approvals:  The number of approvals required. If left blank, one approval is needed.
        :type required_approvals: int
        :param current_user_can_decide:  True or False indicating whether the current user can make a decision on the staged modification.
        :type current_user_can_decide: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._staging_rule_set_id = None
        self._rule_id = None
        self._required_approvals = None
        self._current_user_can_decide = None
        self.discriminator = None

        self.staging_rule_set_id = staging_rule_set_id
        self.rule_id = rule_id
        if required_approvals is not None:
            self.required_approvals = required_approvals
        if current_user_can_decide is not None:
            self.current_user_can_decide = current_user_can_decide

    @property
    def staging_rule_set_id(self):
        """Gets the staging_rule_set_id of this StagedModificationStagingRule.  # noqa: E501

        System generated unique id for the staging rule set.  # noqa: E501

        :return: The staging_rule_set_id of this StagedModificationStagingRule.  # noqa: E501
        :rtype: str
        """
        return self._staging_rule_set_id

    @staging_rule_set_id.setter
    def staging_rule_set_id(self, staging_rule_set_id):
        """Sets the staging_rule_set_id of this StagedModificationStagingRule.

        System generated unique id for the staging rule set.  # noqa: E501

        :param staging_rule_set_id: The staging_rule_set_id of this StagedModificationStagingRule.  # noqa: E501
        :type staging_rule_set_id: str
        """

        self._staging_rule_set_id = staging_rule_set_id

    @property
    def rule_id(self):
        """Gets the rule_id of this StagedModificationStagingRule.  # noqa: E501

        The ID of the staging rule.  # noqa: E501

        :return: The rule_id of this StagedModificationStagingRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this StagedModificationStagingRule.

        The ID of the staging rule.  # noqa: E501

        :param rule_id: The rule_id of this StagedModificationStagingRule.  # noqa: E501
        :type rule_id: str
        """

        self._rule_id = rule_id

    @property
    def required_approvals(self):
        """Gets the required_approvals of this StagedModificationStagingRule.  # noqa: E501

        The number of approvals required. If left blank, one approval is needed.  # noqa: E501

        :return: The required_approvals of this StagedModificationStagingRule.  # noqa: E501
        :rtype: int
        """
        return self._required_approvals

    @required_approvals.setter
    def required_approvals(self, required_approvals):
        """Sets the required_approvals of this StagedModificationStagingRule.

        The number of approvals required. If left blank, one approval is needed.  # noqa: E501

        :param required_approvals: The required_approvals of this StagedModificationStagingRule.  # noqa: E501
        :type required_approvals: int
        """

        self._required_approvals = required_approvals

    @property
    def current_user_can_decide(self):
        """Gets the current_user_can_decide of this StagedModificationStagingRule.  # noqa: E501

        True or False indicating whether the current user can make a decision on the staged modification.  # noqa: E501

        :return: The current_user_can_decide of this StagedModificationStagingRule.  # noqa: E501
        :rtype: bool
        """
        return self._current_user_can_decide

    @current_user_can_decide.setter
    def current_user_can_decide(self, current_user_can_decide):
        """Sets the current_user_can_decide of this StagedModificationStagingRule.

        True or False indicating whether the current user can make a decision on the staged modification.  # noqa: E501

        :param current_user_can_decide: The current_user_can_decide of this StagedModificationStagingRule.  # noqa: E501
        :type current_user_can_decide: bool
        """

        self._current_user_can_decide = current_user_can_decide

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
        if not isinstance(other, StagedModificationStagingRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModificationStagingRule):
            return True

        return self.to_dict() != other.to_dict()
