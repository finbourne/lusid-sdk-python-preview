# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4448
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


class InstrumentPaymentDiaryRow(object):
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
        'quantity': 'float',
        'currency': 'str',
        'payment_date': 'datetime',
        'pay_or_receive': 'str',
        'accrual_start': 'datetime',
        'accrual_end': 'datetime',
        'cash_flow_type': 'str',
        'is_cash_flow_determined': 'bool',
        'is_cash_flow_historic': 'bool',
        'discount_factor': 'float',
        'discounted_expected_cash_flow_amount': 'float',
        'day_count_fraction': 'float',
        'forward_rate': 'float',
        'reset_rate': 'float',
        'spread': 'float'
    }

    attribute_map = {
        'quantity': 'quantity',
        'currency': 'currency',
        'payment_date': 'paymentDate',
        'pay_or_receive': 'payOrReceive',
        'accrual_start': 'accrualStart',
        'accrual_end': 'accrualEnd',
        'cash_flow_type': 'cashFlowType',
        'is_cash_flow_determined': 'isCashFlowDetermined',
        'is_cash_flow_historic': 'isCashFlowHistoric',
        'discount_factor': 'discountFactor',
        'discounted_expected_cash_flow_amount': 'discountedExpectedCashFlowAmount',
        'day_count_fraction': 'dayCountFraction',
        'forward_rate': 'forwardRate',
        'reset_rate': 'resetRate',
        'spread': 'spread'
    }

    required_map = {
        'quantity': 'optional',
        'currency': 'optional',
        'payment_date': 'optional',
        'pay_or_receive': 'optional',
        'accrual_start': 'optional',
        'accrual_end': 'optional',
        'cash_flow_type': 'optional',
        'is_cash_flow_determined': 'optional',
        'is_cash_flow_historic': 'optional',
        'discount_factor': 'optional',
        'discounted_expected_cash_flow_amount': 'optional',
        'day_count_fraction': 'optional',
        'forward_rate': 'optional',
        'reset_rate': 'optional',
        'spread': 'optional'
    }

    def __init__(self, quantity=None, currency=None, payment_date=None, pay_or_receive=None, accrual_start=None, accrual_end=None, cash_flow_type=None, is_cash_flow_determined=None, is_cash_flow_historic=None, discount_factor=None, discounted_expected_cash_flow_amount=None, day_count_fraction=None, forward_rate=None, reset_rate=None, spread=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentPaymentDiaryRow - a model defined in OpenAPI"
        
        :param quantity:  The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.
        :type quantity: float
        :param currency:  The payment currency of the cash flow.
        :type currency: str
        :param payment_date:  The date at which the given cash flow is due to be paid.
        :type payment_date: datetime
        :param pay_or_receive:  Does the cash flow belong to the Pay or Receive leg.
        :type pay_or_receive: str
        :param accrual_start:  The date on which accruals start for this cashflow.
        :type accrual_start: datetime
        :param accrual_end:  The date on which accruals end for this cashflow.
        :type accrual_end: datetime
        :param cash_flow_type:  The type of cashflow.
        :type cash_flow_type: str
        :param is_cash_flow_determined:  Is the cashflow determined as of the effective date time.
        :type is_cash_flow_determined: bool
        :param is_cash_flow_historic:  Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt.
        :type is_cash_flow_historic: bool
        :param discount_factor:  Weighting factor to discount cashflow to the present value.
        :type discount_factor: float
        :param discounted_expected_cash_flow_amount:  The expected cashflow amount taking into account the discount factor.
        :type discounted_expected_cash_flow_amount: float
        :param day_count_fraction:  The day count fraction, if appropriate.
        :type day_count_fraction: float
        :param forward_rate:  Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg)
        :type forward_rate: float
        :param reset_rate:  The value of the reset, if any.
        :type reset_rate: float
        :param spread:  The spread that exists on the payoff.
        :type spread: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._quantity = None
        self._currency = None
        self._payment_date = None
        self._pay_or_receive = None
        self._accrual_start = None
        self._accrual_end = None
        self._cash_flow_type = None
        self._is_cash_flow_determined = None
        self._is_cash_flow_historic = None
        self._discount_factor = None
        self._discounted_expected_cash_flow_amount = None
        self._day_count_fraction = None
        self._forward_rate = None
        self._reset_rate = None
        self._spread = None
        self.discriminator = None

        if quantity is not None:
            self.quantity = quantity
        self.currency = currency
        if payment_date is not None:
            self.payment_date = payment_date
        self.pay_or_receive = pay_or_receive
        if accrual_start is not None:
            self.accrual_start = accrual_start
        if accrual_end is not None:
            self.accrual_end = accrual_end
        self.cash_flow_type = cash_flow_type
        if is_cash_flow_determined is not None:
            self.is_cash_flow_determined = is_cash_flow_determined
        if is_cash_flow_historic is not None:
            self.is_cash_flow_historic = is_cash_flow_historic
        if discount_factor is not None:
            self.discount_factor = discount_factor
        if discounted_expected_cash_flow_amount is not None:
            self.discounted_expected_cash_flow_amount = discounted_expected_cash_flow_amount
        self.day_count_fraction = day_count_fraction
        self.forward_rate = forward_rate
        self.reset_rate = reset_rate
        self.spread = spread

    @property
    def quantity(self):
        """Gets the quantity of this InstrumentPaymentDiaryRow.  # noqa: E501

        The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.  # noqa: E501

        :return: The quantity of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InstrumentPaymentDiaryRow.

        The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.  # noqa: E501

        :param quantity: The quantity of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def currency(self):
        """Gets the currency of this InstrumentPaymentDiaryRow.  # noqa: E501

        The payment currency of the cash flow.  # noqa: E501

        :return: The currency of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InstrumentPaymentDiaryRow.

        The payment currency of the cash flow.  # noqa: E501

        :param currency: The currency of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def payment_date(self):
        """Gets the payment_date of this InstrumentPaymentDiaryRow.  # noqa: E501

        The date at which the given cash flow is due to be paid.  # noqa: E501

        :return: The payment_date of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this InstrumentPaymentDiaryRow.

        The date at which the given cash flow is due to be paid.  # noqa: E501

        :param payment_date: The payment_date of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type payment_date: datetime
        """

        self._payment_date = payment_date

    @property
    def pay_or_receive(self):
        """Gets the pay_or_receive of this InstrumentPaymentDiaryRow.  # noqa: E501

        Does the cash flow belong to the Pay or Receive leg.  # noqa: E501

        :return: The pay_or_receive of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: str
        """
        return self._pay_or_receive

    @pay_or_receive.setter
    def pay_or_receive(self, pay_or_receive):
        """Sets the pay_or_receive of this InstrumentPaymentDiaryRow.

        Does the cash flow belong to the Pay or Receive leg.  # noqa: E501

        :param pay_or_receive: The pay_or_receive of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type pay_or_receive: str
        """

        self._pay_or_receive = pay_or_receive

    @property
    def accrual_start(self):
        """Gets the accrual_start of this InstrumentPaymentDiaryRow.  # noqa: E501

        The date on which accruals start for this cashflow.  # noqa: E501

        :return: The accrual_start of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: datetime
        """
        return self._accrual_start

    @accrual_start.setter
    def accrual_start(self, accrual_start):
        """Sets the accrual_start of this InstrumentPaymentDiaryRow.

        The date on which accruals start for this cashflow.  # noqa: E501

        :param accrual_start: The accrual_start of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type accrual_start: datetime
        """

        self._accrual_start = accrual_start

    @property
    def accrual_end(self):
        """Gets the accrual_end of this InstrumentPaymentDiaryRow.  # noqa: E501

        The date on which accruals end for this cashflow.  # noqa: E501

        :return: The accrual_end of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: datetime
        """
        return self._accrual_end

    @accrual_end.setter
    def accrual_end(self, accrual_end):
        """Sets the accrual_end of this InstrumentPaymentDiaryRow.

        The date on which accruals end for this cashflow.  # noqa: E501

        :param accrual_end: The accrual_end of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type accrual_end: datetime
        """

        self._accrual_end = accrual_end

    @property
    def cash_flow_type(self):
        """Gets the cash_flow_type of this InstrumentPaymentDiaryRow.  # noqa: E501

        The type of cashflow.  # noqa: E501

        :return: The cash_flow_type of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: str
        """
        return self._cash_flow_type

    @cash_flow_type.setter
    def cash_flow_type(self, cash_flow_type):
        """Sets the cash_flow_type of this InstrumentPaymentDiaryRow.

        The type of cashflow.  # noqa: E501

        :param cash_flow_type: The cash_flow_type of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type cash_flow_type: str
        """

        self._cash_flow_type = cash_flow_type

    @property
    def is_cash_flow_determined(self):
        """Gets the is_cash_flow_determined of this InstrumentPaymentDiaryRow.  # noqa: E501

        Is the cashflow determined as of the effective date time.  # noqa: E501

        :return: The is_cash_flow_determined of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: bool
        """
        return self._is_cash_flow_determined

    @is_cash_flow_determined.setter
    def is_cash_flow_determined(self, is_cash_flow_determined):
        """Sets the is_cash_flow_determined of this InstrumentPaymentDiaryRow.

        Is the cashflow determined as of the effective date time.  # noqa: E501

        :param is_cash_flow_determined: The is_cash_flow_determined of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type is_cash_flow_determined: bool
        """

        self._is_cash_flow_determined = is_cash_flow_determined

    @property
    def is_cash_flow_historic(self):
        """Gets the is_cash_flow_historic of this InstrumentPaymentDiaryRow.  # noqa: E501

        Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt.  # noqa: E501

        :return: The is_cash_flow_historic of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: bool
        """
        return self._is_cash_flow_historic

    @is_cash_flow_historic.setter
    def is_cash_flow_historic(self, is_cash_flow_historic):
        """Sets the is_cash_flow_historic of this InstrumentPaymentDiaryRow.

        Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt.  # noqa: E501

        :param is_cash_flow_historic: The is_cash_flow_historic of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type is_cash_flow_historic: bool
        """

        self._is_cash_flow_historic = is_cash_flow_historic

    @property
    def discount_factor(self):
        """Gets the discount_factor of this InstrumentPaymentDiaryRow.  # noqa: E501

        Weighting factor to discount cashflow to the present value.  # noqa: E501

        :return: The discount_factor of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._discount_factor

    @discount_factor.setter
    def discount_factor(self, discount_factor):
        """Sets the discount_factor of this InstrumentPaymentDiaryRow.

        Weighting factor to discount cashflow to the present value.  # noqa: E501

        :param discount_factor: The discount_factor of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type discount_factor: float
        """

        self._discount_factor = discount_factor

    @property
    def discounted_expected_cash_flow_amount(self):
        """Gets the discounted_expected_cash_flow_amount of this InstrumentPaymentDiaryRow.  # noqa: E501

        The expected cashflow amount taking into account the discount factor.  # noqa: E501

        :return: The discounted_expected_cash_flow_amount of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._discounted_expected_cash_flow_amount

    @discounted_expected_cash_flow_amount.setter
    def discounted_expected_cash_flow_amount(self, discounted_expected_cash_flow_amount):
        """Sets the discounted_expected_cash_flow_amount of this InstrumentPaymentDiaryRow.

        The expected cashflow amount taking into account the discount factor.  # noqa: E501

        :param discounted_expected_cash_flow_amount: The discounted_expected_cash_flow_amount of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type discounted_expected_cash_flow_amount: float
        """

        self._discounted_expected_cash_flow_amount = discounted_expected_cash_flow_amount

    @property
    def day_count_fraction(self):
        """Gets the day_count_fraction of this InstrumentPaymentDiaryRow.  # noqa: E501

        The day count fraction, if appropriate.  # noqa: E501

        :return: The day_count_fraction of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._day_count_fraction

    @day_count_fraction.setter
    def day_count_fraction(self, day_count_fraction):
        """Sets the day_count_fraction of this InstrumentPaymentDiaryRow.

        The day count fraction, if appropriate.  # noqa: E501

        :param day_count_fraction: The day_count_fraction of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type day_count_fraction: float
        """

        self._day_count_fraction = day_count_fraction

    @property
    def forward_rate(self):
        """Gets the forward_rate of this InstrumentPaymentDiaryRow.  # noqa: E501

        Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg)  # noqa: E501

        :return: The forward_rate of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._forward_rate

    @forward_rate.setter
    def forward_rate(self, forward_rate):
        """Sets the forward_rate of this InstrumentPaymentDiaryRow.

        Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg)  # noqa: E501

        :param forward_rate: The forward_rate of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type forward_rate: float
        """

        self._forward_rate = forward_rate

    @property
    def reset_rate(self):
        """Gets the reset_rate of this InstrumentPaymentDiaryRow.  # noqa: E501

        The value of the reset, if any.  # noqa: E501

        :return: The reset_rate of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._reset_rate

    @reset_rate.setter
    def reset_rate(self, reset_rate):
        """Sets the reset_rate of this InstrumentPaymentDiaryRow.

        The value of the reset, if any.  # noqa: E501

        :param reset_rate: The reset_rate of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type reset_rate: float
        """

        self._reset_rate = reset_rate

    @property
    def spread(self):
        """Gets the spread of this InstrumentPaymentDiaryRow.  # noqa: E501

        The spread that exists on the payoff.  # noqa: E501

        :return: The spread of this InstrumentPaymentDiaryRow.  # noqa: E501
        :rtype: float
        """
        return self._spread

    @spread.setter
    def spread(self, spread):
        """Sets the spread of this InstrumentPaymentDiaryRow.

        The spread that exists on the payoff.  # noqa: E501

        :param spread: The spread of this InstrumentPaymentDiaryRow.  # noqa: E501
        :type spread: float
        """

        self._spread = spread

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
        if not isinstance(other, InstrumentPaymentDiaryRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentPaymentDiaryRow):
            return True

        return self.to_dict() != other.to_dict()
