# lusid.RecipeComposerApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recipe_composer_resolved_inline**](RecipeComposerApi.md#get_recipe_composer_resolved_inline) | **POST** /api/recipecomposers/inline | [EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.


# **get_recipe_composer_resolved_inline**
> GetRecipeResponse get_recipe_composer_resolved_inline(upsert_recipe_composer_request)

[EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.

Resolves an inline recipe composer into a ConfigurationRecipe.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RecipeComposerApi(api_client)
    upsert_recipe_composer_request = {"recipeComposer":{"code":"someCode","scope":"someScope","operations":[{"value":{"fromRecipe":{"scope":"someRecipeScope","code":"SomeRecipeCode"}},"path":".","op":"Insert"},{"value":{"asString":"SimpleStatic"},"path":"Pricing.ModelRules.[*].ModelName","op":"Update"}]}} # UpsertRecipeComposerRequest | Recipe composer used to resolve into the Configuration Recipe.

    try:
        # [EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.
        api_response = api_instance.get_recipe_composer_resolved_inline(upsert_recipe_composer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipeComposerApi->get_recipe_composer_resolved_inline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_composer_request** | [**UpsertRecipeComposerRequest**](UpsertRecipeComposerRequest.md)| Recipe composer used to resolve into the Configuration Recipe. | 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully resolved Configuration Recipe. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

