# OrderGraphBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**order_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all the orders in this block. | 
**placement_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all placements for the block. | 
**allocation_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all allocations of placements to orders in the block. | 
**execution_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all executions against placements in the block. | 
**ordered** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**placed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**allocated** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**executed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a block. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


