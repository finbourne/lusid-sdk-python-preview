# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.105
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


class DateOrDiaryEntry(object):
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
        'date': 'str',
        'diary_entry': 'str'
    }

    attribute_map = {
        'date': 'date',
        'diary_entry': 'diaryEntry'
    }

    required_map = {
        'date': 'optional',
        'diary_entry': 'optional'
    }

    def __init__(self, date=None, diary_entry=None, local_vars_configuration=None):  # noqa: E501
        """DateOrDiaryEntry - a model defined in OpenAPI"
        
        :param date:  A date. If specified, DiaryEntry must not be specified.
        :type date: str
        :param diary_entry:  The code of a diary entry. If specified, Date must not be specified.
        :type diary_entry: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._diary_entry = None
        self.discriminator = None

        self.date = date
        self.diary_entry = diary_entry

    @property
    def date(self):
        """Gets the date of this DateOrDiaryEntry.  # noqa: E501

        A date. If specified, DiaryEntry must not be specified.  # noqa: E501

        :return: The date of this DateOrDiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DateOrDiaryEntry.

        A date. If specified, DiaryEntry must not be specified.  # noqa: E501

        :param date: The date of this DateOrDiaryEntry.  # noqa: E501
        :type date: str
        """

        self._date = date

    @property
    def diary_entry(self):
        """Gets the diary_entry of this DateOrDiaryEntry.  # noqa: E501

        The code of a diary entry. If specified, Date must not be specified.  # noqa: E501

        :return: The diary_entry of this DateOrDiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._diary_entry

    @diary_entry.setter
    def diary_entry(self, diary_entry):
        """Sets the diary_entry of this DateOrDiaryEntry.

        The code of a diary entry. If specified, Date must not be specified.  # noqa: E501

        :param diary_entry: The diary_entry of this DateOrDiaryEntry.  # noqa: E501
        :type diary_entry: str
        """
        if (self.local_vars_configuration.client_side_validation and
                diary_entry is not None and len(diary_entry) > 64):
            raise ValueError("Invalid value for `diary_entry`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diary_entry is not None and len(diary_entry) < 1):
            raise ValueError("Invalid value for `diary_entry`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diary_entry is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', diary_entry)):  # noqa: E501
            raise ValueError(r"Invalid value for `diary_entry`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._diary_entry = diary_entry

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
        if not isinstance(other, DateOrDiaryEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateOrDiaryEntry):
            return True

        return self.to_dict() != other.to_dict()
