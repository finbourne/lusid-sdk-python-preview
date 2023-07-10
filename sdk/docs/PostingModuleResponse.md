# PostingModuleResponse

A posting Module request definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name to identify the Posting Module by | 
**description** | **str** | The description for the posting module | [optional] 
**rule_count** | **int** | The number of posting rules that apply for the Posting Module | [optional] 
**status** | **str** | The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


