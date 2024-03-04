# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.103
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


class RelativeDateOffset(object):
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
        'days': 'int',
        'business_day_convention': 'str'
    }

    attribute_map = {
        'days': 'days',
        'business_day_convention': 'businessDayConvention'
    }

    required_map = {
        'days': 'required',
        'business_day_convention': 'required'
    }

    def __init__(self, days=None, business_day_convention=None, local_vars_configuration=None):  # noqa: E501
        """RelativeDateOffset - a model defined in OpenAPI"
        
        :param days:  The number of business days to add to the anchor date. (required)
        :type days: int
        :param business_day_convention:  The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. (required)
        :type business_day_convention: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._days = None
        self._business_day_convention = None
        self.discriminator = None

        self.days = days
        self.business_day_convention = business_day_convention

    @property
    def days(self):
        """Gets the days of this RelativeDateOffset.  # noqa: E501

        The number of business days to add to the anchor date.  # noqa: E501

        :return: The days of this RelativeDateOffset.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this RelativeDateOffset.

        The number of business days to add to the anchor date.  # noqa: E501

        :param days: The days of this RelativeDateOffset.  # noqa: E501
        :type days: int
        """
        if self.local_vars_configuration.client_side_validation and days is None:  # noqa: E501
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def business_day_convention(self):
        """Gets the business_day_convention of this RelativeDateOffset.  # noqa: E501

        The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  # noqa: E501

        :return: The business_day_convention of this RelativeDateOffset.  # noqa: E501
        :rtype: str
        """
        return self._business_day_convention

    @business_day_convention.setter
    def business_day_convention(self, business_day_convention):
        """Sets the business_day_convention of this RelativeDateOffset.

        The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  # noqa: E501

        :param business_day_convention: The business_day_convention of this RelativeDateOffset.  # noqa: E501
        :type business_day_convention: str
        """
        if self.local_vars_configuration.client_side_validation and business_day_convention is None:  # noqa: E501
            raise ValueError("Invalid value for `business_day_convention`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                business_day_convention is not None and len(business_day_convention) < 1):
            raise ValueError("Invalid value for `business_day_convention`, length must be greater than or equal to `1`")  # noqa: E501

        self._business_day_convention = business_day_convention

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
        if not isinstance(other, RelativeDateOffset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelativeDateOffset):
            return True

        return self.to_dict() != other.to_dict()
