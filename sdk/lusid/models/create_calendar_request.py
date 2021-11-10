# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3705
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


class CreateCalendarRequest(object):
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
        'calendar_id': 'ResourceId',
        'calendar_type': 'str',
        'weekend_mask': 'WeekendMask',
        'source_provider': 'str',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'calendar_id': 'calendarId',
        'calendar_type': 'calendarType',
        'weekend_mask': 'weekendMask',
        'source_provider': 'sourceProvider',
        'properties': 'properties'
    }

    required_map = {
        'calendar_id': 'required',
        'calendar_type': 'required',
        'weekend_mask': 'required',
        'source_provider': 'required',
        'properties': 'optional'
    }

    def __init__(self, calendar_id=None, calendar_type=None, weekend_mask=None, source_provider=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """CreateCalendarRequest - a model defined in OpenAPI"
        
        :param calendar_id:  (required)
        :type calendar_id: lusid.ResourceId
        :param calendar_type:  (required)
        :type calendar_type: str
        :param weekend_mask:  (required)
        :type weekend_mask: lusid.WeekendMask
        :param source_provider:  (required)
        :type source_provider: str
        :param properties: 
        :type properties: list[lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._calendar_id = None
        self._calendar_type = None
        self._weekend_mask = None
        self._source_provider = None
        self._properties = None
        self.discriminator = None

        self.calendar_id = calendar_id
        self.calendar_type = calendar_type
        self.weekend_mask = weekend_mask
        self.source_provider = source_provider
        self.properties = properties

    @property
    def calendar_id(self):
        """Gets the calendar_id of this CreateCalendarRequest.  # noqa: E501


        :return: The calendar_id of this CreateCalendarRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this CreateCalendarRequest.


        :param calendar_id: The calendar_id of this CreateCalendarRequest.  # noqa: E501
        :type calendar_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and calendar_id is None:  # noqa: E501
            raise ValueError("Invalid value for `calendar_id`, must not be `None`")  # noqa: E501

        self._calendar_id = calendar_id

    @property
    def calendar_type(self):
        """Gets the calendar_type of this CreateCalendarRequest.  # noqa: E501


        :return: The calendar_type of this CreateCalendarRequest.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this CreateCalendarRequest.


        :param calendar_type: The calendar_type of this CreateCalendarRequest.  # noqa: E501
        :type calendar_type: str
        """
        if self.local_vars_configuration.client_side_validation and calendar_type is None:  # noqa: E501
            raise ValueError("Invalid value for `calendar_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calendar_type is not None and len(calendar_type) > 256):
            raise ValueError("Invalid value for `calendar_type`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calendar_type is not None and len(calendar_type) < 1):
            raise ValueError("Invalid value for `calendar_type`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calendar_type is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', calendar_type)):  # noqa: E501
            raise ValueError(r"Invalid value for `calendar_type`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._calendar_type = calendar_type

    @property
    def weekend_mask(self):
        """Gets the weekend_mask of this CreateCalendarRequest.  # noqa: E501


        :return: The weekend_mask of this CreateCalendarRequest.  # noqa: E501
        :rtype: lusid.WeekendMask
        """
        return self._weekend_mask

    @weekend_mask.setter
    def weekend_mask(self, weekend_mask):
        """Sets the weekend_mask of this CreateCalendarRequest.


        :param weekend_mask: The weekend_mask of this CreateCalendarRequest.  # noqa: E501
        :type weekend_mask: lusid.WeekendMask
        """
        if self.local_vars_configuration.client_side_validation and weekend_mask is None:  # noqa: E501
            raise ValueError("Invalid value for `weekend_mask`, must not be `None`")  # noqa: E501

        self._weekend_mask = weekend_mask

    @property
    def source_provider(self):
        """Gets the source_provider of this CreateCalendarRequest.  # noqa: E501


        :return: The source_provider of this CreateCalendarRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_provider

    @source_provider.setter
    def source_provider(self, source_provider):
        """Sets the source_provider of this CreateCalendarRequest.


        :param source_provider: The source_provider of this CreateCalendarRequest.  # noqa: E501
        :type source_provider: str
        """
        if self.local_vars_configuration.client_side_validation and source_provider is None:  # noqa: E501
            raise ValueError("Invalid value for `source_provider`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_provider is not None and len(source_provider) > 50):
            raise ValueError("Invalid value for `source_provider`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_provider is not None and len(source_provider) < 0):
            raise ValueError("Invalid value for `source_provider`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_provider is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', source_provider)):  # noqa: E501
            raise ValueError(r"Invalid value for `source_provider`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._source_provider = source_provider

    @property
    def properties(self):
        """Gets the properties of this CreateCalendarRequest.  # noqa: E501


        :return: The properties of this CreateCalendarRequest.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateCalendarRequest.


        :param properties: The properties of this CreateCalendarRequest.  # noqa: E501
        :type properties: list[lusid.ModelProperty]
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
        if not isinstance(other, CreateCalendarRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCalendarRequest):
            return True

        return self.to_dict() != other.to_dict()
