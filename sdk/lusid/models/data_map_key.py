# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.359
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


class DataMapKey(object):
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
        'version': 'str',
        'code': 'str'
    }

    attribute_map = {
        'version': 'version',
        'code': 'code'
    }

    required_map = {
        'version': 'optional',
        'code': 'optional'
    }

    def __init__(self, version=None, code=None, local_vars_configuration=None):  # noqa: E501
        """DataMapKey - a model defined in OpenAPI"
        
        :param version:  The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it.
        :type version: str
        :param code:  A unique name to semantically identify the mapping set.
        :type code: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._code = None
        self.discriminator = None

        self.version = version
        self.code = code

    @property
    def version(self):
        """Gets the version of this DataMapKey.  # noqa: E501

        The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it.  # noqa: E501

        :return: The version of this DataMapKey.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DataMapKey.

        The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it.  # noqa: E501

        :param version: The version of this DataMapKey.  # noqa: E501
        :type version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 32):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 0):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not re.search(r'^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9\.-]{1,30})?$', version)):  # noqa: E501
            raise ValueError(r"Invalid value for `version`, must be a follow pattern or equal to `/^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9\.-]{1,30})?$/`")  # noqa: E501

        self._version = version

    @property
    def code(self):
        """Gets the code of this DataMapKey.  # noqa: E501

        A unique name to semantically identify the mapping set.  # noqa: E501

        :return: The code of this DataMapKey.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DataMapKey.

        A unique name to semantically identify the mapping set.  # noqa: E501

        :param code: The code of this DataMapKey.  # noqa: E501
        :type code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 256):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, DataMapKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataMapKey):
            return True

        return self.to_dict() != other.to_dict()
