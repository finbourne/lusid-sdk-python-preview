# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.263
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


class MappedString(object):
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
        'left_value': 'str',
        'right_value': 'str',
        'mapping_direction': 'str',
        'is_case_sensitive': 'bool'
    }

    attribute_map = {
        'left_value': 'leftValue',
        'right_value': 'rightValue',
        'mapping_direction': 'mappingDirection',
        'is_case_sensitive': 'isCaseSensitive'
    }

    required_map = {
        'left_value': 'optional',
        'right_value': 'optional',
        'mapping_direction': 'optional',
        'is_case_sensitive': 'optional'
    }

    def __init__(self, left_value=None, right_value=None, mapping_direction=None, is_case_sensitive=None, local_vars_configuration=None):  # noqa: E501
        """MappedString - a model defined in OpenAPI"
        
        :param left_value: 
        :type left_value: str
        :param right_value: 
        :type right_value: str
        :param mapping_direction: 
        :type mapping_direction: str
        :param is_case_sensitive: 
        :type is_case_sensitive: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left_value = None
        self._right_value = None
        self._mapping_direction = None
        self._is_case_sensitive = None
        self.discriminator = None

        self.left_value = left_value
        self.right_value = right_value
        self.mapping_direction = mapping_direction
        if is_case_sensitive is not None:
            self.is_case_sensitive = is_case_sensitive

    @property
    def left_value(self):
        """Gets the left_value of this MappedString.  # noqa: E501


        :return: The left_value of this MappedString.  # noqa: E501
        :rtype: str
        """
        return self._left_value

    @left_value.setter
    def left_value(self, left_value):
        """Sets the left_value of this MappedString.


        :param left_value: The left_value of this MappedString.  # noqa: E501
        :type left_value: str
        """

        self._left_value = left_value

    @property
    def right_value(self):
        """Gets the right_value of this MappedString.  # noqa: E501


        :return: The right_value of this MappedString.  # noqa: E501
        :rtype: str
        """
        return self._right_value

    @right_value.setter
    def right_value(self, right_value):
        """Sets the right_value of this MappedString.


        :param right_value: The right_value of this MappedString.  # noqa: E501
        :type right_value: str
        """

        self._right_value = right_value

    @property
    def mapping_direction(self):
        """Gets the mapping_direction of this MappedString.  # noqa: E501


        :return: The mapping_direction of this MappedString.  # noqa: E501
        :rtype: str
        """
        return self._mapping_direction

    @mapping_direction.setter
    def mapping_direction(self, mapping_direction):
        """Sets the mapping_direction of this MappedString.


        :param mapping_direction: The mapping_direction of this MappedString.  # noqa: E501
        :type mapping_direction: str
        """

        self._mapping_direction = mapping_direction

    @property
    def is_case_sensitive(self):
        """Gets the is_case_sensitive of this MappedString.  # noqa: E501


        :return: The is_case_sensitive of this MappedString.  # noqa: E501
        :rtype: bool
        """
        return self._is_case_sensitive

    @is_case_sensitive.setter
    def is_case_sensitive(self, is_case_sensitive):
        """Sets the is_case_sensitive of this MappedString.


        :param is_case_sensitive: The is_case_sensitive of this MappedString.  # noqa: E501
        :type is_case_sensitive: bool
        """

        self._is_case_sensitive = is_case_sensitive

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
        if not isinstance(other, MappedString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MappedString):
            return True

        return self.to_dict() != other.to_dict()
