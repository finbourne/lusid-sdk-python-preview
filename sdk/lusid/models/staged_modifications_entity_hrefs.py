# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.156
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


class StagedModificationsEntityHrefs(object):
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
        'when_staged': 'str',
        'preview': 'str',
        'latest': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'when_staged': 'whenStaged',
        'preview': 'preview',
        'latest': 'latest',
        'links': 'links'
    }

    required_map = {
        'when_staged': 'optional',
        'preview': 'optional',
        'latest': 'optional',
        'links': 'optional'
    }

    def __init__(self, when_staged=None, preview=None, latest=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StagedModificationsEntityHrefs - a model defined in OpenAPI"
        
        :param when_staged:  The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested.
        :type when_staged: str
        :param preview:  The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied.
        :type preview: str
        :param latest:  The specific Uniform Resource Identifier (URI) for the staged modification at latest time.
        :type latest: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._when_staged = None
        self._preview = None
        self._latest = None
        self._links = None
        self.discriminator = None

        self.when_staged = when_staged
        self.preview = preview
        self.latest = latest
        self.links = links

    @property
    def when_staged(self):
        """Gets the when_staged of this StagedModificationsEntityHrefs.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested.  # noqa: E501

        :return: The when_staged of this StagedModificationsEntityHrefs.  # noqa: E501
        :rtype: str
        """
        return self._when_staged

    @when_staged.setter
    def when_staged(self, when_staged):
        """Sets the when_staged of this StagedModificationsEntityHrefs.

        The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested.  # noqa: E501

        :param when_staged: The when_staged of this StagedModificationsEntityHrefs.  # noqa: E501
        :type when_staged: str
        """

        self._when_staged = when_staged

    @property
    def preview(self):
        """Gets the preview of this StagedModificationsEntityHrefs.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied.  # noqa: E501

        :return: The preview of this StagedModificationsEntityHrefs.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this StagedModificationsEntityHrefs.

        The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied.  # noqa: E501

        :param preview: The preview of this StagedModificationsEntityHrefs.  # noqa: E501
        :type preview: str
        """

        self._preview = preview

    @property
    def latest(self):
        """Gets the latest of this StagedModificationsEntityHrefs.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for the staged modification at latest time.  # noqa: E501

        :return: The latest of this StagedModificationsEntityHrefs.  # noqa: E501
        :rtype: str
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this StagedModificationsEntityHrefs.

        The specific Uniform Resource Identifier (URI) for the staged modification at latest time.  # noqa: E501

        :param latest: The latest of this StagedModificationsEntityHrefs.  # noqa: E501
        :type latest: str
        """

        self._latest = latest

    @property
    def links(self):
        """Gets the links of this StagedModificationsEntityHrefs.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this StagedModificationsEntityHrefs.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StagedModificationsEntityHrefs.

        Collection of links.  # noqa: E501

        :param links: The links of this StagedModificationsEntityHrefs.  # noqa: E501
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
        if not isinstance(other, StagedModificationsEntityHrefs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModificationsEntityHrefs):
            return True

        return self.to_dict() != other.to_dict()
