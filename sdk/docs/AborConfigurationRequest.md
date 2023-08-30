# AborConfigurationRequest

The request used to create an AborConfiguration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the AborConfiguration. | 
**description** | **str** | The description for the AborConfiguration. | [optional] 
**name** | **str** | The given name for the AborConfiguration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_ids** | [**list[ResourceId]**](ResourceId.md) | The Posting Modules Ids from where the rules to be applied are retrieved. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Properties to add to the AborConfiguration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


