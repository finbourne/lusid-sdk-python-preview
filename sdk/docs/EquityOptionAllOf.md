# EquityOptionAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The reset code of the option. | 
**strike** | **float** | The strike of the option. | 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | 
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**option_type** | **str** | The available values are: None, Call, Put | 
**delivery_type** | **str** | The available values are: Cash, Physical | 
**underlying_identifier** | **str** | The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Exotic, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedRateLeg, FloatingRateLeg, BespokeCashflowLeg, Unknown | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


