# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.236
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


class StagedModificationDecision(object):
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
        'as_at': 'datetime',
        'user_id': 'str',
        'request_id': 'str',
        'decision': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'as_at': 'asAt',
        'user_id': 'userId',
        'request_id': 'requestId',
        'decision': 'decision',
        'comment': 'comment'
    }

    required_map = {
        'as_at': 'optional',
        'user_id': 'optional',
        'request_id': 'optional',
        'decision': 'optional',
        'comment': 'optional'
    }

    def __init__(self, as_at=None, user_id=None, request_id=None, decision=None, comment=None, local_vars_configuration=None):  # noqa: E501
        """StagedModificationDecision - a model defined in OpenAPI"
        
        :param as_at:  Time the decision request is made.
        :type as_at: datetime
        :param user_id:  ID of user that approved the request.
        :type user_id: str
        :param request_id:  ID of user that made the request.
        :type request_id: str
        :param decision:  The decision on the requested staged modification, can be 'Approve' or 'Reject'.
        :type decision: str
        :param comment:  Comment on decision.
        :type comment: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at = None
        self._user_id = None
        self._request_id = None
        self._decision = None
        self._comment = None
        self.discriminator = None

        if as_at is not None:
            self.as_at = as_at
        self.user_id = user_id
        self.request_id = request_id
        self.decision = decision
        self.comment = comment

    @property
    def as_at(self):
        """Gets the as_at of this StagedModificationDecision.  # noqa: E501

        Time the decision request is made.  # noqa: E501

        :return: The as_at of this StagedModificationDecision.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this StagedModificationDecision.

        Time the decision request is made.  # noqa: E501

        :param as_at: The as_at of this StagedModificationDecision.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def user_id(self):
        """Gets the user_id of this StagedModificationDecision.  # noqa: E501

        ID of user that approved the request.  # noqa: E501

        :return: The user_id of this StagedModificationDecision.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StagedModificationDecision.

        ID of user that approved the request.  # noqa: E501

        :param user_id: The user_id of this StagedModificationDecision.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def request_id(self):
        """Gets the request_id of this StagedModificationDecision.  # noqa: E501

        ID of user that made the request.  # noqa: E501

        :return: The request_id of this StagedModificationDecision.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this StagedModificationDecision.

        ID of user that made the request.  # noqa: E501

        :param request_id: The request_id of this StagedModificationDecision.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def decision(self):
        """Gets the decision of this StagedModificationDecision.  # noqa: E501

        The decision on the requested staged modification, can be 'Approve' or 'Reject'.  # noqa: E501

        :return: The decision of this StagedModificationDecision.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this StagedModificationDecision.

        The decision on the requested staged modification, can be 'Approve' or 'Reject'.  # noqa: E501

        :param decision: The decision of this StagedModificationDecision.  # noqa: E501
        :type decision: str
        """

        self._decision = decision

    @property
    def comment(self):
        """Gets the comment of this StagedModificationDecision.  # noqa: E501

        Comment on decision.  # noqa: E501

        :return: The comment of this StagedModificationDecision.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this StagedModificationDecision.

        Comment on decision.  # noqa: E501

        :param comment: The comment of this StagedModificationDecision.  # noqa: E501
        :type comment: str
        """

        self._comment = comment

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
        if not isinstance(other, StagedModificationDecision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModificationDecision):
            return True

        return self.to_dict() != other.to_dict()
