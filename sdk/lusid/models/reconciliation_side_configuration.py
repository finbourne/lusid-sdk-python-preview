# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.224
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


class ReconciliationSideConfiguration(object):
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
        'recipe_id': 'ResourceId',
        'effective_at': 'datetime',
        'as_at': 'datetime',
        'currency': 'str'
    }

    attribute_map = {
        'recipe_id': 'recipeId',
        'effective_at': 'effectiveAt',
        'as_at': 'asAt',
        'currency': 'currency'
    }

    required_map = {
        'recipe_id': 'optional',
        'effective_at': 'optional',
        'as_at': 'optional',
        'currency': 'optional'
    }

    def __init__(self, recipe_id=None, effective_at=None, as_at=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationSideConfiguration - a model defined in OpenAPI"
        
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param effective_at: 
        :type effective_at: datetime
        :param as_at: 
        :type as_at: datetime
        :param currency: 
        :type currency: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._recipe_id = None
        self._effective_at = None
        self._as_at = None
        self._currency = None
        self.discriminator = None

        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.effective_at = effective_at
        self.as_at = as_at
        self.currency = currency

    @property
    def recipe_id(self):
        """Gets the recipe_id of this ReconciliationSideConfiguration.  # noqa: E501


        :return: The recipe_id of this ReconciliationSideConfiguration.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this ReconciliationSideConfiguration.


        :param recipe_id: The recipe_id of this ReconciliationSideConfiguration.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def effective_at(self):
        """Gets the effective_at of this ReconciliationSideConfiguration.  # noqa: E501


        :return: The effective_at of this ReconciliationSideConfiguration.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this ReconciliationSideConfiguration.


        :param effective_at: The effective_at of this ReconciliationSideConfiguration.  # noqa: E501
        :type effective_at: datetime
        """

        self._effective_at = effective_at

    @property
    def as_at(self):
        """Gets the as_at of this ReconciliationSideConfiguration.  # noqa: E501


        :return: The as_at of this ReconciliationSideConfiguration.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this ReconciliationSideConfiguration.


        :param as_at: The as_at of this ReconciliationSideConfiguration.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def currency(self):
        """Gets the currency of this ReconciliationSideConfiguration.  # noqa: E501


        :return: The currency of this ReconciliationSideConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ReconciliationSideConfiguration.


        :param currency: The currency of this ReconciliationSideConfiguration.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

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
        if not isinstance(other, ReconciliationSideConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationSideConfiguration):
            return True

        return self.to_dict() != other.to_dict()
