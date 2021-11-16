# FxOptionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | 
**is_delivery_not_cash** | **bool** | True if the option is settled in cash, false if delivery. | 
**is_call_not_put** | **bool** | True if the option is a call, false if the option is a put. | 
**strike** | **float** | The strike of the option. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**dom_amount** | **float** | The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1. | [optional] 
**fgn_ccy** | **str** | The foreign currency of the FX. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


