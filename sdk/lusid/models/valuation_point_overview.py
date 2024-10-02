# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.236
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


class ValuationPointOverview(object):
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
        'diary_entry_code': 'str',
        'effective_from': 'datetime',
        'effective_to': 'datetime',
        'query_as_at': 'datetime',
        'type': 'str',
        'status': 'str',
        'gav': 'float',
        'nav': 'float',
        'properties': 'dict(str, ModelProperty)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'diary_entry_code': 'diaryEntryCode',
        'effective_from': 'effectiveFrom',
        'effective_to': 'effectiveTo',
        'query_as_at': 'queryAsAt',
        'type': 'type',
        'status': 'status',
        'gav': 'gav',
        'nav': 'nav',
        'properties': 'properties',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'diary_entry_code': 'required',
        'effective_from': 'required',
        'effective_to': 'required',
        'query_as_at': 'optional',
        'type': 'required',
        'status': 'required',
        'gav': 'required',
        'nav': 'required',
        'properties': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, diary_entry_code=None, effective_from=None, effective_to=None, query_as_at=None, type=None, status=None, gav=None, nav=None, properties=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ValuationPointOverview - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param diary_entry_code:  The code for the Valuation Point. (required)
        :type diary_entry_code: str
        :param effective_from:  The effective time of the last Valuation Point. (required)
        :type effective_from: datetime
        :param effective_to:  The effective time of the current Valuation Point. (required)
        :type effective_to: datetime
        :param query_as_at:  The query time of the Valuation Point. Defaults to latest.
        :type query_as_at: datetime
        :param type:  The type of the diary entry. This is 'ValuationPoint'. (required)
        :type type: str
        :param status:  The status of the Valuation Point. Can be 'Estimate', 'Candidate' or 'Final'. (required)
        :type status: str
        :param gav:  The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'. (required)
        :type gav: float
        :param nav:  The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. (required)
        :type nav: float
        :param properties:  The Fee properties. These will be from the 'Fee' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._diary_entry_code = None
        self._effective_from = None
        self._effective_to = None
        self._query_as_at = None
        self._type = None
        self._status = None
        self._gav = None
        self._nav = None
        self._properties = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.diary_entry_code = diary_entry_code
        self.effective_from = effective_from
        self.effective_to = effective_to
        if query_as_at is not None:
            self.query_as_at = query_as_at
        self.type = type
        self.status = status
        self.gav = gav
        self.nav = nav
        self.properties = properties
        self.links = links

    @property
    def href(self):
        """Gets the href of this ValuationPointOverview.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this ValuationPointOverview.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ValuationPointOverview.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this ValuationPointOverview.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def diary_entry_code(self):
        """Gets the diary_entry_code of this ValuationPointOverview.  # noqa: E501

        The code for the Valuation Point.  # noqa: E501

        :return: The diary_entry_code of this ValuationPointOverview.  # noqa: E501
        :rtype: str
        """
        return self._diary_entry_code

    @diary_entry_code.setter
    def diary_entry_code(self, diary_entry_code):
        """Sets the diary_entry_code of this ValuationPointOverview.

        The code for the Valuation Point.  # noqa: E501

        :param diary_entry_code: The diary_entry_code of this ValuationPointOverview.  # noqa: E501
        :type diary_entry_code: str
        """
        if self.local_vars_configuration.client_side_validation and diary_entry_code is None:  # noqa: E501
            raise ValueError("Invalid value for `diary_entry_code`, must not be `None`")  # noqa: E501

        self._diary_entry_code = diary_entry_code

    @property
    def effective_from(self):
        """Gets the effective_from of this ValuationPointOverview.  # noqa: E501

        The effective time of the last Valuation Point.  # noqa: E501

        :return: The effective_from of this ValuationPointOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this ValuationPointOverview.

        The effective time of the last Valuation Point.  # noqa: E501

        :param effective_from: The effective_from of this ValuationPointOverview.  # noqa: E501
        :type effective_from: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_from is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_from`, must not be `None`")  # noqa: E501

        self._effective_from = effective_from

    @property
    def effective_to(self):
        """Gets the effective_to of this ValuationPointOverview.  # noqa: E501

        The effective time of the current Valuation Point.  # noqa: E501

        :return: The effective_to of this ValuationPointOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_to

    @effective_to.setter
    def effective_to(self, effective_to):
        """Sets the effective_to of this ValuationPointOverview.

        The effective time of the current Valuation Point.  # noqa: E501

        :param effective_to: The effective_to of this ValuationPointOverview.  # noqa: E501
        :type effective_to: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_to is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_to`, must not be `None`")  # noqa: E501

        self._effective_to = effective_to

    @property
    def query_as_at(self):
        """Gets the query_as_at of this ValuationPointOverview.  # noqa: E501

        The query time of the Valuation Point. Defaults to latest.  # noqa: E501

        :return: The query_as_at of this ValuationPointOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._query_as_at

    @query_as_at.setter
    def query_as_at(self, query_as_at):
        """Sets the query_as_at of this ValuationPointOverview.

        The query time of the Valuation Point. Defaults to latest.  # noqa: E501

        :param query_as_at: The query_as_at of this ValuationPointOverview.  # noqa: E501
        :type query_as_at: datetime
        """

        self._query_as_at = query_as_at

    @property
    def type(self):
        """Gets the type of this ValuationPointOverview.  # noqa: E501

        The type of the diary entry. This is 'ValuationPoint'.  # noqa: E501

        :return: The type of this ValuationPointOverview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ValuationPointOverview.

        The type of the diary entry. This is 'ValuationPoint'.  # noqa: E501

        :param type: The type of this ValuationPointOverview.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this ValuationPointOverview.  # noqa: E501

        The status of the Valuation Point. Can be 'Estimate', 'Candidate' or 'Final'.  # noqa: E501

        :return: The status of this ValuationPointOverview.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ValuationPointOverview.

        The status of the Valuation Point. Can be 'Estimate', 'Candidate' or 'Final'.  # noqa: E501

        :param status: The status of this ValuationPointOverview.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def gav(self):
        """Gets the gav of this ValuationPointOverview.  # noqa: E501

        The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'.  # noqa: E501

        :return: The gav of this ValuationPointOverview.  # noqa: E501
        :rtype: float
        """
        return self._gav

    @gav.setter
    def gav(self, gav):
        """Sets the gav of this ValuationPointOverview.

        The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types 'Asset' and 'Liabilities'.  # noqa: E501

        :param gav: The gav of this ValuationPointOverview.  # noqa: E501
        :type gav: float
        """
        if self.local_vars_configuration.client_side_validation and gav is None:  # noqa: E501
            raise ValueError("Invalid value for `gav`, must not be `None`")  # noqa: E501

        self._gav = gav

    @property
    def nav(self):
        """Gets the nav of this ValuationPointOverview.  # noqa: E501

        The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.  # noqa: E501

        :return: The nav of this ValuationPointOverview.  # noqa: E501
        :rtype: float
        """
        return self._nav

    @nav.setter
    def nav(self, nav):
        """Sets the nav of this ValuationPointOverview.

        The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.  # noqa: E501

        :param nav: The nav of this ValuationPointOverview.  # noqa: E501
        :type nav: float
        """
        if self.local_vars_configuration.client_side_validation and nav is None:  # noqa: E501
            raise ValueError("Invalid value for `nav`, must not be `None`")  # noqa: E501

        self._nav = nav

    @property
    def properties(self):
        """Gets the properties of this ValuationPointOverview.  # noqa: E501

        The Fee properties. These will be from the 'Fee' domain.  # noqa: E501

        :return: The properties of this ValuationPointOverview.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ValuationPointOverview.

        The Fee properties. These will be from the 'Fee' domain.  # noqa: E501

        :param properties: The properties of this ValuationPointOverview.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def links(self):
        """Gets the links of this ValuationPointOverview.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this ValuationPointOverview.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ValuationPointOverview.

        Collection of links.  # noqa: E501

        :param links: The links of this ValuationPointOverview.  # noqa: E501
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
        if not isinstance(other, ValuationPointOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValuationPointOverview):
            return True

        return self.to_dict() != other.to_dict()
