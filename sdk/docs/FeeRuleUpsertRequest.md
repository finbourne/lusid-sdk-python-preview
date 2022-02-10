# FeeRuleUpsertRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**transaction_property_key** | **str** |  | 
**transaction_type** | **str** |  | 
**country** | **str** |  | 
**counterparty** | **str** |  | 
**transaction_currency** | **str** |  | 
**settlement_currency** | **str** |  | 
**execution_broker** | **str** |  | 
**custodian** | **str** |  | 
**exchange** | **str** |  | 
**fee** | [**CalculationInfo**](CalculationInfo.md) |  | 
**min_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**max_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**additional_keys** | **dict(str, str)** |  | [optional] 
**description** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


