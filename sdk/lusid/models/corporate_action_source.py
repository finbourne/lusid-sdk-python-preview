# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4454
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


class CorporateActionSource(object):
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
        'href': 'str',
        'id': 'ResourceId',
        'version': 'Version',
        'display_name': 'str',
        'description': 'str',
        'instrument_scopes': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'instrument_scopes': 'instrumentScopes',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'optional',
        'version': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'instrument_scopes': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, version=None, display_name=None, description=None, instrument_scopes=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CorporateActionSource - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id: 
        :type id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param display_name:  The name of the corporate action source
        :type display_name: str
        :param description:  The description of the corporate action source
        :type description: str
        :param instrument_scopes:  The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.
        :type instrument_scopes: list[str]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._id = None
        self._version = None
        self._display_name = None
        self._description = None
        self._instrument_scopes = None
        self._links = None
        self.discriminator = None

        self.href = href
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        self.display_name = display_name
        self.description = description
        self.instrument_scopes = instrument_scopes
        self.links = links

    @property
    def href(self):
        """Gets the href of this CorporateActionSource.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CorporateActionSource.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CorporateActionSource.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this CorporateActionSource.  # noqa: E501


        :return: The id of this CorporateActionSource.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CorporateActionSource.


        :param id: The id of this CorporateActionSource.  # noqa: E501
        :type id: lusid.ResourceId
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this CorporateActionSource.  # noqa: E501


        :return: The version of this CorporateActionSource.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CorporateActionSource.


        :param version: The version of this CorporateActionSource.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this CorporateActionSource.  # noqa: E501

        The name of the corporate action source  # noqa: E501

        :return: The display_name of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CorporateActionSource.

        The name of the corporate action source  # noqa: E501

        :param display_name: The display_name of this CorporateActionSource.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CorporateActionSource.  # noqa: E501

        The description of the corporate action source  # noqa: E501

        :return: The description of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CorporateActionSource.

        The description of the corporate action source  # noqa: E501

        :param description: The description of this CorporateActionSource.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def instrument_scopes(self):
        """Gets the instrument_scopes of this CorporateActionSource.  # noqa: E501

        The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.  # noqa: E501

        :return: The instrument_scopes of this CorporateActionSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._instrument_scopes

    @instrument_scopes.setter
    def instrument_scopes(self, instrument_scopes):
        """Sets the instrument_scopes of this CorporateActionSource.

        The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.  # noqa: E501

        :param instrument_scopes: The instrument_scopes of this CorporateActionSource.  # noqa: E501
        :type instrument_scopes: list[str]
        """

        self._instrument_scopes = instrument_scopes

    @property
    def links(self):
        """Gets the links of this CorporateActionSource.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this CorporateActionSource.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CorporateActionSource.

        Collection of links.  # noqa: E501

        :param links: The links of this CorporateActionSource.  # noqa: E501
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
        if not isinstance(other, CorporateActionSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CorporateActionSource):
            return True

        return self.to_dict() != other.to_dict()
