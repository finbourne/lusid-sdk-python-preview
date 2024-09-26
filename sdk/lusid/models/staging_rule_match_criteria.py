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


class StagingRuleMatchCriteria(object):
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
        'action_in': 'list[str]',
        'requesting_user': 'str',
        'entity_attributes': 'str',
        'changed_attribute_name_in': 'list[str]'
    }

    attribute_map = {
        'action_in': 'actionIn',
        'requesting_user': 'requestingUser',
        'entity_attributes': 'entityAttributes',
        'changed_attribute_name_in': 'changedAttributeNameIn'
    }

    required_map = {
        'action_in': 'optional',
        'requesting_user': 'optional',
        'entity_attributes': 'optional',
        'changed_attribute_name_in': 'optional'
    }

    def __init__(self, action_in=None, requesting_user=None, entity_attributes=None, changed_attribute_name_in=None, local_vars_configuration=None):  # noqa: E501
        """StagingRuleMatchCriteria - a model defined in OpenAPI"
        
        :param action_in: 
        :type action_in: list[str]
        :param requesting_user: 
        :type requesting_user: str
        :param entity_attributes: 
        :type entity_attributes: str
        :param changed_attribute_name_in: 
        :type changed_attribute_name_in: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action_in = None
        self._requesting_user = None
        self._entity_attributes = None
        self._changed_attribute_name_in = None
        self.discriminator = None

        self.action_in = action_in
        self.requesting_user = requesting_user
        self.entity_attributes = entity_attributes
        self.changed_attribute_name_in = changed_attribute_name_in

    @property
    def action_in(self):
        """Gets the action_in of this StagingRuleMatchCriteria.  # noqa: E501


        :return: The action_in of this StagingRuleMatchCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._action_in

    @action_in.setter
    def action_in(self, action_in):
        """Sets the action_in of this StagingRuleMatchCriteria.


        :param action_in: The action_in of this StagingRuleMatchCriteria.  # noqa: E501
        :type action_in: list[str]
        """

        self._action_in = action_in

    @property
    def requesting_user(self):
        """Gets the requesting_user of this StagingRuleMatchCriteria.  # noqa: E501


        :return: The requesting_user of this StagingRuleMatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._requesting_user

    @requesting_user.setter
    def requesting_user(self, requesting_user):
        """Sets the requesting_user of this StagingRuleMatchCriteria.


        :param requesting_user: The requesting_user of this StagingRuleMatchCriteria.  # noqa: E501
        :type requesting_user: str
        """
        if (self.local_vars_configuration.client_side_validation and
                requesting_user is not None and len(requesting_user) > 16384):
            raise ValueError("Invalid value for `requesting_user`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                requesting_user is not None and len(requesting_user) < 0):
            raise ValueError("Invalid value for `requesting_user`, length must be greater than or equal to `0`")  # noqa: E501

        self._requesting_user = requesting_user

    @property
    def entity_attributes(self):
        """Gets the entity_attributes of this StagingRuleMatchCriteria.  # noqa: E501


        :return: The entity_attributes of this StagingRuleMatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._entity_attributes

    @entity_attributes.setter
    def entity_attributes(self, entity_attributes):
        """Sets the entity_attributes of this StagingRuleMatchCriteria.


        :param entity_attributes: The entity_attributes of this StagingRuleMatchCriteria.  # noqa: E501
        :type entity_attributes: str
        """
        if (self.local_vars_configuration.client_side_validation and
                entity_attributes is not None and len(entity_attributes) > 16384):
            raise ValueError("Invalid value for `entity_attributes`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity_attributes is not None and len(entity_attributes) < 0):
            raise ValueError("Invalid value for `entity_attributes`, length must be greater than or equal to `0`")  # noqa: E501

        self._entity_attributes = entity_attributes

    @property
    def changed_attribute_name_in(self):
        """Gets the changed_attribute_name_in of this StagingRuleMatchCriteria.  # noqa: E501


        :return: The changed_attribute_name_in of this StagingRuleMatchCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._changed_attribute_name_in

    @changed_attribute_name_in.setter
    def changed_attribute_name_in(self, changed_attribute_name_in):
        """Sets the changed_attribute_name_in of this StagingRuleMatchCriteria.


        :param changed_attribute_name_in: The changed_attribute_name_in of this StagingRuleMatchCriteria.  # noqa: E501
        :type changed_attribute_name_in: list[str]
        """

        self._changed_attribute_name_in = changed_attribute_name_in

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
        if not isinstance(other, StagingRuleMatchCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingRuleMatchCriteria):
            return True

        return self.to_dict() != other.to_dict()
