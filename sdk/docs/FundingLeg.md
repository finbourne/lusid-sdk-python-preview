# FundingLeg

IL FundingLeg Instrument; Lusid-ibor internal representation of a funding leg with variable notional.  This instrument is a hybrid between a single leg swap and a bank account, in that the notional is not fixed but  can be changed over it's life. The use case for this is to represent the funding leg of a basket of instruments  (e.g. equities) where the contents of the basket can change over time.  The actual notional history is stored in the FundingLegHistory object (implements IHistory) and this can be updated  externally or in some circumstances automatically by LUSID.  The main analytic calculated for this instrument is Accrual rather than PV.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**maturity_date** | **datetime** |  | 
**leg_definition** | [**LegDefinition**](LegDefinition.md) |  | 
**notional** | **float** |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


