# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.359
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


class InstrumentModels(object):
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
        'instrument_id': 'str',
        'supported_models': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'instrument_id': 'instrumentId',
        'supported_models': 'supportedModels',
        'links': 'links'
    }

    required_map = {
        'instrument_id': 'optional',
        'supported_models': 'optional',
        'links': 'optional'
    }

    def __init__(self, instrument_id=None, supported_models=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentModels - a model defined in OpenAPI"
        
        :param instrument_id:  The unique LUSID Instrument Identifier (LUID) of the instrument.
        :type instrument_id: str
        :param supported_models:  The pricing models supported by the instrument e.g. 'Discounting'.
        :type supported_models: list[str]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_id = None
        self._supported_models = None
        self._links = None
        self.discriminator = None

        self.instrument_id = instrument_id
        self.supported_models = supported_models
        self.links = links

    @property
    def instrument_id(self):
        """Gets the instrument_id of this InstrumentModels.  # noqa: E501

        The unique LUSID Instrument Identifier (LUID) of the instrument.  # noqa: E501

        :return: The instrument_id of this InstrumentModels.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this InstrumentModels.

        The unique LUSID Instrument Identifier (LUID) of the instrument.  # noqa: E501

        :param instrument_id: The instrument_id of this InstrumentModels.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    @property
    def supported_models(self):
        """Gets the supported_models of this InstrumentModels.  # noqa: E501

        The pricing models supported by the instrument e.g. 'Discounting'.  # noqa: E501

        :return: The supported_models of this InstrumentModels.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """Sets the supported_models of this InstrumentModels.

        The pricing models supported by the instrument e.g. 'Discounting'.  # noqa: E501

        :param supported_models: The supported_models of this InstrumentModels.  # noqa: E501
        :type supported_models: list[str]
        """

        self._supported_models = supported_models

    @property
    def links(self):
        """Gets the links of this InstrumentModels.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this InstrumentModels.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InstrumentModels.

        Collection of links.  # noqa: E501

        :param links: The links of this InstrumentModels.  # noqa: E501
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
        if not isinstance(other, InstrumentModels):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentModels):
            return True

        return self.to_dict() != other.to_dict()
