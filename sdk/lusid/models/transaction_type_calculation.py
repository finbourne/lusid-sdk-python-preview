# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.595
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


class TransactionTypeCalculation(object):
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
        'type': 'str',
        'side': 'str'
    }

    attribute_map = {
        'type': 'type',
        'side': 'side'
    }

    required_map = {
        'type': 'required',
        'side': 'required'
    }

    def __init__(self, type=None, side=None, local_vars_configuration=None):  # noqa: E501
        """TransactionTypeCalculation - a model defined in OpenAPI"
        
        :param type:  The type of calculation to perform (required)
        :type type: str
        :param side:  The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration (required)
        :type side: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._side = None
        self.discriminator = None

        self.type = type
        self.side = side

    @property
    def type(self):
        """Gets the type of this TransactionTypeCalculation.  # noqa: E501

        The type of calculation to perform  # noqa: E501

        :return: The type of this TransactionTypeCalculation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionTypeCalculation.

        The type of calculation to perform  # noqa: E501

        :param type: The type of this TransactionTypeCalculation.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def side(self):
        """Gets the side of this TransactionTypeCalculation.  # noqa: E501

        The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration  # noqa: E501

        :return: The side of this TransactionTypeCalculation.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this TransactionTypeCalculation.

        The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration  # noqa: E501

        :param side: The side of this TransactionTypeCalculation.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) > 64):
            raise ValueError("Invalid value for `side`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) < 1):
            raise ValueError("Invalid value for `side`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', side)):  # noqa: E501
            raise ValueError(r"Invalid value for `side`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._side = side

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
        if not isinstance(other, TransactionTypeCalculation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionTypeCalculation):
            return True

        return self.to_dict() != other.to_dict()
