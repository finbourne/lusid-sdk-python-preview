# IndustryClassificationScheme

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme_name** | **str** | The type of the industry classification scheme (TRBC, GICs, ICB) | 
**scheme_id** | **str** | Within the given scheme, the unique id that identifies this particular classification.  e.g. within \&quot;TRCS\&quot;, 5010202011 identifies \&quot;Oil Exploration \\amp; Production - Onshore\&quot; within the Energy, fossil-fuels and Oil hierarchy. | 
**economic_sector** | **str** | Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which economic sector is the counterparty assigned to. This is Lvl 1 of that scheme (coarsest) | 
**business_sector** | **str** | Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. fossil fuels within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 2 of that scheme (2nd coarsest)  e.g. Fossil Fuels within energy. | 
**industry** | **str** | Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 3 of that scheme (3rd coarsest)  e.g. Coal or Oil within Fossil Fuels. | 
**industry_activity** | **str** | Various schemes exist to classify the business sector within which a company operates.  They divide it into various categories around business, economic and sub-sectors (e.g. coal within energy)  Under ICB, TRBC, GICS which business sector is the counterparty assigned to. This is Lvl 4 of the scheme (finest)  e.g. Petroleum Refining within Oil within Fossil Fuels. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


