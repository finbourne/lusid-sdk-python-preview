# ContractForDifferenceAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the CFD. | 
**code** | **str** | The code of the underlying. | 
**pay_ccy** | **str** | The currency that this CFD pays out, this can be different to the UnderlyingCcy. | 
**reference_date** | **datetime** | The reference date of the CFD. | 
**reference_rate** | **float** | The reference rate of the CFD. | 
**underlying_ccy** | **str** | The currency of the underlying | 
**underlying_identifier** | **str** | external market codes and identifiers for the CFD, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId]. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


