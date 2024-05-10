# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.140
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


class StagingRuleSet(object):
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
        'entity_type': 'str',
        'staging_rule_set_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'rules': 'list[StagingRule]',
        'href': 'str',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'staging_rule_set_id': 'stagingRuleSetId',
        'display_name': 'displayName',
        'description': 'description',
        'rules': 'rules',
        'href': 'href',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'entity_type': 'required',
        'staging_rule_set_id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'rules': 'required',
        'href': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, entity_type=None, staging_rule_set_id=None, display_name=None, description=None, rules=None, href=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StagingRuleSet - a model defined in OpenAPI"
        
        :param entity_type:  The entity type the staging rule set applies to. (required)
        :type entity_type: str
        :param staging_rule_set_id:  System generated unique id for the staging rule set. (required)
        :type staging_rule_set_id: str
        :param display_name:  The name of the staging rule set. (required)
        :type display_name: str
        :param description:  A description for the staging rule set.
        :type description: str
        :param rules:  The list of staging rules that apply to a specific entity type. (required)
        :type rules: list[lusid.StagingRule]
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity_type = None
        self._staging_rule_set_id = None
        self._display_name = None
        self._description = None
        self._rules = None
        self._href = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.entity_type = entity_type
        self.staging_rule_set_id = staging_rule_set_id
        self.display_name = display_name
        self.description = description
        self.rules = rules
        self.href = href
        if version is not None:
            self.version = version
        self.links = links

    @property
    def entity_type(self):
        """Gets the entity_type of this StagingRuleSet.  # noqa: E501

        The entity type the staging rule set applies to.  # noqa: E501

        :return: The entity_type of this StagingRuleSet.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this StagingRuleSet.

        The entity type the staging rule set applies to.  # noqa: E501

        :param entity_type: The entity_type of this StagingRuleSet.  # noqa: E501
        :type entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity_type is not None and len(entity_type) < 1):
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def staging_rule_set_id(self):
        """Gets the staging_rule_set_id of this StagingRuleSet.  # noqa: E501

        System generated unique id for the staging rule set.  # noqa: E501

        :return: The staging_rule_set_id of this StagingRuleSet.  # noqa: E501
        :rtype: str
        """
        return self._staging_rule_set_id

    @staging_rule_set_id.setter
    def staging_rule_set_id(self, staging_rule_set_id):
        """Sets the staging_rule_set_id of this StagingRuleSet.

        System generated unique id for the staging rule set.  # noqa: E501

        :param staging_rule_set_id: The staging_rule_set_id of this StagingRuleSet.  # noqa: E501
        :type staging_rule_set_id: str
        """
        if self.local_vars_configuration.client_side_validation and staging_rule_set_id is None:  # noqa: E501
            raise ValueError("Invalid value for `staging_rule_set_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                staging_rule_set_id is not None and len(staging_rule_set_id) < 1):
            raise ValueError("Invalid value for `staging_rule_set_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._staging_rule_set_id = staging_rule_set_id

    @property
    def display_name(self):
        """Gets the display_name of this StagingRuleSet.  # noqa: E501

        The name of the staging rule set.  # noqa: E501

        :return: The display_name of this StagingRuleSet.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this StagingRuleSet.

        The name of the staging rule set.  # noqa: E501

        :param display_name: The display_name of this StagingRuleSet.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this StagingRuleSet.  # noqa: E501

        A description for the staging rule set.  # noqa: E501

        :return: The description of this StagingRuleSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StagingRuleSet.

        A description for the staging rule set.  # noqa: E501

        :param description: The description of this StagingRuleSet.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this StagingRuleSet.  # noqa: E501

        The list of staging rules that apply to a specific entity type.  # noqa: E501

        :return: The rules of this StagingRuleSet.  # noqa: E501
        :rtype: list[lusid.StagingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this StagingRuleSet.

        The list of staging rules that apply to a specific entity type.  # noqa: E501

        :param rules: The rules of this StagingRuleSet.  # noqa: E501
        :type rules: list[lusid.StagingRule]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

    @property
    def href(self):
        """Gets the href of this StagingRuleSet.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this StagingRuleSet.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this StagingRuleSet.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this StagingRuleSet.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def version(self):
        """Gets the version of this StagingRuleSet.  # noqa: E501


        :return: The version of this StagingRuleSet.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StagingRuleSet.


        :param version: The version of this StagingRuleSet.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this StagingRuleSet.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this StagingRuleSet.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StagingRuleSet.

        Collection of links.  # noqa: E501

        :param links: The links of this StagingRuleSet.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, StagingRuleSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingRuleSet):
            return True

        return self.to_dict() != other.to_dict()
