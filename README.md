<!---
ws-tang/ws-tang is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

# About

Hello, thank you for visiting my GitHub site.

I am a software engineer with extensive experience in software development in Java, JakartaEE/J2EE (Spring, Hibernate, and JSF etc.), C/C++, MariaDB/MySql, and other things.

My expertise is primarily in the Operation, Administration, and Management (**OAM**) areas and includes design and implementation of whole tool suites for OAM. Although the abbreviation OAM has only three letters, OAM actually contains a lot of activities and operations under the hood as noted below.

The OAM suites that I have designed and implemented cover the whole OAM aspects of a system or a cluster of systems, including but not limited to:

- **Status Monitoring**: the status of a nodal system and a cluster of nodes, including:
  - active alarms
  - event and security logs
  - system components
  - connections between components and systems
- **System Configuration**: all kinds of configuration for the system, including:
  - server profile: CPU and memory
  - networking: IP interfaces, TCP/UDP, and TLS etc.
  - audio and video codecs
  - high availablity: enable a Primary-Backup setup to facilitate the high availability of the services
  - signaling protocols: configuration for the protocols _SIP_, _REST_, and _MRCP_ to ensure the system works properly
  - loggging: configuration for loggings such as Syslog, log throttling and filtering
- **Tools**: utilities to facilite or manage resources related to the system, including:
  - backup: handles system and application backup. The backup files can be stored locally and transferred to a designated remote locaiton. Scheduled backup operations are also available
  - restore: Restore system and/or application configuration from local or uploaded backup files
  - media resources: management of the media resourses for the system
- **Identity and Access Management**: provides the suite's own identity and access management (**IAM**), including:
  - users: user accounts for access the OAM suite. A user can get access permissions from the assigned role(s)
  - roles: roles that has access permissions for tasks in the suite
  - policies: configuration for user account settings like passwords and user session management like maximum inactive interval
- **Licensing**: application of proprietary licensing mechanism

The OAM suites consists of **user interfaces**, **business tiers**, **data stores (databases)**, and **interactions with systems and other entities in the network** via interfaces such as web services.

In short, OAM covers almost all things to make systems function properly for service excellence.

In addition to the OAM suites, I also developed and implemented:

- SOAP web services:
  - SSL certificate management, including identity and trust certificates for various system components.
  - Data queries of audio/video media processing sessions.
- Shell scripts:
  - to generate system default SSL certificates per installation.
  - to clear orphaned data entries in Postgres database.
  - to clear old entries of third-party software after upgrades from systems.
- Data replication among entities in a multi-tier distributed environment.

~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

Here is my personal repositories for software development related notes, including lab setup and side projects as well as the certificates and courses that I took.

<br/>

---

**Table of Contents**

- [Certificates and Learning](#certs_and_learning)
- [Development Environment](#dev_env)
  - [Lab Setup](#dev_env_lab_setup)
- [System Design and Software Development](#sysdesign_swdev)
- [Programming](#programming)
- [Cloud Computing](#cloud_computing)
- [Data Structures and Algorithms](#ds_and_algos)

<br/>

## Certificates and Learning <a name="certs_and_learning"></a>

Details about my professional certificates and learning is available at [doc/certsandlearning](doc/certsandlearning/certsandlearningdetails.md)

<br/>

## Development Environment <a name="dev_env"></a>

My development environment is detailed [here](dev/devenv.md).

### Source Repository and Version Control

- [Git](dev/git/gitnotes.md)

### Lab Setup <a name="dev_env_lab_setup"></a>

#### Ubuntu Linux Server

I use Ubuntu Server as the base image of my lab server. Setup details is available [here](lab/linuxBase.md).

#### Kubernetes

To set up a Kubernetes lab, one option is to use [kind](https://kind.sigs.k8s.io/). Details of my K8S lab setup with **kind** is available [here](lab/k8s/kuberneteslab.md).

#### SSL Certificates

Information for using OpenSSL for SSL certificates is available in [my SSL notes](lab/ssl/ssl.md).

<br/>

## System Design and Software Development <a name="sysdesign_swdev"></a>

My notes about system design and software development are [here](dev/sysdesignswdev.md).

<br/>

## Programming <a name="programming"></a>

- [General Notes](dev/generalnotes.md) (Java and others)
- [Spring Boot](dev/spring/springbootNotes.md)
- [JavaScript](dev/frontend/jsNotes.md)
- [HTML/CSS](dev/frontend/htmlcss.md)
- [RESTful Web Services](dev/rest/restREADME.md)
- [Python](dev/python/pythonREADME.md)
- [Golang/Go](dev/golang/golangREADME.md)
- [Apache Kafka](dev/kafka/kafkaREADME.md)
- [React](dev/react/reactREADME.md)
- [Angular](dev/angular/angularREADME.md)

<br/>

## Cloud Computing <a name="cloud_computing"></a>

- [Amazon Web Services (AWS)](dev/aws/awsnotes.md)

<br/>

# Data Structures and Algorithms <a name="ds_and_algos"></a>

See my notes about data structures and algorithms [here](dev/dsandalgos.md).

<br/>
