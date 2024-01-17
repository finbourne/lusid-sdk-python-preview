# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.58
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


class GeneralLedgerProfileMapping(object):
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
        'mapping_filter': 'str',
        'levels': 'list[str]'
    }

    attribute_map = {
        'mapping_filter': 'mappingFilter',
        'levels': 'levels'
    }

    required_map = {
        'mapping_filter': 'required',
        'levels': 'required'
    }

    def __init__(self, mapping_filter=None, levels=None, local_vars_configuration=None):  # noqa: E501
        """GeneralLedgerProfileMapping - a model defined in OpenAPI"
        
        :param mapping_filter:  The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax (required)
        :type mapping_filter: str
        :param levels:  References fields and properties on the associated Journal Entry Line and graph of associated objects. (required)
        :type levels: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._mapping_filter = None
        self._levels = None
        self.discriminator = None

        self.mapping_filter = mapping_filter
        self.levels = levels

    @property
    def mapping_filter(self):
        """Gets the mapping_filter of this GeneralLedgerProfileMapping.  # noqa: E501

        The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax  # noqa: E501

        :return: The mapping_filter of this GeneralLedgerProfileMapping.  # noqa: E501
        :rtype: str
        """
        return self._mapping_filter

    @mapping_filter.setter
    def mapping_filter(self, mapping_filter):
        """Sets the mapping_filter of this GeneralLedgerProfileMapping.

        The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax  # noqa: E501

        :param mapping_filter: The mapping_filter of this GeneralLedgerProfileMapping.  # noqa: E501
        :type mapping_filter: str
        """
        if self.local_vars_configuration.client_side_validation and mapping_filter is None:  # noqa: E501
            raise ValueError("Invalid value for `mapping_filter`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mapping_filter is not None and len(mapping_filter) > 16384):
            raise ValueError("Invalid value for `mapping_filter`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mapping_filter is not None and len(mapping_filter) < 1):
            raise ValueError("Invalid value for `mapping_filter`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mapping_filter is not None and not re.search(r'^[\s\S]*$', mapping_filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `mapping_filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._mapping_filter = mapping_filter

    @property
    def levels(self):
        """Gets the levels of this GeneralLedgerProfileMapping.  # noqa: E501

        References fields and properties on the associated Journal Entry Line and graph of associated objects.  # noqa: E501

        :return: The levels of this GeneralLedgerProfileMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this GeneralLedgerProfileMapping.

        References fields and properties on the associated Journal Entry Line and graph of associated objects.  # noqa: E501

        :param levels: The levels of this GeneralLedgerProfileMapping.  # noqa: E501
        :type levels: list[str]
        """
        if self.local_vars_configuration.client_side_validation and levels is None:  # noqa: E501
            raise ValueError("Invalid value for `levels`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                levels is not None and len(levels) > 5):
            raise ValueError("Invalid value for `levels`, number of items must be less than or equal to `5`")  # noqa: E501

        self._levels = levels

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
        if not isinstance(other, GeneralLedgerProfileMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralLedgerProfileMapping):
            return True

        return self.to_dict() != other.to_dict()
