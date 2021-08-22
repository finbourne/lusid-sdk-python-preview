# InlineValuationsReconciliationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**right** | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**left_to_right_mapping** | [**list[ReconciliationLeftRightAddressKeyPair]**](ReconciliationLeftRightAddressKeyPair.md) | The mapping from property keys requested by left aggregation to property keys on right hand side | [optional] 
**preserve_keys** | **list[str]** | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


