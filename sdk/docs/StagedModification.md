# StagedModification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Id for the staged modification | [optional] 
**as_at_staged** | **datetime** | Time at which the modification was staged. | [optional] 
**user_id_staged** | **str** | Id of the user who created the stage modification request. | [optional] 
**requested_id_staged** | **str** | The Request Id that initiated this staged modification. | [optional] 
**action** | **str** | Type of action of the staged modification, either create, update or delete. | [optional] 
**staging_rule** | [**StagedModificationStagingRule**](StagedModificationStagingRule.md) |  | [optional] 
**decisions** | [**list[StagedModificationDecision]**](StagedModificationDecision.md) | Object containing information relating to the decision on the staged modification. | [optional] 
**decisions_count** | **int** | Number of decisions made. | [optional] 
**status** | **str** | The status of the staged modification. | [optional] 
**entity_type** | **str** | The type of the entity that the staged modification applies to. | [optional] 
**scope** | **str** | The scope of the entity that this staged modification applies to. | [optional] 
**entity_unique_id** | **str** | The unique Id of the entity the staged modification applies to. | [optional] 
**requested_changes** | [**RequestedChanges**](RequestedChanges.md) |  | [optional] 
**entity_hrefs** | [**StagedModificationsEntityHrefs**](StagedModificationsEntityHrefs.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


