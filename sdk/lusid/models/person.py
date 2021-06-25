# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3197
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Person(object):
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
        'href': 'str',
        'lusid_person_id': 'str',
        'identifiers': 'dict(str, ModelProperty)',
        'properties': 'dict(str, list[ModelProperty])',
        'version': 'Version'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'href': 'href',
        'lusid_person_id': 'lusidPersonId',
        'identifiers': 'identifiers',
        'properties': 'properties',
        'version': 'version'
    }

    required_map = {
        'display_name': 'optional',
        'description': 'optional',
        'href': 'optional',
        'lusid_person_id': 'optional',
        'identifiers': 'optional',
        'properties': 'optional',
        'version': 'optional'
    }

    def __init__(self, display_name=None, description=None, href=None, lusid_person_id=None, identifiers=None, properties=None, version=None):  # noqa: E501
        """
        Person - a model defined in OpenAPI

        :param display_name:  The display name of the Person
        :type display_name: str
        :param description:  The description of the Person
        :type description: str
        :param href:  The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param lusid_person_id:  The unique LUSID Person Identifier (LUPID) of the Person.
        :type lusid_person_id: str
        :param identifiers:  Unique client-defined identifiers of the Person.
        :type identifiers: dict[str, lusid.ModelProperty]
        :param properties:  A set of properties associated to the Person. There can be multiple properties associated with a property key.
        :type properties: dict(str, list[ModelProperty])
        :param version: 
        :type version: lusid.Version

        """  # noqa: E501

        self._display_name = None
        self._description = None
        self._href = None
        self._lusid_person_id = None
        self._identifiers = None
        self._properties = None
        self._version = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.href = href
        self.lusid_person_id = lusid_person_id
        self.identifiers = identifiers
        self.properties = properties
        if version is not None:
            self.version = version

    @property
    def display_name(self):
        """Gets the display_name of this Person.  # noqa: E501

        The display name of the Person  # noqa: E501

        :return: The display_name of this Person.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Person.

        The display name of the Person  # noqa: E501

        :param display_name: The display_name of this Person.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Person.  # noqa: E501

        The description of the Person  # noqa: E501

        :return: The description of this Person.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Person.

        The description of the Person  # noqa: E501

        :param description: The description of this Person.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this Person.  # noqa: E501

        The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Person.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Person.

        The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Person.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def lusid_person_id(self):
        """Gets the lusid_person_id of this Person.  # noqa: E501

        The unique LUSID Person Identifier (LUPID) of the Person.  # noqa: E501

        :return: The lusid_person_id of this Person.  # noqa: E501
        :rtype: str
        """
        return self._lusid_person_id

    @lusid_person_id.setter
    def lusid_person_id(self, lusid_person_id):
        """Sets the lusid_person_id of this Person.

        The unique LUSID Person Identifier (LUPID) of the Person.  # noqa: E501

        :param lusid_person_id: The lusid_person_id of this Person.  # noqa: E501
        :type: str
        """

        self._lusid_person_id = lusid_person_id

    @property
    def identifiers(self):
        """Gets the identifiers of this Person.  # noqa: E501

        Unique client-defined identifiers of the Person.  # noqa: E501

        :return: The identifiers of this Person.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Person.

        Unique client-defined identifiers of the Person.  # noqa: E501

        :param identifiers: The identifiers of this Person.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._identifiers = identifiers

    @property
    def properties(self):
        """Gets the properties of this Person.  # noqa: E501

        A set of properties associated to the Person. There can be multiple properties associated with a property key.  # noqa: E501

        :return: The properties of this Person.  # noqa: E501
        :rtype: dict(str, list[ModelProperty])
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Person.

        A set of properties associated to the Person. There can be multiple properties associated with a property key.  # noqa: E501

        :param properties: The properties of this Person.  # noqa: E501
        :type: dict(str, list[ModelProperty])
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this Person.  # noqa: E501


        :return: The version of this Person.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Person.


        :param version: The version of this Person.  # noqa: E501
        :type: Version
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Person):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
