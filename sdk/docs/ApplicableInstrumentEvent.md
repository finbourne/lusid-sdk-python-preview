# ApplicableInstrumentEvent

Represents applicable instrument event.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**holding_id** | **int** |  | 
**lusid_instrument_id** | **str** |  | 
**instrument_scope** | **str** |  | 
**instrument_type** | **str** |  | 
**instrument_event_type** | **str** |  | 
**instrument_event_id** | **str** |  | 
**generated_event** | [**InstrumentEventHolder**](InstrumentEventHolder.md) |  | [optional] 
**generated_event_diagnostics** | [**GeneratedEventDiagnostics**](GeneratedEventDiagnostics.md) |  | [optional] 
**loaded_event** | [**InstrumentEventHolder**](InstrumentEventHolder.md) |  | [optional] 
**applied_instrument_event_instruction_id** | **str** |  | 
**transactions** | [**list[Transaction]**](Transaction.md) |  | [optional] 
**transaction_diagnostics** | [**TransactionDiagnostics**](TransactionDiagnostics.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


