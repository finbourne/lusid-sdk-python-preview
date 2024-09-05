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


class StagedModification(object):
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
        'id': 'str',
        'as_at_staged': 'datetime',
        'user_id_staged': 'str',
        'requested_id_staged': 'str',
        'action': 'str',
        'staging_rule': 'StagedModificationStagingRule',
        'decisions': 'list[StagedModificationDecision]',
        'decisions_count': 'int',
        'status': 'str',
        'as_at_closed': 'datetime',
        'entity_type': 'str',
        'scope': 'str',
        'entity_unique_id': 'str',
        'requested_changes': 'RequestedChanges',
        'entity_hrefs': 'StagedModificationsEntityHrefs',
        'display_name': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'as_at_staged': 'asAtStaged',
        'user_id_staged': 'userIdStaged',
        'requested_id_staged': 'requestedIdStaged',
        'action': 'action',
        'staging_rule': 'stagingRule',
        'decisions': 'decisions',
        'decisions_count': 'decisionsCount',
        'status': 'status',
        'as_at_closed': 'asAtClosed',
        'entity_type': 'entityType',
        'scope': 'scope',
        'entity_unique_id': 'entityUniqueId',
        'requested_changes': 'requestedChanges',
        'entity_hrefs': 'entityHrefs',
        'display_name': 'displayName',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'as_at_staged': 'optional',
        'user_id_staged': 'optional',
        'requested_id_staged': 'optional',
        'action': 'optional',
        'staging_rule': 'optional',
        'decisions': 'optional',
        'decisions_count': 'optional',
        'status': 'optional',
        'as_at_closed': 'optional',
        'entity_type': 'optional',
        'scope': 'optional',
        'entity_unique_id': 'optional',
        'requested_changes': 'optional',
        'entity_hrefs': 'optional',
        'display_name': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, as_at_staged=None, user_id_staged=None, requested_id_staged=None, action=None, staging_rule=None, decisions=None, decisions_count=None, status=None, as_at_closed=None, entity_type=None, scope=None, entity_unique_id=None, requested_changes=None, entity_hrefs=None, display_name=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StagedModification - a model defined in OpenAPI"
        
        :param id:  The unique Id for the staged modification
        :type id: str
        :param as_at_staged:  Time at which the modification was staged.
        :type as_at_staged: datetime
        :param user_id_staged:  Id of the user who created the stage modification request.
        :type user_id_staged: str
        :param requested_id_staged:  The Request Id that initiated this staged modification.
        :type requested_id_staged: str
        :param action:  Type of action of the staged modification, either create, update or delete.
        :type action: str
        :param staging_rule: 
        :type staging_rule: lusid.StagedModificationStagingRule
        :param decisions:  Object containing information relating to the decision on the staged modification.
        :type decisions: list[lusid.StagedModificationDecision]
        :param decisions_count:  Number of decisions made.
        :type decisions_count: int
        :param status:  The status of the staged modification.
        :type status: str
        :param as_at_closed:  Time at which the modification was closed by either rejection or approval.
        :type as_at_closed: datetime
        :param entity_type:  The type of the entity that the staged modification applies to.
        :type entity_type: str
        :param scope:  The scope of the entity that this staged modification applies to.
        :type scope: str
        :param entity_unique_id:  The unique Id of the entity the staged modification applies to.
        :type entity_unique_id: str
        :param requested_changes: 
        :type requested_changes: lusid.RequestedChanges
        :param entity_hrefs: 
        :type entity_hrefs: lusid.StagedModificationsEntityHrefs
        :param display_name:  The display name of the entity the staged modification applies to.
        :type display_name: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._as_at_staged = None
        self._user_id_staged = None
        self._requested_id_staged = None
        self._action = None
        self._staging_rule = None
        self._decisions = None
        self._decisions_count = None
        self._status = None
        self._as_at_closed = None
        self._entity_type = None
        self._scope = None
        self._entity_unique_id = None
        self._requested_changes = None
        self._entity_hrefs = None
        self._display_name = None
        self._links = None
        self.discriminator = None

        self.id = id
        if as_at_staged is not None:
            self.as_at_staged = as_at_staged
        self.user_id_staged = user_id_staged
        self.requested_id_staged = requested_id_staged
        self.action = action
        if staging_rule is not None:
            self.staging_rule = staging_rule
        self.decisions = decisions
        if decisions_count is not None:
            self.decisions_count = decisions_count
        self.status = status
        self.as_at_closed = as_at_closed
        self.entity_type = entity_type
        self.scope = scope
        self.entity_unique_id = entity_unique_id
        if requested_changes is not None:
            self.requested_changes = requested_changes
        if entity_hrefs is not None:
            self.entity_hrefs = entity_hrefs
        self.display_name = display_name
        self.links = links

    @property
    def id(self):
        """Gets the id of this StagedModification.  # noqa: E501

        The unique Id for the staged modification  # noqa: E501

        :return: The id of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StagedModification.

        The unique Id for the staged modification  # noqa: E501

        :param id: The id of this StagedModification.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def as_at_staged(self):
        """Gets the as_at_staged of this StagedModification.  # noqa: E501

        Time at which the modification was staged.  # noqa: E501

        :return: The as_at_staged of this StagedModification.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_staged

    @as_at_staged.setter
    def as_at_staged(self, as_at_staged):
        """Sets the as_at_staged of this StagedModification.

        Time at which the modification was staged.  # noqa: E501

        :param as_at_staged: The as_at_staged of this StagedModification.  # noqa: E501
        :type as_at_staged: datetime
        """

        self._as_at_staged = as_at_staged

    @property
    def user_id_staged(self):
        """Gets the user_id_staged of this StagedModification.  # noqa: E501

        Id of the user who created the stage modification request.  # noqa: E501

        :return: The user_id_staged of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._user_id_staged

    @user_id_staged.setter
    def user_id_staged(self, user_id_staged):
        """Sets the user_id_staged of this StagedModification.

        Id of the user who created the stage modification request.  # noqa: E501

        :param user_id_staged: The user_id_staged of this StagedModification.  # noqa: E501
        :type user_id_staged: str
        """

        self._user_id_staged = user_id_staged

    @property
    def requested_id_staged(self):
        """Gets the requested_id_staged of this StagedModification.  # noqa: E501

        The Request Id that initiated this staged modification.  # noqa: E501

        :return: The requested_id_staged of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._requested_id_staged

    @requested_id_staged.setter
    def requested_id_staged(self, requested_id_staged):
        """Sets the requested_id_staged of this StagedModification.

        The Request Id that initiated this staged modification.  # noqa: E501

        :param requested_id_staged: The requested_id_staged of this StagedModification.  # noqa: E501
        :type requested_id_staged: str
        """

        self._requested_id_staged = requested_id_staged

    @property
    def action(self):
        """Gets the action of this StagedModification.  # noqa: E501

        Type of action of the staged modification, either create, update or delete.  # noqa: E501

        :return: The action of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this StagedModification.

        Type of action of the staged modification, either create, update or delete.  # noqa: E501

        :param action: The action of this StagedModification.  # noqa: E501
        :type action: str
        """

        self._action = action

    @property
    def staging_rule(self):
        """Gets the staging_rule of this StagedModification.  # noqa: E501


        :return: The staging_rule of this StagedModification.  # noqa: E501
        :rtype: lusid.StagedModificationStagingRule
        """
        return self._staging_rule

    @staging_rule.setter
    def staging_rule(self, staging_rule):
        """Sets the staging_rule of this StagedModification.


        :param staging_rule: The staging_rule of this StagedModification.  # noqa: E501
        :type staging_rule: lusid.StagedModificationStagingRule
        """

        self._staging_rule = staging_rule

    @property
    def decisions(self):
        """Gets the decisions of this StagedModification.  # noqa: E501

        Object containing information relating to the decision on the staged modification.  # noqa: E501

        :return: The decisions of this StagedModification.  # noqa: E501
        :rtype: list[lusid.StagedModificationDecision]
        """
        return self._decisions

    @decisions.setter
    def decisions(self, decisions):
        """Sets the decisions of this StagedModification.

        Object containing information relating to the decision on the staged modification.  # noqa: E501

        :param decisions: The decisions of this StagedModification.  # noqa: E501
        :type decisions: list[lusid.StagedModificationDecision]
        """

        self._decisions = decisions

    @property
    def decisions_count(self):
        """Gets the decisions_count of this StagedModification.  # noqa: E501

        Number of decisions made.  # noqa: E501

        :return: The decisions_count of this StagedModification.  # noqa: E501
        :rtype: int
        """
        return self._decisions_count

    @decisions_count.setter
    def decisions_count(self, decisions_count):
        """Sets the decisions_count of this StagedModification.

        Number of decisions made.  # noqa: E501

        :param decisions_count: The decisions_count of this StagedModification.  # noqa: E501
        :type decisions_count: int
        """

        self._decisions_count = decisions_count

    @property
    def status(self):
        """Gets the status of this StagedModification.  # noqa: E501

        The status of the staged modification.  # noqa: E501

        :return: The status of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StagedModification.

        The status of the staged modification.  # noqa: E501

        :param status: The status of this StagedModification.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def as_at_closed(self):
        """Gets the as_at_closed of this StagedModification.  # noqa: E501

        Time at which the modification was closed by either rejection or approval.  # noqa: E501

        :return: The as_at_closed of this StagedModification.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_closed

    @as_at_closed.setter
    def as_at_closed(self, as_at_closed):
        """Sets the as_at_closed of this StagedModification.

        Time at which the modification was closed by either rejection or approval.  # noqa: E501

        :param as_at_closed: The as_at_closed of this StagedModification.  # noqa: E501
        :type as_at_closed: datetime
        """

        self._as_at_closed = as_at_closed

    @property
    def entity_type(self):
        """Gets the entity_type of this StagedModification.  # noqa: E501

        The type of the entity that the staged modification applies to.  # noqa: E501

        :return: The entity_type of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this StagedModification.

        The type of the entity that the staged modification applies to.  # noqa: E501

        :param entity_type: The entity_type of this StagedModification.  # noqa: E501
        :type entity_type: str
        """

        self._entity_type = entity_type

    @property
    def scope(self):
        """Gets the scope of this StagedModification.  # noqa: E501

        The scope of the entity that this staged modification applies to.  # noqa: E501

        :return: The scope of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this StagedModification.

        The scope of the entity that this staged modification applies to.  # noqa: E501

        :param scope: The scope of this StagedModification.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def entity_unique_id(self):
        """Gets the entity_unique_id of this StagedModification.  # noqa: E501

        The unique Id of the entity the staged modification applies to.  # noqa: E501

        :return: The entity_unique_id of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._entity_unique_id

    @entity_unique_id.setter
    def entity_unique_id(self, entity_unique_id):
        """Sets the entity_unique_id of this StagedModification.

        The unique Id of the entity the staged modification applies to.  # noqa: E501

        :param entity_unique_id: The entity_unique_id of this StagedModification.  # noqa: E501
        :type entity_unique_id: str
        """

        self._entity_unique_id = entity_unique_id

    @property
    def requested_changes(self):
        """Gets the requested_changes of this StagedModification.  # noqa: E501


        :return: The requested_changes of this StagedModification.  # noqa: E501
        :rtype: lusid.RequestedChanges
        """
        return self._requested_changes

    @requested_changes.setter
    def requested_changes(self, requested_changes):
        """Sets the requested_changes of this StagedModification.


        :param requested_changes: The requested_changes of this StagedModification.  # noqa: E501
        :type requested_changes: lusid.RequestedChanges
        """

        self._requested_changes = requested_changes

    @property
    def entity_hrefs(self):
        """Gets the entity_hrefs of this StagedModification.  # noqa: E501


        :return: The entity_hrefs of this StagedModification.  # noqa: E501
        :rtype: lusid.StagedModificationsEntityHrefs
        """
        return self._entity_hrefs

    @entity_hrefs.setter
    def entity_hrefs(self, entity_hrefs):
        """Sets the entity_hrefs of this StagedModification.


        :param entity_hrefs: The entity_hrefs of this StagedModification.  # noqa: E501
        :type entity_hrefs: lusid.StagedModificationsEntityHrefs
        """

        self._entity_hrefs = entity_hrefs

    @property
    def display_name(self):
        """Gets the display_name of this StagedModification.  # noqa: E501

        The display name of the entity the staged modification applies to.  # noqa: E501

        :return: The display_name of this StagedModification.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this StagedModification.

        The display name of the entity the staged modification applies to.  # noqa: E501

        :param display_name: The display_name of this StagedModification.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def links(self):
        """Gets the links of this StagedModification.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this StagedModification.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StagedModification.

        Collection of links.  # noqa: E501

        :param links: The links of this StagedModification.  # noqa: E501
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
        if not isinstance(other, StagedModification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagedModification):
            return True

        return self.to_dict() != other.to_dict()
