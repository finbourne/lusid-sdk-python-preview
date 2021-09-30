# Repo

IL Repo Instrument; Lusid-ibor internal representation of a Repo instrument  The repurchase (repo) agreement involves the transfer of instruments (the collateral) from the seller to the buyer.  Ownership is transferred and returns to the seller upon completion of the contract. If the collateral depreciates sharply, it is possible that additional  margin/collateral will be required depending upon the terms of the agreement. The buyer agrees not to sell the securities unless there is some condition of default  in the repo contract.   Repurchase of the securities is at their value plus the agreed upon fixed repo rate.  On the start date, the buyer receives the collateral and pays Cash.  On the maturity date, the buyer returns the collateral and receives Cash.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**accrual_basis** | **str** | For calculation of interest, the accrual basis to be used.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**collateral_value** | **float** | The full value of the collateral in domCcy, before any margin (or haircut) is applied. | 
**margin** | **float** | The margin (or haircut) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05. | 
**repo_rate** | **float** | the rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


