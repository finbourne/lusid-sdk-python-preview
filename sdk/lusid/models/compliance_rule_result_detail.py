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


class ComplianceRuleResultDetail(object):
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
        'rule_id': 'ResourceId',
        'affected_portfolios_details': 'list[ComplianceRuleResultPortfolioDetail]',
        'affected_orders': 'list[ResourceId]',
        'template_id': 'ResourceId',
        'template_description': 'str',
        'template_variation': 'str',
        'status': 'str',
        'rule_name': 'str',
        'rule_description': 'str',
        'outcome': 'str'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'affected_portfolios_details': 'affectedPortfoliosDetails',
        'affected_orders': 'affectedOrders',
        'template_id': 'templateId',
        'template_description': 'templateDescription',
        'template_variation': 'templateVariation',
        'status': 'status',
        'rule_name': 'ruleName',
        'rule_description': 'ruleDescription',
        'outcome': 'outcome'
    }

    required_map = {
        'rule_id': 'required',
        'affected_portfolios_details': 'required',
        'affected_orders': 'required',
        'template_id': 'required',
        'template_description': 'required',
        'template_variation': 'required',
        'status': 'required',
        'rule_name': 'required',
        'rule_description': 'required',
        'outcome': 'required'
    }

    def __init__(self, rule_id=None, affected_portfolios_details=None, affected_orders=None, template_id=None, template_description=None, template_variation=None, status=None, rule_name=None, rule_description=None, outcome=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRuleResultDetail - a model defined in OpenAPI"
        
        :param rule_id:  (required)
        :type rule_id: lusid.ResourceId
        :param affected_portfolios_details:  (required)
        :type affected_portfolios_details: list[lusid.ComplianceRuleResultPortfolioDetail]
        :param affected_orders:  (required)
        :type affected_orders: list[lusid.ResourceId]
        :param template_id:  (required)
        :type template_id: lusid.ResourceId
        :param template_description:  (required)
        :type template_description: str
        :param template_variation:  (required)
        :type template_variation: str
        :param status:  (required)
        :type status: str
        :param rule_name:  (required)
        :type rule_name: str
        :param rule_description:  (required)
        :type rule_description: str
        :param outcome:  (required)
        :type outcome: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_id = None
        self._affected_portfolios_details = None
        self._affected_orders = None
        self._template_id = None
        self._template_description = None
        self._template_variation = None
        self._status = None
        self._rule_name = None
        self._rule_description = None
        self._outcome = None
        self.discriminator = None

        self.rule_id = rule_id
        self.affected_portfolios_details = affected_portfolios_details
        self.affected_orders = affected_orders
        self.template_id = template_id
        self.template_description = template_description
        self.template_variation = template_variation
        self.status = status
        self.rule_name = rule_name
        self.rule_description = rule_description
        self.outcome = outcome

    @property
    def rule_id(self):
        """Gets the rule_id of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The rule_id of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ComplianceRuleResultDetail.


        :param rule_id: The rule_id of this ComplianceRuleResultDetail.  # noqa: E501
        :type rule_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and rule_id is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def affected_portfolios_details(self):
        """Gets the affected_portfolios_details of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The affected_portfolios_details of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: list[lusid.ComplianceRuleResultPortfolioDetail]
        """
        return self._affected_portfolios_details

    @affected_portfolios_details.setter
    def affected_portfolios_details(self, affected_portfolios_details):
        """Sets the affected_portfolios_details of this ComplianceRuleResultDetail.


        :param affected_portfolios_details: The affected_portfolios_details of this ComplianceRuleResultDetail.  # noqa: E501
        :type affected_portfolios_details: list[lusid.ComplianceRuleResultPortfolioDetail]
        """
        if self.local_vars_configuration.client_side_validation and affected_portfolios_details is None:  # noqa: E501
            raise ValueError("Invalid value for `affected_portfolios_details`, must not be `None`")  # noqa: E501

        self._affected_portfolios_details = affected_portfolios_details

    @property
    def affected_orders(self):
        """Gets the affected_orders of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The affected_orders of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._affected_orders

    @affected_orders.setter
    def affected_orders(self, affected_orders):
        """Sets the affected_orders of this ComplianceRuleResultDetail.


        :param affected_orders: The affected_orders of this ComplianceRuleResultDetail.  # noqa: E501
        :type affected_orders: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and affected_orders is None:  # noqa: E501
            raise ValueError("Invalid value for `affected_orders`, must not be `None`")  # noqa: E501

        self._affected_orders = affected_orders

    @property
    def template_id(self):
        """Gets the template_id of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The template_id of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ComplianceRuleResultDetail.


        :param template_id: The template_id of this ComplianceRuleResultDetail.  # noqa: E501
        :type template_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def template_description(self):
        """Gets the template_description of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The template_description of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this ComplianceRuleResultDetail.


        :param template_description: The template_description of this ComplianceRuleResultDetail.  # noqa: E501
        :type template_description: str
        """
        if self.local_vars_configuration.client_side_validation and template_description is None:  # noqa: E501
            raise ValueError("Invalid value for `template_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                template_description is not None and len(template_description) < 1):
            raise ValueError("Invalid value for `template_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._template_description = template_description

    @property
    def template_variation(self):
        """Gets the template_variation of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The template_variation of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._template_variation

    @template_variation.setter
    def template_variation(self, template_variation):
        """Sets the template_variation of this ComplianceRuleResultDetail.


        :param template_variation: The template_variation of this ComplianceRuleResultDetail.  # noqa: E501
        :type template_variation: str
        """
        if self.local_vars_configuration.client_side_validation and template_variation is None:  # noqa: E501
            raise ValueError("Invalid value for `template_variation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                template_variation is not None and len(template_variation) < 1):
            raise ValueError("Invalid value for `template_variation`, length must be greater than or equal to `1`")  # noqa: E501

        self._template_variation = template_variation

    @property
    def status(self):
        """Gets the status of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The status of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComplianceRuleResultDetail.


        :param status: The status of this ComplianceRuleResultDetail.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def rule_name(self):
        """Gets the rule_name of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The rule_name of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ComplianceRuleResultDetail.


        :param rule_name: The rule_name of this ComplianceRuleResultDetail.  # noqa: E501
        :type rule_name: str
        """
        if self.local_vars_configuration.client_side_validation and rule_name is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_name is not None and len(rule_name) < 1):
            raise ValueError("Invalid value for `rule_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def rule_description(self):
        """Gets the rule_description of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The rule_description of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description):
        """Sets the rule_description of this ComplianceRuleResultDetail.


        :param rule_description: The rule_description of this ComplianceRuleResultDetail.  # noqa: E501
        :type rule_description: str
        """
        if self.local_vars_configuration.client_side_validation and rule_description is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_description is not None and len(rule_description) < 1):
            raise ValueError("Invalid value for `rule_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_description = rule_description

    @property
    def outcome(self):
        """Gets the outcome of this ComplianceRuleResultDetail.  # noqa: E501


        :return: The outcome of this ComplianceRuleResultDetail.  # noqa: E501
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this ComplianceRuleResultDetail.


        :param outcome: The outcome of this ComplianceRuleResultDetail.  # noqa: E501
        :type outcome: str
        """
        if self.local_vars_configuration.client_side_validation and outcome is None:  # noqa: E501
            raise ValueError("Invalid value for `outcome`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outcome is not None and len(outcome) < 1):
            raise ValueError("Invalid value for `outcome`, length must be greater than or equal to `1`")  # noqa: E501

        self._outcome = outcome

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
        if not isinstance(other, ComplianceRuleResultDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRuleResultDetail):
            return True

        return self.to_dict() != other.to_dict()
