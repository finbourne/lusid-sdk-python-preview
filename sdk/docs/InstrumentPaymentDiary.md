# InstrumentPaymentDiary

A payment diary containing all the cashflows on a single instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id_type** | **str** | The identifier type of the instrument. | [optional] 
**instrument_id** | **str** | The identifier for the instrument. | [optional] 
**instrument_scope** | **str** | The scope of the instrument. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**legs** | [**list[InstrumentPaymentDiaryLeg]**](InstrumentPaymentDiaryLeg.md) | Aggregated sets of Cashflows. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


