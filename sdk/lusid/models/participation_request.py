# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3251
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ParticipationRequest(object):
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
        'placement_id': 'ResourceId',
        'order_id': 'ResourceId',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'placement_id': 'placementId',
        'order_id': 'orderId',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'placement_id': 'required',
        'order_id': 'required',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, placement_id=None, order_id=None, version=None, links=None):  # noqa: E501
        """
        ParticipationRequest - a model defined in OpenAPI

        :param id:  (required)
        :type id: lusid.ResourceId
        :param placement_id:  (required)
        :type placement_id: lusid.ResourceId
        :param order_id:  (required)
        :type order_id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._id = None
        self._placement_id = None
        self._order_id = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.placement_id = placement_id
        self.order_id = order_id
        if version is not None:
            self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this ParticipationRequest.  # noqa: E501


        :return: The id of this ParticipationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParticipationRequest.


        :param id: The id of this ParticipationRequest.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def placement_id(self):
        """Gets the placement_id of this ParticipationRequest.  # noqa: E501


        :return: The placement_id of this ParticipationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._placement_id

    @placement_id.setter
    def placement_id(self, placement_id):
        """Sets the placement_id of this ParticipationRequest.


        :param placement_id: The placement_id of this ParticipationRequest.  # noqa: E501
        :type: ResourceId
        """
        if placement_id is None:
            raise ValueError("Invalid value for `placement_id`, must not be `None`")  # noqa: E501

        self._placement_id = placement_id

    @property
    def order_id(self):
        """Gets the order_id of this ParticipationRequest.  # noqa: E501


        :return: The order_id of this ParticipationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ParticipationRequest.


        :param order_id: The order_id of this ParticipationRequest.  # noqa: E501
        :type: ResourceId
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def version(self):
        """Gets the version of this ParticipationRequest.  # noqa: E501


        :return: The version of this ParticipationRequest.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ParticipationRequest.


        :param version: The version of this ParticipationRequest.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this ParticipationRequest.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this ParticipationRequest.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ParticipationRequest.

        Collection of links.  # noqa: E501

        :param links: The links of this ParticipationRequest.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, ParticipationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
