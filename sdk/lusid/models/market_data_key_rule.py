# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2337
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MarketDataKeyRule(object):
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
        'key': 'str',
        'supplier': 'str',
        'data_scope': 'str',
        'quote_type': 'str',
        'field': 'str',
        'quote_interval': 'str',
        'as_at': 'datetime',
        'price_source': 'str',
        'mask': 'str'
    }

    attribute_map = {
        'key': 'key',
        'supplier': 'supplier',
        'data_scope': 'dataScope',
        'quote_type': 'quoteType',
        'field': 'field',
        'quote_interval': 'quoteInterval',
        'as_at': 'asAt',
        'price_source': 'priceSource',
        'mask': 'mask'
    }

    required_map = {
        'key': 'required',
        'supplier': 'required',
        'data_scope': 'required',
        'quote_type': 'required',
        'field': 'required',
        'quote_interval': 'optional',
        'as_at': 'optional',
        'price_source': 'optional',
        'mask': 'optional'
    }

    def __init__(self, key=None, supplier=None, data_scope=None, quote_type=None, field=None, quote_interval=None, as_at=None, price_source=None, mask=None):  # noqa: E501
        """
        MarketDataKeyRule - a model defined in OpenAPI

        :param key:  The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*) (required)
        :type key: str
        :param supplier:  The market data supplier (where the data comes from) (required)
        :type supplier: str
        :param data_scope:  The scope in which the data should be found when using this rule. (required)
        :type data_scope: str
        :param quote_type:  The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront (required)
        :type quote_type: str
        :param field:  The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId (required)
        :type field: str
        :param quote_interval:  Shorthand for the time interval used to select market data.
        :type quote_interval: str
        :param as_at:  The AsAt predicate specification.
        :type as_at: datetime
        :param price_source:  The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote
        :type price_source: str
        :param mask:  Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.
        :type mask: str

        """  # noqa: E501

        self._key = None
        self._supplier = None
        self._data_scope = None
        self._quote_type = None
        self._field = None
        self._quote_interval = None
        self._as_at = None
        self._price_source = None
        self._mask = None
        self.discriminator = None

        self.key = key
        self.supplier = supplier
        self.data_scope = data_scope
        self.quote_type = quote_type
        self.field = field
        self.quote_interval = quote_interval
        self.as_at = as_at
        self.price_source = price_source
        self.mask = mask

    @property
    def key(self):
        """Gets the key of this MarketDataKeyRule.  # noqa: E501

        The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*)  # noqa: E501

        :return: The key of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MarketDataKeyRule.

        The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*)  # noqa: E501

        :param key: The key of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def supplier(self):
        """Gets the supplier of this MarketDataKeyRule.  # noqa: E501

        The market data supplier (where the data comes from)  # noqa: E501

        :return: The supplier of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this MarketDataKeyRule.

        The market data supplier (where the data comes from)  # noqa: E501

        :param supplier: The supplier of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """
        if supplier is None:
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501

        self._supplier = supplier

    @property
    def data_scope(self):
        """Gets the data_scope of this MarketDataKeyRule.  # noqa: E501

        The scope in which the data should be found when using this rule.  # noqa: E501

        :return: The data_scope of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._data_scope

    @data_scope.setter
    def data_scope(self, data_scope):
        """Sets the data_scope of this MarketDataKeyRule.

        The scope in which the data should be found when using this rule.  # noqa: E501

        :param data_scope: The data_scope of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """
        if data_scope is None:
            raise ValueError("Invalid value for `data_scope`, must not be `None`")  # noqa: E501

        self._data_scope = data_scope

    @property
    def quote_type(self):
        """Gets the quote_type of this MarketDataKeyRule.  # noqa: E501

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront  # noqa: E501

        :return: The quote_type of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type):
        """Sets the quote_type of this MarketDataKeyRule.

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront  # noqa: E501

        :param quote_type: The quote_type of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """
        if quote_type is None:
            raise ValueError("Invalid value for `quote_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Price", "Spread", "Rate", "LogNormalVol", "NormalVol", "ParSpread", "IsdaSpread", "Upfront"]  # noqa: E501
        if quote_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quote_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_type, allowed_values)
            )

        self._quote_type = quote_type

    @property
    def field(self):
        """Gets the field of this MarketDataKeyRule.  # noqa: E501

        The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId  # noqa: E501

        :return: The field of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this MarketDataKeyRule.

        The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId  # noqa: E501

        :param field: The field of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def quote_interval(self):
        """Gets the quote_interval of this MarketDataKeyRule.  # noqa: E501

        Shorthand for the time interval used to select market data.  # noqa: E501

        :return: The quote_interval of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._quote_interval

    @quote_interval.setter
    def quote_interval(self, quote_interval):
        """Sets the quote_interval of this MarketDataKeyRule.

        Shorthand for the time interval used to select market data.  # noqa: E501

        :param quote_interval: The quote_interval of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """

        self._quote_interval = quote_interval

    @property
    def as_at(self):
        """Gets the as_at of this MarketDataKeyRule.  # noqa: E501

        The AsAt predicate specification.  # noqa: E501

        :return: The as_at of this MarketDataKeyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this MarketDataKeyRule.

        The AsAt predicate specification.  # noqa: E501

        :param as_at: The as_at of this MarketDataKeyRule.  # noqa: E501
        :type: datetime
        """

        self._as_at = as_at

    @property
    def price_source(self):
        """Gets the price_source of this MarketDataKeyRule.  # noqa: E501

        The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote  # noqa: E501

        :return: The price_source of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._price_source

    @price_source.setter
    def price_source(self, price_source):
        """Sets the price_source of this MarketDataKeyRule.

        The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote  # noqa: E501

        :param price_source: The price_source of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """

        self._price_source = price_source

    @property
    def mask(self):
        """Gets the mask of this MarketDataKeyRule.  # noqa: E501

        Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.  # noqa: E501

        :return: The mask of this MarketDataKeyRule.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this MarketDataKeyRule.

        Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve 'EUR.*' will replace the resolve MarketAsset 'GBP/12M', 'GBP/3M' with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule.  # noqa: E501

        :param mask: The mask of this MarketDataKeyRule.  # noqa: E501
        :type: str
        """

        self._mask = mask

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
        if not isinstance(other, MarketDataKeyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
