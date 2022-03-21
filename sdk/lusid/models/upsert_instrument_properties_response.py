# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4128
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


class UpsertInstrumentPropertiesResponse(object):
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
        'as_at_date': 'datetime',
        'links': 'list[Link]'
    }

    attribute_map = {
        'as_at_date': 'asAtDate',
        'links': 'links'
    }

    required_map = {
        'as_at_date': 'required',
        'links': 'optional'
    }

    def __init__(self, as_at_date=None, links=None, local_vars_configuration=None):  # noqa: E501
        """UpsertInstrumentPropertiesResponse - a model defined in OpenAPI"
        
        :param as_at_date:  The as-at datetime at which properties were created or updated. (required)
        :type as_at_date: datetime
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at_date = None
        self._links = None
        self.discriminator = None

        self.as_at_date = as_at_date
        self.links = links

    @property
    def as_at_date(self):
        """Gets the as_at_date of this UpsertInstrumentPropertiesResponse.  # noqa: E501

        The as-at datetime at which properties were created or updated.  # noqa: E501

        :return: The as_at_date of this UpsertInstrumentPropertiesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_date

    @as_at_date.setter
    def as_at_date(self, as_at_date):
        """Sets the as_at_date of this UpsertInstrumentPropertiesResponse.

        The as-at datetime at which properties were created or updated.  # noqa: E501

        :param as_at_date: The as_at_date of this UpsertInstrumentPropertiesResponse.  # noqa: E501
        :type as_at_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and as_at_date is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at_date`, must not be `None`")  # noqa: E501

        self._as_at_date = as_at_date

    @property
    def links(self):
        """Gets the links of this UpsertInstrumentPropertiesResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this UpsertInstrumentPropertiesResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpsertInstrumentPropertiesResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this UpsertInstrumentPropertiesResponse.  # noqa: E501
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
        if not isinstance(other, UpsertInstrumentPropertiesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertInstrumentPropertiesResponse):
            return True

        return self.to_dict() != other.to_dict()
