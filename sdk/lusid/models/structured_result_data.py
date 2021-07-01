# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3220
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class StructuredResultData(object):
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
        'document_format': 'str',
        'version': 'str',
        'name': 'str',
        'document': 'str',
        'data_map_key': 'DataMapKey'
    }

    attribute_map = {
        'document_format': 'documentFormat',
        'version': 'version',
        'name': 'name',
        'document': 'document',
        'data_map_key': 'dataMapKey'
    }

    required_map = {
        'document_format': 'required',
        'version': 'optional',
        'name': 'optional',
        'document': 'required',
        'data_map_key': 'optional'
    }

    def __init__(self, document_format=None, version=None, name=None, document=None, data_map_key=None):  # noqa: E501
        """
        StructuredResultData - a model defined in OpenAPI

        :param document_format:  The format of the accompanying document. (required)
        :type document_format: str
        :param version:  The semantic version of the document format; MAJOR.MINOR.PATCH
        :type version: str
        :param name:  The name or description for the document
        :type name: str
        :param document:  The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields (required)
        :type document: str
        :param data_map_key: 
        :type data_map_key: lusid.DataMapKey

        """  # noqa: E501

        self._document_format = None
        self._version = None
        self._name = None
        self._document = None
        self._data_map_key = None
        self.discriminator = None

        self.document_format = document_format
        self.version = version
        self.name = name
        self.document = document
        if data_map_key is not None:
            self.data_map_key = data_map_key

    @property
    def document_format(self):
        """Gets the document_format of this StructuredResultData.  # noqa: E501

        The format of the accompanying document.  # noqa: E501

        :return: The document_format of this StructuredResultData.  # noqa: E501
        :rtype: str
        """
        return self._document_format

    @document_format.setter
    def document_format(self, document_format):
        """Sets the document_format of this StructuredResultData.

        The format of the accompanying document.  # noqa: E501

        :param document_format: The document_format of this StructuredResultData.  # noqa: E501
        :type: str
        """
        if document_format is None:
            raise ValueError("Invalid value for `document_format`, must not be `None`")  # noqa: E501

        self._document_format = document_format

    @property
    def version(self):
        """Gets the version of this StructuredResultData.  # noqa: E501

        The semantic version of the document format; MAJOR.MINOR.PATCH  # noqa: E501

        :return: The version of this StructuredResultData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StructuredResultData.

        The semantic version of the document format; MAJOR.MINOR.PATCH  # noqa: E501

        :param version: The version of this StructuredResultData.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this StructuredResultData.  # noqa: E501

        The name or description for the document  # noqa: E501

        :return: The name of this StructuredResultData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StructuredResultData.

        The name or description for the document  # noqa: E501

        :param name: The name of this StructuredResultData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def document(self):
        """Gets the document of this StructuredResultData.  # noqa: E501

        The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields  # noqa: E501

        :return: The document of this StructuredResultData.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this StructuredResultData.

        The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields  # noqa: E501

        :param document: The document of this StructuredResultData.  # noqa: E501
        :type: str
        """
        if document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def data_map_key(self):
        """Gets the data_map_key of this StructuredResultData.  # noqa: E501


        :return: The data_map_key of this StructuredResultData.  # noqa: E501
        :rtype: DataMapKey
        """
        return self._data_map_key

    @data_map_key.setter
    def data_map_key(self, data_map_key):
        """Sets the data_map_key of this StructuredResultData.


        :param data_map_key: The data_map_key of this StructuredResultData.  # noqa: E501
        :type: DataMapKey
        """

        self._data_map_key = data_map_key

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
        if not isinstance(other, StructuredResultData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
