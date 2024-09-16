# FundConfigurationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**dealing_filters** | [**list[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the dealing. | 
**pnl_filters** | [**list[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the PnL. | 
**back_out_filters** | [**list[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the back outs. | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the Fund Configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


