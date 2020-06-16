# MarketOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_supplier** | **str** | The available values are: DataScope, Lusid, Isda, Client, Edi, TraderMade, FactSet | [optional] 
**default_instrument_code_type** | **str** | The available values are: LusidInstrumentId, Figi, RIC, QuotePermId, Isin, CurrencyPair | [optional] 
**default_scope** | **str** | For default rules, which scope should data be searched for in | [optional] 
**attempt_to_infer_missing_fx** | **bool** | if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD | [optional] 
**manifest_level_of_detail** | **str** | The available values are: None, Full | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


