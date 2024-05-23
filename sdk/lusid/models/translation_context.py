# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.156
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


class TranslationContext(object):
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
        'disable_scripted_translation': 'bool',
        'script_map': 'ScriptMapReference'
    }

    attribute_map = {
        'disable_scripted_translation': 'disableScriptedTranslation',
        'script_map': 'scriptMap'
    }

    required_map = {
        'disable_scripted_translation': 'optional',
        'script_map': 'optional'
    }

    def __init__(self, disable_scripted_translation=None, script_map=None, local_vars_configuration=None):  # noqa: E501
        """TranslationContext - a model defined in OpenAPI"
        
        :param disable_scripted_translation: 
        :type disable_scripted_translation: bool
        :param script_map: 
        :type script_map: lusid.ScriptMapReference

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._disable_scripted_translation = None
        self._script_map = None
        self.discriminator = None

        if disable_scripted_translation is not None:
            self.disable_scripted_translation = disable_scripted_translation
        if script_map is not None:
            self.script_map = script_map

    @property
    def disable_scripted_translation(self):
        """Gets the disable_scripted_translation of this TranslationContext.  # noqa: E501


        :return: The disable_scripted_translation of this TranslationContext.  # noqa: E501
        :rtype: bool
        """
        return self._disable_scripted_translation

    @disable_scripted_translation.setter
    def disable_scripted_translation(self, disable_scripted_translation):
        """Sets the disable_scripted_translation of this TranslationContext.


        :param disable_scripted_translation: The disable_scripted_translation of this TranslationContext.  # noqa: E501
        :type disable_scripted_translation: bool
        """

        self._disable_scripted_translation = disable_scripted_translation

    @property
    def script_map(self):
        """Gets the script_map of this TranslationContext.  # noqa: E501


        :return: The script_map of this TranslationContext.  # noqa: E501
        :rtype: lusid.ScriptMapReference
        """
        return self._script_map

    @script_map.setter
    def script_map(self, script_map):
        """Sets the script_map of this TranslationContext.


        :param script_map: The script_map of this TranslationContext.  # noqa: E501
        :type script_map: lusid.ScriptMapReference
        """

        self._script_map = script_map

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
        if not isinstance(other, TranslationContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationContext):
            return True

        return self.to_dict() != other.to_dict()
