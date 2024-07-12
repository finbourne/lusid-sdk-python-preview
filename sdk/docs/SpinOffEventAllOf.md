# SpinOffEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Optional.  The date the spin-off is announced. | [optional] 
**ex_date** | **datetime** | The first date on which the holder of record has entitled ownership of the new shares. | 
**record_date** | **datetime** | Optional.  Date you have to be the holder of record in order to receive the additional shares. | [optional] 
**payment_date** | **datetime** | Date on which the distribution of shares takes place. | 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**cost_factor** | **float** | Optional. The fraction of cost that is transferred from the existing shares to the new shares. | [optional] 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


