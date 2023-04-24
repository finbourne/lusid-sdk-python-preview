# OrderInstructionRequest

A request to create or update a Order Instruction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**created_date** | **datetime** | The active date of this order instruction. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument ordered. | [optional] 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**weight** | **float** | The weight of given instrument ordered. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


