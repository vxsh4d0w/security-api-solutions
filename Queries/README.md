# Curated Sample Queries 
This repository of curated sample queries illustrates how to access Microsoft Graph Security API alerts pertaining to different scenarios for security management, investigations, and hunting. Refer to the [benefits](https://docs.microsoft.com/en-us/graph/security-concept-overview#benefits-of-using-the-microsoft-graph-security-api) of using Microsoft Graph Security API for all scenarios these queries can apply to. Microsoft Graph Security API uses ODATA queries to query and get entity specific information. 
These samples are licensed "as-is" under the [MIT License](https://github.com/microsoftgraph/security-api-solutions/blob/LICENSE).

Refer to the following:
* [Microsoft Graph Security API Documentation](https://aka.ms/securitygraphdocs)
* [Microsoft Graph ODATA query options](https://docs.microsoft.com/en-us/graph/query-parameters)
* [Microsoft Graph Security alert Schema](https://docs.microsoft.com/en-us/graph/api/resources/alert?view=graph-rest-1.0)
* [Querying Microsoft Graph Security alerts](https://docs.microsoft.com/en-us/graph/api/alert-list?view=graph-rest-1.0&tabs=cs)

# Disclaimer
These samples retrieve information from your tenant. Understand the impact of each sample prior to running it.

# Using the Microsoft Graph Security API
The Microsoft Graph Security API provides a unified interface and schema to integrate with security solutions from Microsoft and ecosystem partners. This empowers customers to streamline security operations and better defend against increasing cyber threats. The Microsoft Graph Security API is a federated security aggregation service that sends queries to all onboarded security providers and aggregates the responses. Use Microsoft Graph to combine information from other services and the Security API to build rich cross-service applications for IT professionals or end users.

# Getting Started with the list of curated queries 
We have a starting set of curated queries listed in the table below. Read the guidance and copy / paste the queries to use in your application or try on [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) or any Microsoft Graph Security [connection option](https://docs.microsoft.com/en-us/graph/security-concept-overview#why-use-the-microsoft-graph-security-api). Modify the queries as needed per your scenario or variations suggested. 

## Guidance
* Microsoft Graph Security alerts are across different security products per the [provider support matrix](https://aka.ms/graphsecurityalertschema). For example,  alerts pertaining to a certain user will come from multiple security products like Azure Security Center, Microsoft Cloud App Security, etc. Getting alerts from multiple solutions helps with easier correlation of alerts across different security products running on your Azure Active Directory tenant.
* Multiple [ODATA query options](https://docs.microsoft.com/en-us/graph/query-parameters) can be mixed in with the following scenarios to come up with new additional scenarios per your needs. 
* For each of the following scenarios, the query starts with /security/alerts/. Ensure to prefix each query with “https://graph.microsoft.com/v1.0/”  to correctly identify the endpoint. You can also target the public preview endpoint by “https://graph.microsoft.com/beta/” 
* Refer to the [Microsoft Graph Security alert Schema](https://docs.microsoft.com/en-us/graph/api/resources/alert?view=graph-rest-1.0) to build out your own queries using these as an example and feel free to contribute other queries to add to this table per the guidance at [CONTRIBUTING.MD](https://github.com/microsoftgraph/security-api-solutions/blob/master/CONTRIBUTING.md)
* When using these queries in the [Microsoft Graph Security API connector](https://aka.ms/graphsecurityconnectors) for [Azure Logic Apps](https://docs.microsoft.com/azure/logic-apps/logic-apps-overview), [Microsoft Flow](https://flow.microsoft.com/), and [PowerApps](https://powerapps.microsoft.com/), just use the query option construct. For example, Filter alerts value for ‘Get Alerts’ action, is <b> Severity eq 'high' </b> or <b> vendorInformation/provider eq 'ASC' </b>, etc.

| Scenarios                 | 	Query                                   |   Variations                  |
|:--------------------------|:------------------------------------------|:------------------------------|
| Most recent 3 alerts from each security provider	| /security/alerts?$top=3	| Substitute 3 by any number |
| Alerts created in a certain time interval	| /security/alerts?$filter=createdDateTime gt 2019-04-01T00:00:00.000Z and createdDateTime lt 2019-05-05T00:00:00.000Z | Change date time (e.g. 2019-04-01T00:00:00.000Z) accordingly and/or use just eq, gt and lt |
| Alerts with high severity  	| /security/alerts?$filter=severity eq 'high'	| Substitute high with medium, low, informational, or unknown to get other severities |
| Alerts with high severity in a certain time interval	| /security/alerts?$filter=createdDateTime gt {enter start datetime} and createdDateTime lt {enter end datetime} and severity eq 'high'|
| Alerts from specific providers| /security/alerts?$filter=vendorInformation/provider eq 'ASC' | 	Change provider value to get other variations. For e.g. IPC, WDATP, etc. |
| Active / Unresolved alerts	| /security/alerts?$filter=status ne 'resolved'	| Change resolved to newAlert, inProgress or unknown to get other alert status | 
| Alerts not assigned for investigations | 	/security/alerts?$filter=assignedTo eq ''	| Change assignedTo to the name of the analyst to query by alerts assigned to someone for investigation | 
| Alerts by user principal name  | 	/security/alerts? $filter=userStates/any(a:a/userPrincipalName eq 'enter the user principal name')	| | 
| Alerts where user is a sender	| /security/alerts?$filter=userStates/any(a:a/emailRole eq 'sender')	| Change emailRole to other values ‘unknown’ or ‘recipient’ | 
| Alerts by host or machine internal IP	| /security/alerts?$filter=hostStates/any(a:a/privateIpAddress eq 'enter the IP address')	| The same query can work with publicIPAddress by swapping out privateIPAddress | 
| Alerts by host FQDN (Fully Qualified Domain Name)	| /security/alerts?$filter=hostStates/any(a:a/fqdn eq 'enter the FQDN')	|  | 
| Alerts pertaining to a compromised file  | 	/security/alerts?$filter=fileStates/any(a:a/name eq 'enter the file name') |  | 	
| Alerts tagged by HVA| 	/security/alerts?$filter=tags/any(a:a eq 'HVA')	 |  | 
| Alerts where the file is hashed MD5	| /security/alerts?$filter=fileStates/any(a:a/fileHash/hashType eq 'md5')	| Swap out the md5 hashType with unknown, sha1, sha256, authenticodeHash256, lsHash, ctph, peSha1 or peSha256 | 
| Alerts pertaining to trojan malware | 	/security/alerts?$filter=malwareStates/any(a:a/category eq 'trojan') |  | 
| Alerts where registry values were created, modified or deleted (applicable to Windows machines)| /security/alerts?$filter=RegistryKeyStates/any(a:a/operation ne 'unknown')	| Change blanks to create, modify or delete to get specific registry operation info  | 
| Alerts where the detected vulnerability file was running at the time of detection | 	/security/alerts?$filter=vulnerabilityStates/any(a:a/wasRunning eq true) | | 
| Alerts with untrusted process integrity level   | /security/alerts?$filter=processes/any(a:a/integrityLevel eq 'untrusted')	| Use other integrityLevel like unknown, low, medium, high or system |
| Alerts with a certain destination domain 	| /security/alerts?$filter=networkConnections/any(a:a/destinationDomain eq 'enter destination domain')	| | 

# Contributing
If you'd like to contribute more queries, see [CONTRIBUTING.MD](https://github.com/microsoftgraph/security-api-solutions/blob/master/CONTRIBUTING.md). Create and share your example queries and use the guidance to create a Pull Request to share your queries. You will earn [recognition](https://github.com/microsoftgraph/security-api-solutions#recognition-program) for all contributions.
This project has adopted the Microsoft Open Source Code of Conduct. For more information, see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.
Questions and comments
We'd love to get your feedback about these sample curated queries using the Microsoft Graph Security API. You can send your questions and suggestions to us by filing a GitHub [Issue](https://github.com/microsoftgraph/security-api-solutions/issues/new) in this repository.

# Additional resources
* [Microsoft Graph Security Documentation](https://developer.microsoft.com/en-us/graph/docs/concepts/security-concept-overview)
* [Other Microsoft Graph Security Samples](https://github.com/microsoftgraph/security-api-solutions/blob/master/sample-repos.md)
* [ODATA V4.0 Conventions](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html)
* [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
* [Microsoft Graph code SDKs and samples](https://developer.microsoft.com/en-us/graph/code-samples-and-sdks)

# Copyright
Copyright (c) 2019 Microsoft. All rights reserved.
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact opencode@microsoft.com with any additional questions or comments.
