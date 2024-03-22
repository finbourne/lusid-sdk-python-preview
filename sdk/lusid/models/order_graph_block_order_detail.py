# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.123
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


class OrderGraphBlockOrderDetail(object):
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
        'compliance_state': 'str',
        'approval_state': 'str',
        'portfolio_id': 'ResourceId',
        'portfolio_name': 'str',
        'order_approval_task_id': 'str',
        'order_approval_task_definition_id': 'ResourceId'
    }

    attribute_map = {
        'id': 'id',
        'compliance_state': 'complianceState',
        'approval_state': 'approvalState',
        'portfolio_id': 'portfolioId',
        'portfolio_name': 'portfolioName',
        'order_approval_task_id': 'orderApprovalTaskId',
        'order_approval_task_definition_id': 'orderApprovalTaskDefinitionId'
    }

    required_map = {
        'id': 'required',
        'compliance_state': 'required',
        'approval_state': 'required',
        'portfolio_id': 'optional',
        'portfolio_name': 'optional',
        'order_approval_task_id': 'optional',
        'order_approval_task_definition_id': 'optional'
    }

    def __init__(self, id=None, compliance_state=None, approval_state=None, portfolio_id=None, portfolio_name=None, order_approval_task_id=None, order_approval_task_definition_id=None, local_vars_configuration=None):  # noqa: E501
        """OrderGraphBlockOrderDetail - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param compliance_state:  The compliance state of this order. Possible values are 'Pending', 'Failed', 'Manually approved' and 'Passed'. (required)
        :type compliance_state: str
        :param approval_state:  The approval state of this order. Possible values are 'Pending', 'Rejected' and 'Approved'. (required)
        :type approval_state: str
        :param portfolio_id: 
        :type portfolio_id: lusid.ResourceId
        :param portfolio_name:  The name of the order's referenced Portfolio.
        :type portfolio_name: str
        :param order_approval_task_id:  The task id associated with the approval state of the order.
        :type order_approval_task_id: str
        :param order_approval_task_definition_id: 
        :type order_approval_task_definition_id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._compliance_state = None
        self._approval_state = None
        self._portfolio_id = None
        self._portfolio_name = None
        self._order_approval_task_id = None
        self._order_approval_task_definition_id = None
        self.discriminator = None

        self.id = id
        self.compliance_state = compliance_state
        self.approval_state = approval_state
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        self.portfolio_name = portfolio_name
        self.order_approval_task_id = order_approval_task_id
        if order_approval_task_definition_id is not None:
            self.order_approval_task_definition_id = order_approval_task_definition_id

    @property
    def id(self):
        """Gets the id of this OrderGraphBlockOrderDetail.  # noqa: E501


        :return: The id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderGraphBlockOrderDetail.


        :param id: The id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def compliance_state(self):
        """Gets the compliance_state of this OrderGraphBlockOrderDetail.  # noqa: E501

        The compliance state of this order. Possible values are 'Pending', 'Failed', 'Manually approved' and 'Passed'.  # noqa: E501

        :return: The compliance_state of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this OrderGraphBlockOrderDetail.

        The compliance state of this order. Possible values are 'Pending', 'Failed', 'Manually approved' and 'Passed'.  # noqa: E501

        :param compliance_state: The compliance_state of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type compliance_state: str
        """
        if self.local_vars_configuration.client_side_validation and compliance_state is None:  # noqa: E501
            raise ValueError("Invalid value for `compliance_state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                compliance_state is not None and len(compliance_state) < 1):
            raise ValueError("Invalid value for `compliance_state`, length must be greater than or equal to `1`")  # noqa: E501

        self._compliance_state = compliance_state

    @property
    def approval_state(self):
        """Gets the approval_state of this OrderGraphBlockOrderDetail.  # noqa: E501

        The approval state of this order. Possible values are 'Pending', 'Rejected' and 'Approved'.  # noqa: E501

        :return: The approval_state of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: str
        """
        return self._approval_state

    @approval_state.setter
    def approval_state(self, approval_state):
        """Sets the approval_state of this OrderGraphBlockOrderDetail.

        The approval state of this order. Possible values are 'Pending', 'Rejected' and 'Approved'.  # noqa: E501

        :param approval_state: The approval_state of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type approval_state: str
        """
        if self.local_vars_configuration.client_side_validation and approval_state is None:  # noqa: E501
            raise ValueError("Invalid value for `approval_state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                approval_state is not None and len(approval_state) < 1):
            raise ValueError("Invalid value for `approval_state`, length must be greater than or equal to `1`")  # noqa: E501

        self._approval_state = approval_state

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this OrderGraphBlockOrderDetail.  # noqa: E501


        :return: The portfolio_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this OrderGraphBlockOrderDetail.


        :param portfolio_id: The portfolio_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """

        self._portfolio_id = portfolio_id

    @property
    def portfolio_name(self):
        """Gets the portfolio_name of this OrderGraphBlockOrderDetail.  # noqa: E501

        The name of the order's referenced Portfolio.  # noqa: E501

        :return: The portfolio_name of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_name

    @portfolio_name.setter
    def portfolio_name(self, portfolio_name):
        """Sets the portfolio_name of this OrderGraphBlockOrderDetail.

        The name of the order's referenced Portfolio.  # noqa: E501

        :param portfolio_name: The portfolio_name of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type portfolio_name: str
        """

        self._portfolio_name = portfolio_name

    @property
    def order_approval_task_id(self):
        """Gets the order_approval_task_id of this OrderGraphBlockOrderDetail.  # noqa: E501

        The task id associated with the approval state of the order.  # noqa: E501

        :return: The order_approval_task_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: str
        """
        return self._order_approval_task_id

    @order_approval_task_id.setter
    def order_approval_task_id(self, order_approval_task_id):
        """Sets the order_approval_task_id of this OrderGraphBlockOrderDetail.

        The task id associated with the approval state of the order.  # noqa: E501

        :param order_approval_task_id: The order_approval_task_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type order_approval_task_id: str
        """

        self._order_approval_task_id = order_approval_task_id

    @property
    def order_approval_task_definition_id(self):
        """Gets the order_approval_task_definition_id of this OrderGraphBlockOrderDetail.  # noqa: E501


        :return: The order_approval_task_definition_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_approval_task_definition_id

    @order_approval_task_definition_id.setter
    def order_approval_task_definition_id(self, order_approval_task_definition_id):
        """Sets the order_approval_task_definition_id of this OrderGraphBlockOrderDetail.


        :param order_approval_task_definition_id: The order_approval_task_definition_id of this OrderGraphBlockOrderDetail.  # noqa: E501
        :type order_approval_task_definition_id: lusid.ResourceId
        """

        self._order_approval_task_definition_id = order_approval_task_definition_id

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
        if not isinstance(other, OrderGraphBlockOrderDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderGraphBlockOrderDetail):
            return True

        return self.to_dict() != other.to_dict()
