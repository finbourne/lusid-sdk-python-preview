# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.236
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


class FxForwardSettlementEventAllOf(object):
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
        'maturity_date': 'datetime',
        'dom_amount_per_unit': 'float',
        'dom_ccy': 'str',
        'fgn_amount_per_unit': 'float',
        'fgn_ccy': 'str',
        'is_ndf': 'bool',
        'fixing_date': 'datetime',
        'settlement_ccy': 'str',
        'cash_flow_per_unit': 'float',
        'domestic_to_foreign_rate': 'float',
        'domestic_to_settlement_rate': 'float',
        'foreign_to_settlement_rate': 'float',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'maturity_date': 'maturityDate',
        'dom_amount_per_unit': 'domAmountPerUnit',
        'dom_ccy': 'domCcy',
        'fgn_amount_per_unit': 'fgnAmountPerUnit',
        'fgn_ccy': 'fgnCcy',
        'is_ndf': 'isNdf',
        'fixing_date': 'fixingDate',
        'settlement_ccy': 'settlementCcy',
        'cash_flow_per_unit': 'cashFlowPerUnit',
        'domestic_to_foreign_rate': 'domesticToForeignRate',
        'domestic_to_settlement_rate': 'domesticToSettlementRate',
        'foreign_to_settlement_rate': 'foreignToSettlementRate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'maturity_date': 'required',
        'dom_amount_per_unit': 'required',
        'dom_ccy': 'required',
        'fgn_amount_per_unit': 'required',
        'fgn_ccy': 'required',
        'is_ndf': 'required',
        'fixing_date': 'optional',
        'settlement_ccy': 'optional',
        'cash_flow_per_unit': 'optional',
        'domestic_to_foreign_rate': 'optional',
        'domestic_to_settlement_rate': 'optional',
        'foreign_to_settlement_rate': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, maturity_date=None, dom_amount_per_unit=None, dom_ccy=None, fgn_amount_per_unit=None, fgn_ccy=None, is_ndf=None, fixing_date=None, settlement_ccy=None, cash_flow_per_unit=None, domestic_to_foreign_rate=None, domestic_to_settlement_rate=None, foreign_to_settlement_rate=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardSettlementEventAllOf - a model defined in OpenAPI"
        
        :param maturity_date:  Maturity date of the forward (required)
        :type maturity_date: datetime
        :param dom_amount_per_unit:  Amount per unit in the DomCcy (domestic currency) (required)
        :type dom_amount_per_unit: float
        :param dom_ccy:  The domestic currency of the forward (required)
        :type dom_ccy: str
        :param fgn_amount_per_unit:  Amount per unit in the FgnCcy (foreign currency) (required)
        :type fgn_amount_per_unit: float
        :param fgn_ccy:  The foreign currency of the forward. (required)
        :type fgn_ccy: str
        :param is_ndf:  Is this settlement corresponding to a deliverable forward, or an NDF (required)
        :type is_ndf: bool
        :param fixing_date:  Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  Date of the FxRate fixings.
        :type fixing_date: datetime
        :param settlement_ccy:  Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  May be set to either DomCcy or FgnCcy, or a third currency.
        :type settlement_ccy: str
        :param cash_flow_per_unit:  Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  CashFlow per unit.  Paid in the SettlementCcy.
        :type cash_flow_per_unit: float
        :param domestic_to_foreign_rate:  Domestic currency to foreign currency FX rate.  Not required, only used to override quotes.
        :type domestic_to_foreign_rate: float
        :param domestic_to_settlement_rate:  Domestic currency to settlement currency FX rate  Not required, only used to override quotes.
        :type domestic_to_settlement_rate: float
        :param foreign_to_settlement_rate:  Foreign currency to settlement currency FX rate  Not required, only used to override quotes.
        :type foreign_to_settlement_rate: float
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._maturity_date = None
        self._dom_amount_per_unit = None
        self._dom_ccy = None
        self._fgn_amount_per_unit = None
        self._fgn_ccy = None
        self._is_ndf = None
        self._fixing_date = None
        self._settlement_ccy = None
        self._cash_flow_per_unit = None
        self._domestic_to_foreign_rate = None
        self._domestic_to_settlement_rate = None
        self._foreign_to_settlement_rate = None
        self._instrument_event_type = None
        self.discriminator = None

        self.maturity_date = maturity_date
        self.dom_amount_per_unit = dom_amount_per_unit
        self.dom_ccy = dom_ccy
        self.fgn_amount_per_unit = fgn_amount_per_unit
        self.fgn_ccy = fgn_ccy
        self.is_ndf = is_ndf
        self.fixing_date = fixing_date
        self.settlement_ccy = settlement_ccy
        self.cash_flow_per_unit = cash_flow_per_unit
        self.domestic_to_foreign_rate = domestic_to_foreign_rate
        self.domestic_to_settlement_rate = domestic_to_settlement_rate
        self.foreign_to_settlement_rate = foreign_to_settlement_rate
        self.instrument_event_type = instrument_event_type

    @property
    def maturity_date(self):
        """Gets the maturity_date of this FxForwardSettlementEventAllOf.  # noqa: E501

        Maturity date of the forward  # noqa: E501

        :return: The maturity_date of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this FxForwardSettlementEventAllOf.

        Maturity date of the forward  # noqa: E501

        :param maturity_date: The maturity_date of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def dom_amount_per_unit(self):
        """Gets the dom_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501

        Amount per unit in the DomCcy (domestic currency)  # noqa: E501

        :return: The dom_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._dom_amount_per_unit

    @dom_amount_per_unit.setter
    def dom_amount_per_unit(self, dom_amount_per_unit):
        """Sets the dom_amount_per_unit of this FxForwardSettlementEventAllOf.

        Amount per unit in the DomCcy (domestic currency)  # noqa: E501

        :param dom_amount_per_unit: The dom_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type dom_amount_per_unit: float
        """
        if self.local_vars_configuration.client_side_validation and dom_amount_per_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_amount_per_unit`, must not be `None`")  # noqa: E501

        self._dom_amount_per_unit = dom_amount_per_unit

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501

        The domestic currency of the forward  # noqa: E501

        :return: The dom_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxForwardSettlementEventAllOf.

        The domestic currency of the forward  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_amount_per_unit(self):
        """Gets the fgn_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501

        Amount per unit in the FgnCcy (foreign currency)  # noqa: E501

        :return: The fgn_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._fgn_amount_per_unit

    @fgn_amount_per_unit.setter
    def fgn_amount_per_unit(self, fgn_amount_per_unit):
        """Sets the fgn_amount_per_unit of this FxForwardSettlementEventAllOf.

        Amount per unit in the FgnCcy (foreign currency)  # noqa: E501

        :param fgn_amount_per_unit: The fgn_amount_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type fgn_amount_per_unit: float
        """
        if self.local_vars_configuration.client_side_validation and fgn_amount_per_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_amount_per_unit`, must not be `None`")  # noqa: E501

        self._fgn_amount_per_unit = fgn_amount_per_unit

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501

        The foreign currency of the forward.  # noqa: E501

        :return: The fgn_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxForwardSettlementEventAllOf.

        The foreign currency of the forward.  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def is_ndf(self):
        """Gets the is_ndf of this FxForwardSettlementEventAllOf.  # noqa: E501

        Is this settlement corresponding to a deliverable forward, or an NDF  # noqa: E501

        :return: The is_ndf of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_ndf

    @is_ndf.setter
    def is_ndf(self, is_ndf):
        """Sets the is_ndf of this FxForwardSettlementEventAllOf.

        Is this settlement corresponding to a deliverable forward, or an NDF  # noqa: E501

        :param is_ndf: The is_ndf of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type is_ndf: bool
        """
        if self.local_vars_configuration.client_side_validation and is_ndf is None:  # noqa: E501
            raise ValueError("Invalid value for `is_ndf`, must not be `None`")  # noqa: E501

        self._is_ndf = is_ndf

    @property
    def fixing_date(self):
        """Gets the fixing_date of this FxForwardSettlementEventAllOf.  # noqa: E501

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  Date of the FxRate fixings.  # noqa: E501

        :return: The fixing_date of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._fixing_date

    @fixing_date.setter
    def fixing_date(self, fixing_date):
        """Sets the fixing_date of this FxForwardSettlementEventAllOf.

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  Date of the FxRate fixings.  # noqa: E501

        :param fixing_date: The fixing_date of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type fixing_date: datetime
        """

        self._fixing_date = fixing_date

    @property
    def settlement_ccy(self):
        """Gets the settlement_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  May be set to either DomCcy or FgnCcy, or a third currency.  # noqa: E501

        :return: The settlement_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._settlement_ccy

    @settlement_ccy.setter
    def settlement_ccy(self, settlement_ccy):
        """Sets the settlement_ccy of this FxForwardSettlementEventAllOf.

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  May be set to either DomCcy or FgnCcy, or a third currency.  # noqa: E501

        :param settlement_ccy: The settlement_ccy of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type settlement_ccy: str
        """

        self._settlement_ccy = settlement_ccy

    @property
    def cash_flow_per_unit(self):
        """Gets the cash_flow_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  CashFlow per unit.  Paid in the SettlementCcy.  # noqa: E501

        :return: The cash_flow_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._cash_flow_per_unit

    @cash_flow_per_unit.setter
    def cash_flow_per_unit(self, cash_flow_per_unit):
        """Sets the cash_flow_per_unit of this FxForwardSettlementEventAllOf.

        Optional.  Required if the event is an NDF (i.e. if IsNdf = true).  CashFlow per unit.  Paid in the SettlementCcy.  # noqa: E501

        :param cash_flow_per_unit: The cash_flow_per_unit of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type cash_flow_per_unit: float
        """

        self._cash_flow_per_unit = cash_flow_per_unit

    @property
    def domestic_to_foreign_rate(self):
        """Gets the domestic_to_foreign_rate of this FxForwardSettlementEventAllOf.  # noqa: E501

        Domestic currency to foreign currency FX rate.  Not required, only used to override quotes.  # noqa: E501

        :return: The domestic_to_foreign_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._domestic_to_foreign_rate

    @domestic_to_foreign_rate.setter
    def domestic_to_foreign_rate(self, domestic_to_foreign_rate):
        """Sets the domestic_to_foreign_rate of this FxForwardSettlementEventAllOf.

        Domestic currency to foreign currency FX rate.  Not required, only used to override quotes.  # noqa: E501

        :param domestic_to_foreign_rate: The domestic_to_foreign_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type domestic_to_foreign_rate: float
        """

        self._domestic_to_foreign_rate = domestic_to_foreign_rate

    @property
    def domestic_to_settlement_rate(self):
        """Gets the domestic_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501

        Domestic currency to settlement currency FX rate  Not required, only used to override quotes.  # noqa: E501

        :return: The domestic_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._domestic_to_settlement_rate

    @domestic_to_settlement_rate.setter
    def domestic_to_settlement_rate(self, domestic_to_settlement_rate):
        """Sets the domestic_to_settlement_rate of this FxForwardSettlementEventAllOf.

        Domestic currency to settlement currency FX rate  Not required, only used to override quotes.  # noqa: E501

        :param domestic_to_settlement_rate: The domestic_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type domestic_to_settlement_rate: float
        """

        self._domestic_to_settlement_rate = domestic_to_settlement_rate

    @property
    def foreign_to_settlement_rate(self):
        """Gets the foreign_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501

        Foreign currency to settlement currency FX rate  Not required, only used to override quotes.  # noqa: E501

        :return: The foreign_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._foreign_to_settlement_rate

    @foreign_to_settlement_rate.setter
    def foreign_to_settlement_rate(self, foreign_to_settlement_rate):
        """Sets the foreign_to_settlement_rate of this FxForwardSettlementEventAllOf.

        Foreign currency to settlement currency FX rate  Not required, only used to override quotes.  # noqa: E501

        :param foreign_to_settlement_rate: The foreign_to_settlement_rate of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type foreign_to_settlement_rate: float
        """

        self._foreign_to_settlement_rate = foreign_to_settlement_rate

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this FxForwardSettlementEventAllOf.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent  # noqa: E501

        :return: The instrument_event_type of this FxForwardSettlementEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this FxForwardSettlementEventAllOf.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this FxForwardSettlementEventAllOf.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent", "ExpiryEvent", "ScripDividendEvent", "StockDividendEvent", "ReverseStockSplitEvent", "CapitalDistributionEvent", "SpinOffEvent", "MergerEvent", "FutureExpiryEvent", "SwapCashFlowEvent", "SwapPrincipalEvent", "CreditPremiumCashFlowEvent", "CdsCreditEvent", "CdxCreditEvent", "MbsCouponEvent", "MbsPrincipalEvent", "BonusIssueEvent", "MbsPrincipalWriteOffEvent", "MbsInterestDeferralEvent"]  # noqa: E501
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
        if not isinstance(other, FxForwardSettlementEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardSettlementEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
