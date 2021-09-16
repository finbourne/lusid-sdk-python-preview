# BondAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**principal** | **float** | The face-value or principal for the bond at outset.              This might be reduced through its lifetime in the event of amortization or similar. | 
**coupon_rate** | **float** | simple coupon rate. | 
**identifiers** | **dict(str, str)** | external market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**ex_dividend_days** | **int** | The number of days before the next coupon payment for which the bond goes ex-dividend. | [optional] 
**initial_coupon_date** | **datetime** | The initial coupon date which specifies the accrual start period for a fixed coupon bond with ex dividend schedule | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


