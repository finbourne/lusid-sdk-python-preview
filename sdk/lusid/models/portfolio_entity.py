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


class PortfolioEntity(object):
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
        'entity_unique_id': 'str',
        'as_at_version_number': 'int',
        'status': 'str',
        'as_at_deleted': 'datetime',
        'user_id_deleted': 'str',
        'request_id_deleted': 'str',
        'effective_at_created': 'datetime',
        'prevailing_portfolio': 'PortfolioWithoutHref',
        'deleted_portfolio': 'PortfolioWithoutHref',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'entity_unique_id': 'entityUniqueId',
        'as_at_version_number': 'asAtVersionNumber',
        'status': 'status',
        'as_at_deleted': 'asAtDeleted',
        'user_id_deleted': 'userIdDeleted',
        'request_id_deleted': 'requestIdDeleted',
        'effective_at_created': 'effectiveAtCreated',
        'prevailing_portfolio': 'prevailingPortfolio',
        'deleted_portfolio': 'deletedPortfolio',
        'links': 'links'
    }

    required_map = {
        'href': 'required',
        'entity_unique_id': 'required',
        'as_at_version_number': 'optional',
        'status': 'required',
        'as_at_deleted': 'optional',
        'user_id_deleted': 'optional',
        'request_id_deleted': 'optional',
        'effective_at_created': 'optional',
        'prevailing_portfolio': 'optional',
        'deleted_portfolio': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, entity_unique_id=None, as_at_version_number=None, status=None, as_at_deleted=None, user_id_deleted=None, request_id_deleted=None, effective_at_created=None, prevailing_portfolio=None, deleted_portfolio=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioEntity - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. (required)
        :type href: str
        :param entity_unique_id:  The unique id of the entity. (required)
        :type entity_unique_id: str
        :param as_at_version_number:  The integer version number for the entity (the entity was created at version 1)
        :type as_at_version_number: int
        :param status:  The status of the entity at the current time. (required)
        :type status: str
        :param as_at_deleted:  The asAt datetime at which the entity was deleted.
        :type as_at_deleted: datetime
        :param user_id_deleted:  The unique id of the user who deleted the entity.
        :type user_id_deleted: str
        :param request_id_deleted:  The unique request id of the command that deleted the entity.
        :type request_id_deleted: str
        :param effective_at_created:  The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt.
        :type effective_at_created: datetime
        :param prevailing_portfolio: 
        :type prevailing_portfolio: lusid.PortfolioWithoutHref
        :param deleted_portfolio: 
        :type deleted_portfolio: lusid.PortfolioWithoutHref
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._entity_unique_id = None
        self._as_at_version_number = None
        self._status = None
        self._as_at_deleted = None
        self._user_id_deleted = None
        self._request_id_deleted = None
        self._effective_at_created = None
        self._prevailing_portfolio = None
        self._deleted_portfolio = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.entity_unique_id = entity_unique_id
        self.as_at_version_number = as_at_version_number
        self.status = status
        self.as_at_deleted = as_at_deleted
        self.user_id_deleted = user_id_deleted
        self.request_id_deleted = request_id_deleted
        self.effective_at_created = effective_at_created
        if prevailing_portfolio is not None:
            self.prevailing_portfolio = prevailing_portfolio
        if deleted_portfolio is not None:
            self.deleted_portfolio = deleted_portfolio
        self.links = links

    @property
    def href(self):
        """Gets the href of this PortfolioEntity.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PortfolioEntity.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PortfolioEntity.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PortfolioEntity.  # noqa: E501
        :type href: str
        """
        if self.local_vars_configuration.client_side_validation and href is None:  # noqa: E501
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def entity_unique_id(self):
        """Gets the entity_unique_id of this PortfolioEntity.  # noqa: E501

        The unique id of the entity.  # noqa: E501

        :return: The entity_unique_id of this PortfolioEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity_unique_id

    @entity_unique_id.setter
    def entity_unique_id(self, entity_unique_id):
        """Sets the entity_unique_id of this PortfolioEntity.

        The unique id of the entity.  # noqa: E501

        :param entity_unique_id: The entity_unique_id of this PortfolioEntity.  # noqa: E501
        :type entity_unique_id: str
        """
        if self.local_vars_configuration.client_side_validation and entity_unique_id is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_unique_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity_unique_id is not None and len(entity_unique_id) < 1):
            raise ValueError("Invalid value for `entity_unique_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_unique_id = entity_unique_id

    @property
    def as_at_version_number(self):
        """Gets the as_at_version_number of this PortfolioEntity.  # noqa: E501

        The integer version number for the entity (the entity was created at version 1)  # noqa: E501

        :return: The as_at_version_number of this PortfolioEntity.  # noqa: E501
        :rtype: int
        """
        return self._as_at_version_number

    @as_at_version_number.setter
    def as_at_version_number(self, as_at_version_number):
        """Sets the as_at_version_number of this PortfolioEntity.

        The integer version number for the entity (the entity was created at version 1)  # noqa: E501

        :param as_at_version_number: The as_at_version_number of this PortfolioEntity.  # noqa: E501
        :type as_at_version_number: int
        """

        self._as_at_version_number = as_at_version_number

    @property
    def status(self):
        """Gets the status of this PortfolioEntity.  # noqa: E501

        The status of the entity at the current time.  # noqa: E501

        :return: The status of this PortfolioEntity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortfolioEntity.

        The status of the entity at the current time.  # noqa: E501

        :param status: The status of this PortfolioEntity.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def as_at_deleted(self):
        """Gets the as_at_deleted of this PortfolioEntity.  # noqa: E501

        The asAt datetime at which the entity was deleted.  # noqa: E501

        :return: The as_at_deleted of this PortfolioEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_deleted

    @as_at_deleted.setter
    def as_at_deleted(self, as_at_deleted):
        """Sets the as_at_deleted of this PortfolioEntity.

        The asAt datetime at which the entity was deleted.  # noqa: E501

        :param as_at_deleted: The as_at_deleted of this PortfolioEntity.  # noqa: E501
        :type as_at_deleted: datetime
        """

        self._as_at_deleted = as_at_deleted

    @property
    def user_id_deleted(self):
        """Gets the user_id_deleted of this PortfolioEntity.  # noqa: E501

        The unique id of the user who deleted the entity.  # noqa: E501

        :return: The user_id_deleted of this PortfolioEntity.  # noqa: E501
        :rtype: str
        """
        return self._user_id_deleted

    @user_id_deleted.setter
    def user_id_deleted(self, user_id_deleted):
        """Sets the user_id_deleted of this PortfolioEntity.

        The unique id of the user who deleted the entity.  # noqa: E501

        :param user_id_deleted: The user_id_deleted of this PortfolioEntity.  # noqa: E501
        :type user_id_deleted: str
        """

        self._user_id_deleted = user_id_deleted

    @property
    def request_id_deleted(self):
        """Gets the request_id_deleted of this PortfolioEntity.  # noqa: E501

        The unique request id of the command that deleted the entity.  # noqa: E501

        :return: The request_id_deleted of this PortfolioEntity.  # noqa: E501
        :rtype: str
        """
        return self._request_id_deleted

    @request_id_deleted.setter
    def request_id_deleted(self, request_id_deleted):
        """Sets the request_id_deleted of this PortfolioEntity.

        The unique request id of the command that deleted the entity.  # noqa: E501

        :param request_id_deleted: The request_id_deleted of this PortfolioEntity.  # noqa: E501
        :type request_id_deleted: str
        """

        self._request_id_deleted = request_id_deleted

    @property
    def effective_at_created(self):
        """Gets the effective_at_created of this PortfolioEntity.  # noqa: E501

        The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt.  # noqa: E501

        :return: The effective_at_created of this PortfolioEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at_created

    @effective_at_created.setter
    def effective_at_created(self, effective_at_created):
        """Sets the effective_at_created of this PortfolioEntity.

        The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt.  # noqa: E501

        :param effective_at_created: The effective_at_created of this PortfolioEntity.  # noqa: E501
        :type effective_at_created: datetime
        """

        self._effective_at_created = effective_at_created

    @property
    def prevailing_portfolio(self):
        """Gets the prevailing_portfolio of this PortfolioEntity.  # noqa: E501


        :return: The prevailing_portfolio of this PortfolioEntity.  # noqa: E501
        :rtype: lusid.PortfolioWithoutHref
        """
        return self._prevailing_portfolio

    @prevailing_portfolio.setter
    def prevailing_portfolio(self, prevailing_portfolio):
        """Sets the prevailing_portfolio of this PortfolioEntity.


        :param prevailing_portfolio: The prevailing_portfolio of this PortfolioEntity.  # noqa: E501
        :type prevailing_portfolio: lusid.PortfolioWithoutHref
        """

        self._prevailing_portfolio = prevailing_portfolio

    @property
    def deleted_portfolio(self):
        """Gets the deleted_portfolio of this PortfolioEntity.  # noqa: E501


        :return: The deleted_portfolio of this PortfolioEntity.  # noqa: E501
        :rtype: lusid.PortfolioWithoutHref
        """
        return self._deleted_portfolio

    @deleted_portfolio.setter
    def deleted_portfolio(self, deleted_portfolio):
        """Sets the deleted_portfolio of this PortfolioEntity.


        :param deleted_portfolio: The deleted_portfolio of this PortfolioEntity.  # noqa: E501
        :type deleted_portfolio: lusid.PortfolioWithoutHref
        """

        self._deleted_portfolio = deleted_portfolio

    @property
    def links(self):
        """Gets the links of this PortfolioEntity.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioEntity.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioEntity.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioEntity.  # noqa: E501
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
        if not isinstance(other, PortfolioEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioEntity):
            return True

        return self.to_dict() != other.to_dict()
