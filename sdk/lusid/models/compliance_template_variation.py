# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.96
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


class ComplianceTemplateVariation(object):
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
        'label': 'str',
        'description': 'str',
        'required_parameters': 'list[ComplianceTemplateParameter]',
        'properties': 'dict(str, PerpetualProperty)',
        'accepted_address_keys': 'ResourceId',
        'steps': 'list[ComplianceStep]'
    }

    attribute_map = {
        'label': 'label',
        'description': 'description',
        'required_parameters': 'requiredParameters',
        'properties': 'properties',
        'accepted_address_keys': 'acceptedAddressKeys',
        'steps': 'steps'
    }

    required_map = {
        'label': 'required',
        'description': 'required',
        'required_parameters': 'required',
        'properties': 'required',
        'accepted_address_keys': 'required',
        'steps': 'required'
    }

    def __init__(self, label=None, description=None, required_parameters=None, properties=None, accepted_address_keys=None, steps=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceTemplateVariation - a model defined in OpenAPI"
        
        :param label:  Label of a Compliance Template Variation (required)
        :type label: str
        :param description:  The description of the Compliance Template Variation (required)
        :type description: str
        :param required_parameters:  A parameter required by a Compliance Template Variation (required)
        :type required_parameters: list[lusid.ComplianceTemplateParameter]
        :param properties:  Properties associated with the Compliance Template Variation (required)
        :type properties: dict[str, lusid.PerpetualProperty]
        :param accepted_address_keys:  (required)
        :type accepted_address_keys: lusid.ResourceId
        :param steps:  The steps expressed in this template, with their required parameters (required)
        :type steps: list[lusid.ComplianceStep]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._description = None
        self._required_parameters = None
        self._properties = None
        self._accepted_address_keys = None
        self._steps = None
        self.discriminator = None

        self.label = label
        self.description = description
        self.required_parameters = required_parameters
        self.properties = properties
        self.accepted_address_keys = accepted_address_keys
        self.steps = steps

    @property
    def label(self):
        """Gets the label of this ComplianceTemplateVariation.  # noqa: E501

        Label of a Compliance Template Variation  # noqa: E501

        :return: The label of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ComplianceTemplateVariation.

        Label of a Compliance Template Variation  # noqa: E501

        :param label: The label of this ComplianceTemplateVariation.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) < 1):
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `1`")  # noqa: E501

        self._label = label

    @property
    def description(self):
        """Gets the description of this ComplianceTemplateVariation.  # noqa: E501

        The description of the Compliance Template Variation  # noqa: E501

        :return: The description of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComplianceTemplateVariation.

        The description of the Compliance Template Variation  # noqa: E501

        :param description: The description of this ComplianceTemplateVariation.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def required_parameters(self):
        """Gets the required_parameters of this ComplianceTemplateVariation.  # noqa: E501

        A parameter required by a Compliance Template Variation  # noqa: E501

        :return: The required_parameters of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: list[lusid.ComplianceTemplateParameter]
        """
        return self._required_parameters

    @required_parameters.setter
    def required_parameters(self, required_parameters):
        """Sets the required_parameters of this ComplianceTemplateVariation.

        A parameter required by a Compliance Template Variation  # noqa: E501

        :param required_parameters: The required_parameters of this ComplianceTemplateVariation.  # noqa: E501
        :type required_parameters: list[lusid.ComplianceTemplateParameter]
        """
        if self.local_vars_configuration.client_side_validation and required_parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `required_parameters`, must not be `None`")  # noqa: E501

        self._required_parameters = required_parameters

    @property
    def properties(self):
        """Gets the properties of this ComplianceTemplateVariation.  # noqa: E501

        Properties associated with the Compliance Template Variation  # noqa: E501

        :return: The properties of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ComplianceTemplateVariation.

        Properties associated with the Compliance Template Variation  # noqa: E501

        :param properties: The properties of this ComplianceTemplateVariation.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def accepted_address_keys(self):
        """Gets the accepted_address_keys of this ComplianceTemplateVariation.  # noqa: E501


        :return: The accepted_address_keys of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._accepted_address_keys

    @accepted_address_keys.setter
    def accepted_address_keys(self, accepted_address_keys):
        """Sets the accepted_address_keys of this ComplianceTemplateVariation.


        :param accepted_address_keys: The accepted_address_keys of this ComplianceTemplateVariation.  # noqa: E501
        :type accepted_address_keys: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and accepted_address_keys is None:  # noqa: E501
            raise ValueError("Invalid value for `accepted_address_keys`, must not be `None`")  # noqa: E501

        self._accepted_address_keys = accepted_address_keys

    @property
    def steps(self):
        """Gets the steps of this ComplianceTemplateVariation.  # noqa: E501

        The steps expressed in this template, with their required parameters  # noqa: E501

        :return: The steps of this ComplianceTemplateVariation.  # noqa: E501
        :rtype: list[lusid.ComplianceStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this ComplianceTemplateVariation.

        The steps expressed in this template, with their required parameters  # noqa: E501

        :param steps: The steps of this ComplianceTemplateVariation.  # noqa: E501
        :type steps: list[lusid.ComplianceStep]
        """
        if self.local_vars_configuration.client_side_validation and steps is None:  # noqa: E501
            raise ValueError("Invalid value for `steps`, must not be `None`")  # noqa: E501

        self._steps = steps

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
        if not isinstance(other, ComplianceTemplateVariation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceTemplateVariation):
            return True

        return self.to_dict() != other.to_dict()
