# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2721
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ContractForDifference(object):
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
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'code': 'str',
        'contract_size': 'float',
        'pay_ccy': 'str',
        'reference_rate': 'float',
        'type': 'str',
        'underlying_ccy': 'str',
        'underlying_identifier': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'code': 'code',
        'contract_size': 'contractSize',
        'pay_ccy': 'payCcy',
        'reference_rate': 'referenceRate',
        'type': 'type',
        'underlying_ccy': 'underlyingCcy',
        'underlying_identifier': 'underlyingIdentifier',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'code': 'required',
        'contract_size': 'required',
        'pay_ccy': 'required',
        'reference_rate': 'required',
        'type': 'required',
        'underlying_ccy': 'required',
        'underlying_identifier': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, code=None, contract_size=None, pay_ccy=None, reference_rate=None, type=None, underlying_ccy=None, underlying_identifier=None, instrument_type=None):  # noqa: E501
        """
        ContractForDifference - a model defined in OpenAPI

        :param start_date:  The start date of the CFD. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date (required)
        :type maturity_date: datetime
        :param code:  The code of the underlying. (required)
        :type code: str
        :param contract_size:  With an OTC we have the problem of multiple ways of booking a quantity.  e.g.  If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.  When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and  fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.  The logical effect of this is that  instrument clean price = contract size * quoted unit price  holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price  In calculating accrued interest the same should hold.  NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold. (required)
        :type contract_size: float
        :param pay_ccy:  The currency that this CFD pays out, this can be different to the UnderlyingCcy. (required)
        :type pay_ccy: str
        :param reference_rate:  The reference rate of the CFD, this can be set to 0 but not negative values. (required)
        :type reference_rate: float
        :param type:  The type of CFD.  Supported string (enumeration) values are: [Cash, Futures]. (required)
        :type type: str
        :param underlying_ccy:  The currency of the underlying (required)
        :type underlying_ccy: str
        :param underlying_identifier:  external market codes and identifiers for the CFD, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId]. (required)
        :type underlying_identifier: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket (required)
        :type instrument_type: str

        """  # noqa: E501

        self._start_date = None
        self._maturity_date = None
        self._code = None
        self._contract_size = None
        self._pay_ccy = None
        self._reference_rate = None
        self._type = None
        self._underlying_ccy = None
        self._underlying_identifier = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.code = code
        self.contract_size = contract_size
        self.pay_ccy = pay_ccy
        self.reference_rate = reference_rate
        self.type = type
        self.underlying_ccy = underlying_ccy
        self.underlying_identifier = underlying_identifier
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this ContractForDifference.  # noqa: E501

        The start date of the CFD.  # noqa: E501

        :return: The start_date of this ContractForDifference.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ContractForDifference.

        The start date of the CFD.  # noqa: E501

        :param start_date: The start_date of this ContractForDifference.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this ContractForDifference.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :return: The maturity_date of this ContractForDifference.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this ContractForDifference.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :param maturity_date: The maturity_date of this ContractForDifference.  # noqa: E501
        :type: datetime
        """
        if maturity_date is None:
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def code(self):
        """Gets the code of this ContractForDifference.  # noqa: E501

        The code of the underlying.  # noqa: E501

        :return: The code of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ContractForDifference.

        The code of the underlying.  # noqa: E501

        :param code: The code of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def contract_size(self):
        """Gets the contract_size of this ContractForDifference.  # noqa: E501

        With an OTC we have the problem of multiple ways of booking a quantity.  e.g.  If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.  When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and  fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.  The logical effect of this is that  instrument clean price = contract size * quoted unit price  holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price  In calculating accrued interest the same should hold.  NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold.  # noqa: E501

        :return: The contract_size of this ContractForDifference.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this ContractForDifference.

        With an OTC we have the problem of multiple ways of booking a quantity.  e.g.  If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.  When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and  fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.  The logical effect of this is that  instrument clean price = contract size * quoted unit price  holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price  In calculating accrued interest the same should hold.  NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold.  # noqa: E501

        :param contract_size: The contract_size of this ContractForDifference.  # noqa: E501
        :type: float
        """
        if contract_size is None:
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def pay_ccy(self):
        """Gets the pay_ccy of this ContractForDifference.  # noqa: E501

        The currency that this CFD pays out, this can be different to the UnderlyingCcy.  # noqa: E501

        :return: The pay_ccy of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._pay_ccy

    @pay_ccy.setter
    def pay_ccy(self, pay_ccy):
        """Sets the pay_ccy of this ContractForDifference.

        The currency that this CFD pays out, this can be different to the UnderlyingCcy.  # noqa: E501

        :param pay_ccy: The pay_ccy of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if pay_ccy is None:
            raise ValueError("Invalid value for `pay_ccy`, must not be `None`")  # noqa: E501

        self._pay_ccy = pay_ccy

    @property
    def reference_rate(self):
        """Gets the reference_rate of this ContractForDifference.  # noqa: E501

        The reference rate of the CFD, this can be set to 0 but not negative values.  # noqa: E501

        :return: The reference_rate of this ContractForDifference.  # noqa: E501
        :rtype: float
        """
        return self._reference_rate

    @reference_rate.setter
    def reference_rate(self, reference_rate):
        """Sets the reference_rate of this ContractForDifference.

        The reference rate of the CFD, this can be set to 0 but not negative values.  # noqa: E501

        :param reference_rate: The reference_rate of this ContractForDifference.  # noqa: E501
        :type: float
        """
        if reference_rate is None:
            raise ValueError("Invalid value for `reference_rate`, must not be `None`")  # noqa: E501

        self._reference_rate = reference_rate

    @property
    def type(self):
        """Gets the type of this ContractForDifference.  # noqa: E501

        The type of CFD.  Supported string (enumeration) values are: [Cash, Futures].  # noqa: E501

        :return: The type of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContractForDifference.

        The type of CFD.  Supported string (enumeration) values are: [Cash, Futures].  # noqa: E501

        :param type: The type of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def underlying_ccy(self):
        """Gets the underlying_ccy of this ContractForDifference.  # noqa: E501

        The currency of the underlying  # noqa: E501

        :return: The underlying_ccy of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._underlying_ccy

    @underlying_ccy.setter
    def underlying_ccy(self, underlying_ccy):
        """Sets the underlying_ccy of this ContractForDifference.

        The currency of the underlying  # noqa: E501

        :param underlying_ccy: The underlying_ccy of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if underlying_ccy is None:
            raise ValueError("Invalid value for `underlying_ccy`, must not be `None`")  # noqa: E501

        self._underlying_ccy = underlying_ccy

    @property
    def underlying_identifier(self):
        """Gets the underlying_identifier of this ContractForDifference.  # noqa: E501

        external market codes and identifiers for the CFD, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId].  # noqa: E501

        :return: The underlying_identifier of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._underlying_identifier

    @underlying_identifier.setter
    def underlying_identifier(self, underlying_identifier):
        """Sets the underlying_identifier of this ContractForDifference.

        external market codes and identifiers for the CFD, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId].  # noqa: E501

        :param underlying_identifier: The underlying_identifier of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if underlying_identifier is None:
            raise ValueError("Invalid value for `underlying_identifier`, must not be `None`")  # noqa: E501

        self._underlying_identifier = underlying_identifier

    @property
    def instrument_type(self):
        """Gets the instrument_type of this ContractForDifference.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket  # noqa: E501

        :return: The instrument_type of this ContractForDifference.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this ContractForDifference.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket  # noqa: E501

        :param instrument_type: The instrument_type of this ContractForDifference.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashflowLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CashSettled", "CdsIndex", "Basket"]  # noqa: E501
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, ContractForDifference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
