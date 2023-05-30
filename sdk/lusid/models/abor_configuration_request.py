# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.210
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


class AborConfigurationRequest(object):
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
        'description': 'str',
        'name': 'str',
        'recipe_id': 'ResourceId',
        'chart_of_accounts_id': 'ResourceId',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'name': 'name',
        'recipe_id': 'recipeId',
        'chart_of_accounts_id': 'chartOfAccountsId',
        'properties': 'properties'
    }

    required_map = {
        'code': 'required',
        'description': 'optional',
        'name': 'optional',
        'recipe_id': 'optional',
        'chart_of_accounts_id': 'optional',
        'properties': 'optional'
    }

    def __init__(self, code=None, description=None, name=None, recipe_id=None, chart_of_accounts_id=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """AborConfigurationRequest - a model defined in OpenAPI"
        
        :param code:  The code given for the AborConfiguration. (required)
        :type code: str
        :param description:  The description for the AborConfiguration.
        :type description: str
        :param name:  The given name for the AborConfiguration.
        :type name: str
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param chart_of_accounts_id: 
        :type chart_of_accounts_id: lusid.ResourceId
        :param properties:  Properties to add to the AborConfiguration.
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._description = None
        self._name = None
        self._recipe_id = None
        self._chart_of_accounts_id = None
        self._properties = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.name = name
        if recipe_id is not None:
            self.recipe_id = recipe_id
        if chart_of_accounts_id is not None:
            self.chart_of_accounts_id = chart_of_accounts_id
        self.properties = properties

    @property
    def code(self):
        """Gets the code of this AborConfigurationRequest.  # noqa: E501

        The code given for the AborConfiguration.  # noqa: E501

        :return: The code of this AborConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AborConfigurationRequest.

        The code given for the AborConfiguration.  # noqa: E501

        :param code: The code of this AborConfigurationRequest.  # noqa: E501
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
    def description(self):
        """Gets the description of this AborConfigurationRequest.  # noqa: E501

        The description for the AborConfiguration.  # noqa: E501

        :return: The description of this AborConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AborConfigurationRequest.

        The description for the AborConfiguration.  # noqa: E501

        :param description: The description of this AborConfigurationRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this AborConfigurationRequest.  # noqa: E501

        The given name for the AborConfiguration.  # noqa: E501

        :return: The name of this AborConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AborConfigurationRequest.

        The given name for the AborConfiguration.  # noqa: E501

        :param name: The name of this AborConfigurationRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def recipe_id(self):
        """Gets the recipe_id of this AborConfigurationRequest.  # noqa: E501


        :return: The recipe_id of this AborConfigurationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this AborConfigurationRequest.


        :param recipe_id: The recipe_id of this AborConfigurationRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def chart_of_accounts_id(self):
        """Gets the chart_of_accounts_id of this AborConfigurationRequest.  # noqa: E501


        :return: The chart_of_accounts_id of this AborConfigurationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._chart_of_accounts_id

    @chart_of_accounts_id.setter
    def chart_of_accounts_id(self, chart_of_accounts_id):
        """Sets the chart_of_accounts_id of this AborConfigurationRequest.


        :param chart_of_accounts_id: The chart_of_accounts_id of this AborConfigurationRequest.  # noqa: E501
        :type chart_of_accounts_id: lusid.ResourceId
        """

        self._chart_of_accounts_id = chart_of_accounts_id

    @property
    def properties(self):
        """Gets the properties of this AborConfigurationRequest.  # noqa: E501

        Properties to add to the AborConfiguration.  # noqa: E501

        :return: The properties of this AborConfigurationRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AborConfigurationRequest.

        Properties to add to the AborConfiguration.  # noqa: E501

        :param properties: The properties of this AborConfigurationRequest.  # noqa: E501
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
        if not isinstance(other, AborConfigurationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AborConfigurationRequest):
            return True

        return self.to_dict() != other.to_dict()
