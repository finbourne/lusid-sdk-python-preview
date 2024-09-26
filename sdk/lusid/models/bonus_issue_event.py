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


class BonusIssueEvent(object):
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
        'announcement_date': 'datetime',
        'ex_date': 'datetime',
        'record_date': 'datetime',
        'payment_date': 'datetime',
        'fractional_units_cash_price': 'float',
        'fractional_units_cash_currency': 'str',
        'security_offer_elections': 'list[SecurityOfferElection]',
        'cash_offer_elections': 'list[CashOfferElection]',
        'lapse_elections': 'list[LapseElection]',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'announcement_date': 'announcementDate',
        'ex_date': 'exDate',
        'record_date': 'recordDate',
        'payment_date': 'paymentDate',
        'fractional_units_cash_price': 'fractionalUnitsCashPrice',
        'fractional_units_cash_currency': 'fractionalUnitsCashCurrency',
        'security_offer_elections': 'securityOfferElections',
        'cash_offer_elections': 'cashOfferElections',
        'lapse_elections': 'lapseElections',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'announcement_date': 'optional',
        'ex_date': 'required',
        'record_date': 'optional',
        'payment_date': 'required',
        'fractional_units_cash_price': 'optional',
        'fractional_units_cash_currency': 'optional',
        'security_offer_elections': 'optional',
        'cash_offer_elections': 'optional',
        'lapse_elections': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, announcement_date=None, ex_date=None, record_date=None, payment_date=None, fractional_units_cash_price=None, fractional_units_cash_currency=None, security_offer_elections=None, cash_offer_elections=None, lapse_elections=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """BonusIssueEvent - a model defined in OpenAPI"
        
        :param announcement_date:  The date the Bonus Issue is announced.
        :type announcement_date: datetime
        :param ex_date:  The ex-date of the Bonus Issue. (required)
        :type ex_date: datetime
        :param record_date:  The record date of the Bonus Issue.
        :type record_date: datetime
        :param payment_date:  The date the Bonus Issue is executed. (required)
        :type payment_date: datetime
        :param fractional_units_cash_price:  Optional. Used in calculating cash-in-lieu of fractional shares.
        :type fractional_units_cash_price: float
        :param fractional_units_cash_currency:  Optional. Used in calculating cash-in-lieu of fractional shares.
        :type fractional_units_cash_currency: str
        :param security_offer_elections:  Possible SecurityElections for this Bonus Issue event, if any.
        :type security_offer_elections: list[lusid.SecurityOfferElection]
        :param cash_offer_elections:  Possible CashOfferElections for this Bonus Issue event, if any.
        :type cash_offer_elections: list[lusid.CashOfferElection]
        :param lapse_elections:  Possible LapseElections for this Bonus Issue event, if any.
        :type lapse_elections: list[lusid.LapseElection]
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._announcement_date = None
        self._ex_date = None
        self._record_date = None
        self._payment_date = None
        self._fractional_units_cash_price = None
        self._fractional_units_cash_currency = None
        self._security_offer_elections = None
        self._cash_offer_elections = None
        self._lapse_elections = None
        self._instrument_event_type = None
        self.discriminator = None

        self.announcement_date = announcement_date
        self.ex_date = ex_date
        self.record_date = record_date
        self.payment_date = payment_date
        self.fractional_units_cash_price = fractional_units_cash_price
        self.fractional_units_cash_currency = fractional_units_cash_currency
        self.security_offer_elections = security_offer_elections
        self.cash_offer_elections = cash_offer_elections
        self.lapse_elections = lapse_elections
        self.instrument_event_type = instrument_event_type

    @property
    def announcement_date(self):
        """Gets the announcement_date of this BonusIssueEvent.  # noqa: E501

        The date the Bonus Issue is announced.  # noqa: E501

        :return: The announcement_date of this BonusIssueEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this BonusIssueEvent.

        The date the Bonus Issue is announced.  # noqa: E501

        :param announcement_date: The announcement_date of this BonusIssueEvent.  # noqa: E501
        :type announcement_date: datetime
        """

        self._announcement_date = announcement_date

    @property
    def ex_date(self):
        """Gets the ex_date of this BonusIssueEvent.  # noqa: E501

        The ex-date of the Bonus Issue.  # noqa: E501

        :return: The ex_date of this BonusIssueEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this BonusIssueEvent.

        The ex-date of the Bonus Issue.  # noqa: E501

        :param ex_date: The ex_date of this BonusIssueEvent.  # noqa: E501
        :type ex_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and ex_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def record_date(self):
        """Gets the record_date of this BonusIssueEvent.  # noqa: E501

        The record date of the Bonus Issue.  # noqa: E501

        :return: The record_date of this BonusIssueEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this BonusIssueEvent.

        The record date of the Bonus Issue.  # noqa: E501

        :param record_date: The record_date of this BonusIssueEvent.  # noqa: E501
        :type record_date: datetime
        """

        self._record_date = record_date

    @property
    def payment_date(self):
        """Gets the payment_date of this BonusIssueEvent.  # noqa: E501

        The date the Bonus Issue is executed.  # noqa: E501

        :return: The payment_date of this BonusIssueEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this BonusIssueEvent.

        The date the Bonus Issue is executed.  # noqa: E501

        :param payment_date: The payment_date of this BonusIssueEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def fractional_units_cash_price(self):
        """Gets the fractional_units_cash_price of this BonusIssueEvent.  # noqa: E501

        Optional. Used in calculating cash-in-lieu of fractional shares.  # noqa: E501

        :return: The fractional_units_cash_price of this BonusIssueEvent.  # noqa: E501
        :rtype: float
        """
        return self._fractional_units_cash_price

    @fractional_units_cash_price.setter
    def fractional_units_cash_price(self, fractional_units_cash_price):
        """Sets the fractional_units_cash_price of this BonusIssueEvent.

        Optional. Used in calculating cash-in-lieu of fractional shares.  # noqa: E501

        :param fractional_units_cash_price: The fractional_units_cash_price of this BonusIssueEvent.  # noqa: E501
        :type fractional_units_cash_price: float
        """

        self._fractional_units_cash_price = fractional_units_cash_price

    @property
    def fractional_units_cash_currency(self):
        """Gets the fractional_units_cash_currency of this BonusIssueEvent.  # noqa: E501

        Optional. Used in calculating cash-in-lieu of fractional shares.  # noqa: E501

        :return: The fractional_units_cash_currency of this BonusIssueEvent.  # noqa: E501
        :rtype: str
        """
        return self._fractional_units_cash_currency

    @fractional_units_cash_currency.setter
    def fractional_units_cash_currency(self, fractional_units_cash_currency):
        """Sets the fractional_units_cash_currency of this BonusIssueEvent.

        Optional. Used in calculating cash-in-lieu of fractional shares.  # noqa: E501

        :param fractional_units_cash_currency: The fractional_units_cash_currency of this BonusIssueEvent.  # noqa: E501
        :type fractional_units_cash_currency: str
        """

        self._fractional_units_cash_currency = fractional_units_cash_currency

    @property
    def security_offer_elections(self):
        """Gets the security_offer_elections of this BonusIssueEvent.  # noqa: E501

        Possible SecurityElections for this Bonus Issue event, if any.  # noqa: E501

        :return: The security_offer_elections of this BonusIssueEvent.  # noqa: E501
        :rtype: list[lusid.SecurityOfferElection]
        """
        return self._security_offer_elections

    @security_offer_elections.setter
    def security_offer_elections(self, security_offer_elections):
        """Sets the security_offer_elections of this BonusIssueEvent.

        Possible SecurityElections for this Bonus Issue event, if any.  # noqa: E501

        :param security_offer_elections: The security_offer_elections of this BonusIssueEvent.  # noqa: E501
        :type security_offer_elections: list[lusid.SecurityOfferElection]
        """

        self._security_offer_elections = security_offer_elections

    @property
    def cash_offer_elections(self):
        """Gets the cash_offer_elections of this BonusIssueEvent.  # noqa: E501

        Possible CashOfferElections for this Bonus Issue event, if any.  # noqa: E501

        :return: The cash_offer_elections of this BonusIssueEvent.  # noqa: E501
        :rtype: list[lusid.CashOfferElection]
        """
        return self._cash_offer_elections

    @cash_offer_elections.setter
    def cash_offer_elections(self, cash_offer_elections):
        """Sets the cash_offer_elections of this BonusIssueEvent.

        Possible CashOfferElections for this Bonus Issue event, if any.  # noqa: E501

        :param cash_offer_elections: The cash_offer_elections of this BonusIssueEvent.  # noqa: E501
        :type cash_offer_elections: list[lusid.CashOfferElection]
        """

        self._cash_offer_elections = cash_offer_elections

    @property
    def lapse_elections(self):
        """Gets the lapse_elections of this BonusIssueEvent.  # noqa: E501

        Possible LapseElections for this Bonus Issue event, if any.  # noqa: E501

        :return: The lapse_elections of this BonusIssueEvent.  # noqa: E501
        :rtype: list[lusid.LapseElection]
        """
        return self._lapse_elections

    @lapse_elections.setter
    def lapse_elections(self, lapse_elections):
        """Sets the lapse_elections of this BonusIssueEvent.

        Possible LapseElections for this Bonus Issue event, if any.  # noqa: E501

        :param lapse_elections: The lapse_elections of this BonusIssueEvent.  # noqa: E501
        :type lapse_elections: list[lusid.LapseElection]
        """

        self._lapse_elections = lapse_elections

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this BonusIssueEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent  # noqa: E501

        :return: The instrument_event_type of this BonusIssueEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this BonusIssueEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this BonusIssueEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent", "ExpiryEvent", "ScripDividendEvent", "StockDividendEvent", "ReverseStockSplitEvent", "CapitalDistributionEvent", "SpinOffEvent", "MergerEvent", "FutureExpiryEvent", "SwapCashFlowEvent", "SwapPrincipalEvent", "CreditPremiumCashFlowEvent", "CdsCreditEvent", "CdxCreditEvent", "MbsCouponEvent", "MbsPrincipalEvent", "BonusIssueEvent"]  # noqa: E501
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
        if not isinstance(other, BonusIssueEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BonusIssueEvent):
            return True

        return self.to_dict() != other.to_dict()
