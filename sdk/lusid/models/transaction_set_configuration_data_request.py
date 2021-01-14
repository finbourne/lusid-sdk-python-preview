# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2470
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionSetConfigurationDataRequest(object):
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
        'transaction_config_requests': 'list[TransactionConfigurationDataRequest]',
        'side_config_requests': 'list[SideConfigurationDataRequest]'
    }

    attribute_map = {
        'transaction_config_requests': 'transactionConfigRequests',
        'side_config_requests': 'sideConfigRequests'
    }

    required_map = {
        'transaction_config_requests': 'required',
        'side_config_requests': 'optional'
    }

    def __init__(self, transaction_config_requests=None, side_config_requests=None):  # noqa: E501
        """
        TransactionSetConfigurationDataRequest - a model defined in OpenAPI

        :param transaction_config_requests:  Collection of transaction type models (required)
        :type transaction_config_requests: list[lusid.TransactionConfigurationDataRequest]
        :param side_config_requests:  Collection of side definition requests.
        :type side_config_requests: list[lusid.SideConfigurationDataRequest]

        """  # noqa: E501

        self._transaction_config_requests = None
        self._side_config_requests = None
        self.discriminator = None

        self.transaction_config_requests = transaction_config_requests
        self.side_config_requests = side_config_requests

    @property
    def transaction_config_requests(self):
        """Gets the transaction_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501

        Collection of transaction type models  # noqa: E501

        :return: The transaction_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501
        :rtype: list[TransactionConfigurationDataRequest]
        """
        return self._transaction_config_requests

    @transaction_config_requests.setter
    def transaction_config_requests(self, transaction_config_requests):
        """Sets the transaction_config_requests of this TransactionSetConfigurationDataRequest.

        Collection of transaction type models  # noqa: E501

        :param transaction_config_requests: The transaction_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501
        :type: list[TransactionConfigurationDataRequest]
        """
        if transaction_config_requests is None:
            raise ValueError("Invalid value for `transaction_config_requests`, must not be `None`")  # noqa: E501

        self._transaction_config_requests = transaction_config_requests

    @property
    def side_config_requests(self):
        """Gets the side_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501

        Collection of side definition requests.  # noqa: E501

        :return: The side_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501
        :rtype: list[SideConfigurationDataRequest]
        """
        return self._side_config_requests

    @side_config_requests.setter
    def side_config_requests(self, side_config_requests):
        """Sets the side_config_requests of this TransactionSetConfigurationDataRequest.

        Collection of side definition requests.  # noqa: E501

        :param side_config_requests: The side_config_requests of this TransactionSetConfigurationDataRequest.  # noqa: E501
        :type: list[SideConfigurationDataRequest]
        """

        self._side_config_requests = side_config_requests

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
        if not isinstance(other, TransactionSetConfigurationDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
