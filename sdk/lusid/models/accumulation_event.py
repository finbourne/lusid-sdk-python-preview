# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.123
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


class AccumulationEvent(object):
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
        'dividend_currency': 'str',
        'dividend_rate': 'float',
        'ex_date': 'datetime',
        'payment_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'announcement_date': 'announcementDate',
        'dividend_currency': 'dividendCurrency',
        'dividend_rate': 'dividendRate',
        'ex_date': 'exDate',
        'payment_date': 'paymentDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'announcement_date': 'optional',
        'dividend_currency': 'required',
        'dividend_rate': 'required',
        'ex_date': 'required',
        'payment_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, announcement_date=None, dividend_currency=None, dividend_rate=None, ex_date=None, payment_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """AccumulationEvent - a model defined in OpenAPI"
        
        :param announcement_date:  Date on which the dividend was announced / declared.
        :type announcement_date: datetime
        :param dividend_currency:  Payment currency (required)
        :type dividend_currency: str
        :param dividend_rate:  Dividend rate or payment rate as a percentage.  i.e. 5% is written as 0.05 (required)
        :type dividend_rate: float
        :param ex_date:  The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. (required)
        :type ex_date: datetime
        :param payment_date:  The date the company pays out dividends to shareholders. (required)
        :type payment_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._announcement_date = None
        self._dividend_currency = None
        self._dividend_rate = None
        self._ex_date = None
        self._payment_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.announcement_date = announcement_date
        self.dividend_currency = dividend_currency
        self.dividend_rate = dividend_rate
        self.ex_date = ex_date
        self.payment_date = payment_date
        self.instrument_event_type = instrument_event_type

    @property
    def announcement_date(self):
        """Gets the announcement_date of this AccumulationEvent.  # noqa: E501

        Date on which the dividend was announced / declared.  # noqa: E501

        :return: The announcement_date of this AccumulationEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this AccumulationEvent.

        Date on which the dividend was announced / declared.  # noqa: E501

        :param announcement_date: The announcement_date of this AccumulationEvent.  # noqa: E501
        :type announcement_date: datetime
        """

        self._announcement_date = announcement_date

    @property
    def dividend_currency(self):
        """Gets the dividend_currency of this AccumulationEvent.  # noqa: E501

        Payment currency  # noqa: E501

        :return: The dividend_currency of this AccumulationEvent.  # noqa: E501
        :rtype: str
        """
        return self._dividend_currency

    @dividend_currency.setter
    def dividend_currency(self, dividend_currency):
        """Sets the dividend_currency of this AccumulationEvent.

        Payment currency  # noqa: E501

        :param dividend_currency: The dividend_currency of this AccumulationEvent.  # noqa: E501
        :type dividend_currency: str
        """
        if self.local_vars_configuration.client_side_validation and dividend_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `dividend_currency`, must not be `None`")  # noqa: E501

        self._dividend_currency = dividend_currency

    @property
    def dividend_rate(self):
        """Gets the dividend_rate of this AccumulationEvent.  # noqa: E501

        Dividend rate or payment rate as a percentage.  i.e. 5% is written as 0.05  # noqa: E501

        :return: The dividend_rate of this AccumulationEvent.  # noqa: E501
        :rtype: float
        """
        return self._dividend_rate

    @dividend_rate.setter
    def dividend_rate(self, dividend_rate):
        """Sets the dividend_rate of this AccumulationEvent.

        Dividend rate or payment rate as a percentage.  i.e. 5% is written as 0.05  # noqa: E501

        :param dividend_rate: The dividend_rate of this AccumulationEvent.  # noqa: E501
        :type dividend_rate: float
        """
        if self.local_vars_configuration.client_side_validation and dividend_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `dividend_rate`, must not be `None`")  # noqa: E501

        self._dividend_rate = dividend_rate

    @property
    def ex_date(self):
        """Gets the ex_date of this AccumulationEvent.  # noqa: E501

        The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.  # noqa: E501

        :return: The ex_date of this AccumulationEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this AccumulationEvent.

        The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.  # noqa: E501

        :param ex_date: The ex_date of this AccumulationEvent.  # noqa: E501
        :type ex_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and ex_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def payment_date(self):
        """Gets the payment_date of this AccumulationEvent.  # noqa: E501

        The date the company pays out dividends to shareholders.  # noqa: E501

        :return: The payment_date of this AccumulationEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this AccumulationEvent.

        The date the company pays out dividends to shareholders.  # noqa: E501

        :param payment_date: The payment_date of this AccumulationEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this AccumulationEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :return: The instrument_event_type of this AccumulationEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this AccumulationEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this AccumulationEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent"]  # noqa: E501
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
        if not isinstance(other, AccumulationEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccumulationEvent):
            return True

        return self.to_dict() != other.to_dict()
