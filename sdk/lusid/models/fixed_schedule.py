# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.148
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


class FixedSchedule(object):
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
        'coupon_rate': 'float',
        'convention_name': 'FlowConventionName',
        'ex_dividend_days': 'int',
        'notional': 'float',
        'payment_currency': 'str',
        'stub_type': 'str',
        'ex_dividend_configuration': 'ExDividendConfiguration',
        'schedule_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'flow_conventions': 'flowConventions',
        'coupon_rate': 'couponRate',
        'convention_name': 'conventionName',
        'ex_dividend_days': 'exDividendDays',
        'notional': 'notional',
        'payment_currency': 'paymentCurrency',
        'stub_type': 'stubType',
        'ex_dividend_configuration': 'exDividendConfiguration',
        'schedule_type': 'scheduleType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'flow_conventions': 'optional',
        'coupon_rate': 'optional',
        'convention_name': 'optional',
        'ex_dividend_days': 'optional',
        'notional': 'optional',
        'payment_currency': 'required',
        'stub_type': 'optional',
        'ex_dividend_configuration': 'optional',
        'schedule_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, flow_conventions=None, coupon_rate=None, convention_name=None, ex_dividend_days=None, notional=None, payment_currency=None, stub_type=None, ex_dividend_configuration=None, schedule_type=None, local_vars_configuration=None):  # noqa: E501
        """FixedSchedule - a model defined in OpenAPI"
        
        :param start_date:  Date to start generate from (required)
        :type start_date: datetime
        :param maturity_date:  Date to generate to (required)
        :type maturity_date: datetime
        :param flow_conventions: 
        :type flow_conventions: lusid.FlowConventions
        :param coupon_rate:  Coupon rate given as a fraction.
        :type coupon_rate: float
        :param convention_name: 
        :type convention_name: lusid.FlowConventionName
        :param ex_dividend_days:  Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.
        :type ex_dividend_days: int
        :param notional:  Scaling factor, the quantity outstanding on which the rate will be paid.
        :type notional: float
        :param payment_currency:  Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. (required)
        :type payment_currency: str
        :param stub_type:  StubType required of the schedule    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].
        :type stub_type: str
        :param ex_dividend_configuration: 
        :type ex_dividend_configuration: lusid.ExDividendConfiguration
        :param schedule_type:  The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, Invalid (required)
        :type schedule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._flow_conventions = None
        self._coupon_rate = None
        self._convention_name = None
        self._ex_dividend_days = None
        self._notional = None
        self._payment_currency = None
        self._stub_type = None
        self._ex_dividend_configuration = None
        self._schedule_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        if flow_conventions is not None:
            self.flow_conventions = flow_conventions
        if coupon_rate is not None:
            self.coupon_rate = coupon_rate
        if convention_name is not None:
            self.convention_name = convention_name
        self.ex_dividend_days = ex_dividend_days
        if notional is not None:
            self.notional = notional
        self.payment_currency = payment_currency
        self.stub_type = stub_type
        if ex_dividend_configuration is not None:
            self.ex_dividend_configuration = ex_dividend_configuration
        self.schedule_type = schedule_type

    @property
    def start_date(self):
        """Gets the start_date of this FixedSchedule.  # noqa: E501

        Date to start generate from  # noqa: E501

        :return: The start_date of this FixedSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FixedSchedule.

        Date to start generate from  # noqa: E501

        :param start_date: The start_date of this FixedSchedule.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this FixedSchedule.  # noqa: E501

        Date to generate to  # noqa: E501

        :return: The maturity_date of this FixedSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this FixedSchedule.

        Date to generate to  # noqa: E501

        :param maturity_date: The maturity_date of this FixedSchedule.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this FixedSchedule.  # noqa: E501


        :return: The flow_conventions of this FixedSchedule.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this FixedSchedule.


        :param flow_conventions: The flow_conventions of this FixedSchedule.  # noqa: E501
        :type flow_conventions: lusid.FlowConventions
        """

        self._flow_conventions = flow_conventions

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this FixedSchedule.  # noqa: E501

        Coupon rate given as a fraction.  # noqa: E501

        :return: The coupon_rate of this FixedSchedule.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this FixedSchedule.

        Coupon rate given as a fraction.  # noqa: E501

        :param coupon_rate: The coupon_rate of this FixedSchedule.  # noqa: E501
        :type coupon_rate: float
        """

        self._coupon_rate = coupon_rate

    @property
    def convention_name(self):
        """Gets the convention_name of this FixedSchedule.  # noqa: E501


        :return: The convention_name of this FixedSchedule.  # noqa: E501
        :rtype: lusid.FlowConventionName
        """
        return self._convention_name

    @convention_name.setter
    def convention_name(self, convention_name):
        """Sets the convention_name of this FixedSchedule.


        :param convention_name: The convention_name of this FixedSchedule.  # noqa: E501
        :type convention_name: lusid.FlowConventionName
        """

        self._convention_name = convention_name

    @property
    def ex_dividend_days(self):
        """Gets the ex_dividend_days of this FixedSchedule.  # noqa: E501

        Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.  # noqa: E501

        :return: The ex_dividend_days of this FixedSchedule.  # noqa: E501
        :rtype: int
        """
        return self._ex_dividend_days

    @ex_dividend_days.setter
    def ex_dividend_days(self, ex_dividend_days):
        """Sets the ex_dividend_days of this FixedSchedule.

        Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.  # noqa: E501

        :param ex_dividend_days: The ex_dividend_days of this FixedSchedule.  # noqa: E501
        :type ex_dividend_days: int
        """

        self._ex_dividend_days = ex_dividend_days

    @property
    def notional(self):
        """Gets the notional of this FixedSchedule.  # noqa: E501

        Scaling factor, the quantity outstanding on which the rate will be paid.  # noqa: E501

        :return: The notional of this FixedSchedule.  # noqa: E501
        :rtype: float
        """
        return self._notional

    @notional.setter
    def notional(self, notional):
        """Sets the notional of this FixedSchedule.

        Scaling factor, the quantity outstanding on which the rate will be paid.  # noqa: E501

        :param notional: The notional of this FixedSchedule.  # noqa: E501
        :type notional: float
        """

        self._notional = notional

    @property
    def payment_currency(self):
        """Gets the payment_currency of this FixedSchedule.  # noqa: E501

        Payment currency. This does not have to be the same as the nominal bond or observation/reset currency.  # noqa: E501

        :return: The payment_currency of this FixedSchedule.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this FixedSchedule.

        Payment currency. This does not have to be the same as the nominal bond or observation/reset currency.  # noqa: E501

        :param payment_currency: The payment_currency of this FixedSchedule.  # noqa: E501
        :type payment_currency: str
        """
        if self.local_vars_configuration.client_side_validation and payment_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_currency`, must not be `None`")  # noqa: E501

        self._payment_currency = payment_currency

    @property
    def stub_type(self):
        """Gets the stub_type of this FixedSchedule.  # noqa: E501

        StubType required of the schedule    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :return: The stub_type of this FixedSchedule.  # noqa: E501
        :rtype: str
        """
        return self._stub_type

    @stub_type.setter
    def stub_type(self, stub_type):
        """Sets the stub_type of this FixedSchedule.

        StubType required of the schedule    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].  # noqa: E501

        :param stub_type: The stub_type of this FixedSchedule.  # noqa: E501
        :type stub_type: str
        """

        self._stub_type = stub_type

    @property
    def ex_dividend_configuration(self):
        """Gets the ex_dividend_configuration of this FixedSchedule.  # noqa: E501


        :return: The ex_dividend_configuration of this FixedSchedule.  # noqa: E501
        :rtype: lusid.ExDividendConfiguration
        """
        return self._ex_dividend_configuration

    @ex_dividend_configuration.setter
    def ex_dividend_configuration(self, ex_dividend_configuration):
        """Sets the ex_dividend_configuration of this FixedSchedule.


        :param ex_dividend_configuration: The ex_dividend_configuration of this FixedSchedule.  # noqa: E501
        :type ex_dividend_configuration: lusid.ExDividendConfiguration
        """

        self._ex_dividend_configuration = ex_dividend_configuration

    @property
    def schedule_type(self):
        """Gets the schedule_type of this FixedSchedule.  # noqa: E501

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, Invalid  # noqa: E501

        :return: The schedule_type of this FixedSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this FixedSchedule.

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, Invalid  # noqa: E501

        :param schedule_type: The schedule_type of this FixedSchedule.  # noqa: E501
        :type schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FixedSchedule", "FloatSchedule", "OptionalitySchedule", "StepSchedule", "Exercise", "FxRateSchedule", "FxLinkedNotionalSchedule", "Invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and schedule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

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
        if not isinstance(other, FixedSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FixedSchedule):
            return True

        return self.to_dict() != other.to_dict()
