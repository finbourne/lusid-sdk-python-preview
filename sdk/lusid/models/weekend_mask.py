# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3049
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class WeekendMask(object):
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
        'days': 'list[DayOfWeek]',
        'time_zone': 'str'
    }

    attribute_map = {
        'days': 'days',
        'time_zone': 'timeZone'
    }

    required_map = {
        'days': 'required',
        'time_zone': 'required'
    }

    def __init__(self, days=None, time_zone=None):  # noqa: E501
        """
        WeekendMask - a model defined in OpenAPI

        :param days:  (required)
        :type days: list[lusid.DayOfWeek]
        :param time_zone:  (required)
        :type time_zone: str

        """  # noqa: E501

        self._days = None
        self._time_zone = None
        self.discriminator = None

        self.days = days
        self.time_zone = time_zone

    @property
    def days(self):
        """Gets the days of this WeekendMask.  # noqa: E501


        :return: The days of this WeekendMask.  # noqa: E501
        :rtype: list[DayOfWeek]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this WeekendMask.


        :param days: The days of this WeekendMask.  # noqa: E501
        :type: list[DayOfWeek]
        """
        if days is None:
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def time_zone(self):
        """Gets the time_zone of this WeekendMask.  # noqa: E501


        :return: The time_zone of this WeekendMask.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this WeekendMask.


        :param time_zone: The time_zone of this WeekendMask.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501
        if time_zone is not None and len(time_zone) > 256:
            raise ValueError("Invalid value for `time_zone`, length must be less than or equal to `256`")  # noqa: E501
        if time_zone is not None and len(time_zone) < 1:
            raise ValueError("Invalid value for `time_zone`, length must be greater than or equal to `1`")  # noqa: E501
        if (time_zone is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', time_zone)):  # noqa: E501
            raise ValueError(r"Invalid value for `time_zone`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._time_zone = time_zone

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
        if not isinstance(other, WeekendMask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
