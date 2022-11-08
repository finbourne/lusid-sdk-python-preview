# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4943
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


class ReconciliationResponse(object):
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
        'comparisons': 'list[ReconciliationLine]',
        'data_schema': 'ResultDataSchema'
    }

    attribute_map = {
        'comparisons': 'comparisons',
        'data_schema': 'dataSchema'
    }

    required_map = {
        'comparisons': 'optional',
        'data_schema': 'optional'
    }

    def __init__(self, comparisons=None, data_schema=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationResponse - a model defined in OpenAPI"
        
        :param comparisons:  List of comparisons of left to right hand sides.
        :type comparisons: list[lusid.ReconciliationLine]
        :param data_schema: 
        :type data_schema: lusid.ResultDataSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._comparisons = None
        self._data_schema = None
        self.discriminator = None

        self.comparisons = comparisons
        if data_schema is not None:
            self.data_schema = data_schema

    @property
    def comparisons(self):
        """Gets the comparisons of this ReconciliationResponse.  # noqa: E501

        List of comparisons of left to right hand sides.  # noqa: E501

        :return: The comparisons of this ReconciliationResponse.  # noqa: E501
        :rtype: list[lusid.ReconciliationLine]
        """
        return self._comparisons

    @comparisons.setter
    def comparisons(self, comparisons):
        """Sets the comparisons of this ReconciliationResponse.

        List of comparisons of left to right hand sides.  # noqa: E501

        :param comparisons: The comparisons of this ReconciliationResponse.  # noqa: E501
        :type comparisons: list[lusid.ReconciliationLine]
        """

        self._comparisons = comparisons

    @property
    def data_schema(self):
        """Gets the data_schema of this ReconciliationResponse.  # noqa: E501


        :return: The data_schema of this ReconciliationResponse.  # noqa: E501
        :rtype: lusid.ResultDataSchema
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this ReconciliationResponse.


        :param data_schema: The data_schema of this ReconciliationResponse.  # noqa: E501
        :type data_schema: lusid.ResultDataSchema
        """

        self._data_schema = data_schema

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
        if not isinstance(other, ReconciliationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationResponse):
            return True

        return self.to_dict() != other.to_dict()
