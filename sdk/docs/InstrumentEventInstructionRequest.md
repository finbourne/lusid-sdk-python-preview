# InstrumentEventInstructionRequest

The request to create an instruction for an instrument event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_instruction_id** | **str** | The unique identifier for this instruction | 
**instrument_event_id** | **str** | The identifier of the instrument event being instructed | 
**instruction_type** | **str** | The type of instruction (Ignore, ElectForPortfolio, ElectForHolding) | 
**election_key** | **str** | For elected instructions, the key to be chosen | [optional] 
**holding_id** | **int** | For holding instructions, the id of the holding for which the instruction will apply | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


