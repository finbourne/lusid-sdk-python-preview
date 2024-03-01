# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.97
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


class CompositeDispersion(object):
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
        'dispersion_calculation': 'float',
        'variance': 'float',
        'first_quartile': 'float',
        'third_quartile': 'float',
        'range': 'float',
        'constituents_in_scope': 'list[ResourceId]',
        'constituents_excluded': 'list[ResourceId]'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'dispersion_calculation': 'dispersionCalculation',
        'variance': 'variance',
        'first_quartile': 'firstQuartile',
        'third_quartile': 'thirdQuartile',
        'range': 'range',
        'constituents_in_scope': 'constituentsInScope',
        'constituents_excluded': 'constituentsExcluded'
    }

    required_map = {
        'effective_at': 'required',
        'dispersion_calculation': 'optional',
        'variance': 'optional',
        'first_quartile': 'optional',
        'third_quartile': 'optional',
        'range': 'optional',
        'constituents_in_scope': 'optional',
        'constituents_excluded': 'optional'
    }

    def __init__(self, effective_at=None, dispersion_calculation=None, variance=None, first_quartile=None, third_quartile=None, range=None, constituents_in_scope=None, constituents_excluded=None, local_vars_configuration=None):  # noqa: E501
        """CompositeDispersion - a model defined in OpenAPI"
        
        :param effective_at:  The date for which dipsersion calculation has been done. This should be 31 Dec for each given year. (required)
        :type effective_at: datetime
        :param dispersion_calculation:  The result for the dispersion calculation on the given effectiveAt.
        :type dispersion_calculation: float
        :param variance:  The variance on the given effectiveAt.
        :type variance: float
        :param first_quartile:  First Quartile (Q1) =  (lower quartile) = the middle of the bottom half of the returns.
        :type first_quartile: float
        :param third_quartile:  Third Quartile (Q3) =  (higher quartile) = the middle of the top half of the returns.
        :type third_quartile: float
        :param range:  Highest return - Lowest return.
        :type range: float
        :param constituents_in_scope:  List containing Composite members which are part of the dispersion calcualtion.
        :type constituents_in_scope: list[lusid.ResourceId]
        :param constituents_excluded:  List containing the Composite members which are not part of the dispersion calculation
        :type constituents_excluded: list[lusid.ResourceId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._dispersion_calculation = None
        self._variance = None
        self._first_quartile = None
        self._third_quartile = None
        self._range = None
        self._constituents_in_scope = None
        self._constituents_excluded = None
        self.discriminator = None

        self.effective_at = effective_at
        self.dispersion_calculation = dispersion_calculation
        self.variance = variance
        self.first_quartile = first_quartile
        self.third_quartile = third_quartile
        self.range = range
        self.constituents_in_scope = constituents_in_scope
        self.constituents_excluded = constituents_excluded

    @property
    def effective_at(self):
        """Gets the effective_at of this CompositeDispersion.  # noqa: E501

        The date for which dipsersion calculation has been done. This should be 31 Dec for each given year.  # noqa: E501

        :return: The effective_at of this CompositeDispersion.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this CompositeDispersion.

        The date for which dipsersion calculation has been done. This should be 31 Dec for each given year.  # noqa: E501

        :param effective_at: The effective_at of this CompositeDispersion.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def dispersion_calculation(self):
        """Gets the dispersion_calculation of this CompositeDispersion.  # noqa: E501

        The result for the dispersion calculation on the given effectiveAt.  # noqa: E501

        :return: The dispersion_calculation of this CompositeDispersion.  # noqa: E501
        :rtype: float
        """
        return self._dispersion_calculation

    @dispersion_calculation.setter
    def dispersion_calculation(self, dispersion_calculation):
        """Sets the dispersion_calculation of this CompositeDispersion.

        The result for the dispersion calculation on the given effectiveAt.  # noqa: E501

        :param dispersion_calculation: The dispersion_calculation of this CompositeDispersion.  # noqa: E501
        :type dispersion_calculation: float
        """

        self._dispersion_calculation = dispersion_calculation

    @property
    def variance(self):
        """Gets the variance of this CompositeDispersion.  # noqa: E501

        The variance on the given effectiveAt.  # noqa: E501

        :return: The variance of this CompositeDispersion.  # noqa: E501
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this CompositeDispersion.

        The variance on the given effectiveAt.  # noqa: E501

        :param variance: The variance of this CompositeDispersion.  # noqa: E501
        :type variance: float
        """

        self._variance = variance

    @property
    def first_quartile(self):
        """Gets the first_quartile of this CompositeDispersion.  # noqa: E501

        First Quartile (Q1) =  (lower quartile) = the middle of the bottom half of the returns.  # noqa: E501

        :return: The first_quartile of this CompositeDispersion.  # noqa: E501
        :rtype: float
        """
        return self._first_quartile

    @first_quartile.setter
    def first_quartile(self, first_quartile):
        """Sets the first_quartile of this CompositeDispersion.

        First Quartile (Q1) =  (lower quartile) = the middle of the bottom half of the returns.  # noqa: E501

        :param first_quartile: The first_quartile of this CompositeDispersion.  # noqa: E501
        :type first_quartile: float
        """

        self._first_quartile = first_quartile

    @property
    def third_quartile(self):
        """Gets the third_quartile of this CompositeDispersion.  # noqa: E501

        Third Quartile (Q3) =  (higher quartile) = the middle of the top half of the returns.  # noqa: E501

        :return: The third_quartile of this CompositeDispersion.  # noqa: E501
        :rtype: float
        """
        return self._third_quartile

    @third_quartile.setter
    def third_quartile(self, third_quartile):
        """Sets the third_quartile of this CompositeDispersion.

        Third Quartile (Q3) =  (higher quartile) = the middle of the top half of the returns.  # noqa: E501

        :param third_quartile: The third_quartile of this CompositeDispersion.  # noqa: E501
        :type third_quartile: float
        """

        self._third_quartile = third_quartile

    @property
    def range(self):
        """Gets the range of this CompositeDispersion.  # noqa: E501

        Highest return - Lowest return.  # noqa: E501

        :return: The range of this CompositeDispersion.  # noqa: E501
        :rtype: float
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this CompositeDispersion.

        Highest return - Lowest return.  # noqa: E501

        :param range: The range of this CompositeDispersion.  # noqa: E501
        :type range: float
        """

        self._range = range

    @property
    def constituents_in_scope(self):
        """Gets the constituents_in_scope of this CompositeDispersion.  # noqa: E501

        List containing Composite members which are part of the dispersion calcualtion.  # noqa: E501

        :return: The constituents_in_scope of this CompositeDispersion.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._constituents_in_scope

    @constituents_in_scope.setter
    def constituents_in_scope(self, constituents_in_scope):
        """Sets the constituents_in_scope of this CompositeDispersion.

        List containing Composite members which are part of the dispersion calcualtion.  # noqa: E501

        :param constituents_in_scope: The constituents_in_scope of this CompositeDispersion.  # noqa: E501
        :type constituents_in_scope: list[lusid.ResourceId]
        """

        self._constituents_in_scope = constituents_in_scope

    @property
    def constituents_excluded(self):
        """Gets the constituents_excluded of this CompositeDispersion.  # noqa: E501

        List containing the Composite members which are not part of the dispersion calculation  # noqa: E501

        :return: The constituents_excluded of this CompositeDispersion.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._constituents_excluded

    @constituents_excluded.setter
    def constituents_excluded(self, constituents_excluded):
        """Sets the constituents_excluded of this CompositeDispersion.

        List containing the Composite members which are not part of the dispersion calculation  # noqa: E501

        :param constituents_excluded: The constituents_excluded of this CompositeDispersion.  # noqa: E501
        :type constituents_excluded: list[lusid.ResourceId]
        """

        self._constituents_excluded = constituents_excluded

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
        if not isinstance(other, CompositeDispersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompositeDispersion):
            return True

        return self.to_dict() != other.to_dict()
