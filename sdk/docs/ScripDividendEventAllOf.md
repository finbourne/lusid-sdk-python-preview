# ScripDividendEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**payment_date** | **datetime** | The date the company pays out dividends to shareholders. | 
**fractional_units_cash_price** | **float** | The cash price per unit paid in lieu when fractional units can not be distributed. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractional units. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, ProtectionPayoutCashFlowEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


