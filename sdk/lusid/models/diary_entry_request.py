# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.484
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


class DiaryEntryRequest(object):
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
        'name': 'str',
        'status': 'str',
        'effective_at': 'datetime',
        'query_as_at': 'datetime',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'effective_at': 'effectiveAt',
        'query_as_at': 'queryAsAt',
        'properties': 'properties'
    }

    required_map = {
        'name': 'optional',
        'status': 'optional',
        'effective_at': 'required',
        'query_as_at': 'optional',
        'properties': 'optional'
    }

    def __init__(self, name=None, status=None, effective_at=None, query_as_at=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """DiaryEntryRequest - a model defined in OpenAPI"
        
        :param name:  The name of the diary entry.
        :type name: str
        :param status:  The status of the diary entry. Defaults to 'Undefined'.
        :type status: str
        :param effective_at:  The effective time of the diary entry. (required)
        :type effective_at: datetime
        :param query_as_at:  The query time of the diary entry. Defaults to latest.
        :type query_as_at: datetime
        :param properties:  Properties to add to the diary entry.
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._status = None
        self._effective_at = None
        self._query_as_at = None
        self._properties = None
        self.discriminator = None

        self.name = name
        self.status = status
        self.effective_at = effective_at
        self.query_as_at = query_as_at
        self.properties = properties

    @property
    def name(self):
        """Gets the name of this DiaryEntryRequest.  # noqa: E501

        The name of the diary entry.  # noqa: E501

        :return: The name of this DiaryEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiaryEntryRequest.

        The name of the diary entry.  # noqa: E501

        :param name: The name of this DiaryEntryRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[\s\S]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this DiaryEntryRequest.  # noqa: E501

        The status of the diary entry. Defaults to 'Undefined'.  # noqa: E501

        :return: The status of this DiaryEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiaryEntryRequest.

        The status of the diary entry. Defaults to 'Undefined'.  # noqa: E501

        :param status: The status of this DiaryEntryRequest.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def effective_at(self):
        """Gets the effective_at of this DiaryEntryRequest.  # noqa: E501

        The effective time of the diary entry.  # noqa: E501

        :return: The effective_at of this DiaryEntryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this DiaryEntryRequest.

        The effective time of the diary entry.  # noqa: E501

        :param effective_at: The effective_at of this DiaryEntryRequest.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def query_as_at(self):
        """Gets the query_as_at of this DiaryEntryRequest.  # noqa: E501

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :return: The query_as_at of this DiaryEntryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._query_as_at

    @query_as_at.setter
    def query_as_at(self, query_as_at):
        """Sets the query_as_at of this DiaryEntryRequest.

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :param query_as_at: The query_as_at of this DiaryEntryRequest.  # noqa: E501
        :type query_as_at: datetime
        """

        self._query_as_at = query_as_at

    @property
    def properties(self):
        """Gets the properties of this DiaryEntryRequest.  # noqa: E501

        Properties to add to the diary entry.  # noqa: E501

        :return: The properties of this DiaryEntryRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DiaryEntryRequest.

        Properties to add to the diary entry.  # noqa: E501

        :param properties: The properties of this DiaryEntryRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

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
        if not isinstance(other, DiaryEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiaryEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
