# CashFlowEvent

Definition of a CashFlow event.  This is an event that describes the occurence of a cashflow and associated information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The quantity (amount) that will be paid, if known. This value will be negative if it is paid, and positive  if it is received. | [optional] 
**currency** | **str** | The payment currency of the cash flow. | 
**event_type** | **str** | What type of internal event does this represent; coupon, principal, premium etc. | [readonly] 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**payment_date** | **datetime** | The date on which the cashflow is scheduled to be paid into the recipient&#39;s bank account. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, RawVendorEvent, InformationalErrorEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


