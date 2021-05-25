# ResultDataKeyRule

A rule that describes how we resolve (unit) result data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_key** | **str** | The result data key that identifies the address pattern that this is a rule for | 
**supplier** | **str** | the result resource supplier (where the data comes from) | 
**data_scope** | **str** | which is the scope in which the data should be found | 
**document_code** | **str** | document code that defines which document is desired | 
**quote_interval** | **str** | Shorthand for the time interval used to select result data. | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


