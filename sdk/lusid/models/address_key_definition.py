# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.230
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


class AddressKeyDefinition(object):
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
        'address_key': 'str',
        'type': 'str',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'address_key': 'addressKey',
        'type': 'type',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'address_key': 'required',
        'type': 'required',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, address_key=None, type=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """AddressKeyDefinition - a model defined in OpenAPI"
        
        :param address_key:  The address key of the address key definition. (required)
        :type address_key: str
        :param type:  The type of the address key definition (required)
        :type type: str
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address_key = None
        self._type = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.address_key = address_key
        self.type = type
        if version is not None:
            self.version = version
        self.links = links

    @property
    def address_key(self):
        """Gets the address_key of this AddressKeyDefinition.  # noqa: E501

        The address key of the address key definition.  # noqa: E501

        :return: The address_key of this AddressKeyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._address_key

    @address_key.setter
    def address_key(self, address_key):
        """Sets the address_key of this AddressKeyDefinition.

        The address key of the address key definition.  # noqa: E501

        :param address_key: The address_key of this AddressKeyDefinition.  # noqa: E501
        :type address_key: str
        """
        if self.local_vars_configuration.client_side_validation and address_key is None:  # noqa: E501
            raise ValueError("Invalid value for `address_key`, must not be `None`")  # noqa: E501

        self._address_key = address_key

    @property
    def type(self):
        """Gets the type of this AddressKeyDefinition.  # noqa: E501

        The type of the address key definition  # noqa: E501

        :return: The type of this AddressKeyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddressKeyDefinition.

        The type of the address key definition  # noqa: E501

        :param type: The type of this AddressKeyDefinition.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def version(self):
        """Gets the version of this AddressKeyDefinition.  # noqa: E501


        :return: The version of this AddressKeyDefinition.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AddressKeyDefinition.


        :param version: The version of this AddressKeyDefinition.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this AddressKeyDefinition.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this AddressKeyDefinition.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AddressKeyDefinition.

        Collection of links.  # noqa: E501

        :param links: The links of this AddressKeyDefinition.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, AddressKeyDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressKeyDefinition):
            return True

        return self.to_dict() != other.to_dict()
