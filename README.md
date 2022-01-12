# LUSID<sup>®</sup> Python Preview SDK
This is the Python Preview SDK for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>


## Installation

The PyPi package for the LUSID SDK can installed using the following:

```
pip install lusid-sdk-preview
```

We publish two versions of the Python SDK:

* [lusid-sdk-python](https://github.com/finbourne/lusid-sdk-python) - supports `Production` and `Early Access` API endpoints**
* **lusid-sdk-python-preview (this one) - supports `Production`, `Early Access`, `Beta` and `Experimental` API endpoints.**

For more details on API endpoint categories, see [What is the LUSID feature release lifecycle?](https://support.lusid.com/knowledgebase/article/KA-01786/en-us).
To find out which category an API endpoint falls into, see [LUSID API Documentation](https://www.lusid.com/api/swagger/index.html).


## Documentation 

For further documentation on building the SDK, running the tutorials and using the SDK please see the [wiki](https://github.com/finbourne/lusid-sdk-python-preview/wiki).

Documentation for classes, methods, attributes and other members of the SDK is [available to view online](https://lusid-sdk-python-preview.readthedocs.io/en/latest/_autosummary/sdk.lusid.html).

## Build Status

| branch | status |
| --- | --- |
| `master` |  ![PyPI](https://img.shields.io/pypi/v/lusid-sdk-preview?color=blue) ![build](https://github.com/finbourne/lusid-sdk-python-preview/workflows/lusid-sdk-python-preview-test/badge.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=finbourne_lusid-sdk-python-preview&metric=alert_status)](https://sonarcloud.io/dashboard?id=finbourne_lusid-sdk-python-preview) |
| `develop` | ![lusid-sdk-python-preview-test](https://github.com/finbourne/lusid-sdk-python-preview/workflows/lusid-sdk-python-preview-test/badge.svg?branch=develop) |
