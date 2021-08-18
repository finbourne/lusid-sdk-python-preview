# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3401
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class SetPersonIdentifiersRequest(object):
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
        'identifiers': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'identifiers': 'identifiers'
    }

    required_map = {
        'identifiers': 'optional'
    }

    def __init__(self, identifiers=None):  # noqa: E501
        """
        SetPersonIdentifiersRequest - a model defined in OpenAPI

        :param identifiers:  Identifiers to set for a Person. Identifiers not included in the request will not be amended.
        :type identifiers: dict[str, lusid.ModelProperty]

        """  # noqa: E501

        self._identifiers = None
        self.discriminator = None

        self.identifiers = identifiers

    @property
    def identifiers(self):
        """Gets the identifiers of this SetPersonIdentifiersRequest.  # noqa: E501

        Identifiers to set for a Person. Identifiers not included in the request will not be amended.  # noqa: E501

        :return: The identifiers of this SetPersonIdentifiersRequest.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this SetPersonIdentifiersRequest.

        Identifiers to set for a Person. Identifiers not included in the request will not be amended.  # noqa: E501

        :param identifiers: The identifiers of this SetPersonIdentifiersRequest.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._identifiers = identifiers

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
        if not isinstance(other, SetPersonIdentifiersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
