# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.195
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


class PreviousFundValuationPointData(object):
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
        'nav': 'FundPreviousNAV',
        'unitisation': 'UnitisationData'
    }

    attribute_map = {
        'nav': 'nav',
        'unitisation': 'unitisation'
    }

    required_map = {
        'nav': 'required',
        'unitisation': 'optional'
    }

    def __init__(self, nav=None, unitisation=None, local_vars_configuration=None):  # noqa: E501
        """PreviousFundValuationPointData - a model defined in OpenAPI"
        
        :param nav:  (required)
        :type nav: lusid.FundPreviousNAV
        :param unitisation: 
        :type unitisation: lusid.UnitisationData

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._nav = None
        self._unitisation = None
        self.discriminator = None

        self.nav = nav
        if unitisation is not None:
            self.unitisation = unitisation

    @property
    def nav(self):
        """Gets the nav of this PreviousFundValuationPointData.  # noqa: E501


        :return: The nav of this PreviousFundValuationPointData.  # noqa: E501
        :rtype: lusid.FundPreviousNAV
        """
        return self._nav

    @nav.setter
    def nav(self, nav):
        """Sets the nav of this PreviousFundValuationPointData.


        :param nav: The nav of this PreviousFundValuationPointData.  # noqa: E501
        :type nav: lusid.FundPreviousNAV
        """
        if self.local_vars_configuration.client_side_validation and nav is None:  # noqa: E501
            raise ValueError("Invalid value for `nav`, must not be `None`")  # noqa: E501

        self._nav = nav

    @property
    def unitisation(self):
        """Gets the unitisation of this PreviousFundValuationPointData.  # noqa: E501


        :return: The unitisation of this PreviousFundValuationPointData.  # noqa: E501
        :rtype: lusid.UnitisationData
        """
        return self._unitisation

    @unitisation.setter
    def unitisation(self, unitisation):
        """Sets the unitisation of this PreviousFundValuationPointData.


        :param unitisation: The unitisation of this PreviousFundValuationPointData.  # noqa: E501
        :type unitisation: lusid.UnitisationData
        """

        self._unitisation = unitisation

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
        if not isinstance(other, PreviousFundValuationPointData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreviousFundValuationPointData):
            return True

        return self.to_dict() != other.to_dict()
