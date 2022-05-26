# OrderGraphPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement** | [**Placement**](Placement.md) |  | 
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all orders in the block - DEPRECATED: see Ordered. | 
**allocation_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all allocations relating to this placement - DEPRECATED: see Allocated. | 
**execution_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all executions against this placement - DEPRECATED: see Executed. | 
**ordered** | [**OrderGraphPlacementOrderSynopsis**](OrderGraphPlacementOrderSynopsis.md) |  | 
**placed** | [**OrderGraphPlacementPlacementSynopsis**](OrderGraphPlacementPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphPlacementExecutionSynopsis**](OrderGraphPlacementExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphPlacementAllocationSynopsis**](OrderGraphPlacementAllocationSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a placement. | 
**calculated_average_price** | **float** | Average price realised on executions for a given placement | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


