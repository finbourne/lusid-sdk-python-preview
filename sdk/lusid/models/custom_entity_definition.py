# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3409
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CustomEntityDefinition(object):
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
        'href': 'str',
        'custom_entity_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'entity_type': 'str',
        'field_schema': 'list[CustomEntityFieldDefinition]'
    }

    attribute_map = {
        'href': 'href',
        'custom_entity_id': 'customEntityId',
        'display_name': 'displayName',
        'description': 'description',
        'entity_type': 'entityType',
        'field_schema': 'fieldSchema'
    }

    required_map = {
        'href': 'optional',
        'custom_entity_id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'entity_type': 'required',
        'field_schema': 'required'
    }

    def __init__(self, href=None, custom_entity_id=None, display_name=None, description=None, entity_type=None, field_schema=None):  # noqa: E501
        """
        CustomEntityDefinition - a model defined in OpenAPI

        :param href: 
        :type href: str
        :param custom_entity_id:  (required)
        :type custom_entity_id: str
        :param display_name:  (required)
        :type display_name: str
        :param description: 
        :type description: str
        :param entity_type:  (required)
        :type entity_type: str
        :param field_schema:  (required)
        :type field_schema: list[lusid.CustomEntityFieldDefinition]

        """  # noqa: E501

        self._href = None
        self._custom_entity_id = None
        self._display_name = None
        self._description = None
        self._entity_type = None
        self._field_schema = None
        self.discriminator = None

        self.href = href
        self.custom_entity_id = custom_entity_id
        self.display_name = display_name
        self.description = description
        self.entity_type = entity_type
        self.field_schema = field_schema

    @property
    def href(self):
        """Gets the href of this CustomEntityDefinition.  # noqa: E501


        :return: The href of this CustomEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CustomEntityDefinition.


        :param href: The href of this CustomEntityDefinition.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def custom_entity_id(self):
        """Gets the custom_entity_id of this CustomEntityDefinition.  # noqa: E501


        :return: The custom_entity_id of this CustomEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._custom_entity_id

    @custom_entity_id.setter
    def custom_entity_id(self, custom_entity_id):
        """Sets the custom_entity_id of this CustomEntityDefinition.


        :param custom_entity_id: The custom_entity_id of this CustomEntityDefinition.  # noqa: E501
        :type: str
        """
        if custom_entity_id is None:
            raise ValueError("Invalid value for `custom_entity_id`, must not be `None`")  # noqa: E501

        self._custom_entity_id = custom_entity_id

    @property
    def display_name(self):
        """Gets the display_name of this CustomEntityDefinition.  # noqa: E501


        :return: The display_name of this CustomEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CustomEntityDefinition.


        :param display_name: The display_name of this CustomEntityDefinition.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CustomEntityDefinition.  # noqa: E501


        :return: The description of this CustomEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomEntityDefinition.


        :param description: The description of this CustomEntityDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this CustomEntityDefinition.  # noqa: E501


        :return: The entity_type of this CustomEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this CustomEntityDefinition.


        :param entity_type: The entity_type of this CustomEntityDefinition.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def field_schema(self):
        """Gets the field_schema of this CustomEntityDefinition.  # noqa: E501


        :return: The field_schema of this CustomEntityDefinition.  # noqa: E501
        :rtype: list[CustomEntityFieldDefinition]
        """
        return self._field_schema

    @field_schema.setter
    def field_schema(self, field_schema):
        """Sets the field_schema of this CustomEntityDefinition.


        :param field_schema: The field_schema of this CustomEntityDefinition.  # noqa: E501
        :type: list[CustomEntityFieldDefinition]
        """
        if field_schema is None:
            raise ValueError("Invalid value for `field_schema`, must not be `None`")  # noqa: E501

        self._field_schema = field_schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomEntityDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
