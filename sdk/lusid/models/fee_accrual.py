# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.230
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


class FeeAccrual(object):
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
        'effective_at': 'datetime',
        'code': 'str',
        'name': 'str',
        'calculation_base': 'float',
        'amount': 'float',
        'previous_accrual': 'float',
        'total_accrual': 'float',
        'links': 'list[Link]'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'code': 'code',
        'name': 'name',
        'calculation_base': 'calculationBase',
        'amount': 'amount',
        'previous_accrual': 'previousAccrual',
        'total_accrual': 'totalAccrual',
        'links': 'links'
    }

    required_map = {
        'effective_at': 'required',
        'code': 'required',
        'name': 'required',
        'calculation_base': 'optional',
        'amount': 'optional',
        'previous_accrual': 'optional',
        'total_accrual': 'optional',
        'links': 'optional'
    }

    def __init__(self, effective_at=None, code=None, name=None, calculation_base=None, amount=None, previous_accrual=None, total_accrual=None, links=None, local_vars_configuration=None):  # noqa: E501
        """FeeAccrual - a model defined in OpenAPI"
        
        :param effective_at:  The effective date for which the fee accrual has been calculated. (required)
        :type effective_at: datetime
        :param code:  The code of the fee for which the accrual has been calculated. (required)
        :type code: str
        :param name:  The name of the fee for which the accrual has been calculated. (required)
        :type name: str
        :param calculation_base:  The result of the evaluating the fee's calculation base expression.
        :type calculation_base: float
        :param amount:  The result of applying the fee to the calculation base, and scaled down to a day.
        :type amount: float
        :param previous_accrual:  The previous valuation point's total accrual.
        :type previous_accrual: float
        :param total_accrual:  The sum of the PreviousAccrual and Amount.
        :type total_accrual: float
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._code = None
        self._name = None
        self._calculation_base = None
        self._amount = None
        self._previous_accrual = None
        self._total_accrual = None
        self._links = None
        self.discriminator = None

        self.effective_at = effective_at
        self.code = code
        self.name = name
        if calculation_base is not None:
            self.calculation_base = calculation_base
        if amount is not None:
            self.amount = amount
        if previous_accrual is not None:
            self.previous_accrual = previous_accrual
        if total_accrual is not None:
            self.total_accrual = total_accrual
        self.links = links

    @property
    def effective_at(self):
        """Gets the effective_at of this FeeAccrual.  # noqa: E501

        The effective date for which the fee accrual has been calculated.  # noqa: E501

        :return: The effective_at of this FeeAccrual.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this FeeAccrual.

        The effective date for which the fee accrual has been calculated.  # noqa: E501

        :param effective_at: The effective_at of this FeeAccrual.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def code(self):
        """Gets the code of this FeeAccrual.  # noqa: E501

        The code of the fee for which the accrual has been calculated.  # noqa: E501

        :return: The code of this FeeAccrual.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FeeAccrual.

        The code of the fee for which the accrual has been calculated.  # noqa: E501

        :param code: The code of this FeeAccrual.  # noqa: E501
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
        """Gets the name of this FeeAccrual.  # noqa: E501

        The name of the fee for which the accrual has been calculated.  # noqa: E501

        :return: The name of this FeeAccrual.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeeAccrual.

        The name of the fee for which the accrual has been calculated.  # noqa: E501

        :param name: The name of this FeeAccrual.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def calculation_base(self):
        """Gets the calculation_base of this FeeAccrual.  # noqa: E501

        The result of the evaluating the fee's calculation base expression.  # noqa: E501

        :return: The calculation_base of this FeeAccrual.  # noqa: E501
        :rtype: float
        """
        return self._calculation_base

    @calculation_base.setter
    def calculation_base(self, calculation_base):
        """Sets the calculation_base of this FeeAccrual.

        The result of the evaluating the fee's calculation base expression.  # noqa: E501

        :param calculation_base: The calculation_base of this FeeAccrual.  # noqa: E501
        :type calculation_base: float
        """

        self._calculation_base = calculation_base

    @property
    def amount(self):
        """Gets the amount of this FeeAccrual.  # noqa: E501

        The result of applying the fee to the calculation base, and scaled down to a day.  # noqa: E501

        :return: The amount of this FeeAccrual.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FeeAccrual.

        The result of applying the fee to the calculation base, and scaled down to a day.  # noqa: E501

        :param amount: The amount of this FeeAccrual.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def previous_accrual(self):
        """Gets the previous_accrual of this FeeAccrual.  # noqa: E501

        The previous valuation point's total accrual.  # noqa: E501

        :return: The previous_accrual of this FeeAccrual.  # noqa: E501
        :rtype: float
        """
        return self._previous_accrual

    @previous_accrual.setter
    def previous_accrual(self, previous_accrual):
        """Sets the previous_accrual of this FeeAccrual.

        The previous valuation point's total accrual.  # noqa: E501

        :param previous_accrual: The previous_accrual of this FeeAccrual.  # noqa: E501
        :type previous_accrual: float
        """

        self._previous_accrual = previous_accrual

    @property
    def total_accrual(self):
        """Gets the total_accrual of this FeeAccrual.  # noqa: E501

        The sum of the PreviousAccrual and Amount.  # noqa: E501

        :return: The total_accrual of this FeeAccrual.  # noqa: E501
        :rtype: float
        """
        return self._total_accrual

    @total_accrual.setter
    def total_accrual(self, total_accrual):
        """Sets the total_accrual of this FeeAccrual.

        The sum of the PreviousAccrual and Amount.  # noqa: E501

        :param total_accrual: The total_accrual of this FeeAccrual.  # noqa: E501
        :type total_accrual: float
        """

        self._total_accrual = total_accrual

    @property
    def links(self):
        """Gets the links of this FeeAccrual.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this FeeAccrual.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeeAccrual.

        Collection of links.  # noqa: E501

        :param links: The links of this FeeAccrual.  # noqa: E501
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
        if not isinstance(other, FeeAccrual):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeeAccrual):
            return True

        return self.to_dict() != other.to_dict()
