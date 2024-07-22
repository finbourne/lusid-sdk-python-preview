# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.195
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


class PortfolioWithoutHref(object):
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
        'id': 'ResourceId',
        'type': 'str',
        'display_name': 'str',
        'description': 'str',
        'created': 'datetime',
        'parent_portfolio_id': 'ResourceId',
        'version': 'Version',
        'staged_modifications': 'StagedModificationsInfo',
        'is_derived': 'bool',
        'base_currency': 'str',
        'properties': 'dict(str, ModelProperty)',
        'relationships': 'list[Relationship]',
        'instrument_scopes': 'list[str]',
        'accounting_method': 'str',
        'amortisation_method': 'str',
        'transaction_type_scope': 'str',
        'cash_gain_loss_calculation_date': 'str',
        'instrument_event_configuration': 'InstrumentEventConfiguration',
        'amortisation_rule_set_id': 'ResourceId',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'display_name': 'displayName',
        'description': 'description',
        'created': 'created',
        'parent_portfolio_id': 'parentPortfolioId',
        'version': 'version',
        'staged_modifications': 'stagedModifications',
        'is_derived': 'isDerived',
        'base_currency': 'baseCurrency',
        'properties': 'properties',
        'relationships': 'relationships',
        'instrument_scopes': 'instrumentScopes',
        'accounting_method': 'accountingMethod',
        'amortisation_method': 'amortisationMethod',
        'transaction_type_scope': 'transactionTypeScope',
        'cash_gain_loss_calculation_date': 'cashGainLossCalculationDate',
        'instrument_event_configuration': 'instrumentEventConfiguration',
        'amortisation_rule_set_id': 'amortisationRuleSetId',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'type': 'required',
        'display_name': 'required',
        'description': 'optional',
        'created': 'required',
        'parent_portfolio_id': 'optional',
        'version': 'optional',
        'staged_modifications': 'optional',
        'is_derived': 'optional',
        'base_currency': 'optional',
        'properties': 'optional',
        'relationships': 'optional',
        'instrument_scopes': 'optional',
        'accounting_method': 'optional',
        'amortisation_method': 'optional',
        'transaction_type_scope': 'optional',
        'cash_gain_loss_calculation_date': 'optional',
        'instrument_event_configuration': 'optional',
        'amortisation_rule_set_id': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, type=None, display_name=None, description=None, created=None, parent_portfolio_id=None, version=None, staged_modifications=None, is_derived=None, base_currency=None, properties=None, relationships=None, instrument_scopes=None, accounting_method=None, amortisation_method=None, transaction_type_scope=None, cash_gain_loss_calculation_date=None, instrument_event_configuration=None, amortisation_rule_set_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioWithoutHref - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param type:  The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction (required)
        :type type: str
        :param display_name:  The name of the portfolio. (required)
        :type display_name: str
        :param description:  The long form description of the portfolio.
        :type description: str
        :param created:  The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. (required)
        :type created: datetime
        :param parent_portfolio_id: 
        :type parent_portfolio_id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param staged_modifications: 
        :type staged_modifications: lusid.StagedModificationsInfo
        :param is_derived:  Whether or not this is a derived portfolio.
        :type is_derived: bool
        :param base_currency:  The base currency of the portfolio.
        :type base_currency: str
        :param properties:  The requested portfolio properties. These will be from the 'Portfolio' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param relationships:  A set of relationships associated to the portfolio.
        :type relationships: list[lusid.Relationship]
        :param instrument_scopes:  The instrument scope resolution strategy of this portfolio.
        :type instrument_scopes: list[str]
        :param accounting_method:  . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency
        :type accounting_method: str
        :param amortisation_method:  The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
        :type amortisation_method: str
        :param transaction_type_scope:  The scope of the transaction types.
        :type transaction_type_scope: str
        :param cash_gain_loss_calculation_date:  The scope of the transaction types.
        :type cash_gain_loss_calculation_date: str
        :param instrument_event_configuration: 
        :type instrument_event_configuration: lusid.InstrumentEventConfiguration
        :param amortisation_rule_set_id: 
        :type amortisation_rule_set_id: lusid.ResourceId
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._display_name = None
        self._description = None
        self._created = None
        self._parent_portfolio_id = None
        self._version = None
        self._staged_modifications = None
        self._is_derived = None
        self._base_currency = None
        self._properties = None
        self._relationships = None
        self._instrument_scopes = None
        self._accounting_method = None
        self._amortisation_method = None
        self._transaction_type_scope = None
        self._cash_gain_loss_calculation_date = None
        self._instrument_event_configuration = None
        self._amortisation_rule_set_id = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.display_name = display_name
        self.description = description
        self.created = created
        if parent_portfolio_id is not None:
            self.parent_portfolio_id = parent_portfolio_id
        if version is not None:
            self.version = version
        if staged_modifications is not None:
            self.staged_modifications = staged_modifications
        if is_derived is not None:
            self.is_derived = is_derived
        self.base_currency = base_currency
        self.properties = properties
        self.relationships = relationships
        self.instrument_scopes = instrument_scopes
        if accounting_method is not None:
            self.accounting_method = accounting_method
        self.amortisation_method = amortisation_method
        self.transaction_type_scope = transaction_type_scope
        self.cash_gain_loss_calculation_date = cash_gain_loss_calculation_date
        if instrument_event_configuration is not None:
            self.instrument_event_configuration = instrument_event_configuration
        if amortisation_rule_set_id is not None:
            self.amortisation_rule_set_id = amortisation_rule_set_id
        self.links = links

    @property
    def id(self):
        """Gets the id of this PortfolioWithoutHref.  # noqa: E501


        :return: The id of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortfolioWithoutHref.


        :param id: The id of this PortfolioWithoutHref.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this PortfolioWithoutHref.  # noqa: E501

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :return: The type of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortfolioWithoutHref.

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :param type: The type of this PortfolioWithoutHref.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Transaction", "Reference", "DerivedTransaction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this PortfolioWithoutHref.  # noqa: E501

        The name of the portfolio.  # noqa: E501

        :return: The display_name of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PortfolioWithoutHref.

        The name of the portfolio.  # noqa: E501

        :param display_name: The display_name of this PortfolioWithoutHref.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PortfolioWithoutHref.  # noqa: E501

        The long form description of the portfolio.  # noqa: E501

        :return: The description of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortfolioWithoutHref.

        The long form description of the portfolio.  # noqa: E501

        :param description: The description of this PortfolioWithoutHref.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this PortfolioWithoutHref.  # noqa: E501

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :return: The created of this PortfolioWithoutHref.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PortfolioWithoutHref.

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :param created: The created of this PortfolioWithoutHref.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def parent_portfolio_id(self):
        """Gets the parent_portfolio_id of this PortfolioWithoutHref.  # noqa: E501


        :return: The parent_portfolio_id of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._parent_portfolio_id

    @parent_portfolio_id.setter
    def parent_portfolio_id(self, parent_portfolio_id):
        """Sets the parent_portfolio_id of this PortfolioWithoutHref.


        :param parent_portfolio_id: The parent_portfolio_id of this PortfolioWithoutHref.  # noqa: E501
        :type parent_portfolio_id: lusid.ResourceId
        """

        self._parent_portfolio_id = parent_portfolio_id

    @property
    def version(self):
        """Gets the version of this PortfolioWithoutHref.  # noqa: E501


        :return: The version of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PortfolioWithoutHref.


        :param version: The version of this PortfolioWithoutHref.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def staged_modifications(self):
        """Gets the staged_modifications of this PortfolioWithoutHref.  # noqa: E501


        :return: The staged_modifications of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.StagedModificationsInfo
        """
        return self._staged_modifications

    @staged_modifications.setter
    def staged_modifications(self, staged_modifications):
        """Sets the staged_modifications of this PortfolioWithoutHref.


        :param staged_modifications: The staged_modifications of this PortfolioWithoutHref.  # noqa: E501
        :type staged_modifications: lusid.StagedModificationsInfo
        """

        self._staged_modifications = staged_modifications

    @property
    def is_derived(self):
        """Gets the is_derived of this PortfolioWithoutHref.  # noqa: E501

        Whether or not this is a derived portfolio.  # noqa: E501

        :return: The is_derived of this PortfolioWithoutHref.  # noqa: E501
        :rtype: bool
        """
        return self._is_derived

    @is_derived.setter
    def is_derived(self, is_derived):
        """Sets the is_derived of this PortfolioWithoutHref.

        Whether or not this is a derived portfolio.  # noqa: E501

        :param is_derived: The is_derived of this PortfolioWithoutHref.  # noqa: E501
        :type is_derived: bool
        """

        self._is_derived = is_derived

    @property
    def base_currency(self):
        """Gets the base_currency of this PortfolioWithoutHref.  # noqa: E501

        The base currency of the portfolio.  # noqa: E501

        :return: The base_currency of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this PortfolioWithoutHref.

        The base currency of the portfolio.  # noqa: E501

        :param base_currency: The base_currency of this PortfolioWithoutHref.  # noqa: E501
        :type base_currency: str
        """

        self._base_currency = base_currency

    @property
    def properties(self):
        """Gets the properties of this PortfolioWithoutHref.  # noqa: E501

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :return: The properties of this PortfolioWithoutHref.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PortfolioWithoutHref.

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :param properties: The properties of this PortfolioWithoutHref.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def relationships(self):
        """Gets the relationships of this PortfolioWithoutHref.  # noqa: E501

        A set of relationships associated to the portfolio.  # noqa: E501

        :return: The relationships of this PortfolioWithoutHref.  # noqa: E501
        :rtype: list[lusid.Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this PortfolioWithoutHref.

        A set of relationships associated to the portfolio.  # noqa: E501

        :param relationships: The relationships of this PortfolioWithoutHref.  # noqa: E501
        :type relationships: list[lusid.Relationship]
        """

        self._relationships = relationships

    @property
    def instrument_scopes(self):
        """Gets the instrument_scopes of this PortfolioWithoutHref.  # noqa: E501

        The instrument scope resolution strategy of this portfolio.  # noqa: E501

        :return: The instrument_scopes of this PortfolioWithoutHref.  # noqa: E501
        :rtype: list[str]
        """
        return self._instrument_scopes

    @instrument_scopes.setter
    def instrument_scopes(self, instrument_scopes):
        """Sets the instrument_scopes of this PortfolioWithoutHref.

        The instrument scope resolution strategy of this portfolio.  # noqa: E501

        :param instrument_scopes: The instrument_scopes of this PortfolioWithoutHref.  # noqa: E501
        :type instrument_scopes: list[str]
        """

        self._instrument_scopes = instrument_scopes

    @property
    def accounting_method(self):
        """Gets the accounting_method of this PortfolioWithoutHref.  # noqa: E501

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency  # noqa: E501

        :return: The accounting_method of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this PortfolioWithoutHref.

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency  # noqa: E501

        :param accounting_method: The accounting_method of this PortfolioWithoutHref.  # noqa: E501
        :type accounting_method: str
        """
        allowed_values = ["Default", "AverageCost", "FirstInFirstOut", "LastInFirstOut", "HighestCostFirst", "LowestCostFirst", "ProRateByUnits", "ProRateByCost", "ProRateByCostPortfolioCurrency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and accounting_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `accounting_method` ({0}), must be one of {1}"  # noqa: E501
                .format(accounting_method, allowed_values)
            )

        self._accounting_method = accounting_method

    @property
    def amortisation_method(self):
        """Gets the amortisation_method of this PortfolioWithoutHref.  # noqa: E501

        The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate  # noqa: E501

        :return: The amortisation_method of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._amortisation_method

    @amortisation_method.setter
    def amortisation_method(self, amortisation_method):
        """Sets the amortisation_method of this PortfolioWithoutHref.

        The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate  # noqa: E501

        :param amortisation_method: The amortisation_method of this PortfolioWithoutHref.  # noqa: E501
        :type amortisation_method: str
        """

        self._amortisation_method = amortisation_method

    @property
    def transaction_type_scope(self):
        """Gets the transaction_type_scope of this PortfolioWithoutHref.  # noqa: E501

        The scope of the transaction types.  # noqa: E501

        :return: The transaction_type_scope of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_scope

    @transaction_type_scope.setter
    def transaction_type_scope(self, transaction_type_scope):
        """Sets the transaction_type_scope of this PortfolioWithoutHref.

        The scope of the transaction types.  # noqa: E501

        :param transaction_type_scope: The transaction_type_scope of this PortfolioWithoutHref.  # noqa: E501
        :type transaction_type_scope: str
        """

        self._transaction_type_scope = transaction_type_scope

    @property
    def cash_gain_loss_calculation_date(self):
        """Gets the cash_gain_loss_calculation_date of this PortfolioWithoutHref.  # noqa: E501

        The scope of the transaction types.  # noqa: E501

        :return: The cash_gain_loss_calculation_date of this PortfolioWithoutHref.  # noqa: E501
        :rtype: str
        """
        return self._cash_gain_loss_calculation_date

    @cash_gain_loss_calculation_date.setter
    def cash_gain_loss_calculation_date(self, cash_gain_loss_calculation_date):
        """Sets the cash_gain_loss_calculation_date of this PortfolioWithoutHref.

        The scope of the transaction types.  # noqa: E501

        :param cash_gain_loss_calculation_date: The cash_gain_loss_calculation_date of this PortfolioWithoutHref.  # noqa: E501
        :type cash_gain_loss_calculation_date: str
        """

        self._cash_gain_loss_calculation_date = cash_gain_loss_calculation_date

    @property
    def instrument_event_configuration(self):
        """Gets the instrument_event_configuration of this PortfolioWithoutHref.  # noqa: E501


        :return: The instrument_event_configuration of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.InstrumentEventConfiguration
        """
        return self._instrument_event_configuration

    @instrument_event_configuration.setter
    def instrument_event_configuration(self, instrument_event_configuration):
        """Sets the instrument_event_configuration of this PortfolioWithoutHref.


        :param instrument_event_configuration: The instrument_event_configuration of this PortfolioWithoutHref.  # noqa: E501
        :type instrument_event_configuration: lusid.InstrumentEventConfiguration
        """

        self._instrument_event_configuration = instrument_event_configuration

    @property
    def amortisation_rule_set_id(self):
        """Gets the amortisation_rule_set_id of this PortfolioWithoutHref.  # noqa: E501


        :return: The amortisation_rule_set_id of this PortfolioWithoutHref.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._amortisation_rule_set_id

    @amortisation_rule_set_id.setter
    def amortisation_rule_set_id(self, amortisation_rule_set_id):
        """Sets the amortisation_rule_set_id of this PortfolioWithoutHref.


        :param amortisation_rule_set_id: The amortisation_rule_set_id of this PortfolioWithoutHref.  # noqa: E501
        :type amortisation_rule_set_id: lusid.ResourceId
        """

        self._amortisation_rule_set_id = amortisation_rule_set_id

    @property
    def links(self):
        """Gets the links of this PortfolioWithoutHref.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioWithoutHref.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioWithoutHref.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioWithoutHref.  # noqa: E501
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
        if not isinstance(other, PortfolioWithoutHref):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioWithoutHref):
            return True

        return self.to_dict() != other.to_dict()
