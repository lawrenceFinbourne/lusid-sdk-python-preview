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


class OrderGraphBlock(object):
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
        'block': 'Block',
        'order_ids': 'list[ResourceId]',
        'placement_ids': 'list[ResourceId]',
        'allocation_ids': 'list[ResourceId]',
        'execution_ids': 'list[ResourceId]',
        'ordered': 'OrderGraphBlockOrderSynopsis',
        'placed': 'OrderGraphBlockPlacementSynopsis',
        'executed': 'OrderGraphBlockExecutionSynopsis',
        'allocated': 'OrderGraphBlockAllocationSynopsis',
        'derived_state': 'str',
        'derived_compliance_state': 'str'
    }

    attribute_map = {
        'block': 'block',
        'order_ids': 'orderIds',
        'placement_ids': 'placementIds',
        'allocation_ids': 'allocationIds',
        'execution_ids': 'executionIds',
        'ordered': 'ordered',
        'placed': 'placed',
        'executed': 'executed',
        'allocated': 'allocated',
        'derived_state': 'derivedState',
        'derived_compliance_state': 'derivedComplianceState'
    }

    required_map = {
        'block': 'required',
        'order_ids': 'required',
        'placement_ids': 'required',
        'allocation_ids': 'required',
        'execution_ids': 'required',
        'ordered': 'required',
        'placed': 'required',
        'executed': 'required',
        'allocated': 'required',
        'derived_state': 'required',
        'derived_compliance_state': 'required'
    }

    def __init__(self, block=None, order_ids=None, placement_ids=None, allocation_ids=None, execution_ids=None, ordered=None, placed=None, executed=None, allocated=None, derived_state=None, derived_compliance_state=None, local_vars_configuration=None):  # noqa: E501
        """OrderGraphBlock - a model defined in OpenAPI"
        
        :param block:  (required)
        :type block: lusid.Block
        :param order_ids:  Identifiers for all the orders in this block - DEPRECATED: see Ordered. (required)
        :type order_ids: list[lusid.ResourceId]
        :param placement_ids:  Identifiers of all placements for the block - DEPRECATED: see Placed. (required)
        :type placement_ids: list[lusid.ResourceId]
        :param allocation_ids:  Identifiers for all allocations of placements to orders in the block - DEPRECATED: see Allocated. (required)
        :type allocation_ids: list[lusid.ResourceId]
        :param execution_ids:  Identifiers of all executions against placements in the block - DEPRECATED: see Executed. (required)
        :type execution_ids: list[lusid.ResourceId]
        :param ordered:  (required)
        :type ordered: lusid.OrderGraphBlockOrderSynopsis
        :param placed:  (required)
        :type placed: lusid.OrderGraphBlockPlacementSynopsis
        :param executed:  (required)
        :type executed: lusid.OrderGraphBlockExecutionSynopsis
        :param allocated:  (required)
        :type allocated: lusid.OrderGraphBlockAllocationSynopsis
        :param derived_state:  A simple description of the overall state of a block. (required)
        :type derived_state: str
        :param derived_compliance_state:  The overall compliance state of a block, derived from the block's orders. Possible values are Pending, Failed, 'Manually approved' and Passed. (required)
        :type derived_compliance_state: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._block = None
        self._order_ids = None
        self._placement_ids = None
        self._allocation_ids = None
        self._execution_ids = None
        self._ordered = None
        self._placed = None
        self._executed = None
        self._allocated = None
        self._derived_state = None
        self._derived_compliance_state = None
        self.discriminator = None

        self.block = block
        self.order_ids = order_ids
        self.placement_ids = placement_ids
        self.allocation_ids = allocation_ids
        self.execution_ids = execution_ids
        self.ordered = ordered
        self.placed = placed
        self.executed = executed
        self.allocated = allocated
        self.derived_state = derived_state
        self.derived_compliance_state = derived_compliance_state

    @property
    def block(self):
        """Gets the block of this OrderGraphBlock.  # noqa: E501


        :return: The block of this OrderGraphBlock.  # noqa: E501
        :rtype: lusid.Block
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this OrderGraphBlock.


        :param block: The block of this OrderGraphBlock.  # noqa: E501
        :type block: lusid.Block
        """
        if self.local_vars_configuration.client_side_validation and block is None:  # noqa: E501
            raise ValueError("Invalid value for `block`, must not be `None`")  # noqa: E501

        self._block = block

    @property
    def order_ids(self):
        """Gets the order_ids of this OrderGraphBlock.  # noqa: E501

        Identifiers for all the orders in this block - DEPRECATED: see Ordered.  # noqa: E501

        :return: The order_ids of this OrderGraphBlock.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this OrderGraphBlock.

        Identifiers for all the orders in this block - DEPRECATED: see Ordered.  # noqa: E501

        :param order_ids: The order_ids of this OrderGraphBlock.  # noqa: E501
        :type order_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and order_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `order_ids`, must not be `None`")  # noqa: E501

        self._order_ids = order_ids

    @property
    def placement_ids(self):
        """Gets the placement_ids of this OrderGraphBlock.  # noqa: E501

        Identifiers of all placements for the block - DEPRECATED: see Placed.  # noqa: E501

        :return: The placement_ids of this OrderGraphBlock.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._placement_ids

    @placement_ids.setter
    def placement_ids(self, placement_ids):
        """Sets the placement_ids of this OrderGraphBlock.

        Identifiers of all placements for the block - DEPRECATED: see Placed.  # noqa: E501

        :param placement_ids: The placement_ids of this OrderGraphBlock.  # noqa: E501
        :type placement_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and placement_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `placement_ids`, must not be `None`")  # noqa: E501

        self._placement_ids = placement_ids

    @property
    def allocation_ids(self):
        """Gets the allocation_ids of this OrderGraphBlock.  # noqa: E501

        Identifiers for all allocations of placements to orders in the block - DEPRECATED: see Allocated.  # noqa: E501

        :return: The allocation_ids of this OrderGraphBlock.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._allocation_ids

    @allocation_ids.setter
    def allocation_ids(self, allocation_ids):
        """Sets the allocation_ids of this OrderGraphBlock.

        Identifiers for all allocations of placements to orders in the block - DEPRECATED: see Allocated.  # noqa: E501

        :param allocation_ids: The allocation_ids of this OrderGraphBlock.  # noqa: E501
        :type allocation_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and allocation_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `allocation_ids`, must not be `None`")  # noqa: E501

        self._allocation_ids = allocation_ids

    @property
    def execution_ids(self):
        """Gets the execution_ids of this OrderGraphBlock.  # noqa: E501

        Identifiers of all executions against placements in the block - DEPRECATED: see Executed.  # noqa: E501

        :return: The execution_ids of this OrderGraphBlock.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._execution_ids

    @execution_ids.setter
    def execution_ids(self, execution_ids):
        """Sets the execution_ids of this OrderGraphBlock.

        Identifiers of all executions against placements in the block - DEPRECATED: see Executed.  # noqa: E501

        :param execution_ids: The execution_ids of this OrderGraphBlock.  # noqa: E501
        :type execution_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and execution_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `execution_ids`, must not be `None`")  # noqa: E501

        self._execution_ids = execution_ids

    @property
    def ordered(self):
        """Gets the ordered of this OrderGraphBlock.  # noqa: E501


        :return: The ordered of this OrderGraphBlock.  # noqa: E501
        :rtype: lusid.OrderGraphBlockOrderSynopsis
        """
        return self._ordered

    @ordered.setter
    def ordered(self, ordered):
        """Sets the ordered of this OrderGraphBlock.


        :param ordered: The ordered of this OrderGraphBlock.  # noqa: E501
        :type ordered: lusid.OrderGraphBlockOrderSynopsis
        """
        if self.local_vars_configuration.client_side_validation and ordered is None:  # noqa: E501
            raise ValueError("Invalid value for `ordered`, must not be `None`")  # noqa: E501

        self._ordered = ordered

    @property
    def placed(self):
        """Gets the placed of this OrderGraphBlock.  # noqa: E501


        :return: The placed of this OrderGraphBlock.  # noqa: E501
        :rtype: lusid.OrderGraphBlockPlacementSynopsis
        """
        return self._placed

    @placed.setter
    def placed(self, placed):
        """Sets the placed of this OrderGraphBlock.


        :param placed: The placed of this OrderGraphBlock.  # noqa: E501
        :type placed: lusid.OrderGraphBlockPlacementSynopsis
        """
        if self.local_vars_configuration.client_side_validation and placed is None:  # noqa: E501
            raise ValueError("Invalid value for `placed`, must not be `None`")  # noqa: E501

        self._placed = placed

    @property
    def executed(self):
        """Gets the executed of this OrderGraphBlock.  # noqa: E501


        :return: The executed of this OrderGraphBlock.  # noqa: E501
        :rtype: lusid.OrderGraphBlockExecutionSynopsis
        """
        return self._executed

    @executed.setter
    def executed(self, executed):
        """Sets the executed of this OrderGraphBlock.


        :param executed: The executed of this OrderGraphBlock.  # noqa: E501
        :type executed: lusid.OrderGraphBlockExecutionSynopsis
        """
        if self.local_vars_configuration.client_side_validation and executed is None:  # noqa: E501
            raise ValueError("Invalid value for `executed`, must not be `None`")  # noqa: E501

        self._executed = executed

    @property
    def allocated(self):
        """Gets the allocated of this OrderGraphBlock.  # noqa: E501


        :return: The allocated of this OrderGraphBlock.  # noqa: E501
        :rtype: lusid.OrderGraphBlockAllocationSynopsis
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this OrderGraphBlock.


        :param allocated: The allocated of this OrderGraphBlock.  # noqa: E501
        :type allocated: lusid.OrderGraphBlockAllocationSynopsis
        """
        if self.local_vars_configuration.client_side_validation and allocated is None:  # noqa: E501
            raise ValueError("Invalid value for `allocated`, must not be `None`")  # noqa: E501

        self._allocated = allocated

    @property
    def derived_state(self):
        """Gets the derived_state of this OrderGraphBlock.  # noqa: E501

        A simple description of the overall state of a block.  # noqa: E501

        :return: The derived_state of this OrderGraphBlock.  # noqa: E501
        :rtype: str
        """
        return self._derived_state

    @derived_state.setter
    def derived_state(self, derived_state):
        """Sets the derived_state of this OrderGraphBlock.

        A simple description of the overall state of a block.  # noqa: E501

        :param derived_state: The derived_state of this OrderGraphBlock.  # noqa: E501
        :type derived_state: str
        """
        if self.local_vars_configuration.client_side_validation and derived_state is None:  # noqa: E501
            raise ValueError("Invalid value for `derived_state`, must not be `None`")  # noqa: E501

        self._derived_state = derived_state

    @property
    def derived_compliance_state(self):
        """Gets the derived_compliance_state of this OrderGraphBlock.  # noqa: E501

        The overall compliance state of a block, derived from the block's orders. Possible values are Pending, Failed, 'Manually approved' and Passed.  # noqa: E501

        :return: The derived_compliance_state of this OrderGraphBlock.  # noqa: E501
        :rtype: str
        """
        return self._derived_compliance_state

    @derived_compliance_state.setter
    def derived_compliance_state(self, derived_compliance_state):
        """Sets the derived_compliance_state of this OrderGraphBlock.

        The overall compliance state of a block, derived from the block's orders. Possible values are Pending, Failed, 'Manually approved' and Passed.  # noqa: E501

        :param derived_compliance_state: The derived_compliance_state of this OrderGraphBlock.  # noqa: E501
        :type derived_compliance_state: str
        """
        if self.local_vars_configuration.client_side_validation and derived_compliance_state is None:  # noqa: E501
            raise ValueError("Invalid value for `derived_compliance_state`, must not be `None`")  # noqa: E501

        self._derived_compliance_state = derived_compliance_state

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
        if not isinstance(other, OrderGraphBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderGraphBlock):
            return True

        return self.to_dict() != other.to_dict()
