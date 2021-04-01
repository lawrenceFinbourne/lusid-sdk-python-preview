# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2815
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class IndustryClassificationScheme(object):
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
        'scheme_name': 'str',
        'scheme_id': 'str',
        'economic_sector': 'str',
        'business_sector': 'str',
        'industry': 'str',
        'industry_activity': 'str'
    }

    attribute_map = {
        'scheme_name': 'schemeName',
        'scheme_id': 'schemeId',
        'economic_sector': 'economicSector',
        'business_sector': 'businessSector',
        'industry': 'industry',
        'industry_activity': 'industryActivity'
    }

    required_map = {
        'scheme_name': 'required',
        'scheme_id': 'required',
        'economic_sector': 'required',
        'business_sector': 'required',
        'industry': 'required',
        'industry_activity': 'required'
    }

    def __init__(self, scheme_name=None, scheme_id=None, economic_sector=None, business_sector=None, industry=None, industry_activity=None):  # noqa: E501
        """
        IndustryClassificationScheme - a model defined in OpenAPI

        :param scheme_name:  The type of the industry classification scheme (TRBC, GICs, ICB) (required)
        :type scheme_name: str
        :param scheme_id:  Within the given scheme, the unique id that identifies this particular classification.  e.g. within \"TRCS\", 5010202011 identifies \"Oil Exploration \\amp; Production - Onshore\" within the Energy, fossil-fuels and Oil hierarchy. (required)
        :type scheme_id: str
        :param economic_sector:  Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which economic sector is the counterparty assigned to. This is Lvl 1 of that scheme (coarsest) (required)
        :type economic_sector: str
        :param business_sector:  Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 2 of that scheme (2nd coarsest)  e.g. Fossil Fuels within energy. (required)
        :type business_sector: str
        :param industry:  Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 3 of that scheme (3rd coarsest)  e.g. Coal or Oil within Fossil Fuels. (required)
        :type industry: str
        :param industry_activity:  Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 4 of the scheme (finest)  e.g. Petroleum Refining within Oil within Fossil Fuels. (required)
        :type industry_activity: str

        """  # noqa: E501

        self._scheme_name = None
        self._scheme_id = None
        self._economic_sector = None
        self._business_sector = None
        self._industry = None
        self._industry_activity = None
        self.discriminator = None

        self.scheme_name = scheme_name
        self.scheme_id = scheme_id
        self.economic_sector = economic_sector
        self.business_sector = business_sector
        self.industry = industry
        self.industry_activity = industry_activity

    @property
    def scheme_name(self):
        """Gets the scheme_name of this IndustryClassificationScheme.  # noqa: E501

        The type of the industry classification scheme (TRBC, GICs, ICB)  # noqa: E501

        :return: The scheme_name of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._scheme_name

    @scheme_name.setter
    def scheme_name(self, scheme_name):
        """Sets the scheme_name of this IndustryClassificationScheme.

        The type of the industry classification scheme (TRBC, GICs, ICB)  # noqa: E501

        :param scheme_name: The scheme_name of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if scheme_name is None:
            raise ValueError("Invalid value for `scheme_name`, must not be `None`")  # noqa: E501

        self._scheme_name = scheme_name

    @property
    def scheme_id(self):
        """Gets the scheme_id of this IndustryClassificationScheme.  # noqa: E501

        Within the given scheme, the unique id that identifies this particular classification.  e.g. within \"TRCS\", 5010202011 identifies \"Oil Exploration \\amp; Production - Onshore\" within the Energy, fossil-fuels and Oil hierarchy.  # noqa: E501

        :return: The scheme_id of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, scheme_id):
        """Sets the scheme_id of this IndustryClassificationScheme.

        Within the given scheme, the unique id that identifies this particular classification.  e.g. within \"TRCS\", 5010202011 identifies \"Oil Exploration \\amp; Production - Onshore\" within the Energy, fossil-fuels and Oil hierarchy.  # noqa: E501

        :param scheme_id: The scheme_id of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if scheme_id is None:
            raise ValueError("Invalid value for `scheme_id`, must not be `None`")  # noqa: E501

        self._scheme_id = scheme_id

    @property
    def economic_sector(self):
        """Gets the economic_sector of this IndustryClassificationScheme.  # noqa: E501

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which economic sector is the counterparty assigned to. This is Lvl 1 of that scheme (coarsest)  # noqa: E501

        :return: The economic_sector of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._economic_sector

    @economic_sector.setter
    def economic_sector(self, economic_sector):
        """Sets the economic_sector of this IndustryClassificationScheme.

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which economic sector is the counterparty assigned to. This is Lvl 1 of that scheme (coarsest)  # noqa: E501

        :param economic_sector: The economic_sector of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if economic_sector is None:
            raise ValueError("Invalid value for `economic_sector`, must not be `None`")  # noqa: E501

        self._economic_sector = economic_sector

    @property
    def business_sector(self):
        """Gets the business_sector of this IndustryClassificationScheme.  # noqa: E501

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 2 of that scheme (2nd coarsest)  e.g. Fossil Fuels within energy.  # noqa: E501

        :return: The business_sector of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._business_sector

    @business_sector.setter
    def business_sector(self, business_sector):
        """Sets the business_sector of this IndustryClassificationScheme.

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 2 of that scheme (2nd coarsest)  e.g. Fossil Fuels within energy.  # noqa: E501

        :param business_sector: The business_sector of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if business_sector is None:
            raise ValueError("Invalid value for `business_sector`, must not be `None`")  # noqa: E501

        self._business_sector = business_sector

    @property
    def industry(self):
        """Gets the industry of this IndustryClassificationScheme.  # noqa: E501

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 3 of that scheme (3rd coarsest)  e.g. Coal or Oil within Fossil Fuels.  # noqa: E501

        :return: The industry of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this IndustryClassificationScheme.

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 3 of that scheme (3rd coarsest)  e.g. Coal or Oil within Fossil Fuels.  # noqa: E501

        :param industry: The industry of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if industry is None:
            raise ValueError("Invalid value for `industry`, must not be `None`")  # noqa: E501

        self._industry = industry

    @property
    def industry_activity(self):
        """Gets the industry_activity of this IndustryClassificationScheme.  # noqa: E501

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 4 of the scheme (finest)  e.g. Petroleum Refining within Oil within Fossil Fuels.  # noqa: E501

        :return: The industry_activity of this IndustryClassificationScheme.  # noqa: E501
        :rtype: str
        """
        return self._industry_activity

    @industry_activity.setter
    def industry_activity(self, industry_activity):
        """Sets the industry_activity of this IndustryClassificationScheme.

        Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 4 of the scheme (finest)  e.g. Petroleum Refining within Oil within Fossil Fuels.  # noqa: E501

        :param industry_activity: The industry_activity of this IndustryClassificationScheme.  # noqa: E501
        :type: str
        """
        if industry_activity is None:
            raise ValueError("Invalid value for `industry_activity`, must not be `None`")  # noqa: E501

        self._industry_activity = industry_activity

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
        if not isinstance(other, IndustryClassificationScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
