# AggregatedTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_transaction_date** | **datetime** |  | 
**to_transaction_date** | **datetime** |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**as_at** | **datetime** |  | [optional] 
**metrics** | [**list[AggregateSpec]**](AggregateSpec.md) |  | 
**group_by** | **list[str]** |  | [optional] 
**filters** | [**list[PropertyFilter]**](PropertyFilter.md) |  | [optional] 
**sort** | [**list[OrderBySpec]**](OrderBySpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


