# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.622
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


class PostingModuleDetails(object):
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
        'display_name': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'status': 'status'
    }

    required_map = {
        'display_name': 'required',
        'description': 'optional',
        'status': 'required'
    }

    def __init__(self, display_name=None, description=None, status=None, local_vars_configuration=None):  # noqa: E501
        """PostingModuleDetails - a model defined in OpenAPI"
        
        :param display_name:  The name of the Posting Module. (required)
        :type display_name: str
        :param description:  A description for the Posting Module.
        :type description: str
        :param status:  The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. (required)
        :type status: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._description = None
        self._status = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.status = status

    @property
    def display_name(self):
        """Gets the display_name of this PostingModuleDetails.  # noqa: E501

        The name of the Posting Module.  # noqa: E501

        :return: The display_name of this PostingModuleDetails.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PostingModuleDetails.

        The name of the Posting Module.  # noqa: E501

        :param display_name: The display_name of this PostingModuleDetails.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 256):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[^\\<>&\"]+$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[^\\<>&\"]+$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PostingModuleDetails.  # noqa: E501

        A description for the Posting Module.  # noqa: E501

        :return: The description of this PostingModuleDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostingModuleDetails.

        A description for the Posting Module.  # noqa: E501

        :param description: The description of this PostingModuleDetails.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def status(self):
        """Gets the status of this PostingModuleDetails.  # noqa: E501

        The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :return: The status of this PostingModuleDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostingModuleDetails.

        The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :param status: The status of this PostingModuleDetails.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, PostingModuleDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostingModuleDetails):
            return True

        return self.to_dict() != other.to_dict()
