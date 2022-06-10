# FilterInstrumentEvents

Instrument event query structure. The fields in the body act in and AND-wise fashion  for any instrument event query endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_ids** | **list[str]** | The set of instrument events ids. | [optional] 
**corporate_action_source_ids** | [**list[ResourceId]**](ResourceId.md) | The corporate action sources in which to search for events. | [optional] 
**lusid_instrument_ids** | **list[str]** | The lusid identifers for instruments on which the events apply. | [optional] 
**instrument_scopes** | **list[str]** | The set of scopes in which the instruments of interest belong. | [optional] 
**instrument_event_types** | **list[str]** | The subset of instrument event types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


