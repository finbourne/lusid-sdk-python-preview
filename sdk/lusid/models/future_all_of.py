# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.224
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


class FutureAllOf(object):
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
        'identifiers': 'dict(str, str)',
        'contract_details': 'FuturesContractDetails',
        'contracts': 'float',
        'ref_spot_price': 'float',
        'underlying': 'LusidInstrument',
        'calculation_type': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'identifiers': 'identifiers',
        'contract_details': 'contractDetails',
        'contracts': 'contracts',
        'ref_spot_price': 'refSpotPrice',
        'underlying': 'underlying',
        'calculation_type': 'calculationType',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'identifiers': 'required',
        'contract_details': 'required',
        'contracts': 'optional',
        'ref_spot_price': 'optional',
        'underlying': 'optional',
        'calculation_type': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, identifiers=None, contract_details=None, contracts=None, ref_spot_price=None, underlying=None, calculation_type=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FutureAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param identifiers:  External market codes and identifiers for the bond, e.g. ISIN. (required)
        :type identifiers: dict(str, str)
        :param contract_details:  (required)
        :type contract_details: lusid.FuturesContractDetails
        :param contracts:  The number of contracts held.
        :type contracts: float
        :param ref_spot_price:  The reference spot price for the future at which the contract was entered into.
        :type ref_spot_price: float
        :param underlying: 
        :type underlying: lusid.LusidInstrument
        :param calculation_type:  Calculation type for some Future instruments which have non-standard methodology.  Optional, if not set defaults as follows:  - If ExchangeCode is \"ASX\" and ContractCode is \"IR\" or \"BB\" set to ASX_BankBills  - If ExchangeCode is \"ASX\" and ContractCode is \"YT\" set to ASX_3Year  - If ExchangeCode is \"ASX\" and ContractCode is \"VT\" set to ASX_5Year  - If ExchangeCode is \"ASX\" and ContractCode is \"XT\" set to ASX_10Year  - If ExchangeCode is \"ASX\" and ContractCode is \"LT\" set to ASX_20Year  - otherwise set to Standard    Specific calculation types for ASX bond futures are:  - [Standard] The default calculation type, which does not fit into any of the categories below.  - [ASX_BankBills] Used for AUD and NZD futures “IR” and “BB” on ASX. 90D Bank Bills.  - [ASX_3Year] Used for “YT” on ASX. 3YR semi-annual bond (6 coupons) @ 6%.  - [ASX_5Year] Used for “VT” on ASX. 5yr semi-annual bond (10 coupons) @ 2%.  - [ASX_10Year] Used for “XT” on ASX. 10yr semi-annual bond (20 coupons) @ 6%.  - [ASX_20Year] Used for “LT” on ASX. 20yr semi-annual bond (40 coupons) @ 4%.    Supported string (enumeration) values are: [Standard, ASX_BankBills, ASX_3Year, ASX_5Year, ASX_10Year, ASX_20Year].
        :type calculation_type: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._identifiers = None
        self._contract_details = None
        self._contracts = None
        self._ref_spot_price = None
        self._underlying = None
        self._calculation_type = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.identifiers = identifiers
        self.contract_details = contract_details
        if contracts is not None:
            self.contracts = contracts
        if ref_spot_price is not None:
            self.ref_spot_price = ref_spot_price
        if underlying is not None:
            self.underlying = underlying
        self.calculation_type = calculation_type
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this FutureAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this FutureAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FutureAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this FutureAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this FutureAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this FutureAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this FutureAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this FutureAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def identifiers(self):
        """Gets the identifiers of this FutureAllOf.  # noqa: E501

        External market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :return: The identifiers of this FutureAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this FutureAllOf.

        External market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :param identifiers: The identifiers of this FutureAllOf.  # noqa: E501
        :type identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def contract_details(self):
        """Gets the contract_details of this FutureAllOf.  # noqa: E501


        :return: The contract_details of this FutureAllOf.  # noqa: E501
        :rtype: lusid.FuturesContractDetails
        """
        return self._contract_details

    @contract_details.setter
    def contract_details(self, contract_details):
        """Sets the contract_details of this FutureAllOf.


        :param contract_details: The contract_details of this FutureAllOf.  # noqa: E501
        :type contract_details: lusid.FuturesContractDetails
        """
        if self.local_vars_configuration.client_side_validation and contract_details is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_details`, must not be `None`")  # noqa: E501

        self._contract_details = contract_details

    @property
    def contracts(self):
        """Gets the contracts of this FutureAllOf.  # noqa: E501

        The number of contracts held.  # noqa: E501

        :return: The contracts of this FutureAllOf.  # noqa: E501
        :rtype: float
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this FutureAllOf.

        The number of contracts held.  # noqa: E501

        :param contracts: The contracts of this FutureAllOf.  # noqa: E501
        :type contracts: float
        """

        self._contracts = contracts

    @property
    def ref_spot_price(self):
        """Gets the ref_spot_price of this FutureAllOf.  # noqa: E501

        The reference spot price for the future at which the contract was entered into.  # noqa: E501

        :return: The ref_spot_price of this FutureAllOf.  # noqa: E501
        :rtype: float
        """
        return self._ref_spot_price

    @ref_spot_price.setter
    def ref_spot_price(self, ref_spot_price):
        """Sets the ref_spot_price of this FutureAllOf.

        The reference spot price for the future at which the contract was entered into.  # noqa: E501

        :param ref_spot_price: The ref_spot_price of this FutureAllOf.  # noqa: E501
        :type ref_spot_price: float
        """

        self._ref_spot_price = ref_spot_price

    @property
    def underlying(self):
        """Gets the underlying of this FutureAllOf.  # noqa: E501


        :return: The underlying of this FutureAllOf.  # noqa: E501
        :rtype: lusid.LusidInstrument
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this FutureAllOf.


        :param underlying: The underlying of this FutureAllOf.  # noqa: E501
        :type underlying: lusid.LusidInstrument
        """

        self._underlying = underlying

    @property
    def calculation_type(self):
        """Gets the calculation_type of this FutureAllOf.  # noqa: E501

        Calculation type for some Future instruments which have non-standard methodology.  Optional, if not set defaults as follows:  - If ExchangeCode is \"ASX\" and ContractCode is \"IR\" or \"BB\" set to ASX_BankBills  - If ExchangeCode is \"ASX\" and ContractCode is \"YT\" set to ASX_3Year  - If ExchangeCode is \"ASX\" and ContractCode is \"VT\" set to ASX_5Year  - If ExchangeCode is \"ASX\" and ContractCode is \"XT\" set to ASX_10Year  - If ExchangeCode is \"ASX\" and ContractCode is \"LT\" set to ASX_20Year  - otherwise set to Standard    Specific calculation types for ASX bond futures are:  - [Standard] The default calculation type, which does not fit into any of the categories below.  - [ASX_BankBills] Used for AUD and NZD futures “IR” and “BB” on ASX. 90D Bank Bills.  - [ASX_3Year] Used for “YT” on ASX. 3YR semi-annual bond (6 coupons) @ 6%.  - [ASX_5Year] Used for “VT” on ASX. 5yr semi-annual bond (10 coupons) @ 2%.  - [ASX_10Year] Used for “XT” on ASX. 10yr semi-annual bond (20 coupons) @ 6%.  - [ASX_20Year] Used for “LT” on ASX. 20yr semi-annual bond (40 coupons) @ 4%.    Supported string (enumeration) values are: [Standard, ASX_BankBills, ASX_3Year, ASX_5Year, ASX_10Year, ASX_20Year].  # noqa: E501

        :return: The calculation_type of this FutureAllOf.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this FutureAllOf.

        Calculation type for some Future instruments which have non-standard methodology.  Optional, if not set defaults as follows:  - If ExchangeCode is \"ASX\" and ContractCode is \"IR\" or \"BB\" set to ASX_BankBills  - If ExchangeCode is \"ASX\" and ContractCode is \"YT\" set to ASX_3Year  - If ExchangeCode is \"ASX\" and ContractCode is \"VT\" set to ASX_5Year  - If ExchangeCode is \"ASX\" and ContractCode is \"XT\" set to ASX_10Year  - If ExchangeCode is \"ASX\" and ContractCode is \"LT\" set to ASX_20Year  - otherwise set to Standard    Specific calculation types for ASX bond futures are:  - [Standard] The default calculation type, which does not fit into any of the categories below.  - [ASX_BankBills] Used for AUD and NZD futures “IR” and “BB” on ASX. 90D Bank Bills.  - [ASX_3Year] Used for “YT” on ASX. 3YR semi-annual bond (6 coupons) @ 6%.  - [ASX_5Year] Used for “VT” on ASX. 5yr semi-annual bond (10 coupons) @ 2%.  - [ASX_10Year] Used for “XT” on ASX. 10yr semi-annual bond (20 coupons) @ 6%.  - [ASX_20Year] Used for “LT” on ASX. 20yr semi-annual bond (40 coupons) @ 4%.    Supported string (enumeration) values are: [Standard, ASX_BankBills, ASX_3Year, ASX_5Year, ASX_10Year, ASX_20Year].  # noqa: E501

        :param calculation_type: The calculation_type of this FutureAllOf.  # noqa: E501
        :type calculation_type: str
        """

        self._calculation_type = calculation_type

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FutureAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :return: The instrument_type of this FutureAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FutureAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :param instrument_type: The instrument_type of this FutureAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan"]  # noqa: E501
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
        if not isinstance(other, FutureAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FutureAllOf):
            return True

        return self.to_dict() != other.to_dict()
