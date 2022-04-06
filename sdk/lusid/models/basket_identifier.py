# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4195
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


class BasketIdentifier(object):
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
        'index': 'str',
        'name': 'str',
        'region': 'str',
        'series_id': 'int'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'region': 'region',
        'series_id': 'seriesId'
    }

    required_map = {
        'index': 'required',
        'name': 'required',
        'region': 'required',
        'series_id': 'required'
    }

    def __init__(self, index=None, name=None, region=None, series_id=None, local_vars_configuration=None):  # noqa: E501
        """BasketIdentifier - a model defined in OpenAPI"
        
        :param index:  Index set, e.g. iTraxx or CDX. (required)
        :type index: str
        :param name:  The index name within the set, e.g. \"MAIN\" or \"Crossover\". (required)
        :type name: str
        :param region:  Applicable geographic country or region. Typically something like \"Europe\", \"Asia ex-Japan\", \"Japan\" or \"Australia\". (required)
        :type region: str
        :param series_id:  The series identifier. (required)
        :type series_id: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._name = None
        self._region = None
        self._series_id = None
        self.discriminator = None

        self.index = index
        self.name = name
        self.region = region
        self.series_id = series_id

    @property
    def index(self):
        """Gets the index of this BasketIdentifier.  # noqa: E501

        Index set, e.g. iTraxx or CDX.  # noqa: E501

        :return: The index of this BasketIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this BasketIdentifier.

        Index set, e.g. iTraxx or CDX.  # noqa: E501

        :param index: The index of this BasketIdentifier.  # noqa: E501
        :type index: str
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this BasketIdentifier.  # noqa: E501

        The index name within the set, e.g. \"MAIN\" or \"Crossover\".  # noqa: E501

        :return: The name of this BasketIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasketIdentifier.

        The index name within the set, e.g. \"MAIN\" or \"Crossover\".  # noqa: E501

        :param name: The name of this BasketIdentifier.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region(self):
        """Gets the region of this BasketIdentifier.  # noqa: E501

        Applicable geographic country or region. Typically something like \"Europe\", \"Asia ex-Japan\", \"Japan\" or \"Australia\".  # noqa: E501

        :return: The region of this BasketIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BasketIdentifier.

        Applicable geographic country or region. Typically something like \"Europe\", \"Asia ex-Japan\", \"Japan\" or \"Australia\".  # noqa: E501

        :param region: The region of this BasketIdentifier.  # noqa: E501
        :type region: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def series_id(self):
        """Gets the series_id of this BasketIdentifier.  # noqa: E501

        The series identifier.  # noqa: E501

        :return: The series_id of this BasketIdentifier.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this BasketIdentifier.

        The series identifier.  # noqa: E501

        :param series_id: The series_id of this BasketIdentifier.  # noqa: E501
        :type series_id: int
        """
        if self.local_vars_configuration.client_side_validation and series_id is None:  # noqa: E501
            raise ValueError("Invalid value for `series_id`, must not be `None`")  # noqa: E501

        self._series_id = series_id

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
        if not isinstance(other, BasketIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasketIdentifier):
            return True

        return self.to_dict() != other.to_dict()
