# PostingModuleResponse

A Posting Module definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**posting_module_code** | **str** | The code of the Posting Module. | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name to identify the Posting Module by | 
**description** | **str** | The description for the Posting Module | [optional] 
**rule_count** | **int** | The number of posting rules that apply for the Posting Module | [optional] 
**status** | **str** | The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


