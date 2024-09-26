# MasteredInstrument

LUSID representation of a reference to another instrument that has already been upserted (Mastered)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **dict(str, str)** | Dictionary of identifiers of the mastered instrument | 
**asset_class** | **str** | Asset class of the mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. | [optional] [readonly] 
**mastered_dom_ccy** | **str** | DomCcy of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_instrument_type** | **str** | Type of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_lusid_instrument_id** | **str** | Luid of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_name** | **str** | Name of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_scope** | **str** | Scope of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


