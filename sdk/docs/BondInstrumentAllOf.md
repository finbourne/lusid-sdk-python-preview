# BondInstrumentAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**maturity_date** | **datetime** |  | 
**dom_ccy** | **str** |  | 
**coupon_rate** | **float** | simple coupon rate. | 
**principal** | **float** | The face-value or principal for the bond at outset.              This might be reduced through its lifetime in the event of amortization or similar. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**identifiers** | **dict(str, str)** | set of market identifiers along with their types, e.g. ISIN, CUSIP, SEDOL. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, Exotic, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedRateLeg, FloatingRateLeg, BespokeCashflowLeg, Unknown | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


