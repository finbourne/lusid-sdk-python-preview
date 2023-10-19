# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.625
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


class VendorDependency(object):
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
        'vendor_name': 'str',
        'vendor_path': 'list[str]',
        'date': 'datetime',
        'dependency_type': 'str'
    }

    attribute_map = {
        'vendor_name': 'vendorName',
        'vendor_path': 'vendorPath',
        'date': 'date',
        'dependency_type': 'dependencyType'
    }

    required_map = {
        'vendor_name': 'required',
        'vendor_path': 'required',
        'date': 'required',
        'dependency_type': 'required'
    }

    def __init__(self, vendor_name=None, vendor_path=None, date=None, dependency_type=None, local_vars_configuration=None):  # noqa: E501
        """VendorDependency - a model defined in OpenAPI"
        
        :param vendor_name:  The name of the outside vendor (required)
        :type vendor_name: str
        :param vendor_path:  The specific dependency path (required)
        :type vendor_path: list[str]
        :param date:  The effectiveDate of the entity that this is a dependency for. (required)
        :type date: datetime
        :param dependency_type:  The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency (required)
        :type dependency_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._vendor_name = None
        self._vendor_path = None
        self._date = None
        self._dependency_type = None
        self.discriminator = None

        self.vendor_name = vendor_name
        self.vendor_path = vendor_path
        self.date = date
        self.dependency_type = dependency_type

    @property
    def vendor_name(self):
        """Gets the vendor_name of this VendorDependency.  # noqa: E501

        The name of the outside vendor  # noqa: E501

        :return: The vendor_name of this VendorDependency.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this VendorDependency.

        The name of the outside vendor  # noqa: E501

        :param vendor_name: The vendor_name of this VendorDependency.  # noqa: E501
        :type vendor_name: str
        """
        if self.local_vars_configuration.client_side_validation and vendor_name is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vendor_name is not None and len(vendor_name) < 1):
            raise ValueError("Invalid value for `vendor_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._vendor_name = vendor_name

    @property
    def vendor_path(self):
        """Gets the vendor_path of this VendorDependency.  # noqa: E501

        The specific dependency path  # noqa: E501

        :return: The vendor_path of this VendorDependency.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendor_path

    @vendor_path.setter
    def vendor_path(self, vendor_path):
        """Sets the vendor_path of this VendorDependency.

        The specific dependency path  # noqa: E501

        :param vendor_path: The vendor_path of this VendorDependency.  # noqa: E501
        :type vendor_path: list[str]
        """
        if self.local_vars_configuration.client_side_validation and vendor_path is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor_path`, must not be `None`")  # noqa: E501

        self._vendor_path = vendor_path

    @property
    def date(self):
        """Gets the date of this VendorDependency.  # noqa: E501

        The effectiveDate of the entity that this is a dependency for.  # noqa: E501

        :return: The date of this VendorDependency.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this VendorDependency.

        The effectiveDate of the entity that this is a dependency for.  # noqa: E501

        :param date: The date of this VendorDependency.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def dependency_type(self):
        """Gets the dependency_type of this VendorDependency.  # noqa: E501

        The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency  # noqa: E501

        :return: The dependency_type of this VendorDependency.  # noqa: E501
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this VendorDependency.

        The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency  # noqa: E501

        :param dependency_type: The dependency_type of this VendorDependency.  # noqa: E501
        :type dependency_type: str
        """
        if self.local_vars_configuration.client_side_validation and dependency_type is None:  # noqa: E501
            raise ValueError("Invalid value for `dependency_type`, must not be `None`")  # noqa: E501
        allowed_values = ["OpaqueDependency", "CashDependency", "DiscountingDependency", "EquityCurveDependency", "EquityVolDependency", "FxDependency", "FxForwardsDependency", "FxVolDependency", "IndexProjectionDependency", "IrVolDependency", "QuoteDependency", "Vendor", "CalendarDependency", "InflationFixingDependency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dependency_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dependency_type, allowed_values)
            )

        self._dependency_type = dependency_type

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
        if not isinstance(other, VendorDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VendorDependency):
            return True

        return self.to_dict() != other.to_dict()
