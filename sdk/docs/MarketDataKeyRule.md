# MarketDataKeyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*) | 
**supplier** | **str** | The market data supplier (where the data comes from) | 
**data_scope** | **str** | The scope in which the data should be found when using this rule. | 
**quote_type** | **str** | The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront | 
**field** | **str** | The conceptual qualification for the field, such as bid, mid, or ask.   The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId | 
**quote_interval** | **str** | Shorthand for the time interval used to select market data. | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 
**price_source** | **str** | The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


