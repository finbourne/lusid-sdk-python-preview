# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.148
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


class QueryableKey(object):
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
        'address_key': 'str',
        'description': 'str',
        'display_name': 'str',
        'type': 'str',
        'flattened_type': 'str',
        'holding_quantity_scaling': 'str',
        'supported_usages': 'list[str]',
        'supported_operations': 'list[str]',
        'life_cycle_status': 'str',
        'removal_date': 'datetime',
        'applicable_options': 'dict(str, AddressKeyOptionDefinition)',
        'derivation_formula': 'str'
    }

    attribute_map = {
        'address_key': 'addressKey',
        'description': 'description',
        'display_name': 'displayName',
        'type': 'type',
        'flattened_type': 'flattenedType',
        'holding_quantity_scaling': 'holdingQuantityScaling',
        'supported_usages': 'supportedUsages',
        'supported_operations': 'supportedOperations',
        'life_cycle_status': 'lifeCycleStatus',
        'removal_date': 'removalDate',
        'applicable_options': 'applicableOptions',
        'derivation_formula': 'derivationFormula'
    }

    required_map = {
        'address_key': 'required',
        'description': 'optional',
        'display_name': 'required',
        'type': 'required',
        'flattened_type': 'required',
        'holding_quantity_scaling': 'required',
        'supported_usages': 'required',
        'supported_operations': 'required',
        'life_cycle_status': 'required',
        'removal_date': 'optional',
        'applicable_options': 'optional',
        'derivation_formula': 'optional'
    }

    def __init__(self, address_key=None, description=None, display_name=None, type=None, flattened_type=None, holding_quantity_scaling=None, supported_usages=None, supported_operations=None, life_cycle_status=None, removal_date=None, applicable_options=None, derivation_formula=None, local_vars_configuration=None):  # noqa: E501
        """QueryableKey - a model defined in OpenAPI"
        
        :param address_key:  The address that is the query to be made into the system. e.g. a Valuation/PV or Instrument/MaturityDate (required)
        :type address_key: str
        :param description:  What does the information that is being queried by the address mean. What is the address for.
        :type description: str
        :param display_name:  The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address. (required)
        :type display_name: str
        :param type:  Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the more complex representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Result0D\", the decimal-currency pair. (required)
        :type type: str
        :param flattened_type:  Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the simpler representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Decimal\". (required)
        :type flattened_type: str
        :param holding_quantity_scaling:  Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and PV. The present value of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the contract size. (required)
        :type holding_quantity_scaling: str
        :param supported_usages:  The types of queries that support this key. (required)
        :type supported_usages: list[str]
        :param supported_operations:  When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context). (required)
        :type supported_operations: list[str]
        :param life_cycle_status:  Within an API where an item can be accessed through an address or property, there is an associated status that determines whether the item is stable or likely to change. This status is one of [Experimental, Beta, EAP, Prod,  Deprecated]. If the item is deprecated it will be removed on or after the associated DateTime RemovalDate field. That field will not otherwise be set. (required)
        :type life_cycle_status: str
        :param removal_date:  If the life cycle status is set to deprecated then this will be populated with the date on or after which removal of the address query will happen
        :type removal_date: datetime
        :param applicable_options:  A mapping from option names to the definition that the corresponding option value must match.
        :type applicable_options: dict[str, lusid.AddressKeyOptionDefinition]
        :param derivation_formula:  Derivation formula for when the for when the query key represents a DerivedValuation property.
        :type derivation_formula: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address_key = None
        self._description = None
        self._display_name = None
        self._type = None
        self._flattened_type = None
        self._holding_quantity_scaling = None
        self._supported_usages = None
        self._supported_operations = None
        self._life_cycle_status = None
        self._removal_date = None
        self._applicable_options = None
        self._derivation_formula = None
        self.discriminator = None

        self.address_key = address_key
        self.description = description
        self.display_name = display_name
        self.type = type
        self.flattened_type = flattened_type
        self.holding_quantity_scaling = holding_quantity_scaling
        self.supported_usages = supported_usages
        self.supported_operations = supported_operations
        self.life_cycle_status = life_cycle_status
        self.removal_date = removal_date
        self.applicable_options = applicable_options
        self.derivation_formula = derivation_formula

    @property
    def address_key(self):
        """Gets the address_key of this QueryableKey.  # noqa: E501

        The address that is the query to be made into the system. e.g. a Valuation/PV or Instrument/MaturityDate  # noqa: E501

        :return: The address_key of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._address_key

    @address_key.setter
    def address_key(self, address_key):
        """Sets the address_key of this QueryableKey.

        The address that is the query to be made into the system. e.g. a Valuation/PV or Instrument/MaturityDate  # noqa: E501

        :param address_key: The address_key of this QueryableKey.  # noqa: E501
        :type address_key: str
        """
        if self.local_vars_configuration.client_side_validation and address_key is None:  # noqa: E501
            raise ValueError("Invalid value for `address_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                address_key is not None and len(address_key) < 1):
            raise ValueError("Invalid value for `address_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._address_key = address_key

    @property
    def description(self):
        """Gets the description of this QueryableKey.  # noqa: E501

        What does the information that is being queried by the address mean. What is the address for.  # noqa: E501

        :return: The description of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryableKey.

        What does the information that is being queried by the address mean. What is the address for.  # noqa: E501

        :param description: The description of this QueryableKey.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this QueryableKey.  # noqa: E501

        The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address.  # noqa: E501

        :return: The display_name of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this QueryableKey.

        The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address.  # noqa: E501

        :param display_name: The display_name of this QueryableKey.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this QueryableKey.  # noqa: E501

        Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the more complex representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Result0D\", the decimal-currency pair.  # noqa: E501

        :return: The type of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryableKey.

        Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the more complex representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Result0D\", the decimal-currency pair.  # noqa: E501

        :param type: The type of this QueryableKey.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def flattened_type(self):
        """Gets the flattened_type of this QueryableKey.  # noqa: E501

        Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the simpler representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Decimal\".  # noqa: E501

        :return: The flattened_type of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._flattened_type

    @flattened_type.setter
    def flattened_type(self, flattened_type):
        """Sets the flattened_type of this QueryableKey.

        Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the simpler representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Decimal\".  # noqa: E501

        :param flattened_type: The flattened_type of this QueryableKey.  # noqa: E501
        :type flattened_type: str
        """
        if self.local_vars_configuration.client_side_validation and flattened_type is None:  # noqa: E501
            raise ValueError("Invalid value for `flattened_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                flattened_type is not None and len(flattened_type) < 1):
            raise ValueError("Invalid value for `flattened_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._flattened_type = flattened_type

    @property
    def holding_quantity_scaling(self):
        """Gets the holding_quantity_scaling of this QueryableKey.  # noqa: E501

        Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and PV. The present value of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the contract size.  # noqa: E501

        :return: The holding_quantity_scaling of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._holding_quantity_scaling

    @holding_quantity_scaling.setter
    def holding_quantity_scaling(self, holding_quantity_scaling):
        """Sets the holding_quantity_scaling of this QueryableKey.

        Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and PV. The present value of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the contract size.  # noqa: E501

        :param holding_quantity_scaling: The holding_quantity_scaling of this QueryableKey.  # noqa: E501
        :type holding_quantity_scaling: str
        """
        if self.local_vars_configuration.client_side_validation and holding_quantity_scaling is None:  # noqa: E501
            raise ValueError("Invalid value for `holding_quantity_scaling`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                holding_quantity_scaling is not None and len(holding_quantity_scaling) < 1):
            raise ValueError("Invalid value for `holding_quantity_scaling`, length must be greater than or equal to `1`")  # noqa: E501

        self._holding_quantity_scaling = holding_quantity_scaling

    @property
    def supported_usages(self):
        """Gets the supported_usages of this QueryableKey.  # noqa: E501

        The types of queries that support this key.  # noqa: E501

        :return: The supported_usages of this QueryableKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_usages

    @supported_usages.setter
    def supported_usages(self, supported_usages):
        """Sets the supported_usages of this QueryableKey.

        The types of queries that support this key.  # noqa: E501

        :param supported_usages: The supported_usages of this QueryableKey.  # noqa: E501
        :type supported_usages: list[str]
        """
        if self.local_vars_configuration.client_side_validation and supported_usages is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_usages`, must not be `None`")  # noqa: E501

        self._supported_usages = supported_usages

    @property
    def supported_operations(self):
        """Gets the supported_operations of this QueryableKey.  # noqa: E501

        When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context).  # noqa: E501

        :return: The supported_operations of this QueryableKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_operations

    @supported_operations.setter
    def supported_operations(self, supported_operations):
        """Sets the supported_operations of this QueryableKey.

        When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context).  # noqa: E501

        :param supported_operations: The supported_operations of this QueryableKey.  # noqa: E501
        :type supported_operations: list[str]
        """
        if self.local_vars_configuration.client_side_validation and supported_operations is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_operations`, must not be `None`")  # noqa: E501

        self._supported_operations = supported_operations

    @property
    def life_cycle_status(self):
        """Gets the life_cycle_status of this QueryableKey.  # noqa: E501

        Within an API where an item can be accessed through an address or property, there is an associated status that determines whether the item is stable or likely to change. This status is one of [Experimental, Beta, EAP, Prod,  Deprecated]. If the item is deprecated it will be removed on or after the associated DateTime RemovalDate field. That field will not otherwise be set.  # noqa: E501

        :return: The life_cycle_status of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._life_cycle_status

    @life_cycle_status.setter
    def life_cycle_status(self, life_cycle_status):
        """Sets the life_cycle_status of this QueryableKey.

        Within an API where an item can be accessed through an address or property, there is an associated status that determines whether the item is stable or likely to change. This status is one of [Experimental, Beta, EAP, Prod,  Deprecated]. If the item is deprecated it will be removed on or after the associated DateTime RemovalDate field. That field will not otherwise be set.  # noqa: E501

        :param life_cycle_status: The life_cycle_status of this QueryableKey.  # noqa: E501
        :type life_cycle_status: str
        """
        if self.local_vars_configuration.client_side_validation and life_cycle_status is None:  # noqa: E501
            raise ValueError("Invalid value for `life_cycle_status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                life_cycle_status is not None and len(life_cycle_status) < 1):
            raise ValueError("Invalid value for `life_cycle_status`, length must be greater than or equal to `1`")  # noqa: E501

        self._life_cycle_status = life_cycle_status

    @property
    def removal_date(self):
        """Gets the removal_date of this QueryableKey.  # noqa: E501

        If the life cycle status is set to deprecated then this will be populated with the date on or after which removal of the address query will happen  # noqa: E501

        :return: The removal_date of this QueryableKey.  # noqa: E501
        :rtype: datetime
        """
        return self._removal_date

    @removal_date.setter
    def removal_date(self, removal_date):
        """Sets the removal_date of this QueryableKey.

        If the life cycle status is set to deprecated then this will be populated with the date on or after which removal of the address query will happen  # noqa: E501

        :param removal_date: The removal_date of this QueryableKey.  # noqa: E501
        :type removal_date: datetime
        """

        self._removal_date = removal_date

    @property
    def applicable_options(self):
        """Gets the applicable_options of this QueryableKey.  # noqa: E501

        A mapping from option names to the definition that the corresponding option value must match.  # noqa: E501

        :return: The applicable_options of this QueryableKey.  # noqa: E501
        :rtype: dict[str, lusid.AddressKeyOptionDefinition]
        """
        return self._applicable_options

    @applicable_options.setter
    def applicable_options(self, applicable_options):
        """Sets the applicable_options of this QueryableKey.

        A mapping from option names to the definition that the corresponding option value must match.  # noqa: E501

        :param applicable_options: The applicable_options of this QueryableKey.  # noqa: E501
        :type applicable_options: dict[str, lusid.AddressKeyOptionDefinition]
        """

        self._applicable_options = applicable_options

    @property
    def derivation_formula(self):
        """Gets the derivation_formula of this QueryableKey.  # noqa: E501

        Derivation formula for when the for when the query key represents a DerivedValuation property.  # noqa: E501

        :return: The derivation_formula of this QueryableKey.  # noqa: E501
        :rtype: str
        """
        return self._derivation_formula

    @derivation_formula.setter
    def derivation_formula(self, derivation_formula):
        """Sets the derivation_formula of this QueryableKey.

        Derivation formula for when the for when the query key represents a DerivedValuation property.  # noqa: E501

        :param derivation_formula: The derivation_formula of this QueryableKey.  # noqa: E501
        :type derivation_formula: str
        """

        self._derivation_formula = derivation_formula

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
        if not isinstance(other, QueryableKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryableKey):
            return True

        return self.to_dict() != other.to_dict()
