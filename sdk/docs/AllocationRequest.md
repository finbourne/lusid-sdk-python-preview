# AllocationRequest

A request to create or update an Allocation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument allocated. | 
**quantity** | **int** | The quantity of given instrument allocated. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


