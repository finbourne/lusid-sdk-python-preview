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


class FundShareClassAllOf(object):
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
        'short_code': 'str',
        'fund_share_class_type': 'str',
        'distribution_payment_type': 'str',
        'hedging': 'str',
        'dom_ccy': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'short_code': 'shortCode',
        'fund_share_class_type': 'fundShareClassType',
        'distribution_payment_type': 'distributionPaymentType',
        'hedging': 'hedging',
        'dom_ccy': 'domCcy',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'short_code': 'required',
        'fund_share_class_type': 'required',
        'distribution_payment_type': 'required',
        'hedging': 'required',
        'dom_ccy': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, short_code=None, fund_share_class_type=None, distribution_payment_type=None, hedging=None, dom_ccy=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FundShareClassAllOf - a model defined in OpenAPI"
        
        :param short_code:  A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \"A Accumulation Euro Hedged Class\" could become \"A Acc H EUR\". (required)
        :type short_code: str
        :param fund_share_class_type:  The type of distribution that the ShareClass will calculate. Can be either 'Income' or 'Accumulation' - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income.    Supported string (enumeration) values are: [Income, Accumulation]. (required)
        :type fund_share_class_type: str
        :param distribution_payment_type:  The tax treatment applied to any distributions calculated within the ShareClass. Can be either 'Net' (Distribution Calculated net of tax) or 'Gross' (Distribution calculated gross of tax).    Supported string (enumeration) values are: [Gross, Net]. (required)
        :type distribution_payment_type: str
        :param hedging:  A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of it's investment strategy.    Supported string (enumeration) values are: [Invalid, None, ApplyHedging]. (required)
        :type hedging: str
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._short_code = None
        self._fund_share_class_type = None
        self._distribution_payment_type = None
        self._hedging = None
        self._dom_ccy = None
        self._instrument_type = None
        self.discriminator = None

        self.short_code = short_code
        self.fund_share_class_type = fund_share_class_type
        self.distribution_payment_type = distribution_payment_type
        self.hedging = hedging
        self.dom_ccy = dom_ccy
        self.instrument_type = instrument_type

    @property
    def short_code(self):
        """Gets the short_code of this FundShareClassAllOf.  # noqa: E501

        A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \"A Accumulation Euro Hedged Class\" could become \"A Acc H EUR\".  # noqa: E501

        :return: The short_code of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this FundShareClassAllOf.

        A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \"A Accumulation Euro Hedged Class\" could become \"A Acc H EUR\".  # noqa: E501

        :param short_code: The short_code of this FundShareClassAllOf.  # noqa: E501
        :type short_code: str
        """
        if self.local_vars_configuration.client_side_validation and short_code is None:  # noqa: E501
            raise ValueError("Invalid value for `short_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_code is not None and len(short_code) < 1):
            raise ValueError("Invalid value for `short_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_code = short_code

    @property
    def fund_share_class_type(self):
        """Gets the fund_share_class_type of this FundShareClassAllOf.  # noqa: E501

        The type of distribution that the ShareClass will calculate. Can be either 'Income' or 'Accumulation' - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income.    Supported string (enumeration) values are: [Income, Accumulation].  # noqa: E501

        :return: The fund_share_class_type of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fund_share_class_type

    @fund_share_class_type.setter
    def fund_share_class_type(self, fund_share_class_type):
        """Sets the fund_share_class_type of this FundShareClassAllOf.

        The type of distribution that the ShareClass will calculate. Can be either 'Income' or 'Accumulation' - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income.    Supported string (enumeration) values are: [Income, Accumulation].  # noqa: E501

        :param fund_share_class_type: The fund_share_class_type of this FundShareClassAllOf.  # noqa: E501
        :type fund_share_class_type: str
        """
        if self.local_vars_configuration.client_side_validation and fund_share_class_type is None:  # noqa: E501
            raise ValueError("Invalid value for `fund_share_class_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fund_share_class_type is not None and len(fund_share_class_type) < 1):
            raise ValueError("Invalid value for `fund_share_class_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._fund_share_class_type = fund_share_class_type

    @property
    def distribution_payment_type(self):
        """Gets the distribution_payment_type of this FundShareClassAllOf.  # noqa: E501

        The tax treatment applied to any distributions calculated within the ShareClass. Can be either 'Net' (Distribution Calculated net of tax) or 'Gross' (Distribution calculated gross of tax).    Supported string (enumeration) values are: [Gross, Net].  # noqa: E501

        :return: The distribution_payment_type of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._distribution_payment_type

    @distribution_payment_type.setter
    def distribution_payment_type(self, distribution_payment_type):
        """Sets the distribution_payment_type of this FundShareClassAllOf.

        The tax treatment applied to any distributions calculated within the ShareClass. Can be either 'Net' (Distribution Calculated net of tax) or 'Gross' (Distribution calculated gross of tax).    Supported string (enumeration) values are: [Gross, Net].  # noqa: E501

        :param distribution_payment_type: The distribution_payment_type of this FundShareClassAllOf.  # noqa: E501
        :type distribution_payment_type: str
        """
        if self.local_vars_configuration.client_side_validation and distribution_payment_type is None:  # noqa: E501
            raise ValueError("Invalid value for `distribution_payment_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                distribution_payment_type is not None and len(distribution_payment_type) < 1):
            raise ValueError("Invalid value for `distribution_payment_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._distribution_payment_type = distribution_payment_type

    @property
    def hedging(self):
        """Gets the hedging of this FundShareClassAllOf.  # noqa: E501

        A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of it's investment strategy.    Supported string (enumeration) values are: [Invalid, None, ApplyHedging].  # noqa: E501

        :return: The hedging of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hedging

    @hedging.setter
    def hedging(self, hedging):
        """Sets the hedging of this FundShareClassAllOf.

        A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of it's investment strategy.    Supported string (enumeration) values are: [Invalid, None, ApplyHedging].  # noqa: E501

        :param hedging: The hedging of this FundShareClassAllOf.  # noqa: E501
        :type hedging: str
        """
        if self.local_vars_configuration.client_side_validation and hedging is None:  # noqa: E501
            raise ValueError("Invalid value for `hedging`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hedging is not None and len(hedging) < 1):
            raise ValueError("Invalid value for `hedging`, length must be greater than or equal to `1`")  # noqa: E501

        self._hedging = hedging

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FundShareClassAllOf.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FundShareClassAllOf.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this FundShareClassAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FundShareClassAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan  # noqa: E501

        :return: The instrument_type of this FundShareClassAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FundShareClassAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan  # noqa: E501

        :param instrument_type: The instrument_type of this FundShareClassAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan", "TotalReturnSwap", "InflationLeg", "FundShareClass", "FlexibleLoan"]  # noqa: E501
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
        if not isinstance(other, FundShareClassAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundShareClassAllOf):
            return True

        return self.to_dict() != other.to_dict()
