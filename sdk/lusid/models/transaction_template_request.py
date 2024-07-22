# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.195
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


class TransactionTemplateRequest(object):
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
        'description': 'str',
        'component_transactions': 'list[ComponentTransaction]'
    }

    attribute_map = {
        'description': 'description',
        'component_transactions': 'componentTransactions'
    }

    required_map = {
        'description': 'required',
        'component_transactions': 'required'
    }

    def __init__(self, description=None, component_transactions=None, local_vars_configuration=None):  # noqa: E501
        """TransactionTemplateRequest - a model defined in OpenAPI"
        
        :param description:  The description of the transaction template. (required)
        :type description: str
        :param component_transactions:  A set of component transactions that relate to the template to be created. (required)
        :type component_transactions: list[lusid.ComponentTransaction]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._component_transactions = None
        self.discriminator = None

        self.description = description
        self.component_transactions = component_transactions

    @property
    def description(self):
        """Gets the description of this TransactionTemplateRequest.  # noqa: E501

        The description of the transaction template.  # noqa: E501

        :return: The description of this TransactionTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionTemplateRequest.

        The description of the transaction template.  # noqa: E501

        :param description: The description of this TransactionTemplateRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def component_transactions(self):
        """Gets the component_transactions of this TransactionTemplateRequest.  # noqa: E501

        A set of component transactions that relate to the template to be created.  # noqa: E501

        :return: The component_transactions of this TransactionTemplateRequest.  # noqa: E501
        :rtype: list[lusid.ComponentTransaction]
        """
        return self._component_transactions

    @component_transactions.setter
    def component_transactions(self, component_transactions):
        """Sets the component_transactions of this TransactionTemplateRequest.

        A set of component transactions that relate to the template to be created.  # noqa: E501

        :param component_transactions: The component_transactions of this TransactionTemplateRequest.  # noqa: E501
        :type component_transactions: list[lusid.ComponentTransaction]
        """
        if self.local_vars_configuration.client_side_validation and component_transactions is None:  # noqa: E501
            raise ValueError("Invalid value for `component_transactions`, must not be `None`")  # noqa: E501

        self._component_transactions = component_transactions

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
        if not isinstance(other, TransactionTemplateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionTemplateRequest):
            return True

        return self.to_dict() != other.to_dict()
