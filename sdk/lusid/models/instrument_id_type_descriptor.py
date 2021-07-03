# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3230
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InstrumentIdTypeDescriptor(object):
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
        'identifier_type': 'str',
        'property_key': 'str',
        'is_unique_identifier_type': 'bool'
    }

    attribute_map = {
        'identifier_type': 'identifierType',
        'property_key': 'propertyKey',
        'is_unique_identifier_type': 'isUniqueIdentifierType'
    }

    required_map = {
        'identifier_type': 'required',
        'property_key': 'required',
        'is_unique_identifier_type': 'required'
    }

    def __init__(self, identifier_type=None, property_key=None, is_unique_identifier_type=None):  # noqa: E501
        """
        InstrumentIdTypeDescriptor - a model defined in OpenAPI

        :param identifier_type:  The name of the identifier type. (required)
        :type identifier_type: str
        :param property_key:  The property key that corresponds to the identifier type. (required)
        :type property_key: str
        :param is_unique_identifier_type:  Whether or not the identifier type is enforced to be unique. (required)
        :type is_unique_identifier_type: bool

        """  # noqa: E501

        self._identifier_type = None
        self._property_key = None
        self._is_unique_identifier_type = None
        self.discriminator = None

        self.identifier_type = identifier_type
        self.property_key = property_key
        self.is_unique_identifier_type = is_unique_identifier_type

    @property
    def identifier_type(self):
        """Gets the identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501

        The name of the identifier type.  # noqa: E501

        :return: The identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this InstrumentIdTypeDescriptor.

        The name of the identifier type.  # noqa: E501

        :param identifier_type: The identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type: str
        """
        if identifier_type is None:
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def property_key(self):
        """Gets the property_key of this InstrumentIdTypeDescriptor.  # noqa: E501

        The property key that corresponds to the identifier type.  # noqa: E501

        :return: The property_key of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this InstrumentIdTypeDescriptor.

        The property key that corresponds to the identifier type.  # noqa: E501

        :param property_key: The property_key of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type: str
        """
        if property_key is None:
            raise ValueError("Invalid value for `property_key`, must not be `None`")  # noqa: E501

        self._property_key = property_key

    @property
    def is_unique_identifier_type(self):
        """Gets the is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501

        Whether or not the identifier type is enforced to be unique.  # noqa: E501

        :return: The is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._is_unique_identifier_type

    @is_unique_identifier_type.setter
    def is_unique_identifier_type(self, is_unique_identifier_type):
        """Sets the is_unique_identifier_type of this InstrumentIdTypeDescriptor.

        Whether or not the identifier type is enforced to be unique.  # noqa: E501

        :param is_unique_identifier_type: The is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type: bool
        """
        if is_unique_identifier_type is None:
            raise ValueError("Invalid value for `is_unique_identifier_type`, must not be `None`")  # noqa: E501

        self._is_unique_identifier_type = is_unique_identifier_type

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
        if not isinstance(other, InstrumentIdTypeDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
