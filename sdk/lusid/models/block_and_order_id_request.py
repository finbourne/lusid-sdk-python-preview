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


class BlockAndOrderIdRequest(object):
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
        'destination_block_id': 'ResourceId',
        'order_id': 'ResourceId'
    }

    attribute_map = {
        'destination_block_id': 'destinationBlockId',
        'order_id': 'orderId'
    }

    required_map = {
        'destination_block_id': 'required',
        'order_id': 'required'
    }

    def __init__(self, destination_block_id=None, order_id=None, local_vars_configuration=None):  # noqa: E501
        """BlockAndOrderIdRequest - a model defined in OpenAPI"
        
        :param destination_block_id:  (required)
        :type destination_block_id: lusid.ResourceId
        :param order_id:  (required)
        :type order_id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._destination_block_id = None
        self._order_id = None
        self.discriminator = None

        self.destination_block_id = destination_block_id
        self.order_id = order_id

    @property
    def destination_block_id(self):
        """Gets the destination_block_id of this BlockAndOrderIdRequest.  # noqa: E501


        :return: The destination_block_id of this BlockAndOrderIdRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._destination_block_id

    @destination_block_id.setter
    def destination_block_id(self, destination_block_id):
        """Sets the destination_block_id of this BlockAndOrderIdRequest.


        :param destination_block_id: The destination_block_id of this BlockAndOrderIdRequest.  # noqa: E501
        :type destination_block_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and destination_block_id is None:  # noqa: E501
            raise ValueError("Invalid value for `destination_block_id`, must not be `None`")  # noqa: E501

        self._destination_block_id = destination_block_id

    @property
    def order_id(self):
        """Gets the order_id of this BlockAndOrderIdRequest.  # noqa: E501


        :return: The order_id of this BlockAndOrderIdRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BlockAndOrderIdRequest.


        :param order_id: The order_id of this BlockAndOrderIdRequest.  # noqa: E501
        :type order_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if not isinstance(other, BlockAndOrderIdRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockAndOrderIdRequest):
            return True

        return self.to_dict() != other.to_dict()
