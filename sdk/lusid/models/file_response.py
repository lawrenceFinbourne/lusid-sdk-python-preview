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


class FileResponse(object):
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
        'file_stream': 'Stream',
        'content_type': 'str',
        'downloaded_filename': 'str'
    }

    attribute_map = {
        'file_stream': 'fileStream',
        'content_type': 'contentType',
        'downloaded_filename': 'downloadedFilename'
    }

    required_map = {
        'file_stream': 'optional',
        'content_type': 'optional',
        'downloaded_filename': 'optional'
    }

    def __init__(self, file_stream=None, content_type=None, downloaded_filename=None, local_vars_configuration=None):  # noqa: E501
        """FileResponse - a model defined in OpenAPI"
        
        :param file_stream: 
        :type file_stream: lusid.Stream
        :param content_type: 
        :type content_type: str
        :param downloaded_filename: 
        :type downloaded_filename: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_stream = None
        self._content_type = None
        self._downloaded_filename = None
        self.discriminator = None

        if file_stream is not None:
            self.file_stream = file_stream
        self.content_type = content_type
        self.downloaded_filename = downloaded_filename

    @property
    def file_stream(self):
        """Gets the file_stream of this FileResponse.  # noqa: E501


        :return: The file_stream of this FileResponse.  # noqa: E501
        :rtype: lusid.Stream
        """
        return self._file_stream

    @file_stream.setter
    def file_stream(self, file_stream):
        """Sets the file_stream of this FileResponse.


        :param file_stream: The file_stream of this FileResponse.  # noqa: E501
        :type file_stream: lusid.Stream
        """

        self._file_stream = file_stream

    @property
    def content_type(self):
        """Gets the content_type of this FileResponse.  # noqa: E501


        :return: The content_type of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FileResponse.


        :param content_type: The content_type of this FileResponse.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def downloaded_filename(self):
        """Gets the downloaded_filename of this FileResponse.  # noqa: E501


        :return: The downloaded_filename of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._downloaded_filename

    @downloaded_filename.setter
    def downloaded_filename(self, downloaded_filename):
        """Sets the downloaded_filename of this FileResponse.


        :param downloaded_filename: The downloaded_filename of this FileResponse.  # noqa: E501
        :type downloaded_filename: str
        """

        self._downloaded_filename = downloaded_filename

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
        if not isinstance(other, FileResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileResponse):
            return True

        return self.to_dict() != other.to_dict()
