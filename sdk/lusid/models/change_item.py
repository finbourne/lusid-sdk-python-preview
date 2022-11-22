# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4993
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


class ChangeItem(object):
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
        'field_name': 'str',
        'previous_value': 'str',
        'new_value': 'str',
        'effective_from': 'datetime',
        'effective_until': 'datetime'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'previous_value': 'previousValue',
        'new_value': 'newValue',
        'effective_from': 'effectiveFrom',
        'effective_until': 'effectiveUntil'
    }

    required_map = {
        'field_name': 'required',
        'previous_value': 'optional',
        'new_value': 'optional',
        'effective_from': 'optional',
        'effective_until': 'optional'
    }

    def __init__(self, field_name=None, previous_value=None, new_value=None, effective_from=None, effective_until=None, local_vars_configuration=None):  # noqa: E501
        """ChangeItem - a model defined in OpenAPI"
        
        :param field_name:  The name of the field or property that has been changed. (required)
        :type field_name: str
        :param previous_value:  The previous value for this field / property.
        :type previous_value: str
        :param new_value:  The new value for this field / property.
        :type new_value: str
        :param effective_from:  The market data time, i.e. the time to run the change from.
        :type effective_from: datetime
        :param effective_until:  The market data time, i.e. the time to run the change until.
        :type effective_until: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field_name = None
        self._previous_value = None
        self._new_value = None
        self._effective_from = None
        self._effective_until = None
        self.discriminator = None

        self.field_name = field_name
        self.previous_value = previous_value
        self.new_value = new_value
        self.effective_from = effective_from
        self.effective_until = effective_until

    @property
    def field_name(self):
        """Gets the field_name of this ChangeItem.  # noqa: E501

        The name of the field or property that has been changed.  # noqa: E501

        :return: The field_name of this ChangeItem.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ChangeItem.

        The name of the field or property that has been changed.  # noqa: E501

        :param field_name: The field_name of this ChangeItem.  # noqa: E501
        :type field_name: str
        """
        if self.local_vars_configuration.client_side_validation and field_name is None:  # noqa: E501
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def previous_value(self):
        """Gets the previous_value of this ChangeItem.  # noqa: E501

        The previous value for this field / property.  # noqa: E501

        :return: The previous_value of this ChangeItem.  # noqa: E501
        :rtype: str
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        """Sets the previous_value of this ChangeItem.

        The previous value for this field / property.  # noqa: E501

        :param previous_value: The previous_value of this ChangeItem.  # noqa: E501
        :type previous_value: str
        """

        self._previous_value = previous_value

    @property
    def new_value(self):
        """Gets the new_value of this ChangeItem.  # noqa: E501

        The new value for this field / property.  # noqa: E501

        :return: The new_value of this ChangeItem.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ChangeItem.

        The new value for this field / property.  # noqa: E501

        :param new_value: The new_value of this ChangeItem.  # noqa: E501
        :type new_value: str
        """

        self._new_value = new_value

    @property
    def effective_from(self):
        """Gets the effective_from of this ChangeItem.  # noqa: E501

        The market data time, i.e. the time to run the change from.  # noqa: E501

        :return: The effective_from of this ChangeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this ChangeItem.

        The market data time, i.e. the time to run the change from.  # noqa: E501

        :param effective_from: The effective_from of this ChangeItem.  # noqa: E501
        :type effective_from: datetime
        """

        self._effective_from = effective_from

    @property
    def effective_until(self):
        """Gets the effective_until of this ChangeItem.  # noqa: E501

        The market data time, i.e. the time to run the change until.  # noqa: E501

        :return: The effective_until of this ChangeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_until

    @effective_until.setter
    def effective_until(self, effective_until):
        """Sets the effective_until of this ChangeItem.

        The market data time, i.e. the time to run the change until.  # noqa: E501

        :param effective_until: The effective_until of this ChangeItem.  # noqa: E501
        :type effective_until: datetime
        """

        self._effective_until = effective_until

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
        if not isinstance(other, ChangeItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeItem):
            return True

        return self.to_dict() != other.to_dict()
