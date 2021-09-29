# EquitySwapAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the EquitySwap | 
**maturity_date** | **datetime** | The maturity date of the EquitySwap. | 
**code** | **str** | The code of the underlying. | 
**equity_flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**funding_leg** | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**include_dividends** | **bool** | Dividend inclusion flag, if true dividends are included in the equity leg (total return). | 
**initial_price** | **float** | The initial equity price of the Equity Swap. | 
**notional_reset** | **bool** | Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity) | 
**quantity** | **float** | The quantity or number of shares in the Equity Swap. | 
**underlying_identifier** | **str** | external market codes and identifiers for the EquitySwap, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


