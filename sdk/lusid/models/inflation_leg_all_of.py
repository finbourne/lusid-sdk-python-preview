# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.36
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


class InflationLegAllOf(object):
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
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'flow_conventions': 'FlowConventions',
        'base_cpi': 'float',
        'calculation_type': 'str',
        'cap_rate': 'float',
        'floor_rate': 'float',
        'inflation_index_conventions': 'InflationIndexConventions',
        'notional': 'float',
        'pay_receive': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'flow_conventions': 'flowConventions',
        'base_cpi': 'baseCPI',
        'calculation_type': 'calculationType',
        'cap_rate': 'capRate',
        'floor_rate': 'floorRate',
        'inflation_index_conventions': 'inflationIndexConventions',
        'notional': 'notional',
        'pay_receive': 'payReceive',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'flow_conventions': 'required',
        'base_cpi': 'optional',
        'calculation_type': 'required',
        'cap_rate': 'optional',
        'floor_rate': 'optional',
        'inflation_index_conventions': 'required',
        'notional': 'required',
        'pay_receive': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, flow_conventions=None, base_cpi=None, calculation_type=None, cap_rate=None, floor_rate=None, inflation_index_conventions=None, notional=None, pay_receive=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """InflationLegAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param flow_conventions:  (required)
        :type flow_conventions: lusid.FlowConventions
        :param base_cpi:  Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate).  This should not be required for standard inflation swaps.
        :type base_cpi: float
        :param calculation_type:  The calculation type.  ZeroCoupon is used for CPILegs where there is a single payment at maturity of  Notional * (CPI(T) / CPI(T0) - 1)  where CPI(T0) is the BaseCPI of this leg  YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(t-1) - 1)  If a cap and floor is added to this it becomes an LPI swap leg.  Compounded is used for inflation swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(T0) - 1)  i.e. the BaseCPI is used every year. These swaps are not as common as CPI or    Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded]. (required)
        :type calculation_type: str
        :param cap_rate:  Optional cap, needed for LPI Legs or CPI Legs with Caps
        :type cap_rate: float
        :param floor_rate:  Optional floor, needed for LPI Legs or CPI Legs with Floors.
        :type floor_rate: float
        :param inflation_index_conventions:  (required)
        :type inflation_index_conventions: lusid.InflationIndexConventions
        :param notional:  The notional (required)
        :type notional: float
        :param pay_receive:  PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.    Supported string (enumeration) values are: [Pay, Receive].
        :type pay_receive: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._flow_conventions = None
        self._base_cpi = None
        self._calculation_type = None
        self._cap_rate = None
        self._floor_rate = None
        self._inflation_index_conventions = None
        self._notional = None
        self._pay_receive = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.flow_conventions = flow_conventions
        self.base_cpi = base_cpi
        self.calculation_type = calculation_type
        self.cap_rate = cap_rate
        self.floor_rate = floor_rate
        self.inflation_index_conventions = inflation_index_conventions
        self.notional = notional
        self.pay_receive = pay_receive
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this InflationLegAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this InflationLegAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InflationLegAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this InflationLegAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this InflationLegAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this InflationLegAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this InflationLegAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this InflationLegAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this InflationLegAllOf.  # noqa: E501


        :return: The flow_conventions of this InflationLegAllOf.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this InflationLegAllOf.


        :param flow_conventions: The flow_conventions of this InflationLegAllOf.  # noqa: E501
        :type flow_conventions: lusid.FlowConventions
        """
        if self.local_vars_configuration.client_side_validation and flow_conventions is None:  # noqa: E501
            raise ValueError("Invalid value for `flow_conventions`, must not be `None`")  # noqa: E501

        self._flow_conventions = flow_conventions

    @property
    def base_cpi(self):
        """Gets the base_cpi of this InflationLegAllOf.  # noqa: E501

        Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate).  This should not be required for standard inflation swaps.  # noqa: E501

        :return: The base_cpi of this InflationLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._base_cpi

    @base_cpi.setter
    def base_cpi(self, base_cpi):
        """Sets the base_cpi of this InflationLegAllOf.

        Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate).  This should not be required for standard inflation swaps.  # noqa: E501

        :param base_cpi: The base_cpi of this InflationLegAllOf.  # noqa: E501
        :type base_cpi: float
        """

        self._base_cpi = base_cpi

    @property
    def calculation_type(self):
        """Gets the calculation_type of this InflationLegAllOf.  # noqa: E501

        The calculation type.  ZeroCoupon is used for CPILegs where there is a single payment at maturity of  Notional * (CPI(T) / CPI(T0) - 1)  where CPI(T0) is the BaseCPI of this leg  YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(t-1) - 1)  If a cap and floor is added to this it becomes an LPI swap leg.  Compounded is used for inflation swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(T0) - 1)  i.e. the BaseCPI is used every year. These swaps are not as common as CPI or    Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded].  # noqa: E501

        :return: The calculation_type of this InflationLegAllOf.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this InflationLegAllOf.

        The calculation type.  ZeroCoupon is used for CPILegs where there is a single payment at maturity of  Notional * (CPI(T) / CPI(T0) - 1)  where CPI(T0) is the BaseCPI of this leg  YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(t-1) - 1)  If a cap and floor is added to this it becomes an LPI swap leg.  Compounded is used for inflation swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(T0) - 1)  i.e. the BaseCPI is used every year. These swaps are not as common as CPI or    Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded].  # noqa: E501

        :param calculation_type: The calculation_type of this InflationLegAllOf.  # noqa: E501
        :type calculation_type: str
        """
        if self.local_vars_configuration.client_side_validation and calculation_type is None:  # noqa: E501
            raise ValueError("Invalid value for `calculation_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calculation_type is not None and len(calculation_type) > 32):
            raise ValueError("Invalid value for `calculation_type`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calculation_type is not None and len(calculation_type) < 0):
            raise ValueError("Invalid value for `calculation_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._calculation_type = calculation_type

    @property
    def cap_rate(self):
        """Gets the cap_rate of this InflationLegAllOf.  # noqa: E501

        Optional cap, needed for LPI Legs or CPI Legs with Caps  # noqa: E501

        :return: The cap_rate of this InflationLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._cap_rate

    @cap_rate.setter
    def cap_rate(self, cap_rate):
        """Sets the cap_rate of this InflationLegAllOf.

        Optional cap, needed for LPI Legs or CPI Legs with Caps  # noqa: E501

        :param cap_rate: The cap_rate of this InflationLegAllOf.  # noqa: E501
        :type cap_rate: float
        """

        self._cap_rate = cap_rate

    @property
    def floor_rate(self):
        """Gets the floor_rate of this InflationLegAllOf.  # noqa: E501

        Optional floor, needed for LPI Legs or CPI Legs with Floors.  # noqa: E501

        :return: The floor_rate of this InflationLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._floor_rate

    @floor_rate.setter
    def floor_rate(self, floor_rate):
        """Sets the floor_rate of this InflationLegAllOf.

        Optional floor, needed for LPI Legs or CPI Legs with Floors.  # noqa: E501

        :param floor_rate: The floor_rate of this InflationLegAllOf.  # noqa: E501
        :type floor_rate: float
        """

        self._floor_rate = floor_rate

    @property
    def inflation_index_conventions(self):
        """Gets the inflation_index_conventions of this InflationLegAllOf.  # noqa: E501


        :return: The inflation_index_conventions of this InflationLegAllOf.  # noqa: E501
        :rtype: lusid.InflationIndexConventions
        """
        return self._inflation_index_conventions

    @inflation_index_conventions.setter
    def inflation_index_conventions(self, inflation_index_conventions):
        """Sets the inflation_index_conventions of this InflationLegAllOf.


        :param inflation_index_conventions: The inflation_index_conventions of this InflationLegAllOf.  # noqa: E501
        :type inflation_index_conventions: lusid.InflationIndexConventions
        """
        if self.local_vars_configuration.client_side_validation and inflation_index_conventions is None:  # noqa: E501
            raise ValueError("Invalid value for `inflation_index_conventions`, must not be `None`")  # noqa: E501

        self._inflation_index_conventions = inflation_index_conventions

    @property
    def notional(self):
        """Gets the notional of this InflationLegAllOf.  # noqa: E501

        The notional  # noqa: E501

        :return: The notional of this InflationLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._notional

    @notional.setter
    def notional(self, notional):
        """Sets the notional of this InflationLegAllOf.

        The notional  # noqa: E501

        :param notional: The notional of this InflationLegAllOf.  # noqa: E501
        :type notional: float
        """
        if self.local_vars_configuration.client_side_validation and notional is None:  # noqa: E501
            raise ValueError("Invalid value for `notional`, must not be `None`")  # noqa: E501

        self._notional = notional

    @property
    def pay_receive(self):
        """Gets the pay_receive of this InflationLegAllOf.  # noqa: E501

        PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :return: The pay_receive of this InflationLegAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this InflationLegAllOf.

        PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :param pay_receive: The pay_receive of this InflationLegAllOf.  # noqa: E501
        :type pay_receive: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) > 32):
            raise ValueError("Invalid value for `pay_receive`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) < 0):
            raise ValueError("Invalid value for `pay_receive`, length must be greater than or equal to `0`")  # noqa: E501

        self._pay_receive = pay_receive

    @property
    def instrument_type(self):
        """Gets the instrument_type of this InflationLegAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg  # noqa: E501

        :return: The instrument_type of this InflationLegAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this InflationLegAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg  # noqa: E501

        :param instrument_type: The instrument_type of this InflationLegAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan", "TotalReturnSwap", "InflationLeg"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, InflationLegAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InflationLegAllOf):
            return True

        return self.to_dict() != other.to_dict()
