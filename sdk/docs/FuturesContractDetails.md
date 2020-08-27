# FuturesContractDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | currency in which the contract is paid. | 
**contract_code** | **str** | The two letter contract code abbreviation. e.g. CL &#x3D;&gt; Crude Oil. | 
**contract_month** | **str** | which month does the contract trade for. | 
**contract_size** | **float** | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. | 
**convention** | **str** | The available values are: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActAct, ActualActual, ActActIsda, ActActIsma, ActActIcma, Invalid | 
**country** | **str** | Country (code) for the exchange. | 
**description** | **str** | Description of contract | 
**exchange_code** | **str** | Exchange code for contract | 
**exchange_name** | **str** | Exchange name (for when code is not automatically recognized) | 
**ticker_step** | **float** | Minimal step size change in ticker | 
**unit_value** | **float** | The value in the currency of a 1 unit change in the contract price | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


