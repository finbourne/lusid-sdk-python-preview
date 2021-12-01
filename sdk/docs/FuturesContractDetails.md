# FuturesContractDetails

Most, if not all, information about contracts is standardized. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | Currency in which the contract is paid. | 
**asset_class** | **str** | The asset class of the underlying. Optional and will default to Unknown if not set.  Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. | [optional] 
**contract_code** | **str** | The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc. | 
**contract_month** | **str** | Which month does the contract trade for.  Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z]. | 
**contract_size** | **float** | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. | 
**convention** | **str** | If appropriate, the day count convention method used in pricing (rates futures). | 
**country** | **str** | Country (code) for the exchange. | 
**description** | **str** | Description of contract. | 
**exchange_code** | **str** | Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME]. | 
**exchange_name** | **str** | Exchange name (for when code is not automatically recognised). | 
**ticker_step** | **float** | Minimal step size change in ticker. | 
**unit_value** | **float** | The value in the currency of a 1 unit change in the contract price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


