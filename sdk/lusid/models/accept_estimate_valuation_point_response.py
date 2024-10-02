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


class AcceptEstimateValuationPointResponse(object):
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
        'candidate_valuation_point': 'ValuationPointDataResponse',
        'latest_valuation_point': 'ValuationPointDataResponse',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'candidate_valuation_point': 'candidateValuationPoint',
        'latest_valuation_point': 'latestValuationPoint',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'candidate_valuation_point': 'required',
        'latest_valuation_point': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, candidate_valuation_point=None, latest_valuation_point=None, links=None, local_vars_configuration=None):  # noqa: E501
        """AcceptEstimateValuationPointResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param candidate_valuation_point:  (required)
        :type candidate_valuation_point: lusid.ValuationPointDataResponse
        :param latest_valuation_point: 
        :type latest_valuation_point: lusid.ValuationPointDataResponse
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._candidate_valuation_point = None
        self._latest_valuation_point = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.candidate_valuation_point = candidate_valuation_point
        if latest_valuation_point is not None:
            self.latest_valuation_point = latest_valuation_point
        self.links = links

    @property
    def href(self):
        """Gets the href of this AcceptEstimateValuationPointResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AcceptEstimateValuationPointResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def candidate_valuation_point(self):
        """Gets the candidate_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501


        :return: The candidate_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :rtype: lusid.ValuationPointDataResponse
        """
        return self._candidate_valuation_point

    @candidate_valuation_point.setter
    def candidate_valuation_point(self, candidate_valuation_point):
        """Sets the candidate_valuation_point of this AcceptEstimateValuationPointResponse.


        :param candidate_valuation_point: The candidate_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :type candidate_valuation_point: lusid.ValuationPointDataResponse
        """
        if self.local_vars_configuration.client_side_validation and candidate_valuation_point is None:  # noqa: E501
            raise ValueError("Invalid value for `candidate_valuation_point`, must not be `None`")  # noqa: E501

        self._candidate_valuation_point = candidate_valuation_point

    @property
    def latest_valuation_point(self):
        """Gets the latest_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501


        :return: The latest_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :rtype: lusid.ValuationPointDataResponse
        """
        return self._latest_valuation_point

    @latest_valuation_point.setter
    def latest_valuation_point(self, latest_valuation_point):
        """Sets the latest_valuation_point of this AcceptEstimateValuationPointResponse.


        :param latest_valuation_point: The latest_valuation_point of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :type latest_valuation_point: lusid.ValuationPointDataResponse
        """

        self._latest_valuation_point = latest_valuation_point

    @property
    def links(self):
        """Gets the links of this AcceptEstimateValuationPointResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this AcceptEstimateValuationPointResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AcceptEstimateValuationPointResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this AcceptEstimateValuationPointResponse.  # noqa: E501
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
        if not isinstance(other, AcceptEstimateValuationPointResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AcceptEstimateValuationPointResponse):
            return True

        return self.to_dict() != other.to_dict()
