# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.576
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


class UpsertReconciliationBreakRequest(object):
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
        'left_fields': 'dict(str, str)',
        'right_fields': 'dict(str, str)',
        'diff': 'str'
    }

    attribute_map = {
        'left_fields': 'leftFields',
        'right_fields': 'rightFields',
        'diff': 'diff'
    }

    required_map = {
        'left_fields': 'optional',
        'right_fields': 'optional',
        'diff': 'optional'
    }

    def __init__(self, left_fields=None, right_fields=None, diff=None, local_vars_configuration=None):  # noqa: E501
        """UpsertReconciliationBreakRequest - a model defined in OpenAPI"
        
        :param left_fields:  Fields for the left hand side of the reconciliation
        :type left_fields: dict(str, str)
        :param right_fields:  Fields for the right hand side of the reconciliation
        :type right_fields: dict(str, str)
        :param diff:  The difference between two matching fields
        :type diff: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left_fields = None
        self._right_fields = None
        self._diff = None
        self.discriminator = None

        self.left_fields = left_fields
        self.right_fields = right_fields
        self.diff = diff

    @property
    def left_fields(self):
        """Gets the left_fields of this UpsertReconciliationBreakRequest.  # noqa: E501

        Fields for the left hand side of the reconciliation  # noqa: E501

        :return: The left_fields of this UpsertReconciliationBreakRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._left_fields

    @left_fields.setter
    def left_fields(self, left_fields):
        """Sets the left_fields of this UpsertReconciliationBreakRequest.

        Fields for the left hand side of the reconciliation  # noqa: E501

        :param left_fields: The left_fields of this UpsertReconciliationBreakRequest.  # noqa: E501
        :type left_fields: dict(str, str)
        """

        self._left_fields = left_fields

    @property
    def right_fields(self):
        """Gets the right_fields of this UpsertReconciliationBreakRequest.  # noqa: E501

        Fields for the right hand side of the reconciliation  # noqa: E501

        :return: The right_fields of this UpsertReconciliationBreakRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._right_fields

    @right_fields.setter
    def right_fields(self, right_fields):
        """Sets the right_fields of this UpsertReconciliationBreakRequest.

        Fields for the right hand side of the reconciliation  # noqa: E501

        :param right_fields: The right_fields of this UpsertReconciliationBreakRequest.  # noqa: E501
        :type right_fields: dict(str, str)
        """

        self._right_fields = right_fields

    @property
    def diff(self):
        """Gets the diff of this UpsertReconciliationBreakRequest.  # noqa: E501

        The difference between two matching fields  # noqa: E501

        :return: The diff of this UpsertReconciliationBreakRequest.  # noqa: E501
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this UpsertReconciliationBreakRequest.

        The difference between two matching fields  # noqa: E501

        :param diff: The diff of this UpsertReconciliationBreakRequest.  # noqa: E501
        :type diff: str
        """
        if (self.local_vars_configuration.client_side_validation and
                diff is not None and len(diff) > 512):
            raise ValueError("Invalid value for `diff`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diff is not None and len(diff) < 1):
            raise ValueError("Invalid value for `diff`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diff is not None and not re.search(r'^\d{1,3}(,\d{3})*(\.\d+)?$', diff)):  # noqa: E501
            raise ValueError(r"Invalid value for `diff`, must be a follow pattern or equal to `/^\d{1,3}(,\d{3})*(\.\d+)?$/`")  # noqa: E501

        self._diff = diff

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
        if not isinstance(other, UpsertReconciliationBreakRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertReconciliationBreakRequest):
            return True

        return self.to_dict() != other.to_dict()
