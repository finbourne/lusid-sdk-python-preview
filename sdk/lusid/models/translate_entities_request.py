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


class TranslateEntitiesRequest(object):
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
        'entity_payloads': 'dict(str, TranslationInput)',
        'script_id': 'TranslationScriptId',
        'dialect_id': 'DialectId'
    }

    attribute_map = {
        'entity_payloads': 'entityPayloads',
        'script_id': 'scriptId',
        'dialect_id': 'dialectId'
    }

    required_map = {
        'entity_payloads': 'required',
        'script_id': 'required',
        'dialect_id': 'optional'
    }

    def __init__(self, entity_payloads=None, script_id=None, dialect_id=None, local_vars_configuration=None):  # noqa: E501
        """TranslateEntitiesRequest - a model defined in OpenAPI"
        
        :param entity_payloads:  Entity payloads to be translated, indexed by (ephemeral) unique correlation ids. (required)
        :type entity_payloads: dict[str, lusid.TranslationInput]
        :param script_id:  (required)
        :type script_id: lusid.TranslationScriptId
        :param dialect_id: 
        :type dialect_id: lusid.DialectId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity_payloads = None
        self._script_id = None
        self._dialect_id = None
        self.discriminator = None

        self.entity_payloads = entity_payloads
        self.script_id = script_id
        if dialect_id is not None:
            self.dialect_id = dialect_id

    @property
    def entity_payloads(self):
        """Gets the entity_payloads of this TranslateEntitiesRequest.  # noqa: E501

        Entity payloads to be translated, indexed by (ephemeral) unique correlation ids.  # noqa: E501

        :return: The entity_payloads of this TranslateEntitiesRequest.  # noqa: E501
        :rtype: dict[str, lusid.TranslationInput]
        """
        return self._entity_payloads

    @entity_payloads.setter
    def entity_payloads(self, entity_payloads):
        """Sets the entity_payloads of this TranslateEntitiesRequest.

        Entity payloads to be translated, indexed by (ephemeral) unique correlation ids.  # noqa: E501

        :param entity_payloads: The entity_payloads of this TranslateEntitiesRequest.  # noqa: E501
        :type entity_payloads: dict[str, lusid.TranslationInput]
        """
        if self.local_vars_configuration.client_side_validation and entity_payloads is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_payloads`, must not be `None`")  # noqa: E501

        self._entity_payloads = entity_payloads

    @property
    def script_id(self):
        """Gets the script_id of this TranslateEntitiesRequest.  # noqa: E501


        :return: The script_id of this TranslateEntitiesRequest.  # noqa: E501
        :rtype: lusid.TranslationScriptId
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this TranslateEntitiesRequest.


        :param script_id: The script_id of this TranslateEntitiesRequest.  # noqa: E501
        :type script_id: lusid.TranslationScriptId
        """
        if self.local_vars_configuration.client_side_validation and script_id is None:  # noqa: E501
            raise ValueError("Invalid value for `script_id`, must not be `None`")  # noqa: E501

        self._script_id = script_id

    @property
    def dialect_id(self):
        """Gets the dialect_id of this TranslateEntitiesRequest.  # noqa: E501


        :return: The dialect_id of this TranslateEntitiesRequest.  # noqa: E501
        :rtype: lusid.DialectId
        """
        return self._dialect_id

    @dialect_id.setter
    def dialect_id(self, dialect_id):
        """Sets the dialect_id of this TranslateEntitiesRequest.


        :param dialect_id: The dialect_id of this TranslateEntitiesRequest.  # noqa: E501
        :type dialect_id: lusid.DialectId
        """

        self._dialect_id = dialect_id

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
        if not isinstance(other, TranslateEntitiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateEntitiesRequest):
            return True

        return self.to_dict() != other.to_dict()
