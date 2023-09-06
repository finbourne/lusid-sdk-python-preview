# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.484
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


class CompositeBreakdown(object):
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
        'effective_at': 'datetime',
        'composite': 'PortfolioReturnBreakdown',
        'constituents': 'list[PortfolioReturnBreakdown]'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'composite': 'composite',
        'constituents': 'constituents'
    }

    required_map = {
        'effective_at': 'required',
        'composite': 'optional',
        'constituents': 'optional'
    }

    def __init__(self, effective_at=None, composite=None, constituents=None, local_vars_configuration=None):  # noqa: E501
        """CompositeBreakdown - a model defined in OpenAPI"
        
        :param effective_at:  The effectiveAt for the calculation. (required)
        :type effective_at: datetime
        :param composite: 
        :type composite: lusid.PortfolioReturnBreakdown
        :param constituents:  The constituents with their information which are part of the composite.
        :type constituents: list[lusid.PortfolioReturnBreakdown]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._composite = None
        self._constituents = None
        self.discriminator = None

        self.effective_at = effective_at
        if composite is not None:
            self.composite = composite
        self.constituents = constituents

    @property
    def effective_at(self):
        """Gets the effective_at of this CompositeBreakdown.  # noqa: E501

        The effectiveAt for the calculation.  # noqa: E501

        :return: The effective_at of this CompositeBreakdown.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this CompositeBreakdown.

        The effectiveAt for the calculation.  # noqa: E501

        :param effective_at: The effective_at of this CompositeBreakdown.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def composite(self):
        """Gets the composite of this CompositeBreakdown.  # noqa: E501


        :return: The composite of this CompositeBreakdown.  # noqa: E501
        :rtype: lusid.PortfolioReturnBreakdown
        """
        return self._composite

    @composite.setter
    def composite(self, composite):
        """Sets the composite of this CompositeBreakdown.


        :param composite: The composite of this CompositeBreakdown.  # noqa: E501
        :type composite: lusid.PortfolioReturnBreakdown
        """

        self._composite = composite

    @property
    def constituents(self):
        """Gets the constituents of this CompositeBreakdown.  # noqa: E501

        The constituents with their information which are part of the composite.  # noqa: E501

        :return: The constituents of this CompositeBreakdown.  # noqa: E501
        :rtype: list[lusid.PortfolioReturnBreakdown]
        """
        return self._constituents

    @constituents.setter
    def constituents(self, constituents):
        """Sets the constituents of this CompositeBreakdown.

        The constituents with their information which are part of the composite.  # noqa: E501

        :param constituents: The constituents of this CompositeBreakdown.  # noqa: E501
        :type constituents: list[lusid.PortfolioReturnBreakdown]
        """

        self._constituents = constituents

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
        if not isinstance(other, CompositeBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompositeBreakdown):
            return True

        return self.to_dict() != other.to_dict()
