# CustomEntityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type** | **str** | The EntityType to be used when relations are created to the CustomEntity | 
**custom_entity_id** | **str** | A unique identifier for the CustomEntity | 
**version** | [**Version**](Version.md) |  | 
**display_name** | **str** | The display name of the CustomEntity | 
**description** | **str** | The description of the CustomEntity | [optional] 
**identifiers** | [**list[CustomEntityIdResponse]**](CustomEntityIdResponse.md) | A collection of CustomEntityIdentifiers that can identify the CustomEntity | 
**fields** | [**list[CustomEntityField]**](CustomEntityField.md) | A collection of CustomEntityFields that decorate the CustomEntity | 
**effective_range** | [**DateRange**](DateRange.md) |  | 
**as_at_range** | [**DateRange**](DateRange.md) |  | 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


