# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.195
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


class ElectionSpecification(object):
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
        'election_type': 'str',
        'cardinality': 'dict(str, str)',
        'referenced_as': 'list[str]'
    }

    attribute_map = {
        'election_type': 'electionType',
        'cardinality': 'cardinality',
        'referenced_as': 'referencedAs'
    }

    required_map = {
        'election_type': 'required',
        'cardinality': 'required',
        'referenced_as': 'required'
    }

    def __init__(self, election_type=None, cardinality=None, referenced_as=None, local_vars_configuration=None):  # noqa: E501
        """ElectionSpecification - a model defined in OpenAPI"
        
        :param election_type:  (required)
        :type election_type: str
        :param cardinality:  (required)
        :type cardinality: dict(str, str)
        :param referenced_as:  (required)
        :type referenced_as: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._election_type = None
        self._cardinality = None
        self._referenced_as = None
        self.discriminator = None

        self.election_type = election_type
        self.cardinality = cardinality
        self.referenced_as = referenced_as

    @property
    def election_type(self):
        """Gets the election_type of this ElectionSpecification.  # noqa: E501


        :return: The election_type of this ElectionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._election_type

    @election_type.setter
    def election_type(self, election_type):
        """Sets the election_type of this ElectionSpecification.


        :param election_type: The election_type of this ElectionSpecification.  # noqa: E501
        :type election_type: str
        """
        if self.local_vars_configuration.client_side_validation and election_type is None:  # noqa: E501
            raise ValueError("Invalid value for `election_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                election_type is not None and len(election_type) < 1):
            raise ValueError("Invalid value for `election_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._election_type = election_type

    @property
    def cardinality(self):
        """Gets the cardinality of this ElectionSpecification.  # noqa: E501


        :return: The cardinality of this ElectionSpecification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this ElectionSpecification.


        :param cardinality: The cardinality of this ElectionSpecification.  # noqa: E501
        :type cardinality: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `cardinality`, must not be `None`")  # noqa: E501

        self._cardinality = cardinality

    @property
    def referenced_as(self):
        """Gets the referenced_as of this ElectionSpecification.  # noqa: E501


        :return: The referenced_as of this ElectionSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._referenced_as

    @referenced_as.setter
    def referenced_as(self, referenced_as):
        """Sets the referenced_as of this ElectionSpecification.


        :param referenced_as: The referenced_as of this ElectionSpecification.  # noqa: E501
        :type referenced_as: list[str]
        """
        if self.local_vars_configuration.client_side_validation and referenced_as is None:  # noqa: E501
            raise ValueError("Invalid value for `referenced_as`, must not be `None`")  # noqa: E501

        self._referenced_as = referenced_as

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
        if not isinstance(other, ElectionSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectionSpecification):
            return True

        return self.to_dict() != other.to_dict()
