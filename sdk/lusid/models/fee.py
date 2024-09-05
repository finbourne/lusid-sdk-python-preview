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


class Fee(object):
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
        'fee_code': 'str',
        'fee_type': 'ResourceId',
        'name': 'str',
        'description': 'str',
        'origin': 'str',
        'calculation_base': 'str',
        'accrual_currency': 'str',
        'treatment': 'str',
        'total_annual_accrual_amount': 'float',
        'fee_rate_percentage': 'float',
        'payable_frequency': 'str',
        'business_day_convention': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'anchor_date': 'DayMonth',
        'properties': 'dict(str, ModelProperty)',
        'version': 'Version',
        'portfolio_id': 'ResourceId',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'fee_code': 'feeCode',
        'fee_type': 'feeType',
        'name': 'name',
        'description': 'description',
        'origin': 'origin',
        'calculation_base': 'calculationBase',
        'accrual_currency': 'accrualCurrency',
        'treatment': 'treatment',
        'total_annual_accrual_amount': 'totalAnnualAccrualAmount',
        'fee_rate_percentage': 'feeRatePercentage',
        'payable_frequency': 'payableFrequency',
        'business_day_convention': 'businessDayConvention',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'anchor_date': 'anchorDate',
        'properties': 'properties',
        'version': 'version',
        'portfolio_id': 'portfolioId',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'fee_code': 'optional',
        'fee_type': 'required',
        'name': 'required',
        'description': 'optional',
        'origin': 'optional',
        'calculation_base': 'optional',
        'accrual_currency': 'required',
        'treatment': 'required',
        'total_annual_accrual_amount': 'optional',
        'fee_rate_percentage': 'optional',
        'payable_frequency': 'required',
        'business_day_convention': 'required',
        'start_date': 'required',
        'end_date': 'optional',
        'anchor_date': 'optional',
        'properties': 'optional',
        'version': 'optional',
        'portfolio_id': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, fee_code=None, fee_type=None, name=None, description=None, origin=None, calculation_base=None, accrual_currency=None, treatment=None, total_annual_accrual_amount=None, fee_rate_percentage=None, payable_frequency=None, business_day_convention=None, start_date=None, end_date=None, anchor_date=None, properties=None, version=None, portfolio_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Fee - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param fee_code:  The code of the Fee.
        :type fee_code: str
        :param fee_type:  (required)
        :type fee_type: lusid.ResourceId
        :param name:  The name of the Fee. (required)
        :type name: str
        :param description:  A description for the Fee.
        :type description: str
        :param origin:  The origin or source of the Fee accrual.
        :type origin: str
        :param calculation_base:  The calculation base for the Fee that is calculated using a percentage. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)
        :type calculation_base: str
        :param accrual_currency:  The accrual currency. (required)
        :type accrual_currency: str
        :param treatment:  The accrual period of the Fee; 'Monthly' or 'Daily'. (required)
        :type treatment: str
        :param total_annual_accrual_amount:  The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)
        :type total_annual_accrual_amount: float
        :param fee_rate_percentage:  The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount)
        :type fee_rate_percentage: float
        :param payable_frequency:  The payable frequency for the Fee; 'Annually', 'Quarterly' or 'Monthly'. (required)
        :type payable_frequency: str
        :param business_day_convention:  The business day convention to use for Fee calculations on weekends. Supported string values are: [Previous, P, Following, F]. (required)
        :type business_day_convention: str
        :param start_date:  The start date of the Fee. (required)
        :type start_date: datetime
        :param end_date:  The end date of the Fee.
        :type end_date: datetime
        :param anchor_date: 
        :type anchor_date: lusid.DayMonth
        :param properties:  The Fee properties. These will be from the 'Fee' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param version: 
        :type version: lusid.Version
        :param portfolio_id: 
        :type portfolio_id: lusid.ResourceId
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._fee_code = None
        self._fee_type = None
        self._name = None
        self._description = None
        self._origin = None
        self._calculation_base = None
        self._accrual_currency = None
        self._treatment = None
        self._total_annual_accrual_amount = None
        self._fee_rate_percentage = None
        self._payable_frequency = None
        self._business_day_convention = None
        self._start_date = None
        self._end_date = None
        self._anchor_date = None
        self._properties = None
        self._version = None
        self._portfolio_id = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.fee_code = fee_code
        self.fee_type = fee_type
        self.name = name
        self.description = description
        self.origin = origin
        self.calculation_base = calculation_base
        self.accrual_currency = accrual_currency
        self.treatment = treatment
        self.total_annual_accrual_amount = total_annual_accrual_amount
        self.fee_rate_percentage = fee_rate_percentage
        self.payable_frequency = payable_frequency
        self.business_day_convention = business_day_convention
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if anchor_date is not None:
            self.anchor_date = anchor_date
        self.properties = properties
        if version is not None:
            self.version = version
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        self.links = links

    @property
    def href(self):
        """Gets the href of this Fee.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Fee.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Fee.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def fee_code(self):
        """Gets the fee_code of this Fee.  # noqa: E501

        The code of the Fee.  # noqa: E501

        :return: The fee_code of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._fee_code

    @fee_code.setter
    def fee_code(self, fee_code):
        """Sets the fee_code of this Fee.

        The code of the Fee.  # noqa: E501

        :param fee_code: The fee_code of this Fee.  # noqa: E501
        :type fee_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fee_code is not None and len(fee_code) > 64):
            raise ValueError("Invalid value for `fee_code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fee_code is not None and len(fee_code) < 1):
            raise ValueError("Invalid value for `fee_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fee_code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', fee_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `fee_code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._fee_code = fee_code

    @property
    def fee_type(self):
        """Gets the fee_type of this Fee.  # noqa: E501


        :return: The fee_type of this Fee.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this Fee.


        :param fee_type: The fee_type of this Fee.  # noqa: E501
        :type fee_type: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and fee_type is None:  # noqa: E501
            raise ValueError("Invalid value for `fee_type`, must not be `None`")  # noqa: E501

        self._fee_type = fee_type

    @property
    def name(self):
        """Gets the name of this Fee.  # noqa: E501

        The name of the Fee.  # noqa: E501

        :return: The name of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Fee.

        The name of the Fee.  # noqa: E501

        :param name: The name of this Fee.  # noqa: E501
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
    def description(self):
        """Gets the description of this Fee.  # noqa: E501

        A description for the Fee.  # noqa: E501

        :return: The description of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Fee.

        A description for the Fee.  # noqa: E501

        :param description: The description of this Fee.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def origin(self):
        """Gets the origin of this Fee.  # noqa: E501

        The origin or source of the Fee accrual.  # noqa: E501

        :return: The origin of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Fee.

        The origin or source of the Fee accrual.  # noqa: E501

        :param origin: The origin of this Fee.  # noqa: E501
        :type origin: str
        """
        if (self.local_vars_configuration.client_side_validation and
                origin is not None and len(origin) > 512):
            raise ValueError("Invalid value for `origin`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                origin is not None and len(origin) < 1):
            raise ValueError("Invalid value for `origin`, length must be greater than or equal to `1`")  # noqa: E501

        self._origin = origin

    @property
    def calculation_base(self):
        """Gets the calculation_base of this Fee.  # noqa: E501

        The calculation base for the Fee that is calculated using a percentage. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)  # noqa: E501

        :return: The calculation_base of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._calculation_base

    @calculation_base.setter
    def calculation_base(self, calculation_base):
        """Sets the calculation_base of this Fee.

        The calculation base for the Fee that is calculated using a percentage. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)  # noqa: E501

        :param calculation_base: The calculation_base of this Fee.  # noqa: E501
        :type calculation_base: str
        """
        if (self.local_vars_configuration.client_side_validation and
                calculation_base is not None and len(calculation_base) > 1024):
            raise ValueError("Invalid value for `calculation_base`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calculation_base is not None and len(calculation_base) < 0):
            raise ValueError("Invalid value for `calculation_base`, length must be greater than or equal to `0`")  # noqa: E501

        self._calculation_base = calculation_base

    @property
    def accrual_currency(self):
        """Gets the accrual_currency of this Fee.  # noqa: E501

        The accrual currency.  # noqa: E501

        :return: The accrual_currency of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._accrual_currency

    @accrual_currency.setter
    def accrual_currency(self, accrual_currency):
        """Sets the accrual_currency of this Fee.

        The accrual currency.  # noqa: E501

        :param accrual_currency: The accrual_currency of this Fee.  # noqa: E501
        :type accrual_currency: str
        """
        if self.local_vars_configuration.client_side_validation and accrual_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `accrual_currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accrual_currency is not None and len(accrual_currency) > 3):
            raise ValueError("Invalid value for `accrual_currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accrual_currency is not None and len(accrual_currency) < 0):
            raise ValueError("Invalid value for `accrual_currency`, length must be greater than or equal to `0`")  # noqa: E501

        self._accrual_currency = accrual_currency

    @property
    def treatment(self):
        """Gets the treatment of this Fee.  # noqa: E501

        The accrual period of the Fee; 'Monthly' or 'Daily'.  # noqa: E501

        :return: The treatment of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._treatment

    @treatment.setter
    def treatment(self, treatment):
        """Sets the treatment of this Fee.

        The accrual period of the Fee; 'Monthly' or 'Daily'.  # noqa: E501

        :param treatment: The treatment of this Fee.  # noqa: E501
        :type treatment: str
        """
        if self.local_vars_configuration.client_side_validation and treatment is None:  # noqa: E501
            raise ValueError("Invalid value for `treatment`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                treatment is not None and len(treatment) < 1):
            raise ValueError("Invalid value for `treatment`, length must be greater than or equal to `1`")  # noqa: E501

        self._treatment = treatment

    @property
    def total_annual_accrual_amount(self):
        """Gets the total_annual_accrual_amount of this Fee.  # noqa: E501

        The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)  # noqa: E501

        :return: The total_annual_accrual_amount of this Fee.  # noqa: E501
        :rtype: float
        """
        return self._total_annual_accrual_amount

    @total_annual_accrual_amount.setter
    def total_annual_accrual_amount(self, total_annual_accrual_amount):
        """Sets the total_annual_accrual_amount of this Fee.

        The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present)  # noqa: E501

        :param total_annual_accrual_amount: The total_annual_accrual_amount of this Fee.  # noqa: E501
        :type total_annual_accrual_amount: float
        """

        self._total_annual_accrual_amount = total_annual_accrual_amount

    @property
    def fee_rate_percentage(self):
        """Gets the fee_rate_percentage of this Fee.  # noqa: E501

        The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount)  # noqa: E501

        :return: The fee_rate_percentage of this Fee.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate_percentage

    @fee_rate_percentage.setter
    def fee_rate_percentage(self, fee_rate_percentage):
        """Sets the fee_rate_percentage of this Fee.

        The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount)  # noqa: E501

        :param fee_rate_percentage: The fee_rate_percentage of this Fee.  # noqa: E501
        :type fee_rate_percentage: float
        """

        self._fee_rate_percentage = fee_rate_percentage

    @property
    def payable_frequency(self):
        """Gets the payable_frequency of this Fee.  # noqa: E501

        The payable frequency for the Fee; 'Annually', 'Quarterly' or 'Monthly'.  # noqa: E501

        :return: The payable_frequency of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._payable_frequency

    @payable_frequency.setter
    def payable_frequency(self, payable_frequency):
        """Sets the payable_frequency of this Fee.

        The payable frequency for the Fee; 'Annually', 'Quarterly' or 'Monthly'.  # noqa: E501

        :param payable_frequency: The payable_frequency of this Fee.  # noqa: E501
        :type payable_frequency: str
        """
        if self.local_vars_configuration.client_side_validation and payable_frequency is None:  # noqa: E501
            raise ValueError("Invalid value for `payable_frequency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                payable_frequency is not None and len(payable_frequency) < 1):
            raise ValueError("Invalid value for `payable_frequency`, length must be greater than or equal to `1`")  # noqa: E501

        self._payable_frequency = payable_frequency

    @property
    def business_day_convention(self):
        """Gets the business_day_convention of this Fee.  # noqa: E501

        The business day convention to use for Fee calculations on weekends. Supported string values are: [Previous, P, Following, F].  # noqa: E501

        :return: The business_day_convention of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._business_day_convention

    @business_day_convention.setter
    def business_day_convention(self, business_day_convention):
        """Sets the business_day_convention of this Fee.

        The business day convention to use for Fee calculations on weekends. Supported string values are: [Previous, P, Following, F].  # noqa: E501

        :param business_day_convention: The business_day_convention of this Fee.  # noqa: E501
        :type business_day_convention: str
        """
        if self.local_vars_configuration.client_side_validation and business_day_convention is None:  # noqa: E501
            raise ValueError("Invalid value for `business_day_convention`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                business_day_convention is not None and len(business_day_convention) < 1):
            raise ValueError("Invalid value for `business_day_convention`, length must be greater than or equal to `1`")  # noqa: E501

        self._business_day_convention = business_day_convention

    @property
    def start_date(self):
        """Gets the start_date of this Fee.  # noqa: E501

        The start date of the Fee.  # noqa: E501

        :return: The start_date of this Fee.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Fee.

        The start date of the Fee.  # noqa: E501

        :param start_date: The start_date of this Fee.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Fee.  # noqa: E501

        The end date of the Fee.  # noqa: E501

        :return: The end_date of this Fee.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Fee.

        The end date of the Fee.  # noqa: E501

        :param end_date: The end_date of this Fee.  # noqa: E501
        :type end_date: datetime
        """

        self._end_date = end_date

    @property
    def anchor_date(self):
        """Gets the anchor_date of this Fee.  # noqa: E501


        :return: The anchor_date of this Fee.  # noqa: E501
        :rtype: lusid.DayMonth
        """
        return self._anchor_date

    @anchor_date.setter
    def anchor_date(self, anchor_date):
        """Sets the anchor_date of this Fee.


        :param anchor_date: The anchor_date of this Fee.  # noqa: E501
        :type anchor_date: lusid.DayMonth
        """

        self._anchor_date = anchor_date

    @property
    def properties(self):
        """Gets the properties of this Fee.  # noqa: E501

        The Fee properties. These will be from the 'Fee' domain.  # noqa: E501

        :return: The properties of this Fee.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Fee.

        The Fee properties. These will be from the 'Fee' domain.  # noqa: E501

        :param properties: The properties of this Fee.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this Fee.  # noqa: E501


        :return: The version of this Fee.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Fee.


        :param version: The version of this Fee.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this Fee.  # noqa: E501


        :return: The portfolio_id of this Fee.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this Fee.


        :param portfolio_id: The portfolio_id of this Fee.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """

        self._portfolio_id = portfolio_id

    @property
    def links(self):
        """Gets the links of this Fee.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Fee.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Fee.

        Collection of links.  # noqa: E501

        :param links: The links of this Fee.  # noqa: E501
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
        if not isinstance(other, Fee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Fee):
            return True

        return self.to_dict() != other.to_dict()
