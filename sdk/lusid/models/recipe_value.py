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


class RecipeValue(object):
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
        'as_json': 'str',
        'as_string': 'str',
        'from_recipe': 'FromRecipe'
    }

    attribute_map = {
        'as_json': 'asJson',
        'as_string': 'asString',
        'from_recipe': 'fromRecipe'
    }

    required_map = {
        'as_json': 'optional',
        'as_string': 'optional',
        'from_recipe': 'optional'
    }

    def __init__(self, as_json=None, as_string=None, from_recipe=None, local_vars_configuration=None):  # noqa: E501
        """RecipeValue - a model defined in OpenAPI"
        
        :param as_json:  Field to allow providing a potentially complex json value.
        :type as_json: str
        :param as_string:  For simple value, a single input value, note complex nested objects are not allowed here.
        :type as_string: str
        :param from_recipe: 
        :type from_recipe: lusid.FromRecipe

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_json = None
        self._as_string = None
        self._from_recipe = None
        self.discriminator = None

        self.as_json = as_json
        self.as_string = as_string
        if from_recipe is not None:
            self.from_recipe = from_recipe

    @property
    def as_json(self):
        """Gets the as_json of this RecipeValue.  # noqa: E501

        Field to allow providing a potentially complex json value.  # noqa: E501

        :return: The as_json of this RecipeValue.  # noqa: E501
        :rtype: str
        """
        return self._as_json

    @as_json.setter
    def as_json(self, as_json):
        """Sets the as_json of this RecipeValue.

        Field to allow providing a potentially complex json value.  # noqa: E501

        :param as_json: The as_json of this RecipeValue.  # noqa: E501
        :type as_json: str
        """

        self._as_json = as_json

    @property
    def as_string(self):
        """Gets the as_string of this RecipeValue.  # noqa: E501

        For simple value, a single input value, note complex nested objects are not allowed here.  # noqa: E501

        :return: The as_string of this RecipeValue.  # noqa: E501
        :rtype: str
        """
        return self._as_string

    @as_string.setter
    def as_string(self, as_string):
        """Sets the as_string of this RecipeValue.

        For simple value, a single input value, note complex nested objects are not allowed here.  # noqa: E501

        :param as_string: The as_string of this RecipeValue.  # noqa: E501
        :type as_string: str
        """

        self._as_string = as_string

    @property
    def from_recipe(self):
        """Gets the from_recipe of this RecipeValue.  # noqa: E501


        :return: The from_recipe of this RecipeValue.  # noqa: E501
        :rtype: lusid.FromRecipe
        """
        return self._from_recipe

    @from_recipe.setter
    def from_recipe(self, from_recipe):
        """Sets the from_recipe of this RecipeValue.


        :param from_recipe: The from_recipe of this RecipeValue.  # noqa: E501
        :type from_recipe: lusid.FromRecipe
        """

        self._from_recipe = from_recipe

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
        if not isinstance(other, RecipeValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipeValue):
            return True

        return self.to_dict() != other.to_dict()
