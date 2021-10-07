# OrderGraphBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**order_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all the orders in this block. | 
**placement_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all placements for the block. | 
**allocation_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers for all allocations of placements to orders in the block. | 
**execution_ids** | [**list[ResourceId]**](ResourceId.md) | Identifiers of all executions against placements in the block. | 
**ordered** | **float** | Total number of units of the instrument across all orders in the block. | 
**placed** | **float** | Number of units of the instrument across all placements in the block. | 
**allocated** | **float** | Number of units of the instrument across all allocations in the block. | 
**executed** | **float** | How many of the quantity ordered for this block have been executed in the market. | 
**derived_state** | **str** | A simple description of the overall state of a block. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


