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


class StagedModificationsInfo(object):
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
        'count_pending': 'int',
        'href_pending': 'str',
        'ids_previewed': 'list[str]'
    }

    attribute_map = {
        'count_pending': 'countPending',
        'href_pending': 'hrefPending',
        'ids_previewed': 'idsPreviewed'
    }

    required_map = {
        'count_pending': 'required',
        'href_pending': 'required',
        'ids_previewed': 'optional'
    }

    def __init__(self, count_pending=None, href_pending=None, ids_previewed=None, local_vars_configuration=None):  # noqa: E501
        """StagedModificationsInfo - a model defined in OpenAPI"
        
        :param count_pending:  The number of staged modifications for the entity with a status of Pending for the requested asAt. (required)
        :type count_pending: int
        :param href_pending:  Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (= Pending). (required)
        :type href_pending: str
        :param ids_previewed:  An array of the ids of any StagedModifications being previewed.
        :type ids_previewed: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count_pending = None
        self._href_pending = None
        self._ids_previewed = None
        self.discriminator = None

        self.count_pending = count_pending
        self.href_pending = href_pending
        self.ids_previewed = ids_previewed

    @property
    def count_pending(self):
        """Gets the count_pending of this StagedModificationsInfo.  # noqa: E501

        The number of staged modifications for the entity with a status of Pending for the requested asAt.  # noqa: E501

        :return: The count_pending of this StagedModificationsInfo.  # noqa: E501
        :rtype: int
        """
        return self._count_pending

    @count_pending.setter
    def count_pending(self, count_pending):
        """Sets the count_pending of this StagedModificationsInfo.

        The number of staged modifications for the entity with a status of Pending for the requested asAt.  # noqa: E501

        :param count_pending: The count_pending of this StagedModificationsInfo.  # noqa: E501
        :type count_pending: int
        """
        if self.local_vars_configuration.client_side_validation and count_pending is None:  # noqa: E501
            raise ValueError("Invalid value for `count_pending`, must not be `None`")  # noqa: E501

        self._count_pending = count_pending

    @property
    def href_pending(self):
        """Gets the href_pending of this StagedModificationsInfo.  # noqa: E501

        Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (= Pending).  # noqa: E501

        :return: The href_pending of this StagedModificationsInfo.  # noqa: E501
        :rtype: str
        """
        return self._href_pending

    @href_pending.setter
    def href_pending(self, href_pending):
        """Sets the href_pending of this StagedModificationsInfo.

        Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (= Pending).  # noqa: E501

        :param href_pending: The href_pending of this StagedModificationsInfo.  # noqa: E501
        :type href_pending: str
        """
        if self.local_vars_configuration.client_side_validation and href_pending is None:  # noqa: E501
            raise ValueError("Invalid value for `href_pending`, must not be `None`")  # noqa: E501

        self._href_pending = href_pending

    @property
    def ids_previewed(self):
        """Gets the ids_previewed of this StagedModificationsInfo.  # noqa: E501

        An array of the ids of any StagedModifications being previewed.  # noqa: E501

        :return: The ids_previewed of this StagedModificationsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids_previewed

    @ids_previewed.setter
    def ids_previewed(self, ids_previewed):
        """Sets the ids_previewed of this StagedModificationsInfo.

        An array of the ids of any StagedModifications being previewed.  # noqa: E501

        :param ids_previewed: The ids_previewed of this StagedModificationsInfo.  # noqa: E501
        :type ids_previewed: list[str]
        """

        self._ids_previewed = ids_previewed

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
        if not isinstance(other, StagedModificationsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModificationsInfo):
            return True

        return self.to_dict() != other.to_dict()
