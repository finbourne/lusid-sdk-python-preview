# InstrumentCapabilities

Instrument capabilities containing useful information about the instrument and the model. This includes  - features corresponding to the instrument i.e. Optionality:American, Other:InflationLinked  - supported addresses (if model provided) i.e. Valuation/Pv, Valuation/DirtyPriceKey, Valuation/Accrued  - economic dependencies (if model provided) i.e. Cash:USD, Fx:GBP.USD, Rates:GBP.GBPOIS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The Lusid insturment id for the instrument e.g. &#39;LUID_00003D4X&#39;. | [optional] 
**model** | **str** | The pricing model e.g. &#39;Discounting&#39;. | [optional] 
**features** | **list[str]** | Features of the instrument describing its optionality, payoff type and more e.g. &#39;Other:Callable&#39;, &#39;Other:Delivery&#39;, &#39;Optionality:European&#39; | [optional] 
**supported_addresses** | **list[str]** | Queryable addresses supported by the model, e.g. &#39;Valuation/Pv&#39;, &#39;Valuation/Accrued&#39;. | [optional] 
**economic_dependencies** | [**list[EconomicDependency]**](EconomicDependency.md) | Economic dependencies for the model, e.g. &#39;Fx:GBP.USD&#39;, &#39;Cash:GBP&#39;, &#39;Rates:GBP.GBPOIS&#39;. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


