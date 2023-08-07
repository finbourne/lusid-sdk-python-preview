# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.419
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


class MarketDataSpecificRule(object):
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
        'key': 'str',
        'supplier': 'str',
        'data_scope': 'str',
        'quote_type': 'str',
        'field': 'str',
        'quote_interval': 'str',
        'as_at': 'datetime',
        'price_source': 'str',
        'mask': 'str',
        'dependency_source_filter': 'DependencySourceFilter',
        'source_system': 'str'
    }

    attribute_map = {
        'key': 'key',
        'supplier': 'supplier',
        'data_scope': 'dataScope',
        'quote_type': 'quoteType',
        'field': 'field',
        'quote_interval': 'quoteInterval',
        'as_at': 'asAt',
        'price_source': 'priceSource',
        'mask': 'mask',
        'dependency_source_filter': 'dependencySourceFilter',
        'source_system': 'sourceSystem'
    }

    required_map = {
        'key': 'required',
        'supplier': 'required',
        'data_scope': 'required',
        'quote_type': 'required',
        'field': 'required',
        'quote_interval': 'optional',
        'as_at': 'optional',
        'price_source': 'optional',
        'mask': 'optional',
        'dependency_source_filter': 'required',
        'source_system': 'optional'
    }

    def __init__(self, key=None, supplier=None, data_scope=None, quote_type=None, field=None, quote_interval=None, as_at=None, price_source=None, mask=None, dependency_source_filter=None, source_system=None, local_vars_configuration=None):  # noqa: E501
        """MarketDataSpecificRule - a model defined in OpenAPI"
        
        :param key:  The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*) (required)
        :type key: str
        :param supplier:  The market data supplier (where the data comes from) (required)
        :type supplier: str
        :param data_scope:  The scope in which the data should be found when using this rule. (required)
        :type data_scope: str
        :param quote_type:  The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor (required)
        :type quote_type: str
        :param field:  The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId (required)
        :type field: str
        :param quote_interval:  Shorthand for the time interval used to select market data. This must be a dot-separated string              nominating a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago). The syntax              is <i>int</i><i>char</i>.<i>int</i><i>char</i>, where <i>char</i> is one of D(ay), W(eek), M(onth) or Y(ear).
        :type quote_interval: str
        :param as_at:  The AsAt predicate specification.
        :type as_at: datetime
        :param price_source:  The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote
        :type price_source: str
        :param mask:  Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.
        :type mask: str
        :param dependency_source_filter:  (required)
        :type dependency_source_filter: lusid.DependencySourceFilter
        :param source_system:  Determines from where LUSID should attempt to find the data. Optional and, if omitted, will default to \"Lusid\".  This means that data will be retrieved from the Quotes store and the ComplexMarketData store.  These can be populated using the Quotes and ComplexMarketData endpoints.
        :type source_system: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._supplier = None
        self._data_scope = None
        self._quote_type = None
        self._field = None
        self._quote_interval = None
        self._as_at = None
        self._price_source = None
        self._mask = None
        self._dependency_source_filter = None
        self._source_system = None
        self.discriminator = None

        self.key = key
        self.supplier = supplier
        self.data_scope = data_scope
        self.quote_type = quote_type
        self.field = field
        self.quote_interval = quote_interval
        self.as_at = as_at
        self.price_source = price_source
        self.mask = mask
        self.dependency_source_filter = dependency_source_filter
        self.source_system = source_system

    @property
    def key(self):
        """Gets the key of this MarketDataSpecificRule.  # noqa: E501

        The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*)  # noqa: E501

        :return: The key of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MarketDataSpecificRule.

        The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*)  # noqa: E501

        :param key: The key of this MarketDataSpecificRule.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) > 128):
            raise ValueError("Invalid value for `key`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 0):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `0`")  # noqa: E501

        self._key = key

    @property
    def supplier(self):
        """Gets the supplier of this MarketDataSpecificRule.  # noqa: E501

        The market data supplier (where the data comes from)  # noqa: E501

        :return: The supplier of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this MarketDataSpecificRule.

        The market data supplier (where the data comes from)  # noqa: E501

        :param supplier: The supplier of this MarketDataSpecificRule.  # noqa: E501
        :type supplier: str
        """
        if self.local_vars_configuration.client_side_validation and supplier is None:  # noqa: E501
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) > 32):
            raise ValueError("Invalid value for `supplier`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) < 0):
            raise ValueError("Invalid value for `supplier`, length must be greater than or equal to `0`")  # noqa: E501

        self._supplier = supplier

    @property
    def data_scope(self):
        """Gets the data_scope of this MarketDataSpecificRule.  # noqa: E501

        The scope in which the data should be found when using this rule.  # noqa: E501

        :return: The data_scope of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._data_scope

    @data_scope.setter
    def data_scope(self, data_scope):
        """Sets the data_scope of this MarketDataSpecificRule.

        The scope in which the data should be found when using this rule.  # noqa: E501

        :param data_scope: The data_scope of this MarketDataSpecificRule.  # noqa: E501
        :type data_scope: str
        """
        if self.local_vars_configuration.client_side_validation and data_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `data_scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) > 256):
            raise ValueError("Invalid value for `data_scope`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) < 1):
            raise ValueError("Invalid value for `data_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', data_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `data_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._data_scope = data_scope

    @property
    def quote_type(self):
        """Gets the quote_type of this MarketDataSpecificRule.  # noqa: E501

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor  # noqa: E501

        :return: The quote_type of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type):
        """Sets the quote_type of this MarketDataSpecificRule.

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor  # noqa: E501

        :param quote_type: The quote_type of this MarketDataSpecificRule.  # noqa: E501
        :type quote_type: str
        """
        if self.local_vars_configuration.client_side_validation and quote_type is None:  # noqa: E501
            raise ValueError("Invalid value for `quote_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Price", "Spread", "Rate", "LogNormalVol", "NormalVol", "ParSpread", "IsdaSpread", "Upfront", "Index", "Ratio", "Delta", "PoolFactor"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and quote_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `quote_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_type, allowed_values)
            )

        self._quote_type = quote_type

    @property
    def field(self):
        """Gets the field of this MarketDataSpecificRule.  # noqa: E501

        The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId  # noqa: E501

        :return: The field of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this MarketDataSpecificRule.

        The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId  # noqa: E501

        :param field: The field of this MarketDataSpecificRule.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                field is not None and len(field) > 32):
            raise ValueError("Invalid value for `field`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                field is not None and len(field) < 0):
            raise ValueError("Invalid value for `field`, length must be greater than or equal to `0`")  # noqa: E501

        self._field = field

    @property
    def quote_interval(self):
        """Gets the quote_interval of this MarketDataSpecificRule.  # noqa: E501

        Shorthand for the time interval used to select market data. This must be a dot-separated string              nominating a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago). The syntax              is <i>int</i><i>char</i>.<i>int</i><i>char</i>, where <i>char</i> is one of D(ay), W(eek), M(onth) or Y(ear).  # noqa: E501

        :return: The quote_interval of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._quote_interval

    @quote_interval.setter
    def quote_interval(self, quote_interval):
        """Sets the quote_interval of this MarketDataSpecificRule.

        Shorthand for the time interval used to select market data. This must be a dot-separated string              nominating a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago). The syntax              is <i>int</i><i>char</i>.<i>int</i><i>char</i>, where <i>char</i> is one of D(ay), W(eek), M(onth) or Y(ear).  # noqa: E501

        :param quote_interval: The quote_interval of this MarketDataSpecificRule.  # noqa: E501
        :type quote_interval: str
        """
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) > 16):
            raise ValueError("Invalid value for `quote_interval`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) < 0):
            raise ValueError("Invalid value for `quote_interval`, length must be greater than or equal to `0`")  # noqa: E501

        self._quote_interval = quote_interval

    @property
    def as_at(self):
        """Gets the as_at of this MarketDataSpecificRule.  # noqa: E501

        The AsAt predicate specification.  # noqa: E501

        :return: The as_at of this MarketDataSpecificRule.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this MarketDataSpecificRule.

        The AsAt predicate specification.  # noqa: E501

        :param as_at: The as_at of this MarketDataSpecificRule.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def price_source(self):
        """Gets the price_source of this MarketDataSpecificRule.  # noqa: E501

        The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote  # noqa: E501

        :return: The price_source of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._price_source

    @price_source.setter
    def price_source(self, price_source):
        """Sets the price_source of this MarketDataSpecificRule.

        The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote  # noqa: E501

        :param price_source: The price_source of this MarketDataSpecificRule.  # noqa: E501
        :type price_source: str
        """
        if (self.local_vars_configuration.client_side_validation and
                price_source is not None and len(price_source) > 256):
            raise ValueError("Invalid value for `price_source`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                price_source is not None and len(price_source) < 0):
            raise ValueError("Invalid value for `price_source`, length must be greater than or equal to `0`")  # noqa: E501

        self._price_source = price_source

    @property
    def mask(self):
        """Gets the mask of this MarketDataSpecificRule.  # noqa: E501

        Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.  # noqa: E501

        :return: The mask of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this MarketDataSpecificRule.

        Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.  # noqa: E501

        :param mask: The mask of this MarketDataSpecificRule.  # noqa: E501
        :type mask: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mask is not None and len(mask) > 256):
            raise ValueError("Invalid value for `mask`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mask is not None and len(mask) < 0):
            raise ValueError("Invalid value for `mask`, length must be greater than or equal to `0`")  # noqa: E501

        self._mask = mask

    @property
    def dependency_source_filter(self):
        """Gets the dependency_source_filter of this MarketDataSpecificRule.  # noqa: E501


        :return: The dependency_source_filter of this MarketDataSpecificRule.  # noqa: E501
        :rtype: lusid.DependencySourceFilter
        """
        return self._dependency_source_filter

    @dependency_source_filter.setter
    def dependency_source_filter(self, dependency_source_filter):
        """Sets the dependency_source_filter of this MarketDataSpecificRule.


        :param dependency_source_filter: The dependency_source_filter of this MarketDataSpecificRule.  # noqa: E501
        :type dependency_source_filter: lusid.DependencySourceFilter
        """
        if self.local_vars_configuration.client_side_validation and dependency_source_filter is None:  # noqa: E501
            raise ValueError("Invalid value for `dependency_source_filter`, must not be `None`")  # noqa: E501

        self._dependency_source_filter = dependency_source_filter

    @property
    def source_system(self):
        """Gets the source_system of this MarketDataSpecificRule.  # noqa: E501

        Determines from where LUSID should attempt to find the data. Optional and, if omitted, will default to \"Lusid\".  This means that data will be retrieved from the Quotes store and the ComplexMarketData store.  These can be populated using the Quotes and ComplexMarketData endpoints.  # noqa: E501

        :return: The source_system of this MarketDataSpecificRule.  # noqa: E501
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        """Sets the source_system of this MarketDataSpecificRule.

        Determines from where LUSID should attempt to find the data. Optional and, if omitted, will default to \"Lusid\".  This means that data will be retrieved from the Quotes store and the ComplexMarketData store.  These can be populated using the Quotes and ComplexMarketData endpoints.  # noqa: E501

        :param source_system: The source_system of this MarketDataSpecificRule.  # noqa: E501
        :type source_system: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source_system is not None and len(source_system) > 256):
            raise ValueError("Invalid value for `source_system`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_system is not None and len(source_system) < 0):
            raise ValueError("Invalid value for `source_system`, length must be greater than or equal to `0`")  # noqa: E501

        self._source_system = source_system

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
        if not isinstance(other, MarketDataSpecificRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketDataSpecificRule):
            return True

        return self.to_dict() != other.to_dict()
