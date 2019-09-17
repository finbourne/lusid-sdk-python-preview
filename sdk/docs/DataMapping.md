# DataMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_field_name_mappings** | **dict(str, str)** | A map from a client source, or other source that is not addressed in terms of the internal LUSID property paths to the internal LUSID property paths.  In a simple case this could be something like \&quot;ISIN\&quot; to \&quot;Instrument/default/ISIN\&quot;. The DataMapping dictionary provides a way to make LUSID aware of  documents that have an external format that the client might not wish to change but where it would be useful to be able to query that data within LUSID.  Queries within LUSID are preferably to be written using the LUSID property paths in order to encourage the same semantic meaning to be attached to pieces of data. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


