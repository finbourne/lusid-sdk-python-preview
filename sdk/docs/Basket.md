# Basket

Class that models a basket of risky instruments that can default.  Upon default, the weight of a defaulting instrument can (will) change and this then affects the behaviour of the basket.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basket_name** | [**BasketIdentifier**](BasketIdentifier.md) |  | 
**basket_type** | **str** | What contents does the basket have. The validation will check that the instrument types contained match those expected.  Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap, Unknown]. | 
**weighted_instruments** | [**WeightedInstruments**](WeightedInstruments.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket, FundingLeg | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


