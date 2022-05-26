# OrderGraphBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**order_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all the orders in this block - DEPRECATED: see Ordered. | 
**placement_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all placements for the block - DEPRECATED: see Placed. | 
**allocation_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all allocations of placements to orders in the block - DEPRECATED: see Allocated. | 
**execution_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all executions against placements in the block - DEPRECATED: see Executed. | 
**ordered** | [**OrderGraphBlockOrderSynopsis**](OrderGraphBlockOrderSynopsis.md) |  | 
**placed** | [**OrderGraphBlockPlacementSynopsis**](OrderGraphBlockPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphBlockExecutionSynopsis**](OrderGraphBlockExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphBlockAllocationSynopsis**](OrderGraphBlockAllocationSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a block. | 
**derived_compliance_state** | **str** | The overall compliance state of a block, derived from the block&#39;s orders. Possible values are Pending, Failed, and Passed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


