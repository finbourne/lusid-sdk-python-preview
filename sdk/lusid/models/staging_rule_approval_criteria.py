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


class StagingRuleApprovalCriteria(object):
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
        'required_approvals': 'int',
        'deciding_user': 'str'
    }

    attribute_map = {
        'required_approvals': 'requiredApprovals',
        'deciding_user': 'decidingUser'
    }

    required_map = {
        'required_approvals': 'optional',
        'deciding_user': 'optional'
    }

    def __init__(self, required_approvals=None, deciding_user=None, local_vars_configuration=None):  # noqa: E501
        """StagingRuleApprovalCriteria - a model defined in OpenAPI"
        
        :param required_approvals: 
        :type required_approvals: int
        :param deciding_user: 
        :type deciding_user: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._required_approvals = None
        self._deciding_user = None
        self.discriminator = None

        self.required_approvals = required_approvals
        self.deciding_user = deciding_user

    @property
    def required_approvals(self):
        """Gets the required_approvals of this StagingRuleApprovalCriteria.  # noqa: E501


        :return: The required_approvals of this StagingRuleApprovalCriteria.  # noqa: E501
        :rtype: int
        """
        return self._required_approvals

    @required_approvals.setter
    def required_approvals(self, required_approvals):
        """Sets the required_approvals of this StagingRuleApprovalCriteria.


        :param required_approvals: The required_approvals of this StagingRuleApprovalCriteria.  # noqa: E501
        :type required_approvals: int
        """

        self._required_approvals = required_approvals

    @property
    def deciding_user(self):
        """Gets the deciding_user of this StagingRuleApprovalCriteria.  # noqa: E501


        :return: The deciding_user of this StagingRuleApprovalCriteria.  # noqa: E501
        :rtype: str
        """
        return self._deciding_user

    @deciding_user.setter
    def deciding_user(self, deciding_user):
        """Sets the deciding_user of this StagingRuleApprovalCriteria.


        :param deciding_user: The deciding_user of this StagingRuleApprovalCriteria.  # noqa: E501
        :type deciding_user: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deciding_user is not None and len(deciding_user) > 16384):
            raise ValueError("Invalid value for `deciding_user`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                deciding_user is not None and len(deciding_user) < 0):
            raise ValueError("Invalid value for `deciding_user`, length must be greater than or equal to `0`")  # noqa: E501

        self._deciding_user = deciding_user

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
        if not isinstance(other, StagingRuleApprovalCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingRuleApprovalCriteria):
            return True

        return self.to_dict() != other.to_dict()
