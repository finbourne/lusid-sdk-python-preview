# TranslateInstrumentDefinitionsResponse

A response from a request to translate a collection of instruments to a given target dialect.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, LusidInstrument)**](LusidInstrument.md) | The instruments which have been successfully translated. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The instruments that could not be translated along with a reason for their failure. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


