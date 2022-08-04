# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4674
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


class CashFlowLineage(object):
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
        'instrument_type': 'str',
        'cash_flow_type': 'str',
        'instrument_id': 'str',
        'leg_id': 'str',
        'source_transaction_id': 'str',
        'pay_receive': 'str'
    }

    attribute_map = {
        'instrument_type': 'instrumentType',
        'cash_flow_type': 'cashFlowType',
        'instrument_id': 'instrumentId',
        'leg_id': 'legId',
        'source_transaction_id': 'sourceTransactionId',
        'pay_receive': 'payReceive'
    }

    required_map = {
        'instrument_type': 'optional',
        'cash_flow_type': 'optional',
        'instrument_id': 'optional',
        'leg_id': 'optional',
        'source_transaction_id': 'optional',
        'pay_receive': 'optional'
    }

    def __init__(self, instrument_type=None, cash_flow_type=None, instrument_id=None, leg_id=None, source_transaction_id=None, pay_receive=None, local_vars_configuration=None):  # noqa: E501
        """CashFlowLineage - a model defined in OpenAPI"
        
        :param instrument_type:  The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null.
        :type instrument_type: str
        :param cash_flow_type:  The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash]
        :type cash_flow_type: str
        :param instrument_id:  The LUID of the instrument to which the cash flow belongs to. When upserting this should be null.
        :type instrument_id: str
        :param leg_id:  The leg id to which the cash flow belongs to.
        :type leg_id: str
        :param source_transaction_id:  The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null
        :type source_transaction_id: str
        :param pay_receive:  Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable]
        :type pay_receive: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_type = None
        self._cash_flow_type = None
        self._instrument_id = None
        self._leg_id = None
        self._source_transaction_id = None
        self._pay_receive = None
        self.discriminator = None

        self.instrument_type = instrument_type
        self.cash_flow_type = cash_flow_type
        self.instrument_id = instrument_id
        self.leg_id = leg_id
        self.source_transaction_id = source_transaction_id
        self.pay_receive = pay_receive

    @property
    def instrument_type(self):
        """Gets the instrument_type of this CashFlowLineage.  # noqa: E501

        The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null.  # noqa: E501

        :return: The instrument_type of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this CashFlowLineage.

        The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null.  # noqa: E501

        :param instrument_type: The instrument_type of this CashFlowLineage.  # noqa: E501
        :type instrument_type: str
        """

        self._instrument_type = instrument_type

    @property
    def cash_flow_type(self):
        """Gets the cash_flow_type of this CashFlowLineage.  # noqa: E501

        The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash]  # noqa: E501

        :return: The cash_flow_type of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._cash_flow_type

    @cash_flow_type.setter
    def cash_flow_type(self, cash_flow_type):
        """Sets the cash_flow_type of this CashFlowLineage.

        The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash]  # noqa: E501

        :param cash_flow_type: The cash_flow_type of this CashFlowLineage.  # noqa: E501
        :type cash_flow_type: str
        """

        self._cash_flow_type = cash_flow_type

    @property
    def instrument_id(self):
        """Gets the instrument_id of this CashFlowLineage.  # noqa: E501

        The LUID of the instrument to which the cash flow belongs to. When upserting this should be null.  # noqa: E501

        :return: The instrument_id of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this CashFlowLineage.

        The LUID of the instrument to which the cash flow belongs to. When upserting this should be null.  # noqa: E501

        :param instrument_id: The instrument_id of this CashFlowLineage.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    @property
    def leg_id(self):
        """Gets the leg_id of this CashFlowLineage.  # noqa: E501

        The leg id to which the cash flow belongs to.  # noqa: E501

        :return: The leg_id of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._leg_id

    @leg_id.setter
    def leg_id(self, leg_id):
        """Sets the leg_id of this CashFlowLineage.

        The leg id to which the cash flow belongs to.  # noqa: E501

        :param leg_id: The leg_id of this CashFlowLineage.  # noqa: E501
        :type leg_id: str
        """

        self._leg_id = leg_id

    @property
    def source_transaction_id(self):
        """Gets the source_transaction_id of this CashFlowLineage.  # noqa: E501

        The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null  # noqa: E501

        :return: The source_transaction_id of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._source_transaction_id

    @source_transaction_id.setter
    def source_transaction_id(self, source_transaction_id):
        """Sets the source_transaction_id of this CashFlowLineage.

        The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null  # noqa: E501

        :param source_transaction_id: The source_transaction_id of this CashFlowLineage.  # noqa: E501
        :type source_transaction_id: str
        """

        self._source_transaction_id = source_transaction_id

    @property
    def pay_receive(self):
        """Gets the pay_receive of this CashFlowLineage.  # noqa: E501

        Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable]  # noqa: E501

        :return: The pay_receive of this CashFlowLineage.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this CashFlowLineage.

        Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable]  # noqa: E501

        :param pay_receive: The pay_receive of this CashFlowLineage.  # noqa: E501
        :type pay_receive: str
        """

        self._pay_receive = pay_receive

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
        if not isinstance(other, CashFlowLineage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashFlowLineage):
            return True

        return self.to_dict() != other.to_dict()
