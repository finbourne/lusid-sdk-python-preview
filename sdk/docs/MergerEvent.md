# MergerEvent

Merger Event (MRGR).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the merger is announced. | [optional] 
**cash_and_security_offer_elections** | [**list[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this merger event | [optional] 
**cash_elections** | [**list[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this merger event | [optional] 
**ex_date** | **datetime** | The first date on which the holder of record of the original shares has entitled ownership of the new shares. | 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**payment_date** | **datetime** | Date on which the merger takes place. | 
**record_date** | **datetime** | Optional. Date you have to be the holder of record of the original shares in order to receive the new shares. | [optional] 
**security_elections** | [**list[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this merger event | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


