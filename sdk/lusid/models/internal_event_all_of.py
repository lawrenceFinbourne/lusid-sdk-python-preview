# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4572
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


class InternalEventAllOf(object):
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
        'event_type': 'str',
        'event_category': 'str',
        'event_source': 'str',
        'anchor_date': 'datetime',
        'event_window_end': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'event_category': 'eventCategory',
        'event_source': 'eventSource',
        'anchor_date': 'anchorDate',
        'event_window_end': 'eventWindowEnd',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'event_type': 'optional',
        'event_category': 'optional',
        'event_source': 'optional',
        'anchor_date': 'optional',
        'event_window_end': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, event_type=None, event_category=None, event_source=None, anchor_date=None, event_window_end=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """InternalEventAllOf - a model defined in OpenAPI"
        
        :param event_type:  What category of event does this represent; instrument opening, closing, transition or other.
        :type event_type: str
        :param event_category:  What category of event does this represent; instrument opening, closing, transition or other.
        :type event_category: str
        :param event_source:  What is the event source, what causes it to happen.
        :type event_source: str
        :param anchor_date:  In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window.
        :type anchor_date: datetime
        :param event_window_end:  In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.
        :type event_window_end: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._event_category = None
        self._event_source = None
        self._anchor_date = None
        self._event_window_end = None
        self._instrument_event_type = None
        self.discriminator = None

        self.event_type = event_type
        self.event_category = event_category
        self.event_source = event_source
        if anchor_date is not None:
            self.anchor_date = anchor_date
        if event_window_end is not None:
            self.event_window_end = event_window_end
        self.instrument_event_type = instrument_event_type

    @property
    def event_type(self):
        """Gets the event_type of this InternalEventAllOf.  # noqa: E501

        What category of event does this represent; instrument opening, closing, transition or other.  # noqa: E501

        :return: The event_type of this InternalEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this InternalEventAllOf.

        What category of event does this represent; instrument opening, closing, transition or other.  # noqa: E501

        :param event_type: The event_type of this InternalEventAllOf.  # noqa: E501
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def event_category(self):
        """Gets the event_category of this InternalEventAllOf.  # noqa: E501

        What category of event does this represent; instrument opening, closing, transition or other.  # noqa: E501

        :return: The event_category of this InternalEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """Sets the event_category of this InternalEventAllOf.

        What category of event does this represent; instrument opening, closing, transition or other.  # noqa: E501

        :param event_category: The event_category of this InternalEventAllOf.  # noqa: E501
        :type event_category: str
        """

        self._event_category = event_category

    @property
    def event_source(self):
        """Gets the event_source of this InternalEventAllOf.  # noqa: E501

        What is the event source, what causes it to happen.  # noqa: E501

        :return: The event_source of this InternalEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this InternalEventAllOf.

        What is the event source, what causes it to happen.  # noqa: E501

        :param event_source: The event_source of this InternalEventAllOf.  # noqa: E501
        :type event_source: str
        """

        self._event_source = event_source

    @property
    def anchor_date(self):
        """Gets the anchor_date of this InternalEventAllOf.  # noqa: E501

        In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window.  # noqa: E501

        :return: The anchor_date of this InternalEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._anchor_date

    @anchor_date.setter
    def anchor_date(self, anchor_date):
        """Sets the anchor_date of this InternalEventAllOf.

        In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window.  # noqa: E501

        :param anchor_date: The anchor_date of this InternalEventAllOf.  # noqa: E501
        :type anchor_date: datetime
        """

        self._anchor_date = anchor_date

    @property
    def event_window_end(self):
        """Gets the event_window_end of this InternalEventAllOf.  # noqa: E501

        In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.  # noqa: E501

        :return: The event_window_end of this InternalEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._event_window_end

    @event_window_end.setter
    def event_window_end(self, event_window_end):
        """Sets the event_window_end of this InternalEventAllOf.

        In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.  # noqa: E501

        :param event_window_end: The event_window_end of this InternalEventAllOf.  # noqa: E501
        :type event_window_end: datetime
        """

        self._event_window_end = event_window_end

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this InternalEventAllOf.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent  # noqa: E501

        :return: The instrument_event_type of this InternalEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this InternalEventAllOf.

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this InternalEventAllOf.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InternalEvent", "CouponEvent", "OpenEvent", "CloseEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, InternalEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
