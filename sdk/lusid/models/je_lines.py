# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.32
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


class JELines(object):
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
        'accounting_date': 'datetime',
        'portfolio_id': 'ResourceId',
        'instrument_id': 'str',
        'instrument_scope': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'tax_lot_id': 'str',
        'gl_code': 'str',
        'local': 'CurrencyAndAmount',
        'base': 'CurrencyAndAmount',
        'posting_module_id': 'ResourceId',
        'posting_rule': 'str',
        'as_at_date': 'datetime',
        'activities_description': 'str',
        'source_type': 'str',
        'source_id': 'str',
        'properties': 'dict(str, ModelProperty)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'accounting_date': 'accountingDate',
        'portfolio_id': 'portfolioId',
        'instrument_id': 'instrumentId',
        'instrument_scope': 'instrumentScope',
        'sub_holding_keys': 'subHoldingKeys',
        'tax_lot_id': 'taxLotId',
        'gl_code': 'glCode',
        'local': 'local',
        'base': 'base',
        'posting_module_id': 'postingModuleId',
        'posting_rule': 'postingRule',
        'as_at_date': 'asAtDate',
        'activities_description': 'activitiesDescription',
        'source_type': 'sourceType',
        'source_id': 'sourceId',
        'properties': 'properties',
        'links': 'links'
    }

    required_map = {
        'accounting_date': 'required',
        'portfolio_id': 'required',
        'instrument_id': 'required',
        'instrument_scope': 'required',
        'sub_holding_keys': 'optional',
        'tax_lot_id': 'required',
        'gl_code': 'required',
        'local': 'required',
        'base': 'required',
        'posting_module_id': 'required',
        'posting_rule': 'required',
        'as_at_date': 'required',
        'activities_description': 'optional',
        'source_type': 'required',
        'source_id': 'required',
        'properties': 'optional',
        'links': 'optional'
    }

    def __init__(self, accounting_date=None, portfolio_id=None, instrument_id=None, instrument_scope=None, sub_holding_keys=None, tax_lot_id=None, gl_code=None, local=None, base=None, posting_module_id=None, posting_rule=None, as_at_date=None, activities_description=None, source_type=None, source_id=None, properties=None, links=None, local_vars_configuration=None):  # noqa: E501
        """JELines - a model defined in OpenAPI"
        
        :param accounting_date:  The JELines accounting date. (required)
        :type accounting_date: datetime
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param instrument_id:  To indicate the instrument of the transaction that the JE line posted for, if applicable. (required)
        :type instrument_id: str
        :param instrument_scope:  The scope in which the JELines instrument is in. (required)
        :type instrument_scope: str
        :param sub_holding_keys:  The sub-holding properties which are part of the AccountingKey.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param tax_lot_id:  The tax lot Id that JE line is impacting. (required)
        :type tax_lot_id: str
        :param gl_code:  Code of general ledger the JE lines posting to. (required)
        :type gl_code: str
        :param local:  (required)
        :type local: lusid.CurrencyAndAmount
        :param base:  (required)
        :type base: lusid.CurrencyAndAmount
        :param posting_module_id:  (required)
        :type posting_module_id: lusid.ResourceId
        :param posting_rule:  The rule generating the JELinse. (required)
        :type posting_rule: str
        :param as_at_date:  The corresponding input date and time of the Transaction generating the JELine. (required)
        :type as_at_date: datetime
        :param activities_description:  This would be the description of the business activities where these JE lines are posting for.
        :type activities_description: str
        :param source_type:  So far are 4 types: LusidTxn, LusidValuation, Manual and External. (required)
        :type source_type: str
        :param source_id:  For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates. (required)
        :type source_id: str
        :param properties:  Properties to add to the Abor.
        :type properties: dict[str, lusid.ModelProperty]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._accounting_date = None
        self._portfolio_id = None
        self._instrument_id = None
        self._instrument_scope = None
        self._sub_holding_keys = None
        self._tax_lot_id = None
        self._gl_code = None
        self._local = None
        self._base = None
        self._posting_module_id = None
        self._posting_rule = None
        self._as_at_date = None
        self._activities_description = None
        self._source_type = None
        self._source_id = None
        self._properties = None
        self._links = None
        self.discriminator = None

        self.accounting_date = accounting_date
        self.portfolio_id = portfolio_id
        self.instrument_id = instrument_id
        self.instrument_scope = instrument_scope
        self.sub_holding_keys = sub_holding_keys
        self.tax_lot_id = tax_lot_id
        self.gl_code = gl_code
        self.local = local
        self.base = base
        self.posting_module_id = posting_module_id
        self.posting_rule = posting_rule
        self.as_at_date = as_at_date
        self.activities_description = activities_description
        self.source_type = source_type
        self.source_id = source_id
        self.properties = properties
        self.links = links

    @property
    def accounting_date(self):
        """Gets the accounting_date of this JELines.  # noqa: E501

        The JELines accounting date.  # noqa: E501

        :return: The accounting_date of this JELines.  # noqa: E501
        :rtype: datetime
        """
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, accounting_date):
        """Sets the accounting_date of this JELines.

        The JELines accounting date.  # noqa: E501

        :param accounting_date: The accounting_date of this JELines.  # noqa: E501
        :type accounting_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and accounting_date is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_date`, must not be `None`")  # noqa: E501

        self._accounting_date = accounting_date

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this JELines.  # noqa: E501


        :return: The portfolio_id of this JELines.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this JELines.


        :param portfolio_id: The portfolio_id of this JELines.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def instrument_id(self):
        """Gets the instrument_id of this JELines.  # noqa: E501

        To indicate the instrument of the transaction that the JE line posted for, if applicable.  # noqa: E501

        :return: The instrument_id of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this JELines.

        To indicate the instrument of the transaction that the JE line posted for, if applicable.  # noqa: E501

        :param instrument_id: The instrument_id of this JELines.  # noqa: E501
        :type instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_id is not None and len(instrument_id) < 1):
            raise ValueError("Invalid value for `instrument_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_id = instrument_id

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this JELines.  # noqa: E501

        The scope in which the JELines instrument is in.  # noqa: E501

        :return: The instrument_scope of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this JELines.

        The scope in which the JELines instrument is in.  # noqa: E501

        :param instrument_scope: The instrument_scope of this JELines.  # noqa: E501
        :type instrument_scope: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) < 1):
            raise ValueError("Invalid value for `instrument_scope`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_scope = instrument_scope

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this JELines.  # noqa: E501

        The sub-holding properties which are part of the AccountingKey.  # noqa: E501

        :return: The sub_holding_keys of this JELines.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this JELines.

        The sub-holding properties which are part of the AccountingKey.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this JELines.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def tax_lot_id(self):
        """Gets the tax_lot_id of this JELines.  # noqa: E501

        The tax lot Id that JE line is impacting.  # noqa: E501

        :return: The tax_lot_id of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._tax_lot_id

    @tax_lot_id.setter
    def tax_lot_id(self, tax_lot_id):
        """Sets the tax_lot_id of this JELines.

        The tax lot Id that JE line is impacting.  # noqa: E501

        :param tax_lot_id: The tax_lot_id of this JELines.  # noqa: E501
        :type tax_lot_id: str
        """
        if self.local_vars_configuration.client_side_validation and tax_lot_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tax_lot_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tax_lot_id is not None and len(tax_lot_id) < 1):
            raise ValueError("Invalid value for `tax_lot_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._tax_lot_id = tax_lot_id

    @property
    def gl_code(self):
        """Gets the gl_code of this JELines.  # noqa: E501

        Code of general ledger the JE lines posting to.  # noqa: E501

        :return: The gl_code of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._gl_code

    @gl_code.setter
    def gl_code(self, gl_code):
        """Sets the gl_code of this JELines.

        Code of general ledger the JE lines posting to.  # noqa: E501

        :param gl_code: The gl_code of this JELines.  # noqa: E501
        :type gl_code: str
        """
        if self.local_vars_configuration.client_side_validation and gl_code is None:  # noqa: E501
            raise ValueError("Invalid value for `gl_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gl_code is not None and len(gl_code) < 1):
            raise ValueError("Invalid value for `gl_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._gl_code = gl_code

    @property
    def local(self):
        """Gets the local of this JELines.  # noqa: E501


        :return: The local of this JELines.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this JELines.


        :param local: The local of this JELines.  # noqa: E501
        :type local: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and local is None:  # noqa: E501
            raise ValueError("Invalid value for `local`, must not be `None`")  # noqa: E501

        self._local = local

    @property
    def base(self):
        """Gets the base of this JELines.  # noqa: E501


        :return: The base of this JELines.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this JELines.


        :param base: The base of this JELines.  # noqa: E501
        :type base: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and base is None:  # noqa: E501
            raise ValueError("Invalid value for `base`, must not be `None`")  # noqa: E501

        self._base = base

    @property
    def posting_module_id(self):
        """Gets the posting_module_id of this JELines.  # noqa: E501


        :return: The posting_module_id of this JELines.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._posting_module_id

    @posting_module_id.setter
    def posting_module_id(self, posting_module_id):
        """Sets the posting_module_id of this JELines.


        :param posting_module_id: The posting_module_id of this JELines.  # noqa: E501
        :type posting_module_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and posting_module_id is None:  # noqa: E501
            raise ValueError("Invalid value for `posting_module_id`, must not be `None`")  # noqa: E501

        self._posting_module_id = posting_module_id

    @property
    def posting_rule(self):
        """Gets the posting_rule of this JELines.  # noqa: E501

        The rule generating the JELinse.  # noqa: E501

        :return: The posting_rule of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._posting_rule

    @posting_rule.setter
    def posting_rule(self, posting_rule):
        """Sets the posting_rule of this JELines.

        The rule generating the JELinse.  # noqa: E501

        :param posting_rule: The posting_rule of this JELines.  # noqa: E501
        :type posting_rule: str
        """
        if self.local_vars_configuration.client_side_validation and posting_rule is None:  # noqa: E501
            raise ValueError("Invalid value for `posting_rule`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                posting_rule is not None and len(posting_rule) < 1):
            raise ValueError("Invalid value for `posting_rule`, length must be greater than or equal to `1`")  # noqa: E501

        self._posting_rule = posting_rule

    @property
    def as_at_date(self):
        """Gets the as_at_date of this JELines.  # noqa: E501

        The corresponding input date and time of the Transaction generating the JELine.  # noqa: E501

        :return: The as_at_date of this JELines.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_date

    @as_at_date.setter
    def as_at_date(self, as_at_date):
        """Sets the as_at_date of this JELines.

        The corresponding input date and time of the Transaction generating the JELine.  # noqa: E501

        :param as_at_date: The as_at_date of this JELines.  # noqa: E501
        :type as_at_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and as_at_date is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at_date`, must not be `None`")  # noqa: E501

        self._as_at_date = as_at_date

    @property
    def activities_description(self):
        """Gets the activities_description of this JELines.  # noqa: E501

        This would be the description of the business activities where these JE lines are posting for.  # noqa: E501

        :return: The activities_description of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._activities_description

    @activities_description.setter
    def activities_description(self, activities_description):
        """Sets the activities_description of this JELines.

        This would be the description of the business activities where these JE lines are posting for.  # noqa: E501

        :param activities_description: The activities_description of this JELines.  # noqa: E501
        :type activities_description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                activities_description is not None and len(activities_description) > 1024):
            raise ValueError("Invalid value for `activities_description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                activities_description is not None and len(activities_description) < 0):
            raise ValueError("Invalid value for `activities_description`, length must be greater than or equal to `0`")  # noqa: E501

        self._activities_description = activities_description

    @property
    def source_type(self):
        """Gets the source_type of this JELines.  # noqa: E501

        So far are 4 types: LusidTxn, LusidValuation, Manual and External.  # noqa: E501

        :return: The source_type of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this JELines.

        So far are 4 types: LusidTxn, LusidValuation, Manual and External.  # noqa: E501

        :param source_type: The source_type of this JELines.  # noqa: E501
        :type source_type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_type is not None and len(source_type) < 1):
            raise ValueError("Invalid value for `source_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_type = source_type

    @property
    def source_id(self):
        """Gets the source_id of this JELines.  # noqa: E501

        For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates.  # noqa: E501

        :return: The source_id of this JELines.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this JELines.

        For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates.  # noqa: E501

        :param source_id: The source_id of this JELines.  # noqa: E501
        :type source_id: str
        """
        if self.local_vars_configuration.client_side_validation and source_id is None:  # noqa: E501
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_id is not None and len(source_id) < 1):
            raise ValueError("Invalid value for `source_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_id = source_id

    @property
    def properties(self):
        """Gets the properties of this JELines.  # noqa: E501

        Properties to add to the Abor.  # noqa: E501

        :return: The properties of this JELines.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JELines.

        Properties to add to the Abor.  # noqa: E501

        :param properties: The properties of this JELines.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def links(self):
        """Gets the links of this JELines.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this JELines.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this JELines.

        Collection of links.  # noqa: E501

        :param links: The links of this JELines.  # noqa: E501
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
        if not isinstance(other, JELines):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JELines):
            return True

        return self.to_dict() != other.to_dict()
