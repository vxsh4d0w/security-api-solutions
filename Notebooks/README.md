# Microsoft Graph Security API Jupyter Notebook Samples

This repository of Jupyter Notebook samples show how to access Microsoft Graph Security API entities using the [Jupyter Notebooks](https://jupyter.org/). 

These samples are licensed "as-is" under the [MIT License](../../LICENSE).

Refer to the following:
* [Microsoft Graph Security API Documentation](https://aka.ms/securitygraphdocs)

#### Disclaimer
These samples retrieve information from your tenant. Understand the impact of each sample prior to running it.

## What is Azure Notebooks?

Azure Notebooks is a free hosted service to develop and run Jupyter notebooks in the cloud with no installation. Jupyter is an open source project that lets you easily combine markdown text, executable code (Python, R, and F#), persistent data, graphics, and visualizations onto a single, sharable canvas called a notebook.

## How do Azure Notebooks work?
Interactive Azure Notebooks provides security insights and actions to investigate anomalies and hunt for malicious behaviors. Each Azure Notebook is purpose-built with a self-contained workflow for a specific use case. Visualizations are included in each Azure Notebook for faster data exploration. 

### Using the Notebooks locally or in other environments
You can  download the notebooks and use them locally in a supported Python environment (Anaconda Distribution is recommended) or another notebook hosting environment such as Azure Databricks or a JupyterHub environment that supports Python 3.6 or later.

## Using the Microsoft Graph Security API

The Microsoft Graph Security API provides a unified interface and schema to integrate with security solutions from Microsoft and ecosystem partners. This empowers customers to streamline security operations and better defend against increasing cyber threats. The Microsoft Graph Security API is a federated security aggregation service that sends queries to all onboarded security providers and aggregates the responses. Use Microsoft Graph to combine information from other services and the Security API to build rich cross-service applications for IT professionals or end users.     

## Getting Started
* Download the sample notebook(s) and follow the steps below to get the application ID and secret that you can use to authenticate and get data from your Azure Active Directory (Azure AD) tenant using this notebook. 
* [Register your application](https://docs.microsoft.com/en-us/graph/auth-v2-service#1-register-your-app) for this notebook in Azure AD in application only mode. 
* [Configure permissions](https://docs.microsoft.com/en-us/graph/auth-v2-service#2-configure-permissions-for-microsoft-graph) and be sure to add the SecurityEvents.ReadWrite.All permission to your application.
Get your Azure AD tenant administrator to [grant tenant administration consent](https://docs.microsoft.com/en-us/graph/auth-v2-service#3-get-administrator-consent) to your application. This is a one-time activity unless permissions change for the application. 
* Run the notebook in [Azure Notebooks](https://notebooks.azure.com/). 
* When your app is registered to call the Microsoft Graph Security API you need to pass the application ID and application secret from the above mentioned steps in to the respective notebook. 
* There are two ways to enter the application ID and secret in any one of the get_secret() functions. 
    * Hardcode it in the notebook and run the notebook. Ensure the notebook is not publicly shared in case you do so for security reasons.
    * Keep the credentials in environment variables and access these. This is recommended from a security point of view.
* While running the notebook ensure you just run one cell (function) of the get_secret() and not both. After this step you can choose to run the notebook completely. 


## Contributing

If you'd like to contribute to this sample, see [CONTRIBUTING.MD](../CONTRIBUTING.md). Create and share your example notebooks and use the guidance to create a Pull Request to share your templates and examples. We will recognize all contributions. 

This project has adopted the Microsoft Open Source Code of Conduct. For more information, see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Questions and comments

We'd love to get your feedback about the notebook samples using the Microsoft Graph Security API. You can send your questions and suggestions to us by filing a GitHub [Issue](https://github.com/microsoftgraph/security-api-solutions/issues/new) in this repository.

Your feedback is important to us. Connect with us on [Microsoft tech community](https://techcommunity.microsoft.com/t5/Using-Microsoft-Graph-Security/bd-p/SecurityGraphAPI) or [Stack Overflow](https://stackoverflow.com/questions/tagged/microsoft-graph-security). On Stack Overflow tag your questions with [microsoft-graph-security].


## Additional resources
* [Microsoft Graph Security Documentation](https://developer.microsoft.com/en-us/graph/docs/concepts/security-concept-overview)
* [Other Microsoft Graph Security Samples](https://github.com/microsoftgraph/security-api-solutions/blob/master/sample-repos.md)
* [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
* [Microsoft Graph code SDKs and samples](https://developer.microsoft.com/en-us/graph/code-samples-and-sdks)


## Copyright
Copyright (c) 2018 Microsoft. All rights reserved.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
