# TransactionTypeMovement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | Movement types determine the impact of the movement on the holdings | 
**side** | **str** | The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the &#39;security&#39; side of the transaction, ie the Instrument and Units; Side2 means the &#39;cash&#39; side, ie the Total Consideration | 
**direction** | **int** |  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease | 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The properties associated with the underlying Movement | [optional] 
**mappings** | [**list[TransactionTypePropertyMapping]**](TransactionTypePropertyMapping.md) | This allows you to map a transaction property to a property on the underlying holding | [optional] 
**name** | **str** | The movement name (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


