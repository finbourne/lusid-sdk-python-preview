# InstrumentEntity

A list of instruments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_unique_id** | **str** | The unique id of the entity. | 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**status** | **str** | The status of the entity at the current time. | 
**as_at_deleted** | **datetime** | The asAt datetime at which the entity was deleted. | [optional] 
**user_id_deleted** | **str** | The unique id of the user who deleted the entity. | [optional] 
**request_id_deleted** | **str** | The unique request id of the command that deleted the entity. | [optional] 
**effective_at_created** | **datetime** | The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt. | [optional] 
**prevailing_instrument** | [**Instrument**](Instrument.md) |  | [optional] 
**deleted_instrument** | [**Instrument**](Instrument.md) |  | [optional] 
**previewed_status** | **str** | The status of the previewed entity. | [optional] 
**previewed_instrument** | [**Instrument**](Instrument.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


