# A2BDataRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_type** | **str** | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured when a transaction portfolio is created. | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**transaction_id** | **str** | The unique identifier for the transaction. | [optional] 
**start** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**flows** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**gains** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**carry** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**end** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


