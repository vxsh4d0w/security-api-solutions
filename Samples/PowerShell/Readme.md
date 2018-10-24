# Microsoft Graph Security API PowerShell Samples

This repository of PowerShell sample scripts shows how to access Security API alert resources.  They demonstrate this by making HTTPS RESTful API requests to the Microsoft Graph Security API from PowerShell.

Documentation for Microsoft Graph Security API can be found here [Graph Security Documentation](https://developer.microsoft.com/en-us/graph/docs/concepts/security-concept-overview).

These samples demonstrate security administrator or Microsoft partner actions for managing security alert resources.

The following samples are included in this repository:

- Access alerts ([Get_Security_Alerts.ps1](#1.-Get_Security_Alerts.ps1)) - Get and List
- Manage alerts ([Patch_Alerts.ps1](#2.-Patch_Alert.ps1)) - Update


The scripts are licensed "as-is." under the [MIT License](../../LICENSE).

#### Disclaimer
Some script samples retrieve information from your tenant or update data in your tenant.  Understand the impact of each sample script prior to running it; samples should be run using a non-production or "test" tenant account.

## Using the Microsoft Graph Security API

The Microsoft Graph Security API provides a unified interface and schema to integrate with security solutions from Microsoft and ecosystem partners. This empowers customers to streamline security operations and better defend against increasing cyber threats. The Microsoft Graph Security API is a federated security aggregation service that sends queries to all onboarded security providers and aggregates the responses. Use Microsoft Graph to combine information from other services and the Security API to build rich cross-service applications for IT professionals or end users.     

## Prerequisites
Use of these Microsoft Graph Security API PowerShell samples requires the following:
* Install the AzureAD PowerShell module by running 'Install-Module AzureAD' or 'Install-Module AzureADPreview' from an elevated PowerShell prompt
* An Azure tenant that supports the Azure portal with a production or trial license to [onboarded security providers](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/security-api-overview#alerts).
* An account with permissions to administer the Security administrator role.
* PowerShell v5.0 on Windows 10 x64 (PowerShell v4.0 is a minimum requirement for the scripts to function correctly)
* Note: For PowerShell 4.0 you will require the [PowershellGet Module for PS 4.0](https://www.microsoft.com/en-us/download/details.aspx?id=51451) to enable the usage of the Install-Module functionality
* First time usage of these scripts requires a Global Administrator of the Tenant to accept the permissions of the application
* Azure AD v2 App id (Native Application) from <https://apps.dev.microsoft.com> with `SecurityEvents.Read.All (Admin Only)` and `SecurityEvents.ReadWrite.All (Admin Only)` permissions.

## Getting Started
After the prerequisites are installed or met, perform the following steps to use these scripts:

#### 1. Script usage

1. Download the contents of the repository to your local Windows machine
* Extract the files to a local folder (for example, C:\SecurityAPISamples)
* Run PowerShell x64 from the start menu
* Browse to the directory (for example, cd C:\SecurityAPISamples)
* Update the `$clientId` variable with your [App id](https://apps.dev.microsoft.com).
* Example Application script usage:
  * To use the get_security_alerts scripts, from C:\SecurityAPISamples, run .\get_security_alerts.ps1 to get your top alert from all your security providers.

#### 2. Authentication with Microsoft Graph
The first time you run these scripts you will be asked to provide an account to authenticate with the service:
```
Please specify your user principal name for Azure Authentication:
```
Once you have provided a user principal name a popup will open prompting for your password. After a successful authentication with Azure Active Directory the user token will last for an hour, once the hour expires within the PowerShell session you will be asked to reauthenticate.

If you are running the script for the first time against your tenant a popup will be presented stating:

![Scopes](./readme-image/Scope.PNG)


## Sample Scripts

### 1. Get_Security_Alerts.ps1

The following functions are used within the script with example usage.

#### Get-TopAlerts Function

This function is used to get the top=1 alert from the Microsoft Graph Security API.

```PowerShell
Get-TopAlerts
```

#### Get-Alert Function

This function is used to get an alert by id from the Microsoft Graph Security API.

```PowerShell
Get-TopAlerts -ID $AlertId
```

### 2. Patch_Alert.ps1

The following functions are used within the script with example usage.

#### Test-JSON Function

This function is used to test if the JSON passed to the Patch-Alert function is valid, if the JSON isn't valid then it will return a failure otherwise it will run a PATCH request to the Graph Service.

#### Patch-Alert Function

This function is used to update a security alert by specifying the required parameter -id and -JSON.
The JSON object to be used in the patch can be found at the bottom of the script.

```PowerShell
Patch-Alert -JSON $JSON -ID $AlertId
```

## Contributing

If you'd like to contribute to this sample, see [CONTRIBUTING.MD](../../CONTRIBUTING.md).

This project has adopted the Microsoft Open Source Code of Conduct. For more information, see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Questions and comments

We'd love to get your feedback about the Security API PowerShell sample. You can send your questions and suggestions to us in the Issues section of this repository.

Your feedback is important to us. Connect with us on [Microsoft tech community](https://techcommunity.microsoft.com/t5/Using-Microsoft-Graph-Security/bd-p/SecurityGraphAPI) or [Stack Overflow](https://stackoverflow.com/questions/tagged/microsoft-graph-security
). On Stack Overflow tag your questions with [microsoft-graph-security].


## Additional resources
* [Microsoft Graph Security Documentation](https://developer.microsoft.com/en-us/graph/docs/concepts/security-concept-overview)
* [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
* [Microsoft code samples](https://developer.microsoft.com/en-us/graph/code-samples-and-sdks)
* The authentication to Microsoft Graph is leveraged from the [powershell-intune-samples](https://github.com/microsoftgraph/powershell-intune-samples).

## Copyright
Copyright (c) 2018 Microsoft. All rights reserved.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.