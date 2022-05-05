# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4303
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


class ReconciliationLine(object):
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
        'left': 'IDataRecord',
        'right': 'IDataRecord',
        'difference': 'IDataRecord',
        'result_comparison': 'IDataRecord'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'difference': 'difference',
        'result_comparison': 'resultComparison'
    }

    required_map = {
        'left': 'optional',
        'right': 'optional',
        'difference': 'optional',
        'result_comparison': 'optional'
    }

    def __init__(self, left=None, right=None, difference=None, result_comparison=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationLine - a model defined in OpenAPI"
        
        :param left: 
        :type left: lusid.IDataRecord
        :param right: 
        :type right: lusid.IDataRecord
        :param difference: 
        :type difference: lusid.IDataRecord
        :param result_comparison: 
        :type result_comparison: lusid.IDataRecord

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self._difference = None
        self._result_comparison = None
        self.discriminator = None

        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if difference is not None:
            self.difference = difference
        if result_comparison is not None:
            self.result_comparison = result_comparison

    @property
    def left(self):
        """Gets the left of this ReconciliationLine.  # noqa: E501


        :return: The left of this ReconciliationLine.  # noqa: E501
        :rtype: lusid.IDataRecord
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ReconciliationLine.


        :param left: The left of this ReconciliationLine.  # noqa: E501
        :type left: lusid.IDataRecord
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this ReconciliationLine.  # noqa: E501


        :return: The right of this ReconciliationLine.  # noqa: E501
        :rtype: lusid.IDataRecord
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ReconciliationLine.


        :param right: The right of this ReconciliationLine.  # noqa: E501
        :type right: lusid.IDataRecord
        """

        self._right = right

    @property
    def difference(self):
        """Gets the difference of this ReconciliationLine.  # noqa: E501


        :return: The difference of this ReconciliationLine.  # noqa: E501
        :rtype: lusid.IDataRecord
        """
        return self._difference

    @difference.setter
    def difference(self, difference):
        """Sets the difference of this ReconciliationLine.


        :param difference: The difference of this ReconciliationLine.  # noqa: E501
        :type difference: lusid.IDataRecord
        """

        self._difference = difference

    @property
    def result_comparison(self):
        """Gets the result_comparison of this ReconciliationLine.  # noqa: E501


        :return: The result_comparison of this ReconciliationLine.  # noqa: E501
        :rtype: lusid.IDataRecord
        """
        return self._result_comparison

    @result_comparison.setter
    def result_comparison(self, result_comparison):
        """Sets the result_comparison of this ReconciliationLine.


        :param result_comparison: The result_comparison of this ReconciliationLine.  # noqa: E501
        :type result_comparison: lusid.IDataRecord
        """

        self._result_comparison = result_comparison

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
        if not isinstance(other, ReconciliationLine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationLine):
            return True

        return self.to_dict() != other.to_dict()
