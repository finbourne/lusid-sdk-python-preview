# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.150
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


class ClosePeriodDiaryEntryRequest(object):
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
        'diary_entry_code': 'str',
        'name': 'str',
        'effective_at': 'datetime',
        'query_as_at': 'datetime',
        'status': 'str',
        'properties': 'dict(str, ModelProperty)',
        'closing_options': 'list[str]'
    }

    attribute_map = {
        'diary_entry_code': 'diaryEntryCode',
        'name': 'name',
        'effective_at': 'effectiveAt',
        'query_as_at': 'queryAsAt',
        'status': 'status',
        'properties': 'properties',
        'closing_options': 'closingOptions'
    }

    required_map = {
        'diary_entry_code': 'optional',
        'name': 'optional',
        'effective_at': 'optional',
        'query_as_at': 'optional',
        'status': 'optional',
        'properties': 'optional',
        'closing_options': 'optional'
    }

    def __init__(self, diary_entry_code=None, name=None, effective_at=None, query_as_at=None, status=None, properties=None, closing_options=None, local_vars_configuration=None):  # noqa: E501
        """ClosePeriodDiaryEntryRequest - a model defined in OpenAPI"
        
        :param diary_entry_code:  Unique code assigned to a period. When left blank a code will be created by the system in the format 'yyyyMMDD'.
        :type diary_entry_code: str
        :param name:  Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format 'yyyyMMDD'.
        :type name: str
        :param effective_at:  The effective time of the diary entry.
        :type effective_at: datetime
        :param query_as_at:  The query time of the diary entry. Defaults to latest.
        :type query_as_at: datetime
        :param status:  The status of the diary entry. Defaults to 'Undefined' for valuation points and 'Estimate' for closing periods.
        :type status: str
        :param properties:  A set of properties for the diary entry.
        :type properties: dict[str, lusid.ModelProperty]
        :param closing_options:  The options which will be executed once a period is closed or locked.
        :type closing_options: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._diary_entry_code = None
        self._name = None
        self._effective_at = None
        self._query_as_at = None
        self._status = None
        self._properties = None
        self._closing_options = None
        self.discriminator = None

        self.diary_entry_code = diary_entry_code
        self.name = name
        self.effective_at = effective_at
        self.query_as_at = query_as_at
        self.status = status
        self.properties = properties
        self.closing_options = closing_options

    @property
    def diary_entry_code(self):
        """Gets the diary_entry_code of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        Unique code assigned to a period. When left blank a code will be created by the system in the format 'yyyyMMDD'.  # noqa: E501

        :return: The diary_entry_code of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._diary_entry_code

    @diary_entry_code.setter
    def diary_entry_code(self, diary_entry_code):
        """Sets the diary_entry_code of this ClosePeriodDiaryEntryRequest.

        Unique code assigned to a period. When left blank a code will be created by the system in the format 'yyyyMMDD'.  # noqa: E501

        :param diary_entry_code: The diary_entry_code of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type diary_entry_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                diary_entry_code is not None and len(diary_entry_code) > 64):
            raise ValueError("Invalid value for `diary_entry_code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diary_entry_code is not None and len(diary_entry_code) < 1):
            raise ValueError("Invalid value for `diary_entry_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diary_entry_code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', diary_entry_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `diary_entry_code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._diary_entry_code = diary_entry_code

    @property
    def name(self):
        """Gets the name of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format 'yyyyMMDD'.  # noqa: E501

        :return: The name of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClosePeriodDiaryEntryRequest.

        Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format 'yyyyMMDD'.  # noqa: E501

        :param name: The name of this ClosePeriodDiaryEntryRequest.  # noqa: E501
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
    def effective_at(self):
        """Gets the effective_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        The effective time of the diary entry.  # noqa: E501

        :return: The effective_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this ClosePeriodDiaryEntryRequest.

        The effective time of the diary entry.  # noqa: E501

        :param effective_at: The effective_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type effective_at: datetime
        """

        self._effective_at = effective_at

    @property
    def query_as_at(self):
        """Gets the query_as_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :return: The query_as_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._query_as_at

    @query_as_at.setter
    def query_as_at(self, query_as_at):
        """Sets the query_as_at of this ClosePeriodDiaryEntryRequest.

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :param query_as_at: The query_as_at of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type query_as_at: datetime
        """

        self._query_as_at = query_as_at

    @property
    def status(self):
        """Gets the status of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        The status of the diary entry. Defaults to 'Undefined' for valuation points and 'Estimate' for closing periods.  # noqa: E501

        :return: The status of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClosePeriodDiaryEntryRequest.

        The status of the diary entry. Defaults to 'Undefined' for valuation points and 'Estimate' for closing periods.  # noqa: E501

        :param status: The status of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def properties(self):
        """Gets the properties of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        A set of properties for the diary entry.  # noqa: E501

        :return: The properties of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ClosePeriodDiaryEntryRequest.

        A set of properties for the diary entry.  # noqa: E501

        :param properties: The properties of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def closing_options(self):
        """Gets the closing_options of this ClosePeriodDiaryEntryRequest.  # noqa: E501

        The options which will be executed once a period is closed or locked.  # noqa: E501

        :return: The closing_options of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._closing_options

    @closing_options.setter
    def closing_options(self, closing_options):
        """Sets the closing_options of this ClosePeriodDiaryEntryRequest.

        The options which will be executed once a period is closed or locked.  # noqa: E501

        :param closing_options: The closing_options of this ClosePeriodDiaryEntryRequest.  # noqa: E501
        :type closing_options: list[str]
        """

        self._closing_options = closing_options

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
        if not isinstance(other, ClosePeriodDiaryEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClosePeriodDiaryEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
