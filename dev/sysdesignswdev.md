# System Design and Software Development

**Table of Contents**

- [System Design](#sysdesign)
  - [Tutorials and references](#sysdesign_tutorials)
  - [Objectives of Systems Design](#sysdesign_objectives)
  - [Requirements](#sysdesign_requirements)
  - [Models Used for System Design Life Cycle](#sysdesign_models")
- [Software Development Life Cycle (SDLC)](#swdev)
- [Workflow, Continuous Integration, Continuous Delivery, and Continuous Deployment](#cicds)
- [Microservices with Spring Boot](#microservices)

<br/>

## System Design <a name="sysdesign"></a>

### Tutorials and references <a name="sysdesign_tutorials"></a>

- [The System Design Primer](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file) by Donne Martin
- [How To Prepare For a System Design Interview](https://interviewing.io/guides/system-design-interview#what-this-guide-is-and-whom-it-s-for) by interviewing.io
- [System Design Tutorial](https://www.geeksforgeeks.org/system-design-tutorial/) by Geeks for Geeks

### Objectives of Systems Design <a name="sysdesign_objectives"></a>

Below are the main objectives of Systems Design:

- **Practicality**: We need a system that should be targetting the set of audiences(users) corresponding to which they are designing.
- **Accuracy**: Above system design should be designed in such a way it fulfills nearly all requirements around which it is designed be it functional or non-functional requirements.
- **Completeness**: System design should meet all user requirements
- **Efficient**: The system design should be such that it should not overuse surpassing the cost of resources nor under use as it will by now we know will result in low thorough put (output) and less response time(latency).
- **Reliability**: The system designed should be in proximity to a failure-free environment for a certain period of time.
- **Optimization**: Time and space are just likely what we do for code chunks for individual components to work in a system.
- **Scalable(flexibility)**: System design should be adaptable with time as per different user needs of customers which we know will keep on changing on time.

Some of the major advantages of System Design include:

- **Reduces the Design Cost of a Product**: By using established design patterns and reusable components, teams can lower the effort and expense associated with creating new software designs.
- **Speedy Software Development Process**: Using frameworks and libraries accelerates development by providing pre-built functionalities, allowing developers to focus on unique features.
- **Saves Overall Time in SDLC**: Streamlined processes and automation in the Software Development Life Cycle (SDLC) lead to quicker iterations and faster time-to-market.
- **Increases Efficiency and Consistency of a Programmer**: Familiar tools and methodologies enable programmers to work more effectively and produce uniform code, reducing the likelihood of errors.
- **Saves Resources**: Optimized workflows and shared resources minimize the need for redundant efforts, thereby conserving both human and material resources.

([Source](https://www.geeksforgeeks.org/what-is-system-design-learn-system-design/))

### Requirements <a name="sysdesign_requirements"></a>

Requirements may be divided into three categories: **Functional Requirements**, **Non-Functional Requirements**, and **Extended Requirements**.

<span style="text-decoration:underline">Functional Requirements</span>

These are the requirements that the end users specifically demand as the functionalities that MUST exist in the final product or solution when delivered. Examples are:

- What are the features that we need to design for this system?
- What are the edge cases we need to consider, if any, in our design?

<span style="text-decoration:underline">Non-Functional Requirements</span>

These are the quality constraints that the system MUST satisfy in additional to the functional requirements. They deal with issues like:

- Portability
- Security
- Maintainability
- Reliability
- Scalability
- Performance
- Reusability
- Flexibility

Examples are:

- Each request should be processed with the minimum latency?
- System should be highly valuable.

<span style="text-decoration:underline">Extended Requirements</span>

Extended requirements are "nice to have" or optional requirements that might get implemented should the resources allow. Examples are:

- The system should record metrices and analytics.
- Service heath and performance monitoring.

### Models Used for System Design Life Cycle <a name="sysdesign_models"></a>

Below are some models used for System Design Life Cycle:

- **Waterfall Model**: A linear and sequential model where each phase must be completed before moving on to the next. It's a straightforward approach but can be inflexible in the face of changing requirements.
- **Iterative Model**: Involves repeating cycles, with each iteration refining and improving the system based on feedback. It's adaptable to changing requirements.
- **Prototyping Model**: Involves building a prototype (a preliminary version) of the system to gather feedback refine the design before building the final product.
- **Spiral Model**: Incorporates elements of both iterative and prototyping models. It involves cycles of planning, designing, constructing, and evaluating.
- **Agile Model**: Emphasizes flexibility and collaboration, with frequent iterations and continuous feedback. It's well suited for projects where requirements may evolve.

My experience is that mix of the above models more or less seems more often than people think even though they say they are using a specific model for development. It also depends on the need and circumstances during the development and we pick a main model and adopt accordingly.

([Source](https://www.geeksforgeeks.org/system-design-life-cycle-phases-models-and-use-cases/#models-used-for-system-design-life-cycle))

<br/>

## Software Development Life Cycle (SDLC) <a name="swdev"></a>

The typical steps for a solution in a software development cycle are:

1. Define the requirements.
2. Determine the functional specifications.
3. Work on design and implementation (high-level and detailed designs).
4. Testing and verification.
5. Documentation (user guides and release notes)
6. Sustaining
   - Releases of minor updates, including enhancements and bug fixes
   - Hotfixes of high-priority bug fixes

<br/>

## Workflow, Continuous Integration, Continuous Delivery, and Continuous Deployment <a name="cicds"></a>

### Workflow

Using Version Control without a proper workflow is like building a city without traffic lights; without appropriate management, everything will turn into chaos.

For example, let’s say you’re working on a big project and editing a file. Another developer also starts editing a file. Both of you submit the file to the VCS at the same time. Now there’s a conflict! How should the conflict be resolved? A good workflow will have a process for resolving conflicts.

Another example is when a new junior developer is joining your team. If the project code is used for a critical system, it is risky to allow them to submit code changes directly. To solve this, many developers use a peer review system where another developer must review code before it can be merged in.

**Workflows** are essential to ensure code is managed correctly and reduce mistakes from happening. Different projects will have different workflows.

### Continuous Integration

**Continuous Integration**, or CI, is used to automate the integration of code changes from multiple developers into a single main stream. Using a workflow whereby small changes are merged frequently, often many times per day, will reduce the number of merge conflicts.

This process is widespread in test-driven software development strategies. CI is often used to automatically compile the project and run tests on every code change to ensure that the build remains stable and prevent regressions in functionality.

### Continuous Delivery

**Continuous Delivery** is an advanced practice built on top of Continuous Integration. In this approach, once changes are merged into the main codebase, a Continuous Delivery pipeline automates the process of preparing the application for deployment. This process includes tasks like building the application, running tests, and packaging it for deployment to a production-like environment.

The main goal of Continuous Delivery is to ensure that the application is always in a deployable state, even after multiple changes by different developers. By automating these steps, Continuous Delivery eliminates the risk of human errors during the packaging process and reduces delays in getting the application ready for deployment. However, Continuous Delivery requires manual approval to release the application to the production environment. Although this gives teams greater control over when and how changes are deployed to live systems, Continuous Delivery is slower than Continuous Deployment because of this manual step.

### Continuous Deployment

**Continuous Deployment** takes Continuous Delivery a step further by _automating the actual deployment of the application to production_. With this practice, every change that passes through automated tests and validations in the pipeline is automatically deployed to production without the need for manual intervention.

The strategy involves deploying to a staging environment first, where additional checks or validations might occur, and then promoting the changes to the live production environment. Unlike Continuous Delivery, Continuous Deployment eliminates the manual approval step, making it faster and more efficient. This approach ensures that updates, features, and fixes are delivered to customers as soon as they are ready, fostering rapid and iterative delivery. Continuous Deployment is ideal for teams that prioritize speed and frequent releases over manual control.

**Automation is the key difference that sets Continuous Deployment apart from Continuous Delivery.** These two deployment types can be used together in a pipeline or adopted independently, depending on the organization’s processes and requirements. When used together, the Continuous Delivery steps ensure the code is production-ready after passing all tests and reviews. The Continuous Deployment then automates the final step of deploying production-ready code without manual intervention. Using them together in a production environment provides an additional safety layer but also increases the time required.

([Source](https://www.coursera.org/learn/introduction-to-version-control/supplement/iCaLo/version-control-in-professional-software-development))

<br/>

## Microservices with Spring Boot <a name="microservices"></a>

**Microservices**, also called Microservices Architecture, is a software development approach that involves building large applications as a collection of small functional modules. This architectural approach is widely adopted due to its ease of maintenance and faster development process.

**Microservices with the Spring Boot** framework break down complex applications into _smaller services, loosely coupled services_, each focusing on a specific business capability. This architecture promotes _agility_, _scalability_, and _resilience_, leveraging technologies like Docker, Kubernetes, and _RESTful APIs_ for seamless communication and deployment in distributed environments.

<br/>

Comparisons among Monolithic, Serice-Oriented Architecture(SOA), and Microservices.

| Features                   | Monolithic                                                                            | SOA                                                                                                      | Microservices                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Structure                  | A single application where all software components are assembled and tightly coupled. | Collection of services and loosely coupled.                                                              | Collection of small services and services independently deployable.                 |
| Communication              | Within the same application, components communicate with each other.                  | Using some standardized protocols, services communicate with each other.                                 | Through some lightweight protocols, all the services communicate with each other.   |
| Scalability                | Scaling is required according to the needs of the entire application.                 | All services can be scaled independently.                                                                | All the services can be scaled independently according to the business requirement. |
| Development and Deployment | It maintains centralized development and components deployed as a single unit.        | It also maintains centralized development and here the services are deployed as monolithic applications. | It maintains decentralized development and services deployed independently.         |

<br/>

Comparisons between Serice-Oriented Architecture(SOA) and Microservices.

| Feature     | SOA                                                                                                      | Microservices                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Scope       | Enterprise-wide, integrating multiple applications                                                       | Application-specific, breaking down a single application into smaller, independent services                                |
| Granularity | Larger, more coarse-grained services, often with a single data storage layer shared by multiple services | Fine-grained, specialized services, each handling a specific business capability                                           |
| Management  | Centralized governance and management, often with an Enterprise Service Bus (ESB)                        | Decentralized governance, with each service team managing its own development and deployment                               |
| Focus       | Reusability and interoperability of services across the enterprise                                       | Independent deployability, scalability, and fault isolation                                                                |
| Example     | Integrating different business systems (like CRM, ERP, etc.) using a common set of services              | Building a complex e-commerce application with separate services for user management, product catalog, shopping cart, etc. |

#### SAGA Design Pattern

The [SAGA Design Pattern](https://www.geeksforgeeks.org/system-design/saga-design-pattern/) is a pattern used to manage long-running and distributed transactions, particularly in microservices architecture. Unlike traditional monolithic transactions, which require a single, centralized transaction management system, the SAGA pattern breaks down a complex transaction into a series of smaller, isolated operations, each handled by a different service.

<span style="text-decoration:underline">Key Concepts</span>

- **Local Transactions**: Each step in the saga is a local transaction within a single service, typically using ACID properties for that service's data store.
- **Compensating Transactions**: For each local transaction, there's a corresponding compensating transaction. If a step fails, the saga executes these compensating transactions in reverse order to undo the changes made by successful steps.
- **Eventual Consistency**: The Saga pattern aims for eventual consistency, meaning that while data might be temporarily inconsistent during a failure, it will eventually become consistent as compensating transactions are executed.

Two Approaches:

- **Choreography**: Services independently react to events published by other services, triggering their local transactions and compensating transactions.
- **Orchestration**: A central orchestrator service manages the saga, telling each service what steps to execute and when to execute compensating transactions.

When to use the Saga Pattern:

- When you need to manage long-running transactions that span multiple services.
- When you need to ensure data consistency across those services, even when failures occur.
- When you can tolerate eventual consistency rather than immediate consistency.

<span style="text-decoration:underline">Benefits</span>

- Improved Resilience: The saga pattern allows for graceful failure handling by using compensating transactions, making systems more resilient to failures.
- Loose Coupling: Orchestration-based sagas can achieve loose coupling between services, as the orchestrator manages the overall workflow, reducing dependencies.
- Increased Scalability: The asynchronous nature of sagas allows for better scalability compared to synchronous, two-phase commit approaches.

<span style="text-decoration:underline">Challenges</span>

- Complexity: Sagas can be complex to implement, especially with many services and complex business logic.
- Debugging: Tracing and debugging sagas can be challenging, particularly in choreography-based approaches.
- Eventual Consistency: While a strength, eventual consistency might not be suitable for all scenarios, requiring careful consideration.
- Single Point of Failure (Orchestration): The orchestrator in an orchestration-based saga can become a single point of failure.

#### Design patterns of Java Spring Boot Microservices

- **Service Registry and Discovery**: Services automatically register in a central registry, allowing others to identify and interact with them dynamically.
- **API Gateway**: It acts as a customer entry point and forwards requests to appropriate microservices to provide additional functionality such as authentication and rate limits.
- **Circuit Breaker**: It monitors the availability of services and protects from failures by sending requests or by providing responses if service is unavailable.
- **CQRS** (Command Query Responsibility Segregation): It separates the read and write operations. Also, it optimizes each and every operation separately for efficiency.
- **Saga Pattern**: It manages distributed tasks by organizing a sequence of local transactions.
- **Database per service**: Each of the services has separate databases. This ensures data isolation and also enables scaling and individual development.
- **Asynchronous messaging**: Each services communicate with each other through message queues like Kafka or RabbitMQ.

#### Spring Cloud for Microservices Development

- Spring Cloud Config Server: centralizes configuration management for microservices.
- Service registration and discovery using Netflix Eureka: enables dynamic service discovery and registration.
- Spring Cloud LoadBalancer: distributes traffic evenly among microservice instances.
- resilience4j-ratelimiter: implements rate limiting to maintain stability under heavy load.
- Circuit Breakers Pattern: with tools like Hystrix provides fault isolation and fallback mechanisms.

#### Circuit Breaker Pattern in Java Microservices

Circuit Breaker pattern in microservices follows fault-tolerance mechanism. It monitors and controls the interaction between different services. It dynamically manages service availability by temporarily canceling requests for failed services, prevents system overloading, and ensures graceful degradation in distributed environments. Circuit Breaker pattern typically operates in three basic states: _Closed_, _Open_, and _Half-Open_.

Some characteristics of Circuit Breaker pattern are: _Fault Tolerance_, _Resilience_, _Monitoring_, _Failure Isolation_, _Fallback Mechanism_, and _Automatic Recovery_.

#### Strangler Pattern in Micro-services

The [Strangler pattern](https://www.geeksforgeeks.org/system-design/strangler-pattern-in-micro-services-system-design/) is an architectural approach employed during the migration from a monolithic application to a microservices-based architecture.

#### Service Mesh

A [service mesh](https://www.geeksforgeeks.org/system-design/service-mesh-in-microservices/) provides a dedicated infrastructure layer for handling service-to-service communication, offering features like load balancing, security, and observability. This is again one of the most asked microservices architecture interview questions.

#### Eventual consistency in microservices

Eventual consistency is the idea that, given enough time, all updates made to a distributed system will propagate and converge to a consistent state, even though intermediate states might be inconsistent.

#### Reverse Proxy

A _reverse proxy_ plays a crucial role in a microservices architecture by acting as an intermediary between client requests and the individual microservices that make up the application. Its primary function is to handle incoming requests and route them to the appropriate microservice, based on factors such as URL paths, headers, or other criteria.

## CAP theorem

The [CAP theorem](https://www.geeksforgeeks.org/system-design/cap-theorem-in-system-design/) states that a distributed system cannot simultaneously provide Consistency, Availability, and Partition tolerance. In microservices, architects need to make trade-offs based on these factors.

### Additional Resources

- [Java Microservices Interview Questions and Answers](https://www.geeksforgeeks.org/advance-java/microservices-interview-questions/)
- [Top 50 Microservices Interview Questions](https://www.geeksforgeeks.org/system-design/top-microservices-interview-questions/)
- [Deploy a Microservices Architecture with AWS](https://www.geeksforgeeks.org/deploy-a-microservices-architecture-with-aws/)

<br/>
