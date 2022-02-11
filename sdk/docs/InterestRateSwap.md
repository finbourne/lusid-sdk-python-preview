# InterestRateSwap

IL Swap Instrument; Lusid-ibor internal representation of a swap instrument.                A swap is the exchange of two sets of cashflows, occurring at one or more dates in one or more currencies.  These may include a notional exchange at the start and, or, maturity of the trade. Depending upon the choice of  payment currency, payment frequency and so on they can be used to match sets of future obligations.    The implementation supports the following swap types:      * Vanilla (single currency fixed-float non-amortising)    * CrossCurrency (>1 currency is used by the swap legs)    * Basis (single currency, floating-floating legs of different tenors)    * Amortising (the swap has 1+ leg with amortised notional)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | 
**is_non_deliverable** | **bool** | Is the contract an IRS of \&quot;Non-Deliverable\&quot; type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates. | [optional] 
**legs** | [**list[InstrumentLeg]**](InstrumentLeg.md) | The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg. | 
**settlement_ccy** | **str** | Settlement currency if IRS is non-deliverable. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


