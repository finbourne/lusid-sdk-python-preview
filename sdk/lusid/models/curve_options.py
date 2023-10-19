# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.625
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


class CurveOptions(object):
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
        'day_count_convention': 'str',
        'front_extrapolation_type': 'str',
        'back_extrapolation_type': 'str',
        'market_data_options_type': 'str'
    }

    attribute_map = {
        'day_count_convention': 'dayCountConvention',
        'front_extrapolation_type': 'frontExtrapolationType',
        'back_extrapolation_type': 'backExtrapolationType',
        'market_data_options_type': 'marketDataOptionsType'
    }

    required_map = {
        'day_count_convention': 'optional',
        'front_extrapolation_type': 'optional',
        'back_extrapolation_type': 'optional',
        'market_data_options_type': 'required'
    }

    def __init__(self, day_count_convention=None, front_extrapolation_type=None, back_extrapolation_type=None, market_data_options_type=None, local_vars_configuration=None):  # noqa: E501
        """CurveOptions - a model defined in OpenAPI"
        
        :param day_count_convention:  Day count convention of the curve. Defaults to \"Act360\".
        :type day_count_convention: str
        :param front_extrapolation_type:  What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \"front\" direction is the closest point on the curve onward. <br />  example: 0D tenor to past  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].
        :type front_extrapolation_type: str
        :param back_extrapolation_type:  What type of extrapolation is used to build the curve.  <br />  Imagine that the curve is facing the observer(you), then the \"back\" direction is the furthest point on the curve onward. <br />  example: 30Y tenor to infinity  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].
        :type back_extrapolation_type: str
        :param market_data_options_type:  The available values are: CurveOptions (required)
        :type market_data_options_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._day_count_convention = None
        self._front_extrapolation_type = None
        self._back_extrapolation_type = None
        self._market_data_options_type = None
        self.discriminator = None

        self.day_count_convention = day_count_convention
        self.front_extrapolation_type = front_extrapolation_type
        self.back_extrapolation_type = back_extrapolation_type
        self.market_data_options_type = market_data_options_type

    @property
    def day_count_convention(self):
        """Gets the day_count_convention of this CurveOptions.  # noqa: E501

        Day count convention of the curve. Defaults to \"Act360\".  # noqa: E501

        :return: The day_count_convention of this CurveOptions.  # noqa: E501
        :rtype: str
        """
        return self._day_count_convention

    @day_count_convention.setter
    def day_count_convention(self, day_count_convention):
        """Sets the day_count_convention of this CurveOptions.

        Day count convention of the curve. Defaults to \"Act360\".  # noqa: E501

        :param day_count_convention: The day_count_convention of this CurveOptions.  # noqa: E501
        :type day_count_convention: str
        """
        if (self.local_vars_configuration.client_side_validation and
                day_count_convention is not None and len(day_count_convention) > 50):
            raise ValueError("Invalid value for `day_count_convention`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                day_count_convention is not None and len(day_count_convention) < 0):
            raise ValueError("Invalid value for `day_count_convention`, length must be greater than or equal to `0`")  # noqa: E501

        self._day_count_convention = day_count_convention

    @property
    def front_extrapolation_type(self):
        """Gets the front_extrapolation_type of this CurveOptions.  # noqa: E501

        What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \"front\" direction is the closest point on the curve onward. <br />  example: 0D tenor to past  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].  # noqa: E501

        :return: The front_extrapolation_type of this CurveOptions.  # noqa: E501
        :rtype: str
        """
        return self._front_extrapolation_type

    @front_extrapolation_type.setter
    def front_extrapolation_type(self, front_extrapolation_type):
        """Sets the front_extrapolation_type of this CurveOptions.

        What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \"front\" direction is the closest point on the curve onward. <br />  example: 0D tenor to past  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].  # noqa: E501

        :param front_extrapolation_type: The front_extrapolation_type of this CurveOptions.  # noqa: E501
        :type front_extrapolation_type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                front_extrapolation_type is not None and len(front_extrapolation_type) > 50):
            raise ValueError("Invalid value for `front_extrapolation_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                front_extrapolation_type is not None and len(front_extrapolation_type) < 0):
            raise ValueError("Invalid value for `front_extrapolation_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._front_extrapolation_type = front_extrapolation_type

    @property
    def back_extrapolation_type(self):
        """Gets the back_extrapolation_type of this CurveOptions.  # noqa: E501

        What type of extrapolation is used to build the curve.  <br />  Imagine that the curve is facing the observer(you), then the \"back\" direction is the furthest point on the curve onward. <br />  example: 30Y tenor to infinity  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].  # noqa: E501

        :return: The back_extrapolation_type of this CurveOptions.  # noqa: E501
        :rtype: str
        """
        return self._back_extrapolation_type

    @back_extrapolation_type.setter
    def back_extrapolation_type(self, back_extrapolation_type):
        """Sets the back_extrapolation_type of this CurveOptions.

        What type of extrapolation is used to build the curve.  <br />  Imagine that the curve is facing the observer(you), then the \"back\" direction is the furthest point on the curve onward. <br />  example: 30Y tenor to infinity  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].  # noqa: E501

        :param back_extrapolation_type: The back_extrapolation_type of this CurveOptions.  # noqa: E501
        :type back_extrapolation_type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                back_extrapolation_type is not None and len(back_extrapolation_type) > 50):
            raise ValueError("Invalid value for `back_extrapolation_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                back_extrapolation_type is not None and len(back_extrapolation_type) < 0):
            raise ValueError("Invalid value for `back_extrapolation_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._back_extrapolation_type = back_extrapolation_type

    @property
    def market_data_options_type(self):
        """Gets the market_data_options_type of this CurveOptions.  # noqa: E501

        The available values are: CurveOptions  # noqa: E501

        :return: The market_data_options_type of this CurveOptions.  # noqa: E501
        :rtype: str
        """
        return self._market_data_options_type

    @market_data_options_type.setter
    def market_data_options_type(self, market_data_options_type):
        """Sets the market_data_options_type of this CurveOptions.

        The available values are: CurveOptions  # noqa: E501

        :param market_data_options_type: The market_data_options_type of this CurveOptions.  # noqa: E501
        :type market_data_options_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_options_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_options_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CurveOptions"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_options_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_options_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_options_type, allowed_values)
            )

        self._market_data_options_type = market_data_options_type

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
        if not isinstance(other, CurveOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurveOptions):
            return True

        return self.to_dict() != other.to_dict()
