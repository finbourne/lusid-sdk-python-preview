# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3220
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionConfigurationTypeAlias(object):
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
        'type': 'str',
        'description': 'str',
        'transaction_class': 'str',
        'transaction_group': 'str',
        'transaction_roles': 'str'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'transaction_class': 'transactionClass',
        'transaction_group': 'transactionGroup',
        'transaction_roles': 'transactionRoles'
    }

    required_map = {
        'type': 'required',
        'description': 'required',
        'transaction_class': 'required',
        'transaction_group': 'required',
        'transaction_roles': 'required'
    }

    def __init__(self, type=None, description=None, transaction_class=None, transaction_group=None, transaction_roles=None):  # noqa: E501
        """
        TransactionConfigurationTypeAlias - a model defined in OpenAPI

        :param type:  The transaction type (required)
        :type type: str
        :param description:  Brief description of the transaction (required)
        :type description: str
        :param transaction_class:  Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut (required)
        :type transaction_class: str
        :param transaction_group:  Group is a set of codes related to a source, or sync (required)
        :type transaction_group: str
        :param transaction_roles:  . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles (required)
        :type transaction_roles: str

        """  # noqa: E501

        self._type = None
        self._description = None
        self._transaction_class = None
        self._transaction_group = None
        self._transaction_roles = None
        self.discriminator = None

        self.type = type
        self.description = description
        self.transaction_class = transaction_class
        self.transaction_group = transaction_group
        self.transaction_roles = transaction_roles

    @property
    def type(self):
        """Gets the type of this TransactionConfigurationTypeAlias.  # noqa: E501

        The transaction type  # noqa: E501

        :return: The type of this TransactionConfigurationTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionConfigurationTypeAlias.

        The transaction type  # noqa: E501

        :param type: The type of this TransactionConfigurationTypeAlias.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this TransactionConfigurationTypeAlias.  # noqa: E501

        Brief description of the transaction  # noqa: E501

        :return: The description of this TransactionConfigurationTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionConfigurationTypeAlias.

        Brief description of the transaction  # noqa: E501

        :param description: The description of this TransactionConfigurationTypeAlias.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def transaction_class(self):
        """Gets the transaction_class of this TransactionConfigurationTypeAlias.  # noqa: E501

        Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut  # noqa: E501

        :return: The transaction_class of this TransactionConfigurationTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._transaction_class

    @transaction_class.setter
    def transaction_class(self, transaction_class):
        """Sets the transaction_class of this TransactionConfigurationTypeAlias.

        Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut  # noqa: E501

        :param transaction_class: The transaction_class of this TransactionConfigurationTypeAlias.  # noqa: E501
        :type: str
        """
        if transaction_class is None:
            raise ValueError("Invalid value for `transaction_class`, must not be `None`")  # noqa: E501

        self._transaction_class = transaction_class

    @property
    def transaction_group(self):
        """Gets the transaction_group of this TransactionConfigurationTypeAlias.  # noqa: E501

        Group is a set of codes related to a source, or sync  # noqa: E501

        :return: The transaction_group of this TransactionConfigurationTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._transaction_group

    @transaction_group.setter
    def transaction_group(self, transaction_group):
        """Sets the transaction_group of this TransactionConfigurationTypeAlias.

        Group is a set of codes related to a source, or sync  # noqa: E501

        :param transaction_group: The transaction_group of this TransactionConfigurationTypeAlias.  # noqa: E501
        :type: str
        """
        if transaction_group is None:
            raise ValueError("Invalid value for `transaction_group`, must not be `None`")  # noqa: E501

        self._transaction_group = transaction_group

    @property
    def transaction_roles(self):
        """Gets the transaction_roles of this TransactionConfigurationTypeAlias.  # noqa: E501

        . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles  # noqa: E501

        :return: The transaction_roles of this TransactionConfigurationTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._transaction_roles

    @transaction_roles.setter
    def transaction_roles(self, transaction_roles):
        """Sets the transaction_roles of this TransactionConfigurationTypeAlias.

        . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles  # noqa: E501

        :param transaction_roles: The transaction_roles of this TransactionConfigurationTypeAlias.  # noqa: E501
        :type: str
        """
        if transaction_roles is None:
            raise ValueError("Invalid value for `transaction_roles`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "LongLonger", "LongShorter", "ShortShorter", "Shorter", "ShortLonger", "Longer", "AllRoles"]  # noqa: E501
        if transaction_roles not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_roles` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_roles, allowed_values)
            )

        self._transaction_roles = transaction_roles

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
        if not isinstance(other, TransactionConfigurationTypeAlias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
