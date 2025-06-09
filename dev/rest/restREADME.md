# REST Dev Notes

**Table of Contents**

- [RESTful Web Services](#restws)
- [Webhooks](#webhooks)
- [References](#references)

<br/>

## RESTful Web Services <a name="restws"></a>

### RESTful Architecture

1. **Division of State and Functionality**: State and functionality are divided into distributed resources. This is because every resource has to be accessible via normal HTTP commands.
1. **Stateless, Layered, Caching-Support, Client/Server Architecture**: A type of architecture where the web browser acts as the client, and the web server acts as the server hosting the application, is called a client/server architecture. The state of the application should not be maintained by REST. The architecture should also be layered, meaning that there can be intermediate servers between the client and the end server. It should also be able to implement a well-managed caching mechanism.

The common patterns for designing RESTful APIs are:

1. Resource-oriented design: Structuring APIs around resources and their representations.
1. Action-oriented design: Focusing on actions that can be performed on resources.
1. Collection pattern: Handling groups of resources as collections.
1. Singleton pattern: Representing single resources.

The purpose of API gateways in microservices architecture is to provide **a single entry point** for clients to interact with multiple microservices. They handle routing, composition, security, rate limiting, and monitoring, simplifying client interactions and centralizing common functionalities.

**API gateways** in microservices architecture provide a single entry point for clients to interact with multiple microservices. They handle routing, composition, security, rate limiting, and monitoring, simplifying client interactions and centralizing common functionalities.

### Principles of RESTful applications

1. **URI Resource Identification**: A RESTful web service should have a set of resources that can be used to select targets of interactions with clients. These resources can be identified by URI (Uniform Resource Identifiers). The URIs provide a global addressing space and help with service discovery.
1. **Uniform Interface**: Resources should have a uniform or fixed set of operations, such as PUT, GET, POST, and DELETE operations. This is a key principle that differentiates between a REST web service and a non-REST web service.
1. **Self-Descriptive Messages**: As resources are decoupled from their representation, content can be accessed through a large number of formats like HTML, PDF, JPEG, XML, plain text, JSON, etc. The metadata of the resource can be used for various purposes like control caching, detecting transmission errors, finding the appropriate representation format, and performing authentication or access control.
1. **Use of Hyperlinks for State Interactions**: In REST, interactions with a resource are stateless, that is, request messages are self-contained. So explicit state transfer concept is used to provide stateful interactions. URI rewriting, cookies, and form fields can be used to implement the exchange of state. A state can also be embedded in response messages and can be used to point to valid future states of interaction.

### Advantages of RESTful web services

1. **Speed**: As there is no strict specification, RESTful web services are faster as compared to SOAP. It also consumes fewer resources and bandwidth.
1. **Compatible with SOAP**: RESTful web services are compatible with SOAP, which can be used as the implementation.
1. **Language and Platform Independency**: RESTful web services can be written in any programming language and can be used on any platform.
1. **Supports Various Data Formats**: It permits the use of several data formats like HTML, XML, Plain Text, JSON, etc.

([Source](https://www.geeksforgeeks.org/restful-web-services/))

<br/>

## Webhooks <a name="webhooks"></a>

- [What is a webhook](https://www.redhat.com/en/topics/automation/what-is-a-webhook) by Redhat

<br/>

## References <a name="references"></a>

- [Web API Interview Q&As](https://www.geeksforgeeks.org/interview-experiences/web-api-interview-questions-and-answers/) by Geeks-for-Geeks

<br/>
