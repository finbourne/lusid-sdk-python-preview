# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.156
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


class StagedModificationsRequestedChangeInterval(object):
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
        'attribute_name': 'str',
        'effective_range': 'StagedModificationEffectiveRange',
        'previous_value': 'object',
        'new_value': 'object',
        'as_at_basis': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'attribute_name': 'attributeName',
        'effective_range': 'effectiveRange',
        'previous_value': 'previousValue',
        'new_value': 'newValue',
        'as_at_basis': 'asAtBasis',
        'links': 'links'
    }

    required_map = {
        'attribute_name': 'optional',
        'effective_range': 'optional',
        'previous_value': 'optional',
        'new_value': 'optional',
        'as_at_basis': 'optional',
        'links': 'optional'
    }

    def __init__(self, attribute_name=None, effective_range=None, previous_value=None, new_value=None, as_at_basis=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StagedModificationsRequestedChangeInterval - a model defined in OpenAPI"
        
        :param attribute_name:  Name of the property the change applies to.
        :type attribute_name: str
        :param effective_range: 
        :type effective_range: lusid.StagedModificationEffectiveRange
        :param previous_value:  The previous value of the attribute before the requested change is applied.
        :type previous_value: object
        :param new_value:  The value of the attribute once the requested change is applied.
        :type new_value: object
        :param as_at_basis:  Whether the change represents the modification when the request was made or the modification as it would be at the latest time.
        :type as_at_basis: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_name = None
        self._effective_range = None
        self._previous_value = None
        self._new_value = None
        self._as_at_basis = None
        self._links = None
        self.discriminator = None

        self.attribute_name = attribute_name
        if effective_range is not None:
            self.effective_range = effective_range
        self.previous_value = previous_value
        self.new_value = new_value
        self.as_at_basis = as_at_basis
        self.links = links

    @property
    def attribute_name(self):
        """Gets the attribute_name of this StagedModificationsRequestedChangeInterval.  # noqa: E501

        Name of the property the change applies to.  # noqa: E501

        :return: The attribute_name of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this StagedModificationsRequestedChangeInterval.

        Name of the property the change applies to.  # noqa: E501

        :param attribute_name: The attribute_name of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :type attribute_name: str
        """

        self._attribute_name = attribute_name

    @property
    def effective_range(self):
        """Gets the effective_range of this StagedModificationsRequestedChangeInterval.  # noqa: E501


        :return: The effective_range of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: lusid.StagedModificationEffectiveRange
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        """Sets the effective_range of this StagedModificationsRequestedChangeInterval.


        :param effective_range: The effective_range of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :type effective_range: lusid.StagedModificationEffectiveRange
        """

        self._effective_range = effective_range

    @property
    def previous_value(self):
        """Gets the previous_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501

        The previous value of the attribute before the requested change is applied.  # noqa: E501

        :return: The previous_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: object
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        """Sets the previous_value of this StagedModificationsRequestedChangeInterval.

        The previous value of the attribute before the requested change is applied.  # noqa: E501

        :param previous_value: The previous_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :type previous_value: object
        """

        self._previous_value = previous_value

    @property
    def new_value(self):
        """Gets the new_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501

        The value of the attribute once the requested change is applied.  # noqa: E501

        :return: The new_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: object
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this StagedModificationsRequestedChangeInterval.

        The value of the attribute once the requested change is applied.  # noqa: E501

        :param new_value: The new_value of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :type new_value: object
        """

        self._new_value = new_value

    @property
    def as_at_basis(self):
        """Gets the as_at_basis of this StagedModificationsRequestedChangeInterval.  # noqa: E501

        Whether the change represents the modification when the request was made or the modification as it would be at the latest time.  # noqa: E501

        :return: The as_at_basis of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: str
        """
        return self._as_at_basis

    @as_at_basis.setter
    def as_at_basis(self, as_at_basis):
        """Sets the as_at_basis of this StagedModificationsRequestedChangeInterval.

        Whether the change represents the modification when the request was made or the modification as it would be at the latest time.  # noqa: E501

        :param as_at_basis: The as_at_basis of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :type as_at_basis: str
        """

        self._as_at_basis = as_at_basis

    @property
    def links(self):
        """Gets the links of this StagedModificationsRequestedChangeInterval.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this StagedModificationsRequestedChangeInterval.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StagedModificationsRequestedChangeInterval.

        Collection of links.  # noqa: E501

        :param links: The links of this StagedModificationsRequestedChangeInterval.  # noqa: E501
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
        if not isinstance(other, StagedModificationsRequestedChangeInterval):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModificationsRequestedChangeInterval):
            return True

        return self.to_dict() != other.to_dict()
