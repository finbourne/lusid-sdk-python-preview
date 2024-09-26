# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.230
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


class FundValuationPointData(object):
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
        'back_out': 'dict(str, FundAmount)',
        'dealing': 'dict(str, FundAmount)',
        'pn_l': 'FundPnlBreakdown',
        'gav': 'float',
        'fees': 'dict(str, FeeAccrual)',
        'nav': 'float',
        'unitisation': 'UnitisationData',
        'miscellaneous': 'dict(str, FundAmount)',
        'previous_valuation_point_data': 'PreviousFundValuationPointData'
    }

    attribute_map = {
        'back_out': 'backOut',
        'dealing': 'dealing',
        'pn_l': 'pnL',
        'gav': 'gav',
        'fees': 'fees',
        'nav': 'nav',
        'unitisation': 'unitisation',
        'miscellaneous': 'miscellaneous',
        'previous_valuation_point_data': 'previousValuationPointData'
    }

    required_map = {
        'back_out': 'required',
        'dealing': 'required',
        'pn_l': 'required',
        'gav': 'required',
        'fees': 'required',
        'nav': 'required',
        'unitisation': 'optional',
        'miscellaneous': 'optional',
        'previous_valuation_point_data': 'optional'
    }

    def __init__(self, back_out=None, dealing=None, pn_l=None, gav=None, fees=None, nav=None, unitisation=None, miscellaneous=None, previous_valuation_point_data=None, local_vars_configuration=None):  # noqa: E501
        """FundValuationPointData - a model defined in OpenAPI"
        
        :param back_out:  Bucket of detail for the Valuation Point where data points have been 'backed out'. (required)
        :type back_out: dict[str, lusid.FundAmount]
        :param dealing:  Bucket of detail for any 'Dealing' that has occured inside the queried period. (required)
        :type dealing: dict[str, lusid.FundAmount]
        :param pn_l:  (required)
        :type pn_l: lusid.FundPnlBreakdown
        :param gav:  The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'. (required)
        :type gav: float
        :param fees:  Bucket of detail for any 'Fees' that have been charged in the selected period. (required)
        :type fees: dict[str, lusid.FeeAccrual]
        :param nav:  The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. (required)
        :type nav: float
        :param unitisation: 
        :type unitisation: lusid.UnitisationData
        :param miscellaneous:  Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations).
        :type miscellaneous: dict[str, lusid.FundAmount]
        :param previous_valuation_point_data: 
        :type previous_valuation_point_data: lusid.PreviousFundValuationPointData

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._back_out = None
        self._dealing = None
        self._pn_l = None
        self._gav = None
        self._fees = None
        self._nav = None
        self._unitisation = None
        self._miscellaneous = None
        self._previous_valuation_point_data = None
        self.discriminator = None

        self.back_out = back_out
        self.dealing = dealing
        self.pn_l = pn_l
        self.gav = gav
        self.fees = fees
        self.nav = nav
        if unitisation is not None:
            self.unitisation = unitisation
        self.miscellaneous = miscellaneous
        if previous_valuation_point_data is not None:
            self.previous_valuation_point_data = previous_valuation_point_data

    @property
    def back_out(self):
        """Gets the back_out of this FundValuationPointData.  # noqa: E501

        Bucket of detail for the Valuation Point where data points have been 'backed out'.  # noqa: E501

        :return: The back_out of this FundValuationPointData.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._back_out

    @back_out.setter
    def back_out(self, back_out):
        """Sets the back_out of this FundValuationPointData.

        Bucket of detail for the Valuation Point where data points have been 'backed out'.  # noqa: E501

        :param back_out: The back_out of this FundValuationPointData.  # noqa: E501
        :type back_out: dict[str, lusid.FundAmount]
        """
        if self.local_vars_configuration.client_side_validation and back_out is None:  # noqa: E501
            raise ValueError("Invalid value for `back_out`, must not be `None`")  # noqa: E501

        self._back_out = back_out

    @property
    def dealing(self):
        """Gets the dealing of this FundValuationPointData.  # noqa: E501

        Bucket of detail for any 'Dealing' that has occured inside the queried period.  # noqa: E501

        :return: The dealing of this FundValuationPointData.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._dealing

    @dealing.setter
    def dealing(self, dealing):
        """Sets the dealing of this FundValuationPointData.

        Bucket of detail for any 'Dealing' that has occured inside the queried period.  # noqa: E501

        :param dealing: The dealing of this FundValuationPointData.  # noqa: E501
        :type dealing: dict[str, lusid.FundAmount]
        """
        if self.local_vars_configuration.client_side_validation and dealing is None:  # noqa: E501
            raise ValueError("Invalid value for `dealing`, must not be `None`")  # noqa: E501

        self._dealing = dealing

    @property
    def pn_l(self):
        """Gets the pn_l of this FundValuationPointData.  # noqa: E501


        :return: The pn_l of this FundValuationPointData.  # noqa: E501
        :rtype: lusid.FundPnlBreakdown
        """
        return self._pn_l

    @pn_l.setter
    def pn_l(self, pn_l):
        """Sets the pn_l of this FundValuationPointData.


        :param pn_l: The pn_l of this FundValuationPointData.  # noqa: E501
        :type pn_l: lusid.FundPnlBreakdown
        """
        if self.local_vars_configuration.client_side_validation and pn_l is None:  # noqa: E501
            raise ValueError("Invalid value for `pn_l`, must not be `None`")  # noqa: E501

        self._pn_l = pn_l

    @property
    def gav(self):
        """Gets the gav of this FundValuationPointData.  # noqa: E501

        The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'.  # noqa: E501

        :return: The gav of this FundValuationPointData.  # noqa: E501
        :rtype: float
        """
        return self._gav

    @gav.setter
    def gav(self, gav):
        """Sets the gav of this FundValuationPointData.

        The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'.  # noqa: E501

        :param gav: The gav of this FundValuationPointData.  # noqa: E501
        :type gav: float
        """
        if self.local_vars_configuration.client_side_validation and gav is None:  # noqa: E501
            raise ValueError("Invalid value for `gav`, must not be `None`")  # noqa: E501

        self._gav = gav

    @property
    def fees(self):
        """Gets the fees of this FundValuationPointData.  # noqa: E501

        Bucket of detail for any 'Fees' that have been charged in the selected period.  # noqa: E501

        :return: The fees of this FundValuationPointData.  # noqa: E501
        :rtype: dict[str, lusid.FeeAccrual]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this FundValuationPointData.

        Bucket of detail for any 'Fees' that have been charged in the selected period.  # noqa: E501

        :param fees: The fees of this FundValuationPointData.  # noqa: E501
        :type fees: dict[str, lusid.FeeAccrual]
        """
        if self.local_vars_configuration.client_side_validation and fees is None:  # noqa: E501
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def nav(self):
        """Gets the nav of this FundValuationPointData.  # noqa: E501

        The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.  # noqa: E501

        :return: The nav of this FundValuationPointData.  # noqa: E501
        :rtype: float
        """
        return self._nav

    @nav.setter
    def nav(self, nav):
        """Sets the nav of this FundValuationPointData.

        The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.  # noqa: E501

        :param nav: The nav of this FundValuationPointData.  # noqa: E501
        :type nav: float
        """
        if self.local_vars_configuration.client_side_validation and nav is None:  # noqa: E501
            raise ValueError("Invalid value for `nav`, must not be `None`")  # noqa: E501

        self._nav = nav

    @property
    def unitisation(self):
        """Gets the unitisation of this FundValuationPointData.  # noqa: E501


        :return: The unitisation of this FundValuationPointData.  # noqa: E501
        :rtype: lusid.UnitisationData
        """
        return self._unitisation

    @unitisation.setter
    def unitisation(self, unitisation):
        """Sets the unitisation of this FundValuationPointData.


        :param unitisation: The unitisation of this FundValuationPointData.  # noqa: E501
        :type unitisation: lusid.UnitisationData
        """

        self._unitisation = unitisation

    @property
    def miscellaneous(self):
        """Gets the miscellaneous of this FundValuationPointData.  # noqa: E501

        Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations).  # noqa: E501

        :return: The miscellaneous of this FundValuationPointData.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._miscellaneous

    @miscellaneous.setter
    def miscellaneous(self, miscellaneous):
        """Sets the miscellaneous of this FundValuationPointData.

        Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations).  # noqa: E501

        :param miscellaneous: The miscellaneous of this FundValuationPointData.  # noqa: E501
        :type miscellaneous: dict[str, lusid.FundAmount]
        """

        self._miscellaneous = miscellaneous

    @property
    def previous_valuation_point_data(self):
        """Gets the previous_valuation_point_data of this FundValuationPointData.  # noqa: E501


        :return: The previous_valuation_point_data of this FundValuationPointData.  # noqa: E501
        :rtype: lusid.PreviousFundValuationPointData
        """
        return self._previous_valuation_point_data

    @previous_valuation_point_data.setter
    def previous_valuation_point_data(self, previous_valuation_point_data):
        """Sets the previous_valuation_point_data of this FundValuationPointData.


        :param previous_valuation_point_data: The previous_valuation_point_data of this FundValuationPointData.  # noqa: E501
        :type previous_valuation_point_data: lusid.PreviousFundValuationPointData
        """

        self._previous_valuation_point_data = previous_valuation_point_data

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
        if not isinstance(other, FundValuationPointData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundValuationPointData):
            return True

        return self.to_dict() != other.to_dict()
