# FxConventions

The conventions for the calculation of FX fixings, where the fixing rate is expected to be the amount of  DomCcy per unit of FgnCcy.  As an example, assume the required fixing is the WM/R 4pm mid closing rate for the USD amount per 1 EUR.  This is published with RIC EURUSDFIXM=WM, which would be the FixingReference, with FgnCcy EUR and DomCcy USD.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fgn_ccy** | **str** | The foreign currency | 
**dom_ccy** | **str** | The domestic currency | 
**fixing_reference** | **str** | The reference name used to find the desired quote | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


