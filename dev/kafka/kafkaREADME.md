# Apache Kafka Notes

**Table of Contents**

- [Apache Kafka](#apache_kafka)
- [Tutorials, Documentations, and Resources](#tutorials_docs)
- [Certificate Preparation](#cert_prep)
- [Kafka Notes](#kafka_notes)

<br/>

## Apache Kafka <a name="apache_kafka"></a>

- [Apache Kafka official site](https://kafka.apache.org/)
- [Apache Kafka downloads](https://kafka.apache.org/downloads)

<br/>

## Tutorials, Documentations, and Resources <a name="tutorials_docs"></a>

### Apache Kafka

- [Quick Start](https://kafka.apache.org/quickstart)
- [Documentation](https://kafka.apache.org/documentation/) (The link leads to the documentation for the current version of Apache Kafka. As of this writing, the version is **4.0**.)

### Confluent

- [Learn Apache Kafka & Flink](https://developer.confluent.io/courses/?course=for-developers#fundamentals)
- [Introduction to Apache Kafka® 101](https://developer.confluent.io/courses/apache-kafka/events/)
- [Introduction to Kafka Connect](https://developer.confluent.io/courses/kafka-connect/intro/)
- [Introduction to Designing Events and Event Streams](https://developer.confluent.io/courses/event-design/intro/)
- [Introduction to Event Modeling](https://developer.confluent.io/courses/event-modeling/intro/)
- [Getting Started with Kafka Streams](https://developer.confluent.io/courses/kafka-streams/get-started/)
- [Designing Event Driven Microservices](https://developer.confluent.io/courses/microservices/overview/)
- [What's new in Apache Kafka 4.0?](https://www.confluent.io/blog/latest-apache-kafka-release/)

- [Apache **Kafka Fundamentals and Accreditation**](https://training.confluent.io/channeldetail/apache-kafka-fundamentals-and-accreditation)

#### Additional Reading

- [Using Apache Kafka as a Scalable, Event-Driven Backbone for Service Architectures](https://www.confluent.io/blog/apache-kafka-for-service-architectures/)
- [The Changing Face of ETL](https://www.confluent.io/blog/changing-face-etl/)
- [How to choose the number of topics/partitions in a Kafka cluster?](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster)
- [Kafka Clients](https://docs.confluent.io/current/clients/index.html)
- Optimizing your Kafka Deployment
  - https://www.confluent.io/blog/optimizing-apache-kafka-deployment/
  - https://www.confluent.io/white-paper/optimizing-your-apache-kafka-deployment/
- [Is it OK to store data in Kafka?](https://www.confluent.io/blog/okay-store-data-apachekafka/)
- [Security Tutorial](https://docs.confluent.io/current/tutorials/security_tutorial.html)
- [Kafka, Avro, Serialization and the Schema Registry](https://bit.ly/2OLUkbb)
- [Introducing Kafka Streams: Stream Processing Made Simple](https://www.confluent.io/blog/introducing-kafka-streams-stream-processing-made-simple/)
- [ksqlDB Tutorials and Examples](https://docs.confluent.io/current/ksql/docs/tutorials/index.html)
- [Manage, Monitor and Understand the Apache Kafka Cluster](https://www.confluent.io/confluent-control-center)

### Linked-In Learning

- _Complete Guide to Apache Kafka for Beginners_ by Stephane Maarek

<br/>

## Certificate Preparation <a name="cert_prep"></a>

One can find the syllabus for **Confluent Certified Developer for Apache Kafka&reg;** (CCDAK) at Confluent [web site](https://training.confluent.io/examdetail/confluent-dev). (It is the link )

<br/>

## Kafka Notes <a name="kafka_notes"></a>

### Simple Architecture View

```
Producers (1..N) <---> Brokers (1..N) <---> Consumers (1..N)
```

### Topics

- Streams of "related" Messages in Kafka
  - Is a **Logical Representation**
  - **Categorizes Messages** into Groups
- Developers define Topics
- Producer <-> Topic: N-to-N Relation
- Unlimited numbers of Topics

**A Kafka data element/record**

- Headers (optional)
- Key
- Value
- Timestamp

where **key** and **value** together contain the business relevant data.

### Broker

<span style="text-decoration:underline">Basics</span>

- Producers sends Messages to Brokers
- Brokers receive and store Messages
- A Kafka Cluster can have many Brokers
- Each Broker manages multiple Partitions

Broker manages partitions:

- Messages of Topic spread across Partitions
- Partitions spread across Brokers
- Each Broker handles many Partitions
- Each Partition is stored on Broker's disk
- Paritions: 1..N `log` files
- Each message in Log identified by _Offset_
- Configurable Retention Policy for the logs

### Producer

<span style="text-decoration:underline">Basics</span>

- Producers write Data as Messages
- Can be written in any language
  - Native: Java, C/C++, Python, Go, .NET, JMS
  - More Languages by Community
  - REST Proxy for any unsupported Language
- Command Line Producer Tool

Producers write data in the form of messages to the Kafka cluster

- Producers can be written in any language
  - Native Java, C/C++, Python, Go, .NET, JMS clients (for legacy or enterprise Java apps) are supported by Confluent
  - Clients for many other languages exist that are supported by the community
  - Confluent develops and supports a REST server which can be used by clients written in any language for which a native client does not exists
- A command-line Producer tool exists to send messages to the cluster which is useful for experimenting, testing and debugging.

#### Load Balancing and Semantic Partitioning

- Producers use a Partitioning Strategy to assign each Message to a Partition
- Two Purposes:
  - Load Balancing
  - Semantic Partitioning
- Partitioning Strategy specified by Producer
  - Default Strategy: hash(key) % number_of_partitions
  - No Key → Round-Robin
- Custom Partitioner possible

- Producers use a partitioning strategy to assign each message to a Partition
- Having a partitioning strategy serves two purposes
  - Load balancing: shares the load across the Brokers
  - Semantic partitioning: user-specified key allows locality-sensitive message processing
- The partitioning strategy is specified by the Producer
  - Default strategy is a hash of the message key
    - hash(key) % number_of_partitions
  - If a key is not specified, messages are sent to Partitions on a round-robin basis
- Developers can provide a custom partitioner class
- Load balancing: for example, round robin just to do random load balancing
- Semantic partitioning: for example, user-specified key is the user id, allows Consumers to make locality assumptions about their consumption. This style of partitioning is explicitly designed to allow locality-sensitive processing in Consumers.

#### Producer Guarantees

When using a producer, you can configure its `acks` (Acknowledgments) which default to `all`.

The acks config setting is the write-acknowledgment received count required from partition
leader before the producer write request is deemed complete. This setting controls the
producer’s durability which can be very strong (`all`) or none. Durability is a tradeoff
between _throughput_ and _consistency_. The acks setting is set to “all” (`-1`), “none” (`0`), or
“leader” (`1`).

- **Acks 0 (NONE)**: The `acks=0` is none meaning the Producer does not wait for any ack from Kafka broker at all. The records added to the socket buffer are considered sent. There are no guarantees of durability. The record offset returned from the send method is set to -1 (unknown). There could be record loss if the leader is down. There could be use cases that need to maximize throughput over durability, for example, log aggregation.
- **Acks 1 (LEADER)**: The `acks=1` is leader acknowledgment. The means that the Kafka broker acknowledges that the partition leader wrote the record to its local log but responds without the partition followers confirming the write. If leader fails right after sending ack, the record could be lost as the followers might not have replicated the record yet. Record loss is rare but possible, and you might only see this used if a rarely missed record is not statistically significant, log aggregation, a collection of data for machine learning or dashboards, etc.
- **Acks -1 (ALL)**: The `acks=all` or `acks=-1` is all acknowledgment which means the leader gets write confirmation from the full set of in-sync replicas(ISRs) before sending an ack back to the producer. This guarantees that a record is not lost as long as one ISR remains alive. This `ack=all ` setting is the strongest available guarantee that Kafka provides for durability.

This setting is even stronger with broker setting `min.insync.replicas` which specifies the minimum number of ISRs that must acknowledge a write. Most use cases will use `acks=all` and set a `min.insync.replicas > 1`.

#### Delivery Guarantees

Kafka supports 3 delivery guarantees:

- **At most once**: From all records written to Kafka it is guaranteed that there will never be a
  duplicate. Under certain bad circumstances some record may be lost
- **At least once**: From all records written to Kafka none is ever lost. Under certain bad
  situations there could be duplicates in the log
- **Exactly once**: Every single record written to Kafka will be found in the Kafka logs exactly
  once. There is no situation where either a record is lost or where a record is duplicated

#### Idempotent Producers

An idempotent producer guarantees, in collaboration with the respective broker, that:

- all messages written to a specific partition are maintaining their relative order in the
  commit log of the broker
- each message is only written once. No duplicates ever are to be found in the commit log
- together with acks=all we also make sure that no message is ever lost

#### Exactly Once Semantics

**Exactly Once Semantics (EOS)** bring strong transactional guarantees to Kafka, preventing
duplicate messages from being processed by client applications, even in the event of client
retries and Broker failures

Process:

- A producer can start a transaction
- The producer then writes several records to multiple partitions on different brokers
- The producer can then commit the transaction
- If the TX succeeds, then the producer has the guarantee, that all records have been
  written exactly once and maintaining the local ordering to the Kafka brokers
- If the TX fails, then the producer knows that none of the record written will be showing up
  -n the downstream consumers. That is, the aborted TX will leave no unwanted side effects

NOTE: To have this downstream guarantee the consumers need to set their reading behavior to **read committed**.

### Consumers

<span style="text-decoration:underline">Basics</span>

Consumers **pull** messages from 1…n topics

- New inflowing messages are automatically retrieved
- Consumer offset
  - keeps track of the last message read
  - is stored in special topic
- CLI tools exist to read from cluster

- A Consumers pulls messages from one or more Topics in the cluster. As messages are
  written to a Topic, the Consumer will automatically retrieve them
- The **Consumer Offset** keeps track of the latest message read and it is stored in a special
  Kafka Topic. If necessary, the Consumer Offset can be changed, for example, to reread
  messages
- A command-line Consumer tool exists to read messages from the Kafka cluster, which
  might be useful for experimenting, testing and debugging

**Consumer Groups**

- A consumer group consists of 1 to many consumer instances
- All consumer instances in a consumer group are identical clones of each other
- To be transparently added to a consumer group an instance needs to use the same
  group.id
- A consumer group can scale out and thus parallelize work until the number of consumer
  instances is equal to the number of topic partitions

### Data Retention Policy

How long do I want or can I store my data?

- How long (default: 1 week)
- Set globally or per topic
- Business decision
- Cost factor
- Compliance factor- such as European General Data Protection Regulation (GDPR)

Data purged per segment

### Kafka Connect

**Kafka Connect** is a part of Apache Kafka and a standardized framework for handling _import_ and _export_ of data from/to Kafka. This framework can address a variety of use cases, makes adopting Kafka much simpler for users with various data stores; encourages an ecosystem of tools for integration of other systems with Kafka using a unified interface; and provides a better user experience, guarantees, and scalability than other frameworks that are not Kafka-specific.

Kafka Connect is a pluggable framework for inbound and outbound connectors. It’s fully distributed and integrates Kafka with a number of sources and sinks. This approach is operationally simpler, particularly if you have a diverse set of other systems you need to copy data to/from as it can be holistically and centrally managed. It also pushes a lot of the hard work of scalability into the framework, so if you want to work in the Kafka Connect framework you would only have to worry about getting your data from a source into the Kafka Connect format – scalability, fault tolerance, etc would be handled intrinsically.

Most of the data systems illustrated here are supported with both Sources and Sinks (including JMS, JDBC, and Cassandra).

- **Source Connectors**: get data from common data sources to Kafka
- **Sink Connectors**: publish that data in common data stores from Kafka

**Kafka Connect** also provides parallelism and scalability:

- Splitting the workload into smaller pieces provides the parallelism and scalability
- Connector jobs are broken down into Tasks that do the actual copying of the data
- Workers are processes running one or more tasks, each in a different thread
- Input stream can be partitioned for parallelism

**A Connector is a Connector class and a configuration.** Each connector defines and updates a set of tasks that actually copy the data. Connect distributes these tasks across workers. In the case of Connect, the term partition can mean any subset of data in the source or the sink. How a partition is represented depends on the type of Connector (e.g., tables are partitions for the JDBC connector, files are the partitions for the FileStream connector).

Worker processes are not managed by Kafka. Other tools can do this: YARN, Kubernetes, Chef, Puppet, custom scripts, etc.

As with Kafka topics, the position within the partitions used by Connect must be tracked as well to prevent the unexpected replay of data. As with the partitions, the object used as the offset varies from connector to connector, as does the method of tracking the offset. The most common way to track the offset is through the use of a Kafka topic, though the Connector developer can use whatever they want.

The variation is primarily with source connectors. With sink connectors, the offsets are Kafka topic partition offsets, and they’re usually stored in the external system where the data is being written.

Running in Distributed Mode

- To run in distributed mode, start Kafka Connect on each worker node
  `$ connect-distributed connect-distributed.properties`
- Group coordination
- Connect leverages Kafka’s group membership protocol
- Configure workers with the same group.id
  - Workers distribute load within this Kafka Connect “cluster”

In distributed mode, the connector configurations cannot be kept on the Worker systems; a failure of a worker should not make the configurations unavailable. Instead, distributed workers keep their connector configurations in a special Kafka topic which is specified in the worker configuration file.

Workers coordinate their tasks to distribute the workload using the same mechanisms as Consumer Groups.

### Kafka Stream

Kafka Streams are easy **data processing and transformation library** within Kafka. Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in a Kafka cluster. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology.

- Standard Java Application
- No need to create a separate cluster
- Highly scalable, elasticm and fault tolerant
- Exactly-Once Capabilities
- One record at a time processing (no batching)
- Fully integrated with Kafka security
- Works for any application size

### Schema Registry

Schema registry provides centralized management of schemas:

- Stores a versioned history of all schemas
  - Provides a RESTful interface for storing and retrieving Avro schemas
  - Checks schemas and throws an exception if data does not conform to the schema
  - Allows evolution of schemas according to the configured compatibility setting
- Sending the Avro schema with each message would be inefficient
  - Instead, a globally unique ID representing the Avro schema is sent with each message
- The Schema Registry stores schema information in a special Kafka topic
- The Schema Registry is accessible both via a REST API and a Java API
- Command-line tools to work with Avro: `kafka-avro-console-producer` & `kafka-avroconsole-consumer`
- In addition to Command-line tools tools `kafka-avro-console-producer` & `kafka-avroconsole-consumer`, we now have protobuf and JSON Schema equivalents

The supported Schema formats are **Avro**, **Protobuf**, or **JSON**.

Schema Registry and Data Flow:

1. The message key and value can be independently serialized
1. Producers serialize data and prepend the schema ID
1. Consumers use the schema ID to deserialize the data
1. Schema Registry communication is only on the first message of a new schema
1. Producers and Consumers cache the schema/ID mapping for future messages

Available Kafka Schema Registries:

- [Confluent Schema Registry](https://developer.confluent.io/courses/apache-kafka/schema-registry/) (community version is free open-sourced with limited functionality)
- [Apicurio Registry](https://www.apicur.io/) (fully open-sourced)

Confluent schema registry related scripts like `kafka-avro-console-producer` and `kafka-avroconsole-consumer` are available at Confluent [GitHub repository](https://github.com/confluentinc/schema-registry/tree/master/bin).

**Avro** is an Apache open source project:

- Provides data serialization
- Data is defined with a self-describing schema
- Supported by many programming languages, including Java
- Provides a data structure format
- Supports code generation of data types
- Provides a container file format
- Avro data is binary, so it stores data efficiently
- Type checking is performed at write time

### Confluent REST Proxy

Confluent REST Proxy talks to non-native Kafka apps and outside the firewall.

- Provides a RESTful interface to a Kafka cluster
- Simplifies message creation and consumption
- Simplifies administrative actions

Three uses for the REST Proxy:

1. For remote clients (such as outside the datacenter including over the public internet)
1. For internal client apps that are written in a language not supported by native Kafka client libraries (i.e. other than Java, C/C++, Python, and Go)
1. For developers or existing apps for which REST is more productive and familiar than Kafka Producer/Consumer API.

Regarding _Simplifies administrative actions_, REST Proxy also allows to perform administrative actions without using the native Kafka protocol or clients.

<br/>
