# CdxCreditEvent

Definition of a credit event for credit default swap index (CDX) instruments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_date** | **datetime** | The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation. | 
**auction_date** | **datetime** | The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined. | [optional] 
**recovery_rate** | **float** | The fraction of the defaulted debt that can be recovered. | [optional] 
**constituent_weight** | **float** | The relative weight of the CDX constituent. | 
**constituent_reference** | **str** | Reference value used to identify the CDX constituent. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


