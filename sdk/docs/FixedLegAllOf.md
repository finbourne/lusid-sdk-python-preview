# FixedLegAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notional** | **float** | scaling factor to apply to leg quantities. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date | 
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**leg_definition** | [**LegDefinition**](LegDefinition.md) |  | 
**overrides** | [**FixedLegAllOfOverrides**](FixedLegAllOfOverrides.md) |  | 
**instrument_type** | **str** | Instrument type, must be property for JSON. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


