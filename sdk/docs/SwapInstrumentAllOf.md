# SwapInstrumentAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date | 
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**legs** | [**list[InstrumentLeg]**](InstrumentLeg.md) | The set of instrument legs that define the swap instrument. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, Exotic, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedRateLeg, FloatingRateLeg, BespokeCashflowLeg, Unknown | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


