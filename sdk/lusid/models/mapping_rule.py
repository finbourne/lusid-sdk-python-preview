# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5145
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


class MappingRule(object):
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
        'left': 'str',
        'right': 'str',
        'comparison_type': 'str',
        'comparison_value': 'float',
        'weight': 'float',
        'mapped_strings': 'list[MappedString]',
        'is_case_sensitive': 'bool'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'comparison_type': 'comparisonType',
        'comparison_value': 'comparisonValue',
        'weight': 'weight',
        'mapped_strings': 'mappedStrings',
        'is_case_sensitive': 'isCaseSensitive'
    }

    required_map = {
        'left': 'optional',
        'right': 'optional',
        'comparison_type': 'optional',
        'comparison_value': 'optional',
        'weight': 'optional',
        'mapped_strings': 'optional',
        'is_case_sensitive': 'optional'
    }

    def __init__(self, left=None, right=None, comparison_type=None, comparison_value=None, weight=None, mapped_strings=None, is_case_sensitive=None, local_vars_configuration=None):  # noqa: E501
        """MappingRule - a model defined in OpenAPI"
        
        :param left:  The name of the field/property in the left resource (e.g. a transaction)
        :type left: str
        :param right:  The name of the field/property in the right resource (e.g. a transaction)
        :type right: str
        :param comparison_type:  The type of comparison to be performed
        :type comparison_type: str
        :param comparison_value:  The (optional) value used with Finbourne.WebApi.Interface.Dto.Mappings.MappingRule.ComparisonType
        :type comparison_value: float
        :param weight:  A factor used to influence the importance of this item.
        :type weight: float
        :param mapped_strings:  The (optional) value used to map string values.
        :type mapped_strings: list[lusid.MappedString]
        :param is_case_sensitive:  Should string comparisons take case into account, defaults to {false}.
        :type is_case_sensitive: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self._comparison_type = None
        self._comparison_value = None
        self._weight = None
        self._mapped_strings = None
        self._is_case_sensitive = None
        self.discriminator = None

        self.left = left
        self.right = right
        self.comparison_type = comparison_type
        self.comparison_value = comparison_value
        if weight is not None:
            self.weight = weight
        self.mapped_strings = mapped_strings
        if is_case_sensitive is not None:
            self.is_case_sensitive = is_case_sensitive

    @property
    def left(self):
        """Gets the left of this MappingRule.  # noqa: E501

        The name of the field/property in the left resource (e.g. a transaction)  # noqa: E501

        :return: The left of this MappingRule.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this MappingRule.

        The name of the field/property in the left resource (e.g. a transaction)  # noqa: E501

        :param left: The left of this MappingRule.  # noqa: E501
        :type left: str
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this MappingRule.  # noqa: E501

        The name of the field/property in the right resource (e.g. a transaction)  # noqa: E501

        :return: The right of this MappingRule.  # noqa: E501
        :rtype: str
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this MappingRule.

        The name of the field/property in the right resource (e.g. a transaction)  # noqa: E501

        :param right: The right of this MappingRule.  # noqa: E501
        :type right: str
        """

        self._right = right

    @property
    def comparison_type(self):
        """Gets the comparison_type of this MappingRule.  # noqa: E501

        The type of comparison to be performed  # noqa: E501

        :return: The comparison_type of this MappingRule.  # noqa: E501
        :rtype: str
        """
        return self._comparison_type

    @comparison_type.setter
    def comparison_type(self, comparison_type):
        """Sets the comparison_type of this MappingRule.

        The type of comparison to be performed  # noqa: E501

        :param comparison_type: The comparison_type of this MappingRule.  # noqa: E501
        :type comparison_type: str
        """

        self._comparison_type = comparison_type

    @property
    def comparison_value(self):
        """Gets the comparison_value of this MappingRule.  # noqa: E501

        The (optional) value used with Finbourne.WebApi.Interface.Dto.Mappings.MappingRule.ComparisonType  # noqa: E501

        :return: The comparison_value of this MappingRule.  # noqa: E501
        :rtype: float
        """
        return self._comparison_value

    @comparison_value.setter
    def comparison_value(self, comparison_value):
        """Sets the comparison_value of this MappingRule.

        The (optional) value used with Finbourne.WebApi.Interface.Dto.Mappings.MappingRule.ComparisonType  # noqa: E501

        :param comparison_value: The comparison_value of this MappingRule.  # noqa: E501
        :type comparison_value: float
        """

        self._comparison_value = comparison_value

    @property
    def weight(self):
        """Gets the weight of this MappingRule.  # noqa: E501

        A factor used to influence the importance of this item.  # noqa: E501

        :return: The weight of this MappingRule.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MappingRule.

        A factor used to influence the importance of this item.  # noqa: E501

        :param weight: The weight of this MappingRule.  # noqa: E501
        :type weight: float
        """

        self._weight = weight

    @property
    def mapped_strings(self):
        """Gets the mapped_strings of this MappingRule.  # noqa: E501

        The (optional) value used to map string values.  # noqa: E501

        :return: The mapped_strings of this MappingRule.  # noqa: E501
        :rtype: list[lusid.MappedString]
        """
        return self._mapped_strings

    @mapped_strings.setter
    def mapped_strings(self, mapped_strings):
        """Sets the mapped_strings of this MappingRule.

        The (optional) value used to map string values.  # noqa: E501

        :param mapped_strings: The mapped_strings of this MappingRule.  # noqa: E501
        :type mapped_strings: list[lusid.MappedString]
        """

        self._mapped_strings = mapped_strings

    @property
    def is_case_sensitive(self):
        """Gets the is_case_sensitive of this MappingRule.  # noqa: E501

        Should string comparisons take case into account, defaults to {false}.  # noqa: E501

        :return: The is_case_sensitive of this MappingRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_case_sensitive

    @is_case_sensitive.setter
    def is_case_sensitive(self, is_case_sensitive):
        """Sets the is_case_sensitive of this MappingRule.

        Should string comparisons take case into account, defaults to {false}.  # noqa: E501

        :param is_case_sensitive: The is_case_sensitive of this MappingRule.  # noqa: E501
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
        if not isinstance(other, MappingRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MappingRule):
            return True

        return self.to_dict() != other.to_dict()
