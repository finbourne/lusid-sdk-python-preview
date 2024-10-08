# StockSplitEvent

A split in the company's shares. Shareholders are given additional company shares based on the terms of the stock split.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date on which the stock split takes effect. | 
**ex_date** | **datetime** | The first date on which the shares will trade at the post-split price. | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**record_date** | **datetime** | Date you have to be the holder of record in order to receive the additional shares. | [optional] 
**announcement_date** | **datetime** | Date the stock split was announced. | [optional] 
**fractional_units_cash_price** | **float** | The cash price per unit paid in lieu when fractional units can not be distributed. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractional units. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


