# CashDividendEvent

A cash distribution paid out to shareholders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date the company begins distributing the dividend. | 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party. | 
**cash_elections** | [**list[CashElection]**](CashElection.md) | Possible elections for this event, each keyed with a unique identifier. | 
**announcement_date** | **datetime** | Date on which the dividend is announced by the company. | [optional] 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


