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


class UnitsRatio(object):
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
        'input': 'float',
        'output': 'float'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output'
    }

    required_map = {
        'input': 'required',
        'output': 'required'
    }

    def __init__(self, input=None, output=None, local_vars_configuration=None):  # noqa: E501
        """UnitsRatio - a model defined in OpenAPI"
        
        :param input:  Input amount.  Denominator of the Ratio (required)
        :type input: float
        :param output:  Output amount. Numerator of the Ratio (required)
        :type output: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input = None
        self._output = None
        self.discriminator = None

        self.input = input
        self.output = output

    @property
    def input(self):
        """Gets the input of this UnitsRatio.  # noqa: E501

        Input amount.  Denominator of the Ratio  # noqa: E501

        :return: The input of this UnitsRatio.  # noqa: E501
        :rtype: float
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this UnitsRatio.

        Input amount.  Denominator of the Ratio  # noqa: E501

        :param input: The input of this UnitsRatio.  # noqa: E501
        :type input: float
        """
        if self.local_vars_configuration.client_side_validation and input is None:  # noqa: E501
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def output(self):
        """Gets the output of this UnitsRatio.  # noqa: E501

        Output amount. Numerator of the Ratio  # noqa: E501

        :return: The output of this UnitsRatio.  # noqa: E501
        :rtype: float
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this UnitsRatio.

        Output amount. Numerator of the Ratio  # noqa: E501

        :param output: The output of this UnitsRatio.  # noqa: E501
        :type output: float
        """
        if self.local_vars_configuration.client_side_validation and output is None:  # noqa: E501
            raise ValueError("Invalid value for `output`, must not be `None`")  # noqa: E501

        self._output = output

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
        if not isinstance(other, UnitsRatio):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnitsRatio):
            return True

        return self.to_dict() != other.to_dict()
