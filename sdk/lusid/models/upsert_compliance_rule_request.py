# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.82
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


class UpsertComplianceRuleRequest(object):
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
        'name': 'str',
        'description': 'str',
        'active': 'bool',
        'template_id': 'ResourceId',
        'variation': 'str',
        'portfolio_group_id': 'ResourceId',
        'parameters': 'dict(str, ComplianceParameter)',
        'properties': 'dict(str, PerpetualProperty)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'active': 'active',
        'template_id': 'templateId',
        'variation': 'variation',
        'portfolio_group_id': 'portfolioGroupId',
        'parameters': 'parameters',
        'properties': 'properties'
    }

    required_map = {
        'id': 'required',
        'name': 'optional',
        'description': 'optional',
        'active': 'required',
        'template_id': 'required',
        'variation': 'required',
        'portfolio_group_id': 'required',
        'parameters': 'required',
        'properties': 'required'
    }

    def __init__(self, id=None, name=None, description=None, active=None, template_id=None, variation=None, portfolio_group_id=None, parameters=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """UpsertComplianceRuleRequest - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param active:  (required)
        :type active: bool
        :param template_id:  (required)
        :type template_id: lusid.ResourceId
        :param variation:  (required)
        :type variation: str
        :param portfolio_group_id:  (required)
        :type portfolio_group_id: lusid.ResourceId
        :param parameters:  (required)
        :type parameters: dict[str, lusid.ComplianceParameter]
        :param properties:  (required)
        :type properties: dict[str, lusid.PerpetualProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._active = None
        self._template_id = None
        self._variation = None
        self._portfolio_group_id = None
        self._parameters = None
        self._properties = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.active = active
        self.template_id = template_id
        self.variation = variation
        self.portfolio_group_id = portfolio_group_id
        self.parameters = parameters
        self.properties = properties

    @property
    def id(self):
        """Gets the id of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The id of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpsertComplianceRuleRequest.


        :param id: The id of this UpsertComplianceRuleRequest.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The name of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpsertComplianceRuleRequest.


        :param name: The name of this UpsertComplianceRuleRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 6000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `6000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The description of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpsertComplianceRuleRequest.


        :param description: The description of this UpsertComplianceRuleRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 6000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `6000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def active(self):
        """Gets the active of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The active of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UpsertComplianceRuleRequest.


        :param active: The active of this UpsertComplianceRuleRequest.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def template_id(self):
        """Gets the template_id of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The template_id of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this UpsertComplianceRuleRequest.


        :param template_id: The template_id of this UpsertComplianceRuleRequest.  # noqa: E501
        :type template_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def variation(self):
        """Gets the variation of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The variation of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this UpsertComplianceRuleRequest.


        :param variation: The variation of this UpsertComplianceRuleRequest.  # noqa: E501
        :type variation: str
        """
        if self.local_vars_configuration.client_side_validation and variation is None:  # noqa: E501
            raise ValueError("Invalid value for `variation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                variation is not None and len(variation) > 256):
            raise ValueError("Invalid value for `variation`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                variation is not None and len(variation) < 1):
            raise ValueError("Invalid value for `variation`, length must be greater than or equal to `1`")  # noqa: E501

        self._variation = variation

    @property
    def portfolio_group_id(self):
        """Gets the portfolio_group_id of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The portfolio_group_id of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_group_id

    @portfolio_group_id.setter
    def portfolio_group_id(self, portfolio_group_id):
        """Sets the portfolio_group_id of this UpsertComplianceRuleRequest.


        :param portfolio_group_id: The portfolio_group_id of this UpsertComplianceRuleRequest.  # noqa: E501
        :type portfolio_group_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_group_id`, must not be `None`")  # noqa: E501

        self._portfolio_group_id = portfolio_group_id

    @property
    def parameters(self):
        """Gets the parameters of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The parameters of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: dict[str, lusid.ComplianceParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpsertComplianceRuleRequest.


        :param parameters: The parameters of this UpsertComplianceRuleRequest.  # noqa: E501
        :type parameters: dict[str, lusid.ComplianceParameter]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def properties(self):
        """Gets the properties of this UpsertComplianceRuleRequest.  # noqa: E501


        :return: The properties of this UpsertComplianceRuleRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpsertComplianceRuleRequest.


        :param properties: The properties of this UpsertComplianceRuleRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, UpsertComplianceRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertComplianceRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
