# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.148
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


class PeriodDiaryEntriesReopenedResponse(object):
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
        'href': 'str',
        'effective_from': 'datetime',
        'as_at': 'datetime',
        'period_diary_entries_removed': 'int',
        'period_diary_entries_from': 'datetime',
        'period_diary_entries_to': 'datetime',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'effective_from': 'effectiveFrom',
        'as_at': 'asAt',
        'period_diary_entries_removed': 'periodDiaryEntriesRemoved',
        'period_diary_entries_from': 'periodDiaryEntriesFrom',
        'period_diary_entries_to': 'periodDiaryEntriesTo',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'effective_from': 'optional',
        'as_at': 'required',
        'period_diary_entries_removed': 'required',
        'period_diary_entries_from': 'required',
        'period_diary_entries_to': 'required',
        'links': 'optional'
    }

    def __init__(self, href=None, effective_from=None, as_at=None, period_diary_entries_removed=None, period_diary_entries_from=None, period_diary_entries_to=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PeriodDiaryEntriesReopenedResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param effective_from:  The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.
        :type effective_from: datetime
        :param as_at:  The asAt datetime at which the deletion was committed to LUSID. (required)
        :type as_at: datetime
        :param period_diary_entries_removed:  Number of Diary Entries removed as a result of reopening periods (required)
        :type period_diary_entries_removed: int
        :param period_diary_entries_from:  The start point where periods were removed from (required)
        :type period_diary_entries_from: datetime
        :param period_diary_entries_to:  The end point where periods were removed to (required)
        :type period_diary_entries_to: datetime
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._effective_from = None
        self._as_at = None
        self._period_diary_entries_removed = None
        self._period_diary_entries_from = None
        self._period_diary_entries_to = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.effective_from = effective_from
        self.as_at = as_at
        self.period_diary_entries_removed = period_diary_entries_removed
        self.period_diary_entries_from = period_diary_entries_from
        self.period_diary_entries_to = period_diary_entries_to
        self.links = links

    @property
    def href(self):
        """Gets the href of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PeriodDiaryEntriesReopenedResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def effective_from(self):
        """Gets the effective_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.  # noqa: E501

        :return: The effective_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this PeriodDiaryEntriesReopenedResponse.

        The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.  # noqa: E501

        :param effective_from: The effective_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type effective_from: datetime
        """

        self._effective_from = effective_from

    @property
    def as_at(self):
        """Gets the as_at of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        The asAt datetime at which the deletion was committed to LUSID.  # noqa: E501

        :return: The as_at of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this PeriodDiaryEntriesReopenedResponse.

        The asAt datetime at which the deletion was committed to LUSID.  # noqa: E501

        :param as_at: The as_at of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type as_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and as_at is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at`, must not be `None`")  # noqa: E501

        self._as_at = as_at

    @property
    def period_diary_entries_removed(self):
        """Gets the period_diary_entries_removed of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        Number of Diary Entries removed as a result of reopening periods  # noqa: E501

        :return: The period_diary_entries_removed of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: int
        """
        return self._period_diary_entries_removed

    @period_diary_entries_removed.setter
    def period_diary_entries_removed(self, period_diary_entries_removed):
        """Sets the period_diary_entries_removed of this PeriodDiaryEntriesReopenedResponse.

        Number of Diary Entries removed as a result of reopening periods  # noqa: E501

        :param period_diary_entries_removed: The period_diary_entries_removed of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type period_diary_entries_removed: int
        """
        if self.local_vars_configuration.client_side_validation and period_diary_entries_removed is None:  # noqa: E501
            raise ValueError("Invalid value for `period_diary_entries_removed`, must not be `None`")  # noqa: E501

        self._period_diary_entries_removed = period_diary_entries_removed

    @property
    def period_diary_entries_from(self):
        """Gets the period_diary_entries_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        The start point where periods were removed from  # noqa: E501

        :return: The period_diary_entries_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._period_diary_entries_from

    @period_diary_entries_from.setter
    def period_diary_entries_from(self, period_diary_entries_from):
        """Sets the period_diary_entries_from of this PeriodDiaryEntriesReopenedResponse.

        The start point where periods were removed from  # noqa: E501

        :param period_diary_entries_from: The period_diary_entries_from of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type period_diary_entries_from: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_diary_entries_from is None:  # noqa: E501
            raise ValueError("Invalid value for `period_diary_entries_from`, must not be `None`")  # noqa: E501

        self._period_diary_entries_from = period_diary_entries_from

    @property
    def period_diary_entries_to(self):
        """Gets the period_diary_entries_to of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        The end point where periods were removed to  # noqa: E501

        :return: The period_diary_entries_to of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._period_diary_entries_to

    @period_diary_entries_to.setter
    def period_diary_entries_to(self, period_diary_entries_to):
        """Sets the period_diary_entries_to of this PeriodDiaryEntriesReopenedResponse.

        The end point where periods were removed to  # noqa: E501

        :param period_diary_entries_to: The period_diary_entries_to of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type period_diary_entries_to: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_diary_entries_to is None:  # noqa: E501
            raise ValueError("Invalid value for `period_diary_entries_to`, must not be `None`")  # noqa: E501

        self._period_diary_entries_to = period_diary_entries_to

    @property
    def links(self):
        """Gets the links of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PeriodDiaryEntriesReopenedResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this PeriodDiaryEntriesReopenedResponse.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, PeriodDiaryEntriesReopenedResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PeriodDiaryEntriesReopenedResponse):
            return True

        return self.to_dict() != other.to_dict()
