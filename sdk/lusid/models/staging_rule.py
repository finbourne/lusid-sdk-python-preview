# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.150
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


class StagingRule(object):
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
        'description': 'str',
        'status': 'str',
        'match_criteria': 'StagingRuleMatchCriteria',
        'approval_criteria': 'StagingRuleApprovalCriteria'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'description': 'description',
        'status': 'status',
        'match_criteria': 'matchCriteria',
        'approval_criteria': 'approvalCriteria'
    }

    required_map = {
        'rule_id': 'required',
        'description': 'optional',
        'status': 'required',
        'match_criteria': 'required',
        'approval_criteria': 'required'
    }

    def __init__(self, rule_id=None, description=None, status=None, match_criteria=None, approval_criteria=None, local_vars_configuration=None):  # noqa: E501
        """StagingRule - a model defined in OpenAPI"
        
        :param rule_id:  The ID of the staging rule. (required)
        :type rule_id: str
        :param description:  A description for the staging rule.
        :type description: str
        :param status:  Whether the rule is 'Active' or 'Inactive'. (required)
        :type status: str
        :param match_criteria:  (required)
        :type match_criteria: lusid.StagingRuleMatchCriteria
        :param approval_criteria:  (required)
        :type approval_criteria: lusid.StagingRuleApprovalCriteria

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_id = None
        self._description = None
        self._status = None
        self._match_criteria = None
        self._approval_criteria = None
        self.discriminator = None

        self.rule_id = rule_id
        self.description = description
        self.status = status
        self.match_criteria = match_criteria
        self.approval_criteria = approval_criteria

    @property
    def rule_id(self):
        """Gets the rule_id of this StagingRule.  # noqa: E501

        The ID of the staging rule.  # noqa: E501

        :return: The rule_id of this StagingRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this StagingRule.

        The ID of the staging rule.  # noqa: E501

        :param rule_id: The rule_id of this StagingRule.  # noqa: E501
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

        self._rule_id = rule_id

    @property
    def description(self):
        """Gets the description of this StagingRule.  # noqa: E501

        A description for the staging rule.  # noqa: E501

        :return: The description of this StagingRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StagingRule.

        A description for the staging rule.  # noqa: E501

        :param description: The description of this StagingRule.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def status(self):
        """Gets the status of this StagingRule.  # noqa: E501

        Whether the rule is 'Active' or 'Inactive'.  # noqa: E501

        :return: The status of this StagingRule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StagingRule.

        Whether the rule is 'Active' or 'Inactive'.  # noqa: E501

        :param status: The status of this StagingRule.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def match_criteria(self):
        """Gets the match_criteria of this StagingRule.  # noqa: E501


        :return: The match_criteria of this StagingRule.  # noqa: E501
        :rtype: lusid.StagingRuleMatchCriteria
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, match_criteria):
        """Sets the match_criteria of this StagingRule.


        :param match_criteria: The match_criteria of this StagingRule.  # noqa: E501
        :type match_criteria: lusid.StagingRuleMatchCriteria
        """
        if self.local_vars_configuration.client_side_validation and match_criteria is None:  # noqa: E501
            raise ValueError("Invalid value for `match_criteria`, must not be `None`")  # noqa: E501

        self._match_criteria = match_criteria

    @property
    def approval_criteria(self):
        """Gets the approval_criteria of this StagingRule.  # noqa: E501


        :return: The approval_criteria of this StagingRule.  # noqa: E501
        :rtype: lusid.StagingRuleApprovalCriteria
        """
        return self._approval_criteria

    @approval_criteria.setter
    def approval_criteria(self, approval_criteria):
        """Sets the approval_criteria of this StagingRule.


        :param approval_criteria: The approval_criteria of this StagingRule.  # noqa: E501
        :type approval_criteria: lusid.StagingRuleApprovalCriteria
        """
        if self.local_vars_configuration.client_side_validation and approval_criteria is None:  # noqa: E501
            raise ValueError("Invalid value for `approval_criteria`, must not be `None`")  # noqa: E501

        self._approval_criteria = approval_criteria

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
        if not isinstance(other, StagingRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingRule):
            return True

        return self.to_dict() != other.to_dict()
