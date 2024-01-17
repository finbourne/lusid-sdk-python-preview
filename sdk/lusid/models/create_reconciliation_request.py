# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.58
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


class CreateReconciliationRequest(object):
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
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'is_portfolio_group': 'bool',
        'left': 'ResourceId',
        'right': 'ResourceId',
        'transactions': 'ReconciliationTransactions',
        'positions': 'ReconciliationConfiguration',
        'valuations': 'ReconciliationConfiguration',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'is_portfolio_group': 'isPortfolioGroup',
        'left': 'left',
        'right': 'right',
        'transactions': 'transactions',
        'positions': 'positions',
        'valuations': 'valuations',
        'properties': 'properties'
    }

    required_map = {
        'code': 'required',
        'name': 'optional',
        'description': 'optional',
        'is_portfolio_group': 'optional',
        'left': 'optional',
        'right': 'optional',
        'transactions': 'optional',
        'positions': 'optional',
        'valuations': 'optional',
        'properties': 'optional'
    }

    def __init__(self, code=None, name=None, description=None, is_portfolio_group=None, left=None, right=None, transactions=None, positions=None, valuations=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """CreateReconciliationRequest - a model defined in OpenAPI"
        
        :param code:  The unique identifier associated with the reconciliation (required)
        :type code: str
        :param name:  The name of the scheduled reconciliation
        :type name: str
        :param description:  A description of the scheduled reconciliation
        :type description: str
        :param is_portfolio_group:  Specifies whether reconciliation is between portfolios or portfolio groups
        :type is_portfolio_group: bool
        :param left: 
        :type left: lusid.ResourceId
        :param right: 
        :type right: lusid.ResourceId
        :param transactions: 
        :type transactions: lusid.ReconciliationTransactions
        :param positions: 
        :type positions: lusid.ReconciliationConfiguration
        :param valuations: 
        :type valuations: lusid.ReconciliationConfiguration
        :param properties:  Reconciliation properties
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._description = None
        self._is_portfolio_group = None
        self._left = None
        self._right = None
        self._transactions = None
        self._positions = None
        self._valuations = None
        self._properties = None
        self.discriminator = None

        self.code = code
        self.name = name
        self.description = description
        if is_portfolio_group is not None:
            self.is_portfolio_group = is_portfolio_group
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if transactions is not None:
            self.transactions = transactions
        if positions is not None:
            self.positions = positions
        if valuations is not None:
            self.valuations = valuations
        self.properties = properties

    @property
    def code(self):
        """Gets the code of this CreateReconciliationRequest.  # noqa: E501

        The unique identifier associated with the reconciliation  # noqa: E501

        :return: The code of this CreateReconciliationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateReconciliationRequest.

        The unique identifier associated with the reconciliation  # noqa: E501

        :param code: The code of this CreateReconciliationRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this CreateReconciliationRequest.  # noqa: E501

        The name of the scheduled reconciliation  # noqa: E501

        :return: The name of this CreateReconciliationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateReconciliationRequest.

        The name of the scheduled reconciliation  # noqa: E501

        :param name: The name of this CreateReconciliationRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateReconciliationRequest.  # noqa: E501

        A description of the scheduled reconciliation  # noqa: E501

        :return: The description of this CreateReconciliationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateReconciliationRequest.

        A description of the scheduled reconciliation  # noqa: E501

        :param description: The description of this CreateReconciliationRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def is_portfolio_group(self):
        """Gets the is_portfolio_group of this CreateReconciliationRequest.  # noqa: E501

        Specifies whether reconciliation is between portfolios or portfolio groups  # noqa: E501

        :return: The is_portfolio_group of this CreateReconciliationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_portfolio_group

    @is_portfolio_group.setter
    def is_portfolio_group(self, is_portfolio_group):
        """Sets the is_portfolio_group of this CreateReconciliationRequest.

        Specifies whether reconciliation is between portfolios or portfolio groups  # noqa: E501

        :param is_portfolio_group: The is_portfolio_group of this CreateReconciliationRequest.  # noqa: E501
        :type is_portfolio_group: bool
        """

        self._is_portfolio_group = is_portfolio_group

    @property
    def left(self):
        """Gets the left of this CreateReconciliationRequest.  # noqa: E501


        :return: The left of this CreateReconciliationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this CreateReconciliationRequest.


        :param left: The left of this CreateReconciliationRequest.  # noqa: E501
        :type left: lusid.ResourceId
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this CreateReconciliationRequest.  # noqa: E501


        :return: The right of this CreateReconciliationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this CreateReconciliationRequest.


        :param right: The right of this CreateReconciliationRequest.  # noqa: E501
        :type right: lusid.ResourceId
        """

        self._right = right

    @property
    def transactions(self):
        """Gets the transactions of this CreateReconciliationRequest.  # noqa: E501


        :return: The transactions of this CreateReconciliationRequest.  # noqa: E501
        :rtype: lusid.ReconciliationTransactions
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this CreateReconciliationRequest.


        :param transactions: The transactions of this CreateReconciliationRequest.  # noqa: E501
        :type transactions: lusid.ReconciliationTransactions
        """

        self._transactions = transactions

    @property
    def positions(self):
        """Gets the positions of this CreateReconciliationRequest.  # noqa: E501


        :return: The positions of this CreateReconciliationRequest.  # noqa: E501
        :rtype: lusid.ReconciliationConfiguration
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this CreateReconciliationRequest.


        :param positions: The positions of this CreateReconciliationRequest.  # noqa: E501
        :type positions: lusid.ReconciliationConfiguration
        """

        self._positions = positions

    @property
    def valuations(self):
        """Gets the valuations of this CreateReconciliationRequest.  # noqa: E501


        :return: The valuations of this CreateReconciliationRequest.  # noqa: E501
        :rtype: lusid.ReconciliationConfiguration
        """
        return self._valuations

    @valuations.setter
    def valuations(self, valuations):
        """Sets the valuations of this CreateReconciliationRequest.


        :param valuations: The valuations of this CreateReconciliationRequest.  # noqa: E501
        :type valuations: lusid.ReconciliationConfiguration
        """

        self._valuations = valuations

    @property
    def properties(self):
        """Gets the properties of this CreateReconciliationRequest.  # noqa: E501

        Reconciliation properties  # noqa: E501

        :return: The properties of this CreateReconciliationRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateReconciliationRequest.

        Reconciliation properties  # noqa: E501

        :param properties: The properties of this CreateReconciliationRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

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
        if not isinstance(other, CreateReconciliationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateReconciliationRequest):
            return True

        return self.to_dict() != other.to_dict()
