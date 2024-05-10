# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.140
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


class BranchStep(object):
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
        'parameters': 'list[ComplianceTemplateParameter]',
        'compliance_step_type': 'str'
    }

    attribute_map = {
        'label': 'label',
        'parameters': 'parameters',
        'compliance_step_type': 'complianceStepType'
    }

    required_map = {
        'label': 'required',
        'parameters': 'required',
        'compliance_step_type': 'required'
    }

    def __init__(self, label=None, parameters=None, compliance_step_type=None, local_vars_configuration=None):  # noqa: E501
        """BranchStep - a model defined in OpenAPI"
        
        :param label:  The label of the compliance step (required)
        :type label: str
        :param parameters:  Parameters required for the step (required)
        :type parameters: list[lusid.ComplianceTemplateParameter]
        :param compliance_step_type:  . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep (required)
        :type compliance_step_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._parameters = None
        self._compliance_step_type = None
        self.discriminator = None

        self.label = label
        self.parameters = parameters
        self.compliance_step_type = compliance_step_type

    @property
    def label(self):
        """Gets the label of this BranchStep.  # noqa: E501

        The label of the compliance step  # noqa: E501

        :return: The label of this BranchStep.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BranchStep.

        The label of the compliance step  # noqa: E501

        :param label: The label of this BranchStep.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) < 1):
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `1`")  # noqa: E501

        self._label = label

    @property
    def parameters(self):
        """Gets the parameters of this BranchStep.  # noqa: E501

        Parameters required for the step  # noqa: E501

        :return: The parameters of this BranchStep.  # noqa: E501
        :rtype: list[lusid.ComplianceTemplateParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BranchStep.

        Parameters required for the step  # noqa: E501

        :param parameters: The parameters of this BranchStep.  # noqa: E501
        :type parameters: list[lusid.ComplianceTemplateParameter]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def compliance_step_type(self):
        """Gets the compliance_step_type of this BranchStep.  # noqa: E501

        . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep  # noqa: E501

        :return: The compliance_step_type of this BranchStep.  # noqa: E501
        :rtype: str
        """
        return self._compliance_step_type

    @compliance_step_type.setter
    def compliance_step_type(self, compliance_step_type):
        """Sets the compliance_step_type of this BranchStep.

        . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep  # noqa: E501

        :param compliance_step_type: The compliance_step_type of this BranchStep.  # noqa: E501
        :type compliance_step_type: str
        """
        if self.local_vars_configuration.client_side_validation and compliance_step_type is None:  # noqa: E501
            raise ValueError("Invalid value for `compliance_step_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FilterStep", "GroupByStep", "GroupFilterStep", "BranchStep", "RecombineStep", "CheckStep"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and compliance_step_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `compliance_step_type` ({0}), must be one of {1}"  # noqa: E501
                .format(compliance_step_type, allowed_values)
            )

        self._compliance_step_type = compliance_step_type

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
        if not isinstance(other, BranchStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BranchStep):
            return True

        return self.to_dict() != other.to_dict()
