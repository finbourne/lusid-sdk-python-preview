# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.150
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


class BookTransactionsRequest(object):
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
        'allocation_ids': 'list[ResourceId]',
        'transaction_properties': 'dict(str, PerpetualProperty)'
    }

    attribute_map = {
        'allocation_ids': 'allocationIds',
        'transaction_properties': 'transactionProperties'
    }

    required_map = {
        'allocation_ids': 'required',
        'transaction_properties': 'optional'
    }

    def __init__(self, allocation_ids=None, transaction_properties=None, local_vars_configuration=None):  # noqa: E501
        """BookTransactionsRequest - a model defined in OpenAPI"
        
        :param allocation_ids:  A collection of Allocation IDs (required)
        :type allocation_ids: list[lusid.ResourceId]
        :param transaction_properties:  A collection of properties
        :type transaction_properties: dict[str, lusid.PerpetualProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_ids = None
        self._transaction_properties = None
        self.discriminator = None

        self.allocation_ids = allocation_ids
        self.transaction_properties = transaction_properties

    @property
    def allocation_ids(self):
        """Gets the allocation_ids of this BookTransactionsRequest.  # noqa: E501

        A collection of Allocation IDs  # noqa: E501

        :return: The allocation_ids of this BookTransactionsRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._allocation_ids

    @allocation_ids.setter
    def allocation_ids(self, allocation_ids):
        """Sets the allocation_ids of this BookTransactionsRequest.

        A collection of Allocation IDs  # noqa: E501

        :param allocation_ids: The allocation_ids of this BookTransactionsRequest.  # noqa: E501
        :type allocation_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and allocation_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `allocation_ids`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                allocation_ids is not None and len(allocation_ids) > 5000):
            raise ValueError("Invalid value for `allocation_ids`, number of items must be less than or equal to `5000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                allocation_ids is not None and len(allocation_ids) < 1):
            raise ValueError("Invalid value for `allocation_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allocation_ids = allocation_ids

    @property
    def transaction_properties(self):
        """Gets the transaction_properties of this BookTransactionsRequest.  # noqa: E501

        A collection of properties  # noqa: E501

        :return: The transaction_properties of this BookTransactionsRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._transaction_properties

    @transaction_properties.setter
    def transaction_properties(self, transaction_properties):
        """Sets the transaction_properties of this BookTransactionsRequest.

        A collection of properties  # noqa: E501

        :param transaction_properties: The transaction_properties of this BookTransactionsRequest.  # noqa: E501
        :type transaction_properties: dict[str, lusid.PerpetualProperty]
        """

        self._transaction_properties = transaction_properties

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
        if not isinstance(other, BookTransactionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BookTransactionsRequest):
            return True

        return self.to_dict() != other.to_dict()
