# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3251
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class A2BMovementRecord(object):
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
        'portfolio_id': 'ResourceId',
        'holding_type': 'str',
        'instrument_uid': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'currency': 'str',
        'transaction_id': 'str',
        'movement_name': 'str',
        'effective_date': 'datetime',
        'units': 'float',
        'start': 'A2BCategory',
        'flows': 'A2BCategory',
        'gains': 'A2BCategory',
        'carry': 'A2BCategory',
        'end': 'A2BCategory',
        'properties': 'dict(str, ModelProperty)',
        'group_id': 'str'
    }

    attribute_map = {
        'portfolio_id': 'portfolioId',
        'holding_type': 'holdingType',
        'instrument_uid': 'instrumentUid',
        'sub_holding_keys': 'subHoldingKeys',
        'currency': 'currency',
        'transaction_id': 'transactionId',
        'movement_name': 'movementName',
        'effective_date': 'effectiveDate',
        'units': 'units',
        'start': 'start',
        'flows': 'flows',
        'gains': 'gains',
        'carry': 'carry',
        'end': 'end',
        'properties': 'properties',
        'group_id': 'groupId'
    }

    required_map = {
        'portfolio_id': 'optional',
        'holding_type': 'optional',
        'instrument_uid': 'optional',
        'sub_holding_keys': 'optional',
        'currency': 'optional',
        'transaction_id': 'optional',
        'movement_name': 'optional',
        'effective_date': 'optional',
        'units': 'optional',
        'start': 'optional',
        'flows': 'optional',
        'gains': 'optional',
        'carry': 'optional',
        'end': 'optional',
        'properties': 'optional',
        'group_id': 'optional'
    }

    def __init__(self, portfolio_id=None, holding_type=None, instrument_uid=None, sub_holding_keys=None, currency=None, transaction_id=None, movement_name=None, effective_date=None, units=None, start=None, flows=None, gains=None, carry=None, end=None, properties=None, group_id=None):  # noqa: E501
        """
        A2BMovementRecord - a model defined in OpenAPI

        :param portfolio_id: 
        :type portfolio_id: lusid.ResourceId
        :param holding_type:  The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.
        :type holding_type: str
        :param instrument_uid:  The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
        :type instrument_uid: str
        :param sub_holding_keys:  The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param currency:  The holding currency.
        :type currency: str
        :param transaction_id:  The unique identifier for the transaction.
        :type transaction_id: str
        :param movement_name:  The name of the movement.
        :type movement_name: str
        :param effective_date:  The date of the movement.
        :type effective_date: datetime
        :param units:  The number of units of the instrument that are affected by the movement.
        :type units: float
        :param start: 
        :type start: lusid.A2BCategory
        :param flows: 
        :type flows: lusid.A2BCategory
        :param gains: 
        :type gains: lusid.A2BCategory
        :param carry: 
        :type carry: lusid.A2BCategory
        :param end: 
        :type end: lusid.A2BCategory
        :param properties:  The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param group_id:  Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon.
        :type group_id: str

        """  # noqa: E501

        self._portfolio_id = None
        self._holding_type = None
        self._instrument_uid = None
        self._sub_holding_keys = None
        self._currency = None
        self._transaction_id = None
        self._movement_name = None
        self._effective_date = None
        self._units = None
        self._start = None
        self._flows = None
        self._gains = None
        self._carry = None
        self._end = None
        self._properties = None
        self._group_id = None
        self.discriminator = None

        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        self.holding_type = holding_type
        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.currency = currency
        self.transaction_id = transaction_id
        self.movement_name = movement_name
        if effective_date is not None:
            self.effective_date = effective_date
        if units is not None:
            self.units = units
        if start is not None:
            self.start = start
        if flows is not None:
            self.flows = flows
        if gains is not None:
            self.gains = gains
        if carry is not None:
            self.carry = carry
        if end is not None:
            self.end = end
        self.properties = properties
        self.group_id = group_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this A2BMovementRecord.  # noqa: E501


        :return: The portfolio_id of this A2BMovementRecord.  # noqa: E501
        :rtype: ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this A2BMovementRecord.


        :param portfolio_id: The portfolio_id of this A2BMovementRecord.  # noqa: E501
        :type: ResourceId
        """

        self._portfolio_id = portfolio_id

    @property
    def holding_type(self):
        """Gets the holding_type of this A2BMovementRecord.  # noqa: E501

        The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.  # noqa: E501

        :return: The holding_type of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._holding_type

    @holding_type.setter
    def holding_type(self, holding_type):
        """Sets the holding_type of this A2BMovementRecord.

        The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.  # noqa: E501

        :param holding_type: The holding_type of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._holding_type = holding_type

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this A2BMovementRecord.  # noqa: E501

        The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :return: The instrument_uid of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this A2BMovementRecord.

        The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :param instrument_uid: The instrument_uid of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._instrument_uid = instrument_uid

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this A2BMovementRecord.  # noqa: E501

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :return: The sub_holding_keys of this A2BMovementRecord.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this A2BMovementRecord.

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this A2BMovementRecord.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def currency(self):
        """Gets the currency of this A2BMovementRecord.  # noqa: E501

        The holding currency.  # noqa: E501

        :return: The currency of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this A2BMovementRecord.

        The holding currency.  # noqa: E501

        :param currency: The currency of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def transaction_id(self):
        """Gets the transaction_id of this A2BMovementRecord.  # noqa: E501

        The unique identifier for the transaction.  # noqa: E501

        :return: The transaction_id of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this A2BMovementRecord.

        The unique identifier for the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def movement_name(self):
        """Gets the movement_name of this A2BMovementRecord.  # noqa: E501

        The name of the movement.  # noqa: E501

        :return: The movement_name of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._movement_name

    @movement_name.setter
    def movement_name(self, movement_name):
        """Sets the movement_name of this A2BMovementRecord.

        The name of the movement.  # noqa: E501

        :param movement_name: The movement_name of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._movement_name = movement_name

    @property
    def effective_date(self):
        """Gets the effective_date of this A2BMovementRecord.  # noqa: E501

        The date of the movement.  # noqa: E501

        :return: The effective_date of this A2BMovementRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this A2BMovementRecord.

        The date of the movement.  # noqa: E501

        :param effective_date: The effective_date of this A2BMovementRecord.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def units(self):
        """Gets the units of this A2BMovementRecord.  # noqa: E501

        The number of units of the instrument that are affected by the movement.  # noqa: E501

        :return: The units of this A2BMovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this A2BMovementRecord.

        The number of units of the instrument that are affected by the movement.  # noqa: E501

        :param units: The units of this A2BMovementRecord.  # noqa: E501
        :type: float
        """

        self._units = units

    @property
    def start(self):
        """Gets the start of this A2BMovementRecord.  # noqa: E501


        :return: The start of this A2BMovementRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this A2BMovementRecord.


        :param start: The start of this A2BMovementRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._start = start

    @property
    def flows(self):
        """Gets the flows of this A2BMovementRecord.  # noqa: E501


        :return: The flows of this A2BMovementRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._flows

    @flows.setter
    def flows(self, flows):
        """Sets the flows of this A2BMovementRecord.


        :param flows: The flows of this A2BMovementRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._flows = flows

    @property
    def gains(self):
        """Gets the gains of this A2BMovementRecord.  # noqa: E501


        :return: The gains of this A2BMovementRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._gains

    @gains.setter
    def gains(self, gains):
        """Sets the gains of this A2BMovementRecord.


        :param gains: The gains of this A2BMovementRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._gains = gains

    @property
    def carry(self):
        """Gets the carry of this A2BMovementRecord.  # noqa: E501


        :return: The carry of this A2BMovementRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._carry

    @carry.setter
    def carry(self, carry):
        """Sets the carry of this A2BMovementRecord.


        :param carry: The carry of this A2BMovementRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._carry = carry

    @property
    def end(self):
        """Gets the end of this A2BMovementRecord.  # noqa: E501


        :return: The end of this A2BMovementRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this A2BMovementRecord.


        :param end: The end of this A2BMovementRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._end = end

    @property
    def properties(self):
        """Gets the properties of this A2BMovementRecord.  # noqa: E501

        The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this A2BMovementRecord.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this A2BMovementRecord.

        The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this A2BMovementRecord.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

    @property
    def group_id(self):
        """Gets the group_id of this A2BMovementRecord.  # noqa: E501

        Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon.  # noqa: E501

        :return: The group_id of this A2BMovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this A2BMovementRecord.

        Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon.  # noqa: E501

        :param group_id: The group_id of this A2BMovementRecord.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, A2BMovementRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
