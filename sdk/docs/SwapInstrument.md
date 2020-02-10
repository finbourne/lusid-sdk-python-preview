# SwapInstrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Starting date of the swap | 
**maturity_date** | **datetime** | Maturity date of the swap | 
**legs** | [**list[InstrumentLeg]**](InstrumentLeg.md) | True if the swap is amortizing | 
**notional** | **float** | The notional. | 
**is_amortizing** | **bool** | True if the swap is amortizing | 
**notional_exchange_type** | **str** | True notional exchange type. | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


