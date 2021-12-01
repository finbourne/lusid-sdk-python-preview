# YieldCurveData

Market data for a yield curve,  represented by a list of instruments and corresponding market quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date | 
**instruments** | [**list[LusidInstrument]**](LusidInstrument.md) | The set of instruments that define the curve. | 
**quotes** | [**list[MarketQuote]**](MarketQuote.md) | The market quotes corresponding to the the instruments used to define the curve | 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


