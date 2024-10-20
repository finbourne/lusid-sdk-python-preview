# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.247
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


class BondConversionScheduleAllOf(object):
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
        'identifiers': 'dict(str, str)',
        'bond_conversion_entries': 'list[BondConversionEntry]',
        'conversion_trigger': 'str',
        'delivery_type': 'str',
        'exercise_type': 'str',
        'includes_accrued': 'bool',
        'mandatory_conversion': 'bool',
        'notification_period_end': 'datetime',
        'notification_period_start': 'datetime',
        'schedule_type': 'str'
    }

    attribute_map = {
        'identifiers': 'identifiers',
        'bond_conversion_entries': 'bondConversionEntries',
        'conversion_trigger': 'conversionTrigger',
        'delivery_type': 'deliveryType',
        'exercise_type': 'exerciseType',
        'includes_accrued': 'includesAccrued',
        'mandatory_conversion': 'mandatoryConversion',
        'notification_period_end': 'notificationPeriodEnd',
        'notification_period_start': 'notificationPeriodStart',
        'schedule_type': 'scheduleType'
    }

    required_map = {
        'identifiers': 'optional',
        'bond_conversion_entries': 'optional',
        'conversion_trigger': 'required',
        'delivery_type': 'optional',
        'exercise_type': 'required',
        'includes_accrued': 'optional',
        'mandatory_conversion': 'optional',
        'notification_period_end': 'optional',
        'notification_period_start': 'optional',
        'schedule_type': 'required'
    }

    def __init__(self, identifiers=None, bond_conversion_entries=None, conversion_trigger=None, delivery_type=None, exercise_type=None, includes_accrued=None, mandatory_conversion=None, notification_period_end=None, notification_period_start=None, schedule_type=None, local_vars_configuration=None):  # noqa: E501
        """BondConversionScheduleAllOf - a model defined in OpenAPI"
        
        :param identifiers:  The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied.
        :type identifiers: dict(str, str)
        :param bond_conversion_entries:  The dates at which the bond may be converted and associated information required about the conversion.
        :type bond_conversion_entries: list[lusid.BondConversionEntry]
        :param conversion_trigger:  Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall]. (required)
        :type conversion_trigger: str
        :param delivery_type:  Is a conversion made into cash or into shares?    Supported string (enumeration) values are: [Cash, Physical].
        :type delivery_type: str
        :param exercise_type:  The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American]. (required)
        :type exercise_type: str
        :param includes_accrued:  Set this to true if a accrued interest is included in the conversion. Defaults to true.
        :type includes_accrued: bool
        :param mandatory_conversion:  Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false.
        :type mandatory_conversion: bool
        :param notification_period_end:  The last day in the notification period for the conversion of the bond
        :type notification_period_end: datetime
        :param notification_period_start:  The first day in the notification period for the conversion of the bond
        :type notification_period_start: datetime
        :param schedule_type:  The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid (required)
        :type schedule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifiers = None
        self._bond_conversion_entries = None
        self._conversion_trigger = None
        self._delivery_type = None
        self._exercise_type = None
        self._includes_accrued = None
        self._mandatory_conversion = None
        self._notification_period_end = None
        self._notification_period_start = None
        self._schedule_type = None
        self.discriminator = None

        self.identifiers = identifiers
        self.bond_conversion_entries = bond_conversion_entries
        self.conversion_trigger = conversion_trigger
        self.delivery_type = delivery_type
        self.exercise_type = exercise_type
        if includes_accrued is not None:
            self.includes_accrued = includes_accrued
        if mandatory_conversion is not None:
            self.mandatory_conversion = mandatory_conversion
        if notification_period_end is not None:
            self.notification_period_end = notification_period_end
        if notification_period_start is not None:
            self.notification_period_start = notification_period_start
        self.schedule_type = schedule_type

    @property
    def identifiers(self):
        """Gets the identifiers of this BondConversionScheduleAllOf.  # noqa: E501

        The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied.  # noqa: E501

        :return: The identifiers of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this BondConversionScheduleAllOf.

        The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied.  # noqa: E501

        :param identifiers: The identifiers of this BondConversionScheduleAllOf.  # noqa: E501
        :type identifiers: dict(str, str)
        """

        self._identifiers = identifiers

    @property
    def bond_conversion_entries(self):
        """Gets the bond_conversion_entries of this BondConversionScheduleAllOf.  # noqa: E501

        The dates at which the bond may be converted and associated information required about the conversion.  # noqa: E501

        :return: The bond_conversion_entries of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: list[lusid.BondConversionEntry]
        """
        return self._bond_conversion_entries

    @bond_conversion_entries.setter
    def bond_conversion_entries(self, bond_conversion_entries):
        """Sets the bond_conversion_entries of this BondConversionScheduleAllOf.

        The dates at which the bond may be converted and associated information required about the conversion.  # noqa: E501

        :param bond_conversion_entries: The bond_conversion_entries of this BondConversionScheduleAllOf.  # noqa: E501
        :type bond_conversion_entries: list[lusid.BondConversionEntry]
        """

        self._bond_conversion_entries = bond_conversion_entries

    @property
    def conversion_trigger(self):
        """Gets the conversion_trigger of this BondConversionScheduleAllOf.  # noqa: E501

        Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall].  # noqa: E501

        :return: The conversion_trigger of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._conversion_trigger

    @conversion_trigger.setter
    def conversion_trigger(self, conversion_trigger):
        """Sets the conversion_trigger of this BondConversionScheduleAllOf.

        Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall].  # noqa: E501

        :param conversion_trigger: The conversion_trigger of this BondConversionScheduleAllOf.  # noqa: E501
        :type conversion_trigger: str
        """
        if self.local_vars_configuration.client_side_validation and conversion_trigger is None:  # noqa: E501
            raise ValueError("Invalid value for `conversion_trigger`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                conversion_trigger is not None and len(conversion_trigger) > 50):
            raise ValueError("Invalid value for `conversion_trigger`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                conversion_trigger is not None and len(conversion_trigger) < 0):
            raise ValueError("Invalid value for `conversion_trigger`, length must be greater than or equal to `0`")  # noqa: E501

        self._conversion_trigger = conversion_trigger

    @property
    def delivery_type(self):
        """Gets the delivery_type of this BondConversionScheduleAllOf.  # noqa: E501

        Is a conversion made into cash or into shares?    Supported string (enumeration) values are: [Cash, Physical].  # noqa: E501

        :return: The delivery_type of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this BondConversionScheduleAllOf.

        Is a conversion made into cash or into shares?    Supported string (enumeration) values are: [Cash, Physical].  # noqa: E501

        :param delivery_type: The delivery_type of this BondConversionScheduleAllOf.  # noqa: E501
        :type delivery_type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                delivery_type is not None and len(delivery_type) > 50):
            raise ValueError("Invalid value for `delivery_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                delivery_type is not None and len(delivery_type) < 0):
            raise ValueError("Invalid value for `delivery_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._delivery_type = delivery_type

    @property
    def exercise_type(self):
        """Gets the exercise_type of this BondConversionScheduleAllOf.  # noqa: E501

        The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :return: The exercise_type of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        """Sets the exercise_type of this BondConversionScheduleAllOf.

        The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :param exercise_type: The exercise_type of this BondConversionScheduleAllOf.  # noqa: E501
        :type exercise_type: str
        """
        if self.local_vars_configuration.client_side_validation and exercise_type is None:  # noqa: E501
            raise ValueError("Invalid value for `exercise_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exercise_type is not None and len(exercise_type) > 50):
            raise ValueError("Invalid value for `exercise_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exercise_type is not None and len(exercise_type) < 0):
            raise ValueError("Invalid value for `exercise_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._exercise_type = exercise_type

    @property
    def includes_accrued(self):
        """Gets the includes_accrued of this BondConversionScheduleAllOf.  # noqa: E501

        Set this to true if a accrued interest is included in the conversion. Defaults to true.  # noqa: E501

        :return: The includes_accrued of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._includes_accrued

    @includes_accrued.setter
    def includes_accrued(self, includes_accrued):
        """Sets the includes_accrued of this BondConversionScheduleAllOf.

        Set this to true if a accrued interest is included in the conversion. Defaults to true.  # noqa: E501

        :param includes_accrued: The includes_accrued of this BondConversionScheduleAllOf.  # noqa: E501
        :type includes_accrued: bool
        """

        self._includes_accrued = includes_accrued

    @property
    def mandatory_conversion(self):
        """Gets the mandatory_conversion of this BondConversionScheduleAllOf.  # noqa: E501

        Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false.  # noqa: E501

        :return: The mandatory_conversion of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory_conversion

    @mandatory_conversion.setter
    def mandatory_conversion(self, mandatory_conversion):
        """Sets the mandatory_conversion of this BondConversionScheduleAllOf.

        Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false.  # noqa: E501

        :param mandatory_conversion: The mandatory_conversion of this BondConversionScheduleAllOf.  # noqa: E501
        :type mandatory_conversion: bool
        """

        self._mandatory_conversion = mandatory_conversion

    @property
    def notification_period_end(self):
        """Gets the notification_period_end of this BondConversionScheduleAllOf.  # noqa: E501

        The last day in the notification period for the conversion of the bond  # noqa: E501

        :return: The notification_period_end of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._notification_period_end

    @notification_period_end.setter
    def notification_period_end(self, notification_period_end):
        """Sets the notification_period_end of this BondConversionScheduleAllOf.

        The last day in the notification period for the conversion of the bond  # noqa: E501

        :param notification_period_end: The notification_period_end of this BondConversionScheduleAllOf.  # noqa: E501
        :type notification_period_end: datetime
        """

        self._notification_period_end = notification_period_end

    @property
    def notification_period_start(self):
        """Gets the notification_period_start of this BondConversionScheduleAllOf.  # noqa: E501

        The first day in the notification period for the conversion of the bond  # noqa: E501

        :return: The notification_period_start of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._notification_period_start

    @notification_period_start.setter
    def notification_period_start(self, notification_period_start):
        """Sets the notification_period_start of this BondConversionScheduleAllOf.

        The first day in the notification period for the conversion of the bond  # noqa: E501

        :param notification_period_start: The notification_period_start of this BondConversionScheduleAllOf.  # noqa: E501
        :type notification_period_start: datetime
        """

        self._notification_period_start = notification_period_start

    @property
    def schedule_type(self):
        """Gets the schedule_type of this BondConversionScheduleAllOf.  # noqa: E501

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid  # noqa: E501

        :return: The schedule_type of this BondConversionScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this BondConversionScheduleAllOf.

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid  # noqa: E501

        :param schedule_type: The schedule_type of this BondConversionScheduleAllOf.  # noqa: E501
        :type schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FixedSchedule", "FloatSchedule", "OptionalitySchedule", "StepSchedule", "Exercise", "FxRateSchedule", "FxLinkedNotionalSchedule", "BondConversionSchedule", "Invalid"]  # noqa: E501
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
        if not isinstance(other, BondConversionScheduleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BondConversionScheduleAllOf):
            return True

        return self.to_dict() != other.to_dict()
