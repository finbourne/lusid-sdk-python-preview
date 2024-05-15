# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.148
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


class TransactionTemplateSpecification(object):
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
        'instrument_event_type': 'str',
        'supported_instrument_types': 'list[str]',
        'supported_participation_types': 'list[str]',
        'supported_election_types': 'list[ElectionSpecification]',
        'supported_template_fields': 'list[TemplateField]',
        'eligibility_calculation': 'EligibilityCalculation'
    }

    attribute_map = {
        'instrument_event_type': 'instrumentEventType',
        'supported_instrument_types': 'supportedInstrumentTypes',
        'supported_participation_types': 'supportedParticipationTypes',
        'supported_election_types': 'supportedElectionTypes',
        'supported_template_fields': 'supportedTemplateFields',
        'eligibility_calculation': 'eligibilityCalculation'
    }

    required_map = {
        'instrument_event_type': 'required',
        'supported_instrument_types': 'required',
        'supported_participation_types': 'required',
        'supported_election_types': 'required',
        'supported_template_fields': 'required',
        'eligibility_calculation': 'required'
    }

    def __init__(self, instrument_event_type=None, supported_instrument_types=None, supported_participation_types=None, supported_election_types=None, supported_template_fields=None, eligibility_calculation=None, local_vars_configuration=None):  # noqa: E501
        """TransactionTemplateSpecification - a model defined in OpenAPI"
        
        :param instrument_event_type:  (required)
        :type instrument_event_type: str
        :param supported_instrument_types:  (required)
        :type supported_instrument_types: list[str]
        :param supported_participation_types:  (required)
        :type supported_participation_types: list[str]
        :param supported_election_types:  (required)
        :type supported_election_types: list[lusid.ElectionSpecification]
        :param supported_template_fields:  (required)
        :type supported_template_fields: list[lusid.TemplateField]
        :param eligibility_calculation:  (required)
        :type eligibility_calculation: lusid.EligibilityCalculation

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_event_type = None
        self._supported_instrument_types = None
        self._supported_participation_types = None
        self._supported_election_types = None
        self._supported_template_fields = None
        self._eligibility_calculation = None
        self.discriminator = None

        self.instrument_event_type = instrument_event_type
        self.supported_instrument_types = supported_instrument_types
        self.supported_participation_types = supported_participation_types
        self.supported_election_types = supported_election_types
        self.supported_template_fields = supported_template_fields
        self.eligibility_calculation = eligibility_calculation

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this TransactionTemplateSpecification.  # noqa: E501


        :return: The instrument_event_type of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this TransactionTemplateSpecification.


        :param instrument_event_type: The instrument_event_type of this TransactionTemplateSpecification.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_type is not None and len(instrument_event_type) < 1):
            raise ValueError("Invalid value for `instrument_event_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_event_type = instrument_event_type

    @property
    def supported_instrument_types(self):
        """Gets the supported_instrument_types of this TransactionTemplateSpecification.  # noqa: E501


        :return: The supported_instrument_types of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_instrument_types

    @supported_instrument_types.setter
    def supported_instrument_types(self, supported_instrument_types):
        """Sets the supported_instrument_types of this TransactionTemplateSpecification.


        :param supported_instrument_types: The supported_instrument_types of this TransactionTemplateSpecification.  # noqa: E501
        :type supported_instrument_types: list[str]
        """
        if self.local_vars_configuration.client_side_validation and supported_instrument_types is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_instrument_types`, must not be `None`")  # noqa: E501

        self._supported_instrument_types = supported_instrument_types

    @property
    def supported_participation_types(self):
        """Gets the supported_participation_types of this TransactionTemplateSpecification.  # noqa: E501


        :return: The supported_participation_types of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_participation_types

    @supported_participation_types.setter
    def supported_participation_types(self, supported_participation_types):
        """Sets the supported_participation_types of this TransactionTemplateSpecification.


        :param supported_participation_types: The supported_participation_types of this TransactionTemplateSpecification.  # noqa: E501
        :type supported_participation_types: list[str]
        """
        if self.local_vars_configuration.client_side_validation and supported_participation_types is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_participation_types`, must not be `None`")  # noqa: E501

        self._supported_participation_types = supported_participation_types

    @property
    def supported_election_types(self):
        """Gets the supported_election_types of this TransactionTemplateSpecification.  # noqa: E501


        :return: The supported_election_types of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: list[lusid.ElectionSpecification]
        """
        return self._supported_election_types

    @supported_election_types.setter
    def supported_election_types(self, supported_election_types):
        """Sets the supported_election_types of this TransactionTemplateSpecification.


        :param supported_election_types: The supported_election_types of this TransactionTemplateSpecification.  # noqa: E501
        :type supported_election_types: list[lusid.ElectionSpecification]
        """
        if self.local_vars_configuration.client_side_validation and supported_election_types is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_election_types`, must not be `None`")  # noqa: E501

        self._supported_election_types = supported_election_types

    @property
    def supported_template_fields(self):
        """Gets the supported_template_fields of this TransactionTemplateSpecification.  # noqa: E501


        :return: The supported_template_fields of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: list[lusid.TemplateField]
        """
        return self._supported_template_fields

    @supported_template_fields.setter
    def supported_template_fields(self, supported_template_fields):
        """Sets the supported_template_fields of this TransactionTemplateSpecification.


        :param supported_template_fields: The supported_template_fields of this TransactionTemplateSpecification.  # noqa: E501
        :type supported_template_fields: list[lusid.TemplateField]
        """
        if self.local_vars_configuration.client_side_validation and supported_template_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_template_fields`, must not be `None`")  # noqa: E501

        self._supported_template_fields = supported_template_fields

    @property
    def eligibility_calculation(self):
        """Gets the eligibility_calculation of this TransactionTemplateSpecification.  # noqa: E501


        :return: The eligibility_calculation of this TransactionTemplateSpecification.  # noqa: E501
        :rtype: lusid.EligibilityCalculation
        """
        return self._eligibility_calculation

    @eligibility_calculation.setter
    def eligibility_calculation(self, eligibility_calculation):
        """Sets the eligibility_calculation of this TransactionTemplateSpecification.


        :param eligibility_calculation: The eligibility_calculation of this TransactionTemplateSpecification.  # noqa: E501
        :type eligibility_calculation: lusid.EligibilityCalculation
        """
        if self.local_vars_configuration.client_side_validation and eligibility_calculation is None:  # noqa: E501
            raise ValueError("Invalid value for `eligibility_calculation`, must not be `None`")  # noqa: E501

        self._eligibility_calculation = eligibility_calculation

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
        if not isinstance(other, TransactionTemplateSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionTemplateSpecification):
            return True

        return self.to_dict() != other.to_dict()
