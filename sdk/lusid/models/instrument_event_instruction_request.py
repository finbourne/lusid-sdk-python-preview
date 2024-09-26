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


class InstrumentEventInstructionRequest(object):
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
        'instrument_event_instruction_id': 'str',
        'instrument_event_id': 'str',
        'instruction_type': 'str',
        'election_key': 'str',
        'holding_id': 'int'
    }

    attribute_map = {
        'instrument_event_instruction_id': 'instrumentEventInstructionId',
        'instrument_event_id': 'instrumentEventId',
        'instruction_type': 'instructionType',
        'election_key': 'electionKey',
        'holding_id': 'holdingId'
    }

    required_map = {
        'instrument_event_instruction_id': 'required',
        'instrument_event_id': 'required',
        'instruction_type': 'required',
        'election_key': 'optional',
        'holding_id': 'optional'
    }

    def __init__(self, instrument_event_instruction_id=None, instrument_event_id=None, instruction_type=None, election_key=None, holding_id=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentEventInstructionRequest - a model defined in OpenAPI"
        
        :param instrument_event_instruction_id:  The unique identifier for this instruction (required)
        :type instrument_event_instruction_id: str
        :param instrument_event_id:  The identifier of the instrument event being instructed (required)
        :type instrument_event_id: str
        :param instruction_type:  The type of instruction (Ignore, ElectForPortfolio, ElectForHolding) (required)
        :type instruction_type: str
        :param election_key:  For elected instructions, the key to be chosen
        :type election_key: str
        :param holding_id:  For holding instructions, the id of the holding for which the instruction will apply
        :type holding_id: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_event_instruction_id = None
        self._instrument_event_id = None
        self._instruction_type = None
        self._election_key = None
        self._holding_id = None
        self.discriminator = None

        self.instrument_event_instruction_id = instrument_event_instruction_id
        self.instrument_event_id = instrument_event_id
        self.instruction_type = instruction_type
        self.election_key = election_key
        self.holding_id = holding_id

    @property
    def instrument_event_instruction_id(self):
        """Gets the instrument_event_instruction_id of this InstrumentEventInstructionRequest.  # noqa: E501

        The unique identifier for this instruction  # noqa: E501

        :return: The instrument_event_instruction_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_instruction_id

    @instrument_event_instruction_id.setter
    def instrument_event_instruction_id(self, instrument_event_instruction_id):
        """Sets the instrument_event_instruction_id of this InstrumentEventInstructionRequest.

        The unique identifier for this instruction  # noqa: E501

        :param instrument_event_instruction_id: The instrument_event_instruction_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :type instrument_event_instruction_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_instruction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_instruction_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_instruction_id is not None and len(instrument_event_instruction_id) < 1):
            raise ValueError("Invalid value for `instrument_event_instruction_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_event_instruction_id = instrument_event_instruction_id

    @property
    def instrument_event_id(self):
        """Gets the instrument_event_id of this InstrumentEventInstructionRequest.  # noqa: E501

        The identifier of the instrument event being instructed  # noqa: E501

        :return: The instrument_event_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_id

    @instrument_event_id.setter
    def instrument_event_id(self, instrument_event_id):
        """Sets the instrument_event_id of this InstrumentEventInstructionRequest.

        The identifier of the instrument event being instructed  # noqa: E501

        :param instrument_event_id: The instrument_event_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :type instrument_event_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and len(instrument_event_id) < 1):
            raise ValueError("Invalid value for `instrument_event_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_event_id = instrument_event_id

    @property
    def instruction_type(self):
        """Gets the instruction_type of this InstrumentEventInstructionRequest.  # noqa: E501

        The type of instruction (Ignore, ElectForPortfolio, ElectForHolding)  # noqa: E501

        :return: The instruction_type of this InstrumentEventInstructionRequest.  # noqa: E501
        :rtype: str
        """
        return self._instruction_type

    @instruction_type.setter
    def instruction_type(self, instruction_type):
        """Sets the instruction_type of this InstrumentEventInstructionRequest.

        The type of instruction (Ignore, ElectForPortfolio, ElectForHolding)  # noqa: E501

        :param instruction_type: The instruction_type of this InstrumentEventInstructionRequest.  # noqa: E501
        :type instruction_type: str
        """
        if self.local_vars_configuration.client_side_validation and instruction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instruction_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instruction_type is not None and len(instruction_type) < 1):
            raise ValueError("Invalid value for `instruction_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._instruction_type = instruction_type

    @property
    def election_key(self):
        """Gets the election_key of this InstrumentEventInstructionRequest.  # noqa: E501

        For elected instructions, the key to be chosen  # noqa: E501

        :return: The election_key of this InstrumentEventInstructionRequest.  # noqa: E501
        :rtype: str
        """
        return self._election_key

    @election_key.setter
    def election_key(self, election_key):
        """Sets the election_key of this InstrumentEventInstructionRequest.

        For elected instructions, the key to be chosen  # noqa: E501

        :param election_key: The election_key of this InstrumentEventInstructionRequest.  # noqa: E501
        :type election_key: str
        """

        self._election_key = election_key

    @property
    def holding_id(self):
        """Gets the holding_id of this InstrumentEventInstructionRequest.  # noqa: E501

        For holding instructions, the id of the holding for which the instruction will apply  # noqa: E501

        :return: The holding_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :rtype: int
        """
        return self._holding_id

    @holding_id.setter
    def holding_id(self, holding_id):
        """Sets the holding_id of this InstrumentEventInstructionRequest.

        For holding instructions, the id of the holding for which the instruction will apply  # noqa: E501

        :param holding_id: The holding_id of this InstrumentEventInstructionRequest.  # noqa: E501
        :type holding_id: int
        """

        self._holding_id = holding_id

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
        if not isinstance(other, InstrumentEventInstructionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentEventInstructionRequest):
            return True

        return self.to_dict() != other.to_dict()
