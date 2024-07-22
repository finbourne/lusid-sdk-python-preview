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


class ComponentFilter(object):
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
        'filter_id': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'filter_id': 'filterId',
        'filter': 'filter'
    }

    required_map = {
        'filter_id': 'required',
        'filter': 'required'
    }

    def __init__(self, filter_id=None, filter=None, local_vars_configuration=None):  # noqa: E501
        """ComponentFilter - a model defined in OpenAPI"
        
        :param filter_id:  (required)
        :type filter_id: str
        :param filter:  (required)
        :type filter: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_id = None
        self._filter = None
        self.discriminator = None

        self.filter_id = filter_id
        self.filter = filter

    @property
    def filter_id(self):
        """Gets the filter_id of this ComponentFilter.  # noqa: E501


        :return: The filter_id of this ComponentFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """Sets the filter_id of this ComponentFilter.


        :param filter_id: The filter_id of this ComponentFilter.  # noqa: E501
        :type filter_id: str
        """
        if self.local_vars_configuration.client_side_validation and filter_id is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter_id is not None and len(filter_id) > 16384):
            raise ValueError("Invalid value for `filter_id`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter_id is not None and len(filter_id) < 1):
            raise ValueError("Invalid value for `filter_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter_id is not None and not re.search(r'^[\s\S]*$', filter_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `filter_id`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._filter_id = filter_id

    @property
    def filter(self):
        """Gets the filter of this ComponentFilter.  # noqa: E501


        :return: The filter of this ComponentFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ComponentFilter.


        :param filter: The filter of this ComponentFilter.  # noqa: E501
        :type filter: str
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) > 16384):
            raise ValueError("Invalid value for `filter`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) < 1):
            raise ValueError("Invalid value for `filter`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and not re.search(r'^[\s\S]*$', filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._filter = filter

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
        if not isinstance(other, ComponentFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentFilter):
            return True

        return self.to_dict() != other.to_dict()
