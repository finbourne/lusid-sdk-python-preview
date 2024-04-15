# BondCouponEvent

Definition of a Bond Coupon Event  This is an event that describes the occurence of a cashflow due to a fixed rate bond coupon payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | Ex-Dividend date of the coupon payment | 
**payment_date** | **datetime** | Payment date of the coupon payment | 
**currency** | **str** | Currency of the coupon payment | 
**coupon_per_unit** | **float** | CouponRate*Principal | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


