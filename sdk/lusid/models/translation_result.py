# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.96
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


class TranslationResult(object):
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
        'entity': 'str',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'entity': 'entity',
        'properties': 'properties'
    }

    required_map = {
        'entity': 'required',
        'properties': 'required'
    }

    def __init__(self, entity=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """TranslationResult - a model defined in OpenAPI"
        
        :param entity:  The serialised entity the translation script produced. (required)
        :type entity: str
        :param properties:  Any properties the translation script produced. (required)
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity = None
        self._properties = None
        self.discriminator = None

        self.entity = entity
        self.properties = properties

    @property
    def entity(self):
        """Gets the entity of this TranslationResult.  # noqa: E501

        The serialised entity the translation script produced.  # noqa: E501

        :return: The entity of this TranslationResult.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this TranslationResult.

        The serialised entity the translation script produced.  # noqa: E501

        :param entity: The entity of this TranslationResult.  # noqa: E501
        :type entity: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity is not None and len(entity) < 1):
            raise ValueError("Invalid value for `entity`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity = entity

    @property
    def properties(self):
        """Gets the properties of this TranslationResult.  # noqa: E501

        Any properties the translation script produced.  # noqa: E501

        :return: The properties of this TranslationResult.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TranslationResult.

        Any properties the translation script produced.  # noqa: E501

        :param properties: The properties of this TranslationResult.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, TranslationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationResult):
            return True

        return self.to_dict() != other.to_dict()
