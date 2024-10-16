# OptionExercisePhysicalEvent

Event for physical option exercises.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exercise_date** | **datetime** | The exercise date of the option. | [optional] 
**exercise_type** | **str** | The optionality type of the underlying option e.g. American, European.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**maturity_date** | **datetime** | The maturity date of the option. | 
**moneyness** | **str** | The moneyness of the option e.g. InTheMoney, OutOfTheMoney.    Supported string (enumeration) values are: [InTheMoney, OutOfTheMoney, AtTheMoney]. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**option_exercise_elections** | [**list[OptionExerciseElection]**](OptionExerciseElection.md) | Option exercise election for this OptionExercisePhysicalEvent. | [optional] 
**option_type** | **str** | Type of optionality that is present e.g. call, put.    Supported string (enumeration) values are: [Call, Put]. | 
**start_date** | **datetime** | The trade date of the option. | 
**strike_currency** | **str** | The strike currency of the equity option. | 
**strike_per_unit** | **float** | The strike of the equity option times the number of shares to exchange if exercised. | 
**underlying_value_per_unit** | **float** | The underlying price times the number of shares to exchange if exercised. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, ProtectionPayoutCashFlowEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


