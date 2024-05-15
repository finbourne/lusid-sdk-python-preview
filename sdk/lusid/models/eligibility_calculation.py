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


class EligibilityCalculation(object):
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
        'entitlement_date': 'str',
        'eligible_units': 'str'
    }

    attribute_map = {
        'entitlement_date': 'entitlementDate',
        'eligible_units': 'eligibleUnits'
    }

    required_map = {
        'entitlement_date': 'required',
        'eligible_units': 'required'
    }

    def __init__(self, entitlement_date=None, eligible_units=None, local_vars_configuration=None):  # noqa: E501
        """EligibilityCalculation - a model defined in OpenAPI"
        
        :param entitlement_date:  (required)
        :type entitlement_date: str
        :param eligible_units:  (required)
        :type eligible_units: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entitlement_date = None
        self._eligible_units = None
        self.discriminator = None

        self.entitlement_date = entitlement_date
        self.eligible_units = eligible_units

    @property
    def entitlement_date(self):
        """Gets the entitlement_date of this EligibilityCalculation.  # noqa: E501


        :return: The entitlement_date of this EligibilityCalculation.  # noqa: E501
        :rtype: str
        """
        return self._entitlement_date

    @entitlement_date.setter
    def entitlement_date(self, entitlement_date):
        """Sets the entitlement_date of this EligibilityCalculation.


        :param entitlement_date: The entitlement_date of this EligibilityCalculation.  # noqa: E501
        :type entitlement_date: str
        """
        if self.local_vars_configuration.client_side_validation and entitlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `entitlement_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entitlement_date is not None and len(entitlement_date) < 1):
            raise ValueError("Invalid value for `entitlement_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._entitlement_date = entitlement_date

    @property
    def eligible_units(self):
        """Gets the eligible_units of this EligibilityCalculation.  # noqa: E501


        :return: The eligible_units of this EligibilityCalculation.  # noqa: E501
        :rtype: str
        """
        return self._eligible_units

    @eligible_units.setter
    def eligible_units(self, eligible_units):
        """Sets the eligible_units of this EligibilityCalculation.


        :param eligible_units: The eligible_units of this EligibilityCalculation.  # noqa: E501
        :type eligible_units: str
        """
        if self.local_vars_configuration.client_side_validation and eligible_units is None:  # noqa: E501
            raise ValueError("Invalid value for `eligible_units`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                eligible_units is not None and len(eligible_units) < 1):
            raise ValueError("Invalid value for `eligible_units`, length must be greater than or equal to `1`")  # noqa: E501

        self._eligible_units = eligible_units

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
        if not isinstance(other, EligibilityCalculation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EligibilityCalculation):
            return True

        return self.to_dict() != other.to_dict()
