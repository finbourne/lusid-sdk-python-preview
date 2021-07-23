# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3305
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PackageRequest(object):
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
        'id': 'ResourceId',
        'order_ids': 'list[ResourceId]',
        'order_instruction_ids': 'list[ResourceId]',
        'properties': 'dict(str, PerpetualProperty)'
    }

    attribute_map = {
        'id': 'id',
        'order_ids': 'orderIds',
        'order_instruction_ids': 'orderInstructionIds',
        'properties': 'properties'
    }

    required_map = {
        'id': 'required',
        'order_ids': 'required',
        'order_instruction_ids': 'required',
        'properties': 'optional'
    }

    def __init__(self, id=None, order_ids=None, order_instruction_ids=None, properties=None):  # noqa: E501
        """
        PackageRequest - a model defined in OpenAPI

        :param id:  (required)
        :type id: lusid.ResourceId
        :param order_ids:  A related order ids. (required)
        :type order_ids: list[lusid.ResourceId]
        :param order_instruction_ids:  A related order instruction id. (required)
        :type order_instruction_ids: list[lusid.ResourceId]
        :param properties:  Client-defined properties associated with this execution.
        :type properties: dict[str, lusid.PerpetualProperty]

        """  # noqa: E501

        self._id = None
        self._order_ids = None
        self._order_instruction_ids = None
        self._properties = None
        self.discriminator = None

        self.id = id
        self.order_ids = order_ids
        self.order_instruction_ids = order_instruction_ids
        self.properties = properties

    @property
    def id(self):
        """Gets the id of this PackageRequest.  # noqa: E501


        :return: The id of this PackageRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageRequest.


        :param id: The id of this PackageRequest.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def order_ids(self):
        """Gets the order_ids of this PackageRequest.  # noqa: E501

        A related order ids.  # noqa: E501

        :return: The order_ids of this PackageRequest.  # noqa: E501
        :rtype: list[ResourceId]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this PackageRequest.

        A related order ids.  # noqa: E501

        :param order_ids: The order_ids of this PackageRequest.  # noqa: E501
        :type: list[ResourceId]
        """
        if order_ids is None:
            raise ValueError("Invalid value for `order_ids`, must not be `None`")  # noqa: E501

        self._order_ids = order_ids

    @property
    def order_instruction_ids(self):
        """Gets the order_instruction_ids of this PackageRequest.  # noqa: E501

        A related order instruction id.  # noqa: E501

        :return: The order_instruction_ids of this PackageRequest.  # noqa: E501
        :rtype: list[ResourceId]
        """
        return self._order_instruction_ids

    @order_instruction_ids.setter
    def order_instruction_ids(self, order_instruction_ids):
        """Sets the order_instruction_ids of this PackageRequest.

        A related order instruction id.  # noqa: E501

        :param order_instruction_ids: The order_instruction_ids of this PackageRequest.  # noqa: E501
        :type: list[ResourceId]
        """
        if order_instruction_ids is None:
            raise ValueError("Invalid value for `order_instruction_ids`, must not be `None`")  # noqa: E501

        self._order_instruction_ids = order_instruction_ids

    @property
    def properties(self):
        """Gets the properties of this PackageRequest.  # noqa: E501

        Client-defined properties associated with this execution.  # noqa: E501

        :return: The properties of this PackageRequest.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PackageRequest.

        Client-defined properties associated with this execution.  # noqa: E501

        :param properties: The properties of this PackageRequest.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

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
        if not isinstance(other, PackageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
