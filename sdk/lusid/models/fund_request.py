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


class FundRequest(object):
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
        'code': 'str',
        'display_name': 'str',
        'description': 'str',
        'abor_id': 'ResourceId',
        'share_class_instrument_scopes': 'list[str]',
        'share_class_instruments': 'list[InstrumentResolutionDetail]',
        'type': 'str',
        'inception_date': 'datetime',
        'decimal_places': 'int',
        'year_end_date': 'DayMonth',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'code': 'code',
        'display_name': 'displayName',
        'description': 'description',
        'abor_id': 'aborId',
        'share_class_instrument_scopes': 'shareClassInstrumentScopes',
        'share_class_instruments': 'shareClassInstruments',
        'type': 'type',
        'inception_date': 'inceptionDate',
        'decimal_places': 'decimalPlaces',
        'year_end_date': 'yearEndDate',
        'properties': 'properties'
    }

    required_map = {
        'code': 'required',
        'display_name': 'optional',
        'description': 'optional',
        'abor_id': 'required',
        'share_class_instrument_scopes': 'optional',
        'share_class_instruments': 'optional',
        'type': 'required',
        'inception_date': 'required',
        'decimal_places': 'optional',
        'year_end_date': 'required',
        'properties': 'optional'
    }

    def __init__(self, code=None, display_name=None, description=None, abor_id=None, share_class_instrument_scopes=None, share_class_instruments=None, type=None, inception_date=None, decimal_places=None, year_end_date=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """FundRequest - a model defined in OpenAPI"
        
        :param code:  The code given for the Fund. (required)
        :type code: str
        :param display_name:  The name of the Fund.
        :type display_name: str
        :param description:  A description for the Fund.
        :type description: str
        :param abor_id:  (required)
        :type abor_id: lusid.ResourceId
        :param share_class_instrument_scopes:  The scopes in which the instruments lie.
        :type share_class_instrument_scopes: list[str]
        :param share_class_instruments:  Details the user-provided instrument identifiers and the instrument resolved from them.
        :type share_class_instruments: list[lusid.InstrumentResolutionDetail]
        :param type:  The type of fund; 'Standalone', 'Master' or 'Feeder' (required)
        :type type: str
        :param inception_date:  Inception date of the Fund (required)
        :type inception_date: datetime
        :param decimal_places:  Number of decimal places for reporting
        :type decimal_places: int
        :param year_end_date:  (required)
        :type year_end_date: lusid.DayMonth
        :param properties:  A set of properties for the Fund.
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._display_name = None
        self._description = None
        self._abor_id = None
        self._share_class_instrument_scopes = None
        self._share_class_instruments = None
        self._type = None
        self._inception_date = None
        self._decimal_places = None
        self._year_end_date = None
        self._properties = None
        self.discriminator = None

        self.code = code
        self.display_name = display_name
        self.description = description
        self.abor_id = abor_id
        self.share_class_instrument_scopes = share_class_instrument_scopes
        self.share_class_instruments = share_class_instruments
        self.type = type
        self.inception_date = inception_date
        self.decimal_places = decimal_places
        self.year_end_date = year_end_date
        self.properties = properties

    @property
    def code(self):
        """Gets the code of this FundRequest.  # noqa: E501

        The code given for the Fund.  # noqa: E501

        :return: The code of this FundRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FundRequest.

        The code given for the Fund.  # noqa: E501

        :param code: The code of this FundRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def display_name(self):
        """Gets the display_name of this FundRequest.  # noqa: E501

        The name of the Fund.  # noqa: E501

        :return: The display_name of this FundRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FundRequest.

        The name of the Fund.  # noqa: E501

        :param display_name: The display_name of this FundRequest.  # noqa: E501
        :type display_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 256):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this FundRequest.  # noqa: E501

        A description for the Fund.  # noqa: E501

        :return: The description of this FundRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FundRequest.

        A description for the Fund.  # noqa: E501

        :param description: The description of this FundRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def abor_id(self):
        """Gets the abor_id of this FundRequest.  # noqa: E501


        :return: The abor_id of this FundRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._abor_id

    @abor_id.setter
    def abor_id(self, abor_id):
        """Sets the abor_id of this FundRequest.


        :param abor_id: The abor_id of this FundRequest.  # noqa: E501
        :type abor_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and abor_id is None:  # noqa: E501
            raise ValueError("Invalid value for `abor_id`, must not be `None`")  # noqa: E501

        self._abor_id = abor_id

    @property
    def share_class_instrument_scopes(self):
        """Gets the share_class_instrument_scopes of this FundRequest.  # noqa: E501

        The scopes in which the instruments lie.  # noqa: E501

        :return: The share_class_instrument_scopes of this FundRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._share_class_instrument_scopes

    @share_class_instrument_scopes.setter
    def share_class_instrument_scopes(self, share_class_instrument_scopes):
        """Sets the share_class_instrument_scopes of this FundRequest.

        The scopes in which the instruments lie.  # noqa: E501

        :param share_class_instrument_scopes: The share_class_instrument_scopes of this FundRequest.  # noqa: E501
        :type share_class_instrument_scopes: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                share_class_instrument_scopes is not None and len(share_class_instrument_scopes) > 1):
            raise ValueError("Invalid value for `share_class_instrument_scopes`, number of items must be less than or equal to `1`")  # noqa: E501

        self._share_class_instrument_scopes = share_class_instrument_scopes

    @property
    def share_class_instruments(self):
        """Gets the share_class_instruments of this FundRequest.  # noqa: E501

        Details the user-provided instrument identifiers and the instrument resolved from them.  # noqa: E501

        :return: The share_class_instruments of this FundRequest.  # noqa: E501
        :rtype: list[lusid.InstrumentResolutionDetail]
        """
        return self._share_class_instruments

    @share_class_instruments.setter
    def share_class_instruments(self, share_class_instruments):
        """Sets the share_class_instruments of this FundRequest.

        Details the user-provided instrument identifiers and the instrument resolved from them.  # noqa: E501

        :param share_class_instruments: The share_class_instruments of this FundRequest.  # noqa: E501
        :type share_class_instruments: list[lusid.InstrumentResolutionDetail]
        """

        self._share_class_instruments = share_class_instruments

    @property
    def type(self):
        """Gets the type of this FundRequest.  # noqa: E501

        The type of fund; 'Standalone', 'Master' or 'Feeder'  # noqa: E501

        :return: The type of this FundRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FundRequest.

        The type of fund; 'Standalone', 'Master' or 'Feeder'  # noqa: E501

        :param type: The type of this FundRequest.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def inception_date(self):
        """Gets the inception_date of this FundRequest.  # noqa: E501

        Inception date of the Fund  # noqa: E501

        :return: The inception_date of this FundRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._inception_date

    @inception_date.setter
    def inception_date(self, inception_date):
        """Sets the inception_date of this FundRequest.

        Inception date of the Fund  # noqa: E501

        :param inception_date: The inception_date of this FundRequest.  # noqa: E501
        :type inception_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and inception_date is None:  # noqa: E501
            raise ValueError("Invalid value for `inception_date`, must not be `None`")  # noqa: E501

        self._inception_date = inception_date

    @property
    def decimal_places(self):
        """Gets the decimal_places of this FundRequest.  # noqa: E501

        Number of decimal places for reporting  # noqa: E501

        :return: The decimal_places of this FundRequest.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this FundRequest.

        Number of decimal places for reporting  # noqa: E501

        :param decimal_places: The decimal_places of this FundRequest.  # noqa: E501
        :type decimal_places: int
        """
        if (self.local_vars_configuration.client_side_validation and
                decimal_places is not None and decimal_places > 30):  # noqa: E501
            raise ValueError("Invalid value for `decimal_places`, must be a value less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                decimal_places is not None and decimal_places < 0):  # noqa: E501
            raise ValueError("Invalid value for `decimal_places`, must be a value greater than or equal to `0`")  # noqa: E501

        self._decimal_places = decimal_places

    @property
    def year_end_date(self):
        """Gets the year_end_date of this FundRequest.  # noqa: E501


        :return: The year_end_date of this FundRequest.  # noqa: E501
        :rtype: lusid.DayMonth
        """
        return self._year_end_date

    @year_end_date.setter
    def year_end_date(self, year_end_date):
        """Sets the year_end_date of this FundRequest.


        :param year_end_date: The year_end_date of this FundRequest.  # noqa: E501
        :type year_end_date: lusid.DayMonth
        """
        if self.local_vars_configuration.client_side_validation and year_end_date is None:  # noqa: E501
            raise ValueError("Invalid value for `year_end_date`, must not be `None`")  # noqa: E501

        self._year_end_date = year_end_date

    @property
    def properties(self):
        """Gets the properties of this FundRequest.  # noqa: E501

        A set of properties for the Fund.  # noqa: E501

        :return: The properties of this FundRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this FundRequest.

        A set of properties for the Fund.  # noqa: E501

        :param properties: The properties of this FundRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

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
        if not isinstance(other, FundRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundRequest):
            return True

        return self.to_dict() != other.to_dict()
