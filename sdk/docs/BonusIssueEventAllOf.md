# BonusIssueEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the Bonus Issue is announced. | [optional] 
**ex_date** | **datetime** | The ex-date of the Bonus Issue. | 
**record_date** | **datetime** | The record date of the Bonus Issue. | [optional] 
**payment_date** | **datetime** | The date the Bonus Issue is executed. | 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**security_offer_elections** | [**list[SecurityOfferElection]**](SecurityOfferElection.md) | Possible SecurityElections for this Bonus Issue event, if any. | [optional] 
**cash_offer_elections** | [**list[CashOfferElection]**](CashOfferElection.md) | Possible CashOfferElections for this Bonus Issue event, if any. | [optional] 
**lapse_elections** | [**list[LapseElection]**](LapseElection.md) | Possible LapseElections for this Bonus Issue event, if any. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, ProtectionPayoutCashFlowEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


