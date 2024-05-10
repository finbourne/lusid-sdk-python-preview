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


class InstrumentCapabilities(object):
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
        'model': 'str',
        'features': 'dict(str, str)',
        'supported_addresses': 'list[DescribedAddressKey]',
        'economic_dependencies': 'list[EconomicDependency]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'instrument_id': 'instrumentId',
        'model': 'model',
        'features': 'features',
        'supported_addresses': 'supportedAddresses',
        'economic_dependencies': 'economicDependencies',
        'links': 'links'
    }

    required_map = {
        'instrument_id': 'optional',
        'model': 'optional',
        'features': 'optional',
        'supported_addresses': 'optional',
        'economic_dependencies': 'optional',
        'links': 'optional'
    }

    def __init__(self, instrument_id=None, model=None, features=None, supported_addresses=None, economic_dependencies=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentCapabilities - a model defined in OpenAPI"
        
        :param instrument_id:  The Lusid instrument id for the instrument e.g. 'LUID_00003D4X'.
        :type instrument_id: str
        :param model:  The pricing model e.g. 'Discounting'.
        :type model: str
        :param features:  Features of the instrument describing its optionality, payoff type and more e.g. 'Instrument/Features/Exercise: American', 'Instrument/Features/Product: Option'
        :type features: dict(str, str)
        :param supported_addresses:  Queryable addresses supported by the model, e.g. 'Valuation/Pv', 'Valuation/Accrued'.
        :type supported_addresses: list[lusid.DescribedAddressKey]
        :param economic_dependencies:  Economic dependencies for the model, e.g. 'Fx:GBP.USD', 'Cash:GBP', 'Rates:GBP.GBPOIS'.
        :type economic_dependencies: list[lusid.EconomicDependency]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_id = None
        self._model = None
        self._features = None
        self._supported_addresses = None
        self._economic_dependencies = None
        self._links = None
        self.discriminator = None

        self.instrument_id = instrument_id
        self.model = model
        self.features = features
        self.supported_addresses = supported_addresses
        self.economic_dependencies = economic_dependencies
        self.links = links

    @property
    def instrument_id(self):
        """Gets the instrument_id of this InstrumentCapabilities.  # noqa: E501

        The Lusid instrument id for the instrument e.g. 'LUID_00003D4X'.  # noqa: E501

        :return: The instrument_id of this InstrumentCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this InstrumentCapabilities.

        The Lusid instrument id for the instrument e.g. 'LUID_00003D4X'.  # noqa: E501

        :param instrument_id: The instrument_id of this InstrumentCapabilities.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    @property
    def model(self):
        """Gets the model of this InstrumentCapabilities.  # noqa: E501

        The pricing model e.g. 'Discounting'.  # noqa: E501

        :return: The model of this InstrumentCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InstrumentCapabilities.

        The pricing model e.g. 'Discounting'.  # noqa: E501

        :param model: The model of this InstrumentCapabilities.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def features(self):
        """Gets the features of this InstrumentCapabilities.  # noqa: E501

        Features of the instrument describing its optionality, payoff type and more e.g. 'Instrument/Features/Exercise: American', 'Instrument/Features/Product: Option'  # noqa: E501

        :return: The features of this InstrumentCapabilities.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this InstrumentCapabilities.

        Features of the instrument describing its optionality, payoff type and more e.g. 'Instrument/Features/Exercise: American', 'Instrument/Features/Product: Option'  # noqa: E501

        :param features: The features of this InstrumentCapabilities.  # noqa: E501
        :type features: dict(str, str)
        """

        self._features = features

    @property
    def supported_addresses(self):
        """Gets the supported_addresses of this InstrumentCapabilities.  # noqa: E501

        Queryable addresses supported by the model, e.g. 'Valuation/Pv', 'Valuation/Accrued'.  # noqa: E501

        :return: The supported_addresses of this InstrumentCapabilities.  # noqa: E501
        :rtype: list[lusid.DescribedAddressKey]
        """
        return self._supported_addresses

    @supported_addresses.setter
    def supported_addresses(self, supported_addresses):
        """Sets the supported_addresses of this InstrumentCapabilities.

        Queryable addresses supported by the model, e.g. 'Valuation/Pv', 'Valuation/Accrued'.  # noqa: E501

        :param supported_addresses: The supported_addresses of this InstrumentCapabilities.  # noqa: E501
        :type supported_addresses: list[lusid.DescribedAddressKey]
        """

        self._supported_addresses = supported_addresses

    @property
    def economic_dependencies(self):
        """Gets the economic_dependencies of this InstrumentCapabilities.  # noqa: E501

        Economic dependencies for the model, e.g. 'Fx:GBP.USD', 'Cash:GBP', 'Rates:GBP.GBPOIS'.  # noqa: E501

        :return: The economic_dependencies of this InstrumentCapabilities.  # noqa: E501
        :rtype: list[lusid.EconomicDependency]
        """
        return self._economic_dependencies

    @economic_dependencies.setter
    def economic_dependencies(self, economic_dependencies):
        """Sets the economic_dependencies of this InstrumentCapabilities.

        Economic dependencies for the model, e.g. 'Fx:GBP.USD', 'Cash:GBP', 'Rates:GBP.GBPOIS'.  # noqa: E501

        :param economic_dependencies: The economic_dependencies of this InstrumentCapabilities.  # noqa: E501
        :type economic_dependencies: list[lusid.EconomicDependency]
        """

        self._economic_dependencies = economic_dependencies

    @property
    def links(self):
        """Gets the links of this InstrumentCapabilities.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this InstrumentCapabilities.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InstrumentCapabilities.

        Collection of links.  # noqa: E501

        :param links: The links of this InstrumentCapabilities.  # noqa: E501
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
        if not isinstance(other, InstrumentCapabilities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentCapabilities):
            return True

        return self.to_dict() != other.to_dict()
