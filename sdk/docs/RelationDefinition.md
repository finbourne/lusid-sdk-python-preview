# RelationDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source_entity_domain** | **str** | The entity domain of the source entity object. | [optional] 
**target_entity_domain** | **str** | The entity domain of the target entity object. | [optional] 
**display_name** | **str** | The display name of the relation. | [optional] 
**outward_description** | **str** | The description to relate source entity object and target entity object | [optional] 
**inward_description** | **str** | The description to relate target entity object and source entity object | [optional] 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


