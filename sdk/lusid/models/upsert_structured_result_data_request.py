# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2333
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertStructuredResultDataRequest(object):
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
        'id': 'StructuredResultDataId',
        'data': 'StructuredResultData'
    }

    attribute_map = {
        'id': 'id',
        'data': 'data'
    }

    required_map = {
        'id': 'required',
        'data': 'optional'
    }

    def __init__(self, id=None, data=None):  # noqa: E501
        """
        UpsertStructuredResultDataRequest - a model defined in OpenAPI

        :param id:  (required)
        :type id: lusid.StructuredResultDataId
        :param data: 
        :type data: lusid.StructuredResultData

        """  # noqa: E501

        self._id = None
        self._data = None
        self.discriminator = None

        self.id = id
        if data is not None:
            self.data = data

    @property
    def id(self):
        """Gets the id of this UpsertStructuredResultDataRequest.  # noqa: E501


        :return: The id of this UpsertStructuredResultDataRequest.  # noqa: E501
        :rtype: StructuredResultDataId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpsertStructuredResultDataRequest.


        :param id: The id of this UpsertStructuredResultDataRequest.  # noqa: E501
        :type: StructuredResultDataId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def data(self):
        """Gets the data of this UpsertStructuredResultDataRequest.  # noqa: E501


        :return: The data of this UpsertStructuredResultDataRequest.  # noqa: E501
        :rtype: StructuredResultData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UpsertStructuredResultDataRequest.


        :param data: The data of this UpsertStructuredResultDataRequest.  # noqa: E501
        :type: StructuredResultData
        """

        self._data = data

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
        if not isinstance(other, UpsertStructuredResultDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
