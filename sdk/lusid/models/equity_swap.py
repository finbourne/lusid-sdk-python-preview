# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.263
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


class EquitySwap(object):
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
        'code': 'str',
        'equity_flow_conventions': 'FlowConventions',
        'funding_leg': 'InstrumentLeg',
        'include_dividends': 'bool',
        'initial_price': 'float',
        'notional_reset': 'bool',
        'quantity': 'float',
        'underlying_identifier': 'str',
        'equity_swap_dividend_payment_timing': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'code': 'code',
        'equity_flow_conventions': 'equityFlowConventions',
        'funding_leg': 'fundingLeg',
        'include_dividends': 'includeDividends',
        'initial_price': 'initialPrice',
        'notional_reset': 'notionalReset',
        'quantity': 'quantity',
        'underlying_identifier': 'underlyingIdentifier',
        'equity_swap_dividend_payment_timing': 'equitySwapDividendPaymentTiming',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'code': 'required',
        'equity_flow_conventions': 'required',
        'funding_leg': 'required',
        'include_dividends': 'required',
        'initial_price': 'required',
        'notional_reset': 'required',
        'quantity': 'required',
        'underlying_identifier': 'required',
        'equity_swap_dividend_payment_timing': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, code=None, equity_flow_conventions=None, funding_leg=None, include_dividends=None, initial_price=None, notional_reset=None, quantity=None, underlying_identifier=None, equity_swap_dividend_payment_timing=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """EquitySwap - a model defined in OpenAPI"
        
        :param start_date:  The start date of the EquitySwap. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param code:  The code of the underlying. (required)
        :type code: str
        :param equity_flow_conventions:  (required)
        :type equity_flow_conventions: lusid.FlowConventions
        :param funding_leg:  (required)
        :type funding_leg: lusid.InstrumentLeg
        :param include_dividends:  Dividend inclusion flag, if true dividends are included in the equity leg (total return). (required)
        :type include_dividends: bool
        :param initial_price:  The initial equity price of the Equity Swap. (required)
        :type initial_price: float
        :param notional_reset:  Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity). (required)
        :type notional_reset: bool
        :param quantity:  The quantity or number of shares in the Equity Swap. (required)
        :type quantity: float
        :param underlying_identifier:  External market codes and identifiers for the EquitySwap, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. (required)
        :type underlying_identifier: str
        :param equity_swap_dividend_payment_timing:  Determines how the payment of dividends is handled for the equity swap.  Defaults to paying at the next Equity coupon date.                Supported string (enumeration) values are: [PayAtNextEquityCouponDate, PayAtMaturityOfSwap, PayAtNextFundingLegCouponDate, PayAtPaymentDateOfDividendEvent].
        :type equity_swap_dividend_payment_timing: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._code = None
        self._equity_flow_conventions = None
        self._funding_leg = None
        self._include_dividends = None
        self._initial_price = None
        self._notional_reset = None
        self._quantity = None
        self._underlying_identifier = None
        self._equity_swap_dividend_payment_timing = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.code = code
        self.equity_flow_conventions = equity_flow_conventions
        self.funding_leg = funding_leg
        self.include_dividends = include_dividends
        self.initial_price = initial_price
        self.notional_reset = notional_reset
        self.quantity = quantity
        self.underlying_identifier = underlying_identifier
        self.equity_swap_dividend_payment_timing = equity_swap_dividend_payment_timing
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this EquitySwap.  # noqa: E501

        The start date of the EquitySwap.  # noqa: E501

        :return: The start_date of this EquitySwap.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EquitySwap.

        The start date of the EquitySwap.  # noqa: E501

        :param start_date: The start_date of this EquitySwap.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this EquitySwap.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this EquitySwap.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this EquitySwap.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this EquitySwap.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def code(self):
        """Gets the code of this EquitySwap.  # noqa: E501

        The code of the underlying.  # noqa: E501

        :return: The code of this EquitySwap.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EquitySwap.

        The code of the underlying.  # noqa: E501

        :param code: The code of this EquitySwap.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def equity_flow_conventions(self):
        """Gets the equity_flow_conventions of this EquitySwap.  # noqa: E501


        :return: The equity_flow_conventions of this EquitySwap.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._equity_flow_conventions

    @equity_flow_conventions.setter
    def equity_flow_conventions(self, equity_flow_conventions):
        """Sets the equity_flow_conventions of this EquitySwap.


        :param equity_flow_conventions: The equity_flow_conventions of this EquitySwap.  # noqa: E501
        :type equity_flow_conventions: lusid.FlowConventions
        """
        if self.local_vars_configuration.client_side_validation and equity_flow_conventions is None:  # noqa: E501
            raise ValueError("Invalid value for `equity_flow_conventions`, must not be `None`")  # noqa: E501

        self._equity_flow_conventions = equity_flow_conventions

    @property
    def funding_leg(self):
        """Gets the funding_leg of this EquitySwap.  # noqa: E501


        :return: The funding_leg of this EquitySwap.  # noqa: E501
        :rtype: lusid.InstrumentLeg
        """
        return self._funding_leg

    @funding_leg.setter
    def funding_leg(self, funding_leg):
        """Sets the funding_leg of this EquitySwap.


        :param funding_leg: The funding_leg of this EquitySwap.  # noqa: E501
        :type funding_leg: lusid.InstrumentLeg
        """
        if self.local_vars_configuration.client_side_validation and funding_leg is None:  # noqa: E501
            raise ValueError("Invalid value for `funding_leg`, must not be `None`")  # noqa: E501

        self._funding_leg = funding_leg

    @property
    def include_dividends(self):
        """Gets the include_dividends of this EquitySwap.  # noqa: E501

        Dividend inclusion flag, if true dividends are included in the equity leg (total return).  # noqa: E501

        :return: The include_dividends of this EquitySwap.  # noqa: E501
        :rtype: bool
        """
        return self._include_dividends

    @include_dividends.setter
    def include_dividends(self, include_dividends):
        """Sets the include_dividends of this EquitySwap.

        Dividend inclusion flag, if true dividends are included in the equity leg (total return).  # noqa: E501

        :param include_dividends: The include_dividends of this EquitySwap.  # noqa: E501
        :type include_dividends: bool
        """
        if self.local_vars_configuration.client_side_validation and include_dividends is None:  # noqa: E501
            raise ValueError("Invalid value for `include_dividends`, must not be `None`")  # noqa: E501

        self._include_dividends = include_dividends

    @property
    def initial_price(self):
        """Gets the initial_price of this EquitySwap.  # noqa: E501

        The initial equity price of the Equity Swap.  # noqa: E501

        :return: The initial_price of this EquitySwap.  # noqa: E501
        :rtype: float
        """
        return self._initial_price

    @initial_price.setter
    def initial_price(self, initial_price):
        """Sets the initial_price of this EquitySwap.

        The initial equity price of the Equity Swap.  # noqa: E501

        :param initial_price: The initial_price of this EquitySwap.  # noqa: E501
        :type initial_price: float
        """
        if self.local_vars_configuration.client_side_validation and initial_price is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_price`, must not be `None`")  # noqa: E501

        self._initial_price = initial_price

    @property
    def notional_reset(self):
        """Gets the notional_reset of this EquitySwap.  # noqa: E501

        Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity).  # noqa: E501

        :return: The notional_reset of this EquitySwap.  # noqa: E501
        :rtype: bool
        """
        return self._notional_reset

    @notional_reset.setter
    def notional_reset(self, notional_reset):
        """Sets the notional_reset of this EquitySwap.

        Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity).  # noqa: E501

        :param notional_reset: The notional_reset of this EquitySwap.  # noqa: E501
        :type notional_reset: bool
        """
        if self.local_vars_configuration.client_side_validation and notional_reset is None:  # noqa: E501
            raise ValueError("Invalid value for `notional_reset`, must not be `None`")  # noqa: E501

        self._notional_reset = notional_reset

    @property
    def quantity(self):
        """Gets the quantity of this EquitySwap.  # noqa: E501

        The quantity or number of shares in the Equity Swap.  # noqa: E501

        :return: The quantity of this EquitySwap.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this EquitySwap.

        The quantity or number of shares in the Equity Swap.  # noqa: E501

        :param quantity: The quantity of this EquitySwap.  # noqa: E501
        :type quantity: float
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def underlying_identifier(self):
        """Gets the underlying_identifier of this EquitySwap.  # noqa: E501

        External market codes and identifiers for the EquitySwap, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  # noqa: E501

        :return: The underlying_identifier of this EquitySwap.  # noqa: E501
        :rtype: str
        """
        return self._underlying_identifier

    @underlying_identifier.setter
    def underlying_identifier(self, underlying_identifier):
        """Sets the underlying_identifier of this EquitySwap.

        External market codes and identifiers for the EquitySwap, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  # noqa: E501

        :param underlying_identifier: The underlying_identifier of this EquitySwap.  # noqa: E501
        :type underlying_identifier: str
        """
        if self.local_vars_configuration.client_side_validation and underlying_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                underlying_identifier is not None and len(underlying_identifier) < 1):
            raise ValueError("Invalid value for `underlying_identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._underlying_identifier = underlying_identifier

    @property
    def equity_swap_dividend_payment_timing(self):
        """Gets the equity_swap_dividend_payment_timing of this EquitySwap.  # noqa: E501

        Determines how the payment of dividends is handled for the equity swap.  Defaults to paying at the next Equity coupon date.                Supported string (enumeration) values are: [PayAtNextEquityCouponDate, PayAtMaturityOfSwap, PayAtNextFundingLegCouponDate, PayAtPaymentDateOfDividendEvent].  # noqa: E501

        :return: The equity_swap_dividend_payment_timing of this EquitySwap.  # noqa: E501
        :rtype: str
        """
        return self._equity_swap_dividend_payment_timing

    @equity_swap_dividend_payment_timing.setter
    def equity_swap_dividend_payment_timing(self, equity_swap_dividend_payment_timing):
        """Sets the equity_swap_dividend_payment_timing of this EquitySwap.

        Determines how the payment of dividends is handled for the equity swap.  Defaults to paying at the next Equity coupon date.                Supported string (enumeration) values are: [PayAtNextEquityCouponDate, PayAtMaturityOfSwap, PayAtNextFundingLegCouponDate, PayAtPaymentDateOfDividendEvent].  # noqa: E501

        :param equity_swap_dividend_payment_timing: The equity_swap_dividend_payment_timing of this EquitySwap.  # noqa: E501
        :type equity_swap_dividend_payment_timing: str
        """

        self._equity_swap_dividend_payment_timing = equity_swap_dividend_payment_timing

    @property
    def instrument_type(self):
        """Gets the instrument_type of this EquitySwap.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :return: The instrument_type of this EquitySwap.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this EquitySwap.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :param instrument_type: The instrument_type of this EquitySwap.  # noqa: E501
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
        if not isinstance(other, EquitySwap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquitySwap):
            return True

        return self.to_dict() != other.to_dict()
