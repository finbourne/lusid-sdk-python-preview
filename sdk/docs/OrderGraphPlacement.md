# OrderGraphPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement** | [**Placement**](Placement.md) |  | 
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all orders in the block. | 
**allocation_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all allocations relating to this placement. | 
**execution_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all executions against this placement. | 
**placed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**allocated** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**executed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a placement. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


