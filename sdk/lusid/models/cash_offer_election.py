# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.224
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


class CashOfferElection(object):
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
        'cash_offer_currency': 'str',
        'cash_offer_price': 'float',
        'election_key': 'str',
        'is_chosen': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'cash_offer_currency': 'cashOfferCurrency',
        'cash_offer_price': 'cashOfferPrice',
        'election_key': 'electionKey',
        'is_chosen': 'isChosen',
        'is_default': 'isDefault'
    }

    required_map = {
        'cash_offer_currency': 'required',
        'cash_offer_price': 'required',
        'election_key': 'required',
        'is_chosen': 'optional',
        'is_default': 'optional'
    }

    def __init__(self, cash_offer_currency=None, cash_offer_price=None, election_key=None, is_chosen=None, is_default=None, local_vars_configuration=None):  # noqa: E501
        """CashOfferElection - a model defined in OpenAPI"
        
        :param cash_offer_currency:  Currency of the cash offer (required)
        :type cash_offer_currency: str
        :param cash_offer_price:  Price per share of the cash offer (required)
        :type cash_offer_price: float
        :param election_key:  Unique key associated to this election. (required)
        :type election_key: str
        :param is_chosen:  Is this the election that has been explicitly chosen from multiple options.
        :type is_chosen: bool
        :param is_default:  Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
        :type is_default: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cash_offer_currency = None
        self._cash_offer_price = None
        self._election_key = None
        self._is_chosen = None
        self._is_default = None
        self.discriminator = None

        self.cash_offer_currency = cash_offer_currency
        self.cash_offer_price = cash_offer_price
        self.election_key = election_key
        if is_chosen is not None:
            self.is_chosen = is_chosen
        if is_default is not None:
            self.is_default = is_default

    @property
    def cash_offer_currency(self):
        """Gets the cash_offer_currency of this CashOfferElection.  # noqa: E501

        Currency of the cash offer  # noqa: E501

        :return: The cash_offer_currency of this CashOfferElection.  # noqa: E501
        :rtype: str
        """
        return self._cash_offer_currency

    @cash_offer_currency.setter
    def cash_offer_currency(self, cash_offer_currency):
        """Sets the cash_offer_currency of this CashOfferElection.

        Currency of the cash offer  # noqa: E501

        :param cash_offer_currency: The cash_offer_currency of this CashOfferElection.  # noqa: E501
        :type cash_offer_currency: str
        """
        if self.local_vars_configuration.client_side_validation and cash_offer_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `cash_offer_currency`, must not be `None`")  # noqa: E501

        self._cash_offer_currency = cash_offer_currency

    @property
    def cash_offer_price(self):
        """Gets the cash_offer_price of this CashOfferElection.  # noqa: E501

        Price per share of the cash offer  # noqa: E501

        :return: The cash_offer_price of this CashOfferElection.  # noqa: E501
        :rtype: float
        """
        return self._cash_offer_price

    @cash_offer_price.setter
    def cash_offer_price(self, cash_offer_price):
        """Sets the cash_offer_price of this CashOfferElection.

        Price per share of the cash offer  # noqa: E501

        :param cash_offer_price: The cash_offer_price of this CashOfferElection.  # noqa: E501
        :type cash_offer_price: float
        """
        if self.local_vars_configuration.client_side_validation and cash_offer_price is None:  # noqa: E501
            raise ValueError("Invalid value for `cash_offer_price`, must not be `None`")  # noqa: E501

        self._cash_offer_price = cash_offer_price

    @property
    def election_key(self):
        """Gets the election_key of this CashOfferElection.  # noqa: E501

        Unique key associated to this election.  # noqa: E501

        :return: The election_key of this CashOfferElection.  # noqa: E501
        :rtype: str
        """
        return self._election_key

    @election_key.setter
    def election_key(self, election_key):
        """Sets the election_key of this CashOfferElection.

        Unique key associated to this election.  # noqa: E501

        :param election_key: The election_key of this CashOfferElection.  # noqa: E501
        :type election_key: str
        """
        if self.local_vars_configuration.client_side_validation and election_key is None:  # noqa: E501
            raise ValueError("Invalid value for `election_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                election_key is not None and len(election_key) < 1):
            raise ValueError("Invalid value for `election_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._election_key = election_key

    @property
    def is_chosen(self):
        """Gets the is_chosen of this CashOfferElection.  # noqa: E501

        Is this the election that has been explicitly chosen from multiple options.  # noqa: E501

        :return: The is_chosen of this CashOfferElection.  # noqa: E501
        :rtype: bool
        """
        return self._is_chosen

    @is_chosen.setter
    def is_chosen(self, is_chosen):
        """Sets the is_chosen of this CashOfferElection.

        Is this the election that has been explicitly chosen from multiple options.  # noqa: E501

        :param is_chosen: The is_chosen of this CashOfferElection.  # noqa: E501
        :type is_chosen: bool
        """

        self._is_chosen = is_chosen

    @property
    def is_default(self):
        """Gets the is_default of this CashOfferElection.  # noqa: E501

        Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.  # noqa: E501

        :return: The is_default of this CashOfferElection.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CashOfferElection.

        Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.  # noqa: E501

        :param is_default: The is_default of this CashOfferElection.  # noqa: E501
        :type is_default: bool
        """

        self._is_default = is_default

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
        if not isinstance(other, CashOfferElection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashOfferElection):
            return True

        return self.to_dict() != other.to_dict()
