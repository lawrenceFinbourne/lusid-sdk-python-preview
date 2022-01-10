# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3875
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


class TransactionPropertyMapping(object):
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
        'property_key': 'str',
        'map_from': 'str',
        'set_to': 'object'
    }

    attribute_map = {
        'property_key': 'propertyKey',
        'map_from': 'mapFrom',
        'set_to': 'setTo'
    }

    required_map = {
        'property_key': 'required',
        'map_from': 'optional',
        'set_to': 'optional'
    }

    def __init__(self, property_key=None, map_from=None, set_to=None, local_vars_configuration=None):  # noqa: E501
        """TransactionPropertyMapping - a model defined in OpenAPI"
        
        :param property_key:  Uniquely identifies the property definiton and consists of a Domain, Scope and Code. (required)
        :type property_key: str
        :param map_from:  The Property Key of the Property to map from.
        :type map_from: str
        :param set_to:  A pointer to the Property being mapped from.
        :type set_to: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._property_key = None
        self._map_from = None
        self._set_to = None
        self.discriminator = None

        self.property_key = property_key
        self.map_from = map_from
        self.set_to = set_to

    @property
    def property_key(self):
        """Gets the property_key of this TransactionPropertyMapping.  # noqa: E501

        Uniquely identifies the property definiton and consists of a Domain, Scope and Code.  # noqa: E501

        :return: The property_key of this TransactionPropertyMapping.  # noqa: E501
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this TransactionPropertyMapping.

        Uniquely identifies the property definiton and consists of a Domain, Scope and Code.  # noqa: E501

        :param property_key: The property_key of this TransactionPropertyMapping.  # noqa: E501
        :type property_key: str
        """
        if self.local_vars_configuration.client_side_validation and property_key is None:  # noqa: E501
            raise ValueError("Invalid value for `property_key`, must not be `None`")  # noqa: E501

        self._property_key = property_key

    @property
    def map_from(self):
        """Gets the map_from of this TransactionPropertyMapping.  # noqa: E501

        The Property Key of the Property to map from.  # noqa: E501

        :return: The map_from of this TransactionPropertyMapping.  # noqa: E501
        :rtype: str
        """
        return self._map_from

    @map_from.setter
    def map_from(self, map_from):
        """Sets the map_from of this TransactionPropertyMapping.

        The Property Key of the Property to map from.  # noqa: E501

        :param map_from: The map_from of this TransactionPropertyMapping.  # noqa: E501
        :type map_from: str
        """

        self._map_from = map_from

    @property
    def set_to(self):
        """Gets the set_to of this TransactionPropertyMapping.  # noqa: E501

        A pointer to the Property being mapped from.  # noqa: E501

        :return: The set_to of this TransactionPropertyMapping.  # noqa: E501
        :rtype: object
        """
        return self._set_to

    @set_to.setter
    def set_to(self, set_to):
        """Sets the set_to of this TransactionPropertyMapping.

        A pointer to the Property being mapped from.  # noqa: E501

        :param set_to: The set_to of this TransactionPropertyMapping.  # noqa: E501
        :type set_to: object
        """

        self._set_to = set_to

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
        if not isinstance(other, TransactionPropertyMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionPropertyMapping):
            return True

        return self.to_dict() != other.to_dict()
