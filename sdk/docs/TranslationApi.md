# lusid.TranslationApi

All URIs are relative to *http://local-unit-test-server.lusid.com:32761*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate_instrument_definitions**](TranslationApi.md#translate_instrument_definitions) | **POST** /api/translation/instrumentdefinitions | [EXPERIMENTAL] Translate instruments


# **translate_instrument_definitions**
> TranslateInstrumentDefinitionsResponse translate_instrument_definitions(translate_instrument_definitions_request)

[EXPERIMENTAL] Translate instruments

Translates one or more instruments into the given target dialect.                In the request each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.                The response will return both the collection of successfully translated instruments in the target dialect,  as well as those that failed.  For the failures a reason will be provided explaining why the instrument could not be updated or inserted.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:32761
configuration.host = "http://local-unit-test-server.lusid.com:32761"
# Create an instance of the API class
api_instance = lusid.TranslationApi(lusid.ApiClient(configuration))
translate_instrument_definitions_request = {"instruments":{"myFavouriteInstrument":{"instrumentFormat":{"sourceSystem":"someSource","vendor":"someVendor","version":"someVersion"},"content":"{\"InstrumentContentShouldBeGivenAsAJsonString\": \"OrAnXmlString\"}","instrumentType":"ExoticInstrument"},"myFavouriteLusidInstrument":{"startDate":"2018-01-01T00:00:00.0000000+00:00","maturityDate":"2019-01-01T00:00:00.0000000+00:00","domAmount":1,"domCcy":"GBP","fgnAmount":-1.5,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}},"dialect":"targetDialect"} # TranslateInstrumentDefinitionsRequest | The definitions of the instruments to translate along with the target dialect.

try:
    # [EXPERIMENTAL] Translate instruments
    api_response = api_instance.translate_instrument_definitions(translate_instrument_definitions_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->translate_instrument_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_instrument_definitions_request** | [**TranslateInstrumentDefinitionsRequest**](TranslateInstrumentDefinitionsRequest.md)| The definitions of the instruments to translate along with the target dialect. | 

### Return type

[**TranslateInstrumentDefinitionsResponse**](TranslateInstrumentDefinitionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully translated instruments along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

