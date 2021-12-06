# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3802
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


class BucketedCashFlowRequest(object):
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
        'rounding_method': 'str',
        'bucketing_dates': 'list[datetime]',
        'bucket_tenors': 'list[str]',
        'effective_at': 'str',
        'window_start': 'str',
        'window_end': 'str',
        'recipe_id': 'ResourceId',
        'report_currency': 'str',
        'as_at': 'datetime'
    }

    attribute_map = {
        'rounding_method': 'roundingMethod',
        'bucketing_dates': 'bucketingDates',
        'bucket_tenors': 'bucketTenors',
        'effective_at': 'effectiveAt',
        'window_start': 'windowStart',
        'window_end': 'windowEnd',
        'recipe_id': 'recipeId',
        'report_currency': 'reportCurrency',
        'as_at': 'asAt'
    }

    required_map = {
        'rounding_method': 'required',
        'bucketing_dates': 'optional',
        'bucket_tenors': 'optional',
        'effective_at': 'optional',
        'window_start': 'optional',
        'window_end': 'optional',
        'recipe_id': 'optional',
        'report_currency': 'optional',
        'as_at': 'optional'
    }

    def __init__(self, rounding_method=None, bucketing_dates=None, bucket_tenors=None, effective_at=None, window_start=None, window_end=None, recipe_id=None, report_currency=None, as_at=None, local_vars_configuration=None):  # noqa: E501
        """BucketedCashFlowRequest - a model defined in OpenAPI"
        
        :param rounding_method:  When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod    Supported string (enumeration) values are: [RoundDown, RoundUp]. (required)
        :type rounding_method: str
        :param bucketing_dates:  A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.
        :type bucketing_dates: list[datetime]
        :param bucket_tenors:  A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.
        :type bucket_tenors: list[str]
        :param effective_at:  The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.
        :type effective_at: str
        :param window_start:  The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified.
        :type window_start: str
        :param window_end:  The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to 'today' if it is not specified
        :type window_end: str
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param report_currency:  Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.
        :type report_currency: str
        :param as_at:  The asAt date to use
        :type as_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rounding_method = None
        self._bucketing_dates = None
        self._bucket_tenors = None
        self._effective_at = None
        self._window_start = None
        self._window_end = None
        self._recipe_id = None
        self._report_currency = None
        self._as_at = None
        self.discriminator = None

        self.rounding_method = rounding_method
        self.bucketing_dates = bucketing_dates
        self.bucket_tenors = bucket_tenors
        self.effective_at = effective_at
        self.window_start = window_start
        self.window_end = window_end
        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.report_currency = report_currency
        self.as_at = as_at

    @property
    def rounding_method(self):
        """Gets the rounding_method of this BucketedCashFlowRequest.  # noqa: E501

        When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod    Supported string (enumeration) values are: [RoundDown, RoundUp].  # noqa: E501

        :return: The rounding_method of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._rounding_method

    @rounding_method.setter
    def rounding_method(self, rounding_method):
        """Sets the rounding_method of this BucketedCashFlowRequest.

        When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod    Supported string (enumeration) values are: [RoundDown, RoundUp].  # noqa: E501

        :param rounding_method: The rounding_method of this BucketedCashFlowRequest.  # noqa: E501
        :type rounding_method: str
        """
        if self.local_vars_configuration.client_side_validation and rounding_method is None:  # noqa: E501
            raise ValueError("Invalid value for `rounding_method`, must not be `None`")  # noqa: E501

        self._rounding_method = rounding_method

    @property
    def bucketing_dates(self):
        """Gets the bucketing_dates of this BucketedCashFlowRequest.  # noqa: E501

        A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.  # noqa: E501

        :return: The bucketing_dates of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._bucketing_dates

    @bucketing_dates.setter
    def bucketing_dates(self, bucketing_dates):
        """Sets the bucketing_dates of this BucketedCashFlowRequest.

        A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.  # noqa: E501

        :param bucketing_dates: The bucketing_dates of this BucketedCashFlowRequest.  # noqa: E501
        :type bucketing_dates: list[datetime]
        """

        self._bucketing_dates = bucketing_dates

    @property
    def bucket_tenors(self):
        """Gets the bucket_tenors of this BucketedCashFlowRequest.  # noqa: E501

        A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.  # noqa: E501

        :return: The bucket_tenors of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bucket_tenors

    @bucket_tenors.setter
    def bucket_tenors(self, bucket_tenors):
        """Sets the bucket_tenors of this BucketedCashFlowRequest.

        A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.  # noqa: E501

        :param bucket_tenors: The bucket_tenors of this BucketedCashFlowRequest.  # noqa: E501
        :type bucket_tenors: list[str]
        """

        self._bucket_tenors = bucket_tenors

    @property
    def effective_at(self):
        """Gets the effective_at of this BucketedCashFlowRequest.  # noqa: E501

        The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.  # noqa: E501

        :return: The effective_at of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this BucketedCashFlowRequest.

        The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.  # noqa: E501

        :param effective_at: The effective_at of this BucketedCashFlowRequest.  # noqa: E501
        :type effective_at: str
        """

        self._effective_at = effective_at

    @property
    def window_start(self):
        """Gets the window_start of this BucketedCashFlowRequest.  # noqa: E501

        The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified.  # noqa: E501

        :return: The window_start of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._window_start

    @window_start.setter
    def window_start(self, window_start):
        """Sets the window_start of this BucketedCashFlowRequest.

        The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified.  # noqa: E501

        :param window_start: The window_start of this BucketedCashFlowRequest.  # noqa: E501
        :type window_start: str
        """

        self._window_start = window_start

    @property
    def window_end(self):
        """Gets the window_end of this BucketedCashFlowRequest.  # noqa: E501

        The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to 'today' if it is not specified  # noqa: E501

        :return: The window_end of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._window_end

    @window_end.setter
    def window_end(self, window_end):
        """Sets the window_end of this BucketedCashFlowRequest.

        The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to 'today' if it is not specified  # noqa: E501

        :param window_end: The window_end of this BucketedCashFlowRequest.  # noqa: E501
        :type window_end: str
        """

        self._window_end = window_end

    @property
    def recipe_id(self):
        """Gets the recipe_id of this BucketedCashFlowRequest.  # noqa: E501


        :return: The recipe_id of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this BucketedCashFlowRequest.


        :param recipe_id: The recipe_id of this BucketedCashFlowRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def report_currency(self):
        """Gets the report_currency of this BucketedCashFlowRequest.  # noqa: E501

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.  # noqa: E501

        :return: The report_currency of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_currency

    @report_currency.setter
    def report_currency(self, report_currency):
        """Sets the report_currency of this BucketedCashFlowRequest.

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.  # noqa: E501

        :param report_currency: The report_currency of this BucketedCashFlowRequest.  # noqa: E501
        :type report_currency: str
        """
        if (self.local_vars_configuration.client_side_validation and
                report_currency is not None and len(report_currency) > 3):
            raise ValueError("Invalid value for `report_currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                report_currency is not None and len(report_currency) < 0):
            raise ValueError("Invalid value for `report_currency`, length must be greater than or equal to `0`")  # noqa: E501

        self._report_currency = report_currency

    @property
    def as_at(self):
        """Gets the as_at of this BucketedCashFlowRequest.  # noqa: E501

        The asAt date to use  # noqa: E501

        :return: The as_at of this BucketedCashFlowRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this BucketedCashFlowRequest.

        The asAt date to use  # noqa: E501

        :param as_at: The as_at of this BucketedCashFlowRequest.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

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
        if not isinstance(other, BucketedCashFlowRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BucketedCashFlowRequest):
            return True

        return self.to_dict() != other.to_dict()
