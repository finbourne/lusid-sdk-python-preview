# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.224
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


class CreditPremiumCashFlowEvent(object):
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
        'ex_date': 'datetime',
        'payment_date': 'datetime',
        'currency': 'str',
        'cash_flow_per_unit': 'float',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'ex_date': 'exDate',
        'payment_date': 'paymentDate',
        'currency': 'currency',
        'cash_flow_per_unit': 'cashFlowPerUnit',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'ex_date': 'required',
        'payment_date': 'required',
        'currency': 'required',
        'cash_flow_per_unit': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, ex_date=None, payment_date=None, currency=None, cash_flow_per_unit=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """CreditPremiumCashFlowEvent - a model defined in OpenAPI"
        
        :param ex_date:  The ex-dividend date of the cashflow. (required)
        :type ex_date: datetime
        :param payment_date:  The payment date of the cashflow. (required)
        :type payment_date: datetime
        :param currency:  The currency in which the cashflow is paid. (required)
        :type currency: str
        :param cash_flow_per_unit:  The cashflow amount received for each unit of the instrument held on the ex date.
        :type cash_flow_per_unit: float
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ex_date = None
        self._payment_date = None
        self._currency = None
        self._cash_flow_per_unit = None
        self._instrument_event_type = None
        self.discriminator = None

        self.ex_date = ex_date
        self.payment_date = payment_date
        self.currency = currency
        self.cash_flow_per_unit = cash_flow_per_unit
        self.instrument_event_type = instrument_event_type

    @property
    def ex_date(self):
        """Gets the ex_date of this CreditPremiumCashFlowEvent.  # noqa: E501

        The ex-dividend date of the cashflow.  # noqa: E501

        :return: The ex_date of this CreditPremiumCashFlowEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this CreditPremiumCashFlowEvent.

        The ex-dividend date of the cashflow.  # noqa: E501

        :param ex_date: The ex_date of this CreditPremiumCashFlowEvent.  # noqa: E501
        :type ex_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and ex_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def payment_date(self):
        """Gets the payment_date of this CreditPremiumCashFlowEvent.  # noqa: E501

        The payment date of the cashflow.  # noqa: E501

        :return: The payment_date of this CreditPremiumCashFlowEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this CreditPremiumCashFlowEvent.

        The payment date of the cashflow.  # noqa: E501

        :param payment_date: The payment_date of this CreditPremiumCashFlowEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def currency(self):
        """Gets the currency of this CreditPremiumCashFlowEvent.  # noqa: E501

        The currency in which the cashflow is paid.  # noqa: E501

        :return: The currency of this CreditPremiumCashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditPremiumCashFlowEvent.

        The currency in which the cashflow is paid.  # noqa: E501

        :param currency: The currency of this CreditPremiumCashFlowEvent.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def cash_flow_per_unit(self):
        """Gets the cash_flow_per_unit of this CreditPremiumCashFlowEvent.  # noqa: E501

        The cashflow amount received for each unit of the instrument held on the ex date.  # noqa: E501

        :return: The cash_flow_per_unit of this CreditPremiumCashFlowEvent.  # noqa: E501
        :rtype: float
        """
        return self._cash_flow_per_unit

    @cash_flow_per_unit.setter
    def cash_flow_per_unit(self, cash_flow_per_unit):
        """Sets the cash_flow_per_unit of this CreditPremiumCashFlowEvent.

        The cashflow amount received for each unit of the instrument held on the ex date.  # noqa: E501

        :param cash_flow_per_unit: The cash_flow_per_unit of this CreditPremiumCashFlowEvent.  # noqa: E501
        :type cash_flow_per_unit: float
        """

        self._cash_flow_per_unit = cash_flow_per_unit

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this CreditPremiumCashFlowEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent  # noqa: E501

        :return: The instrument_event_type of this CreditPremiumCashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this CreditPremiumCashFlowEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this CreditPremiumCashFlowEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent", "ExpiryEvent", "ScripDividendEvent", "StockDividendEvent", "ReverseStockSplitEvent", "CapitalDistributionEvent", "SpinOffEvent", "MergerEvent", "FutureExpiryEvent", "SwapCashFlowEvent", "SwapPrincipalEvent", "CreditPremiumCashFlowEvent", "CdsCreditEvent", "CdxCreditEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, CreditPremiumCashFlowEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditPremiumCashFlowEvent):
            return True

        return self.to_dict() != other.to_dict()
