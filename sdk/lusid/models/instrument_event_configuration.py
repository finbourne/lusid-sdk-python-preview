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


class InstrumentEventConfiguration(object):
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
        'transaction_template_scopes': 'list[str]',
        'recipe_id': 'ResourceId'
    }

    attribute_map = {
        'transaction_template_scopes': 'transactionTemplateScopes',
        'recipe_id': 'recipeId'
    }

    required_map = {
        'transaction_template_scopes': 'optional',
        'recipe_id': 'optional'
    }

    def __init__(self, transaction_template_scopes=None, recipe_id=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentEventConfiguration - a model defined in OpenAPI"
        
        :param transaction_template_scopes: 
        :type transaction_template_scopes: list[str]
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_template_scopes = None
        self._recipe_id = None
        self.discriminator = None

        self.transaction_template_scopes = transaction_template_scopes
        if recipe_id is not None:
            self.recipe_id = recipe_id

    @property
    def transaction_template_scopes(self):
        """Gets the transaction_template_scopes of this InstrumentEventConfiguration.  # noqa: E501


        :return: The transaction_template_scopes of this InstrumentEventConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._transaction_template_scopes

    @transaction_template_scopes.setter
    def transaction_template_scopes(self, transaction_template_scopes):
        """Sets the transaction_template_scopes of this InstrumentEventConfiguration.


        :param transaction_template_scopes: The transaction_template_scopes of this InstrumentEventConfiguration.  # noqa: E501
        :type transaction_template_scopes: list[str]
        """

        self._transaction_template_scopes = transaction_template_scopes

    @property
    def recipe_id(self):
        """Gets the recipe_id of this InstrumentEventConfiguration.  # noqa: E501


        :return: The recipe_id of this InstrumentEventConfiguration.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this InstrumentEventConfiguration.


        :param recipe_id: The recipe_id of this InstrumentEventConfiguration.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

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
        if not isinstance(other, InstrumentEventConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentEventConfiguration):
            return True

        return self.to_dict() != other.to_dict()
