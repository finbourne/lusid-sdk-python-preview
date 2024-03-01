# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.97
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


class CashDividendEventAllOf(object):
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
        'payment_date': 'datetime',
        'ex_date': 'datetime',
        'cash_elections': 'list[CashElection]',
        'announcement_date': 'datetime',
        'record_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'payment_date': 'paymentDate',
        'ex_date': 'exDate',
        'cash_elections': 'cashElections',
        'announcement_date': 'announcementDate',
        'record_date': 'recordDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'payment_date': 'required',
        'ex_date': 'required',
        'cash_elections': 'required',
        'announcement_date': 'optional',
        'record_date': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, payment_date=None, ex_date=None, cash_elections=None, announcement_date=None, record_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """CashDividendEventAllOf - a model defined in OpenAPI"
        
        :param payment_date:  The date the company begins distributing the dividend. (required)
        :type payment_date: datetime
        :param ex_date:  The first business day on which the dividend is not owed to the buying party. (required)
        :type ex_date: datetime
        :param cash_elections:  Possible elections for this event, each keyed with a unique identifier. (required)
        :type cash_elections: list[lusid.CashElection]
        :param announcement_date:  Date on which the dividend is announced by the company.
        :type announcement_date: datetime
        :param record_date:  Date you have to be the holder of record in order to participate in the tender.
        :type record_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._payment_date = None
        self._ex_date = None
        self._cash_elections = None
        self._announcement_date = None
        self._record_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.payment_date = payment_date
        self.ex_date = ex_date
        self.cash_elections = cash_elections
        self.announcement_date = announcement_date
        self.record_date = record_date
        self.instrument_event_type = instrument_event_type

    @property
    def payment_date(self):
        """Gets the payment_date of this CashDividendEventAllOf.  # noqa: E501

        The date the company begins distributing the dividend.  # noqa: E501

        :return: The payment_date of this CashDividendEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this CashDividendEventAllOf.

        The date the company begins distributing the dividend.  # noqa: E501

        :param payment_date: The payment_date of this CashDividendEventAllOf.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def ex_date(self):
        """Gets the ex_date of this CashDividendEventAllOf.  # noqa: E501

        The first business day on which the dividend is not owed to the buying party.  # noqa: E501

        :return: The ex_date of this CashDividendEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this CashDividendEventAllOf.

        The first business day on which the dividend is not owed to the buying party.  # noqa: E501

        :param ex_date: The ex_date of this CashDividendEventAllOf.  # noqa: E501
        :type ex_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and ex_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def cash_elections(self):
        """Gets the cash_elections of this CashDividendEventAllOf.  # noqa: E501

        Possible elections for this event, each keyed with a unique identifier.  # noqa: E501

        :return: The cash_elections of this CashDividendEventAllOf.  # noqa: E501
        :rtype: list[lusid.CashElection]
        """
        return self._cash_elections

    @cash_elections.setter
    def cash_elections(self, cash_elections):
        """Sets the cash_elections of this CashDividendEventAllOf.

        Possible elections for this event, each keyed with a unique identifier.  # noqa: E501

        :param cash_elections: The cash_elections of this CashDividendEventAllOf.  # noqa: E501
        :type cash_elections: list[lusid.CashElection]
        """
        if self.local_vars_configuration.client_side_validation and cash_elections is None:  # noqa: E501
            raise ValueError("Invalid value for `cash_elections`, must not be `None`")  # noqa: E501

        self._cash_elections = cash_elections

    @property
    def announcement_date(self):
        """Gets the announcement_date of this CashDividendEventAllOf.  # noqa: E501

        Date on which the dividend is announced by the company.  # noqa: E501

        :return: The announcement_date of this CashDividendEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this CashDividendEventAllOf.

        Date on which the dividend is announced by the company.  # noqa: E501

        :param announcement_date: The announcement_date of this CashDividendEventAllOf.  # noqa: E501
        :type announcement_date: datetime
        """

        self._announcement_date = announcement_date

    @property
    def record_date(self):
        """Gets the record_date of this CashDividendEventAllOf.  # noqa: E501

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :return: The record_date of this CashDividendEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this CashDividendEventAllOf.

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :param record_date: The record_date of this CashDividendEventAllOf.  # noqa: E501
        :type record_date: datetime
        """

        self._record_date = record_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this CashDividendEventAllOf.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :return: The instrument_event_type of this CashDividendEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this CashDividendEventAllOf.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this CashDividendEventAllOf.  # noqa: E501
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
        if not isinstance(other, CashDividendEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashDividendEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
