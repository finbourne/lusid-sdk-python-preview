# Counterparty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | A unique identifier that determines the identity of the counter-party, disambiguating between related legal entities, particularly necessary in the case of multi-nationals. | 
**counterparty_name** | **str** | The legal name of the entity to which this counterparty refers. | 
**country_of_risk** | **str** | To which country would one naturally ascribe risk. Typically this will be synonymous with legal registration entity.  This can be used to infer funding currency and related market data in the absence of specific overrides or preference. | 
**issuer_ratings** | [**list[CreditRating]**](CreditRating.md) | A set of credit ratings for the counterparty fro, e.g. Standard and Poor or Moody&#39;s. | 
**industry_scheme** | [**IndustryClassificationScheme**](IndustryClassificationScheme.md) |  | 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


