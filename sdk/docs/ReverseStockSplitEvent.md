# ReverseStockSplitEvent

A reverse split in the company's shares. Shareholders have their number of shares reduced based on the terms of the stock split.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date on which the stock split takes effect. | 
**ex_date** | **datetime** | The first date on which the shares will trade at the post-split price. | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**record_date** | **datetime** | Date you have to be the holder of record in order to have their shares merged. | [optional] 
**announcement_date** | **datetime** | Date the reverse stock split was announced. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractionalUnits. | [optional] 
**fractional_units_cash_price** | **float** | The cash price paid in lieu of fractionalUnits. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, ProtectionPayoutCashFlowEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


