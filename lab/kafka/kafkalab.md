# Set up a lab for Apache Kafka

Refer to [**Setup the Lab Environment with a Linux Server**](../linuxBase.md) for the base lab Linux environment.

<br/>

## Set up Apache Kafka

([Source](https://kafka.apache.org/quickstart))

_Step 1: Get Kafka_

Download the latest Kafka release and extract it:

```
$ tar -xzf kafka_2.13-4.0.0.tgz
$ cd kafka_2.13-4.0.0
```

_Step 2: Start the Kafka environment_

Using JVM Based Apache Kafka Docker Image

2.1 Get the Docker image:

```
$ docker pull apache/kafka:4.0.0
```

2.2 Start the Kafka Docker container:

```
$ docker run -dp 9092:9092 apache/kafka:4.0.0
```

2.3 Access the shell of the docker container

Run the command `docker container ls` to get the **container Id**. Then use the command `docker exec -it` with the **container Id** to access the shell environment of the docker container of Apache Kafka.

<pre>
root@ubuntu24:/opt/docker/kafkadev2# docker container ls
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                         NAMES
<b>f30adc8973c7</b>   apache/kafka:4.0.0   "/__cacert_entrypoin…"   2 minutes ago   Up 2 minutes   0.0.0.0:9092->9092/tcp, [::]:9092->9092/tcp   sweet_lichterman

root@ubuntu24:/opt/docker/kafkadev2# docker exec -it <b>f30adc8973c7</b> /bin/bash
</pre>

<br/>

## Hands-on Lab Exercises

From the online (free) course [Apache Kafka Fundamentals and Accreditation](https://training.confluent.io/channeldetail/apache-kafka-fundamentals-and-accreditation) from **Confluent**, it offers a number of hands-on lab exercises for Apache Kafka. One can register then access the **exercise book** from the free course.

Confluent schema registry related scripts like `kafka-avro-console-producer` and `kafka-avroconsole-consumer` are available at Confluent [GitHub repository](https://github.com/confluentinc/schema-registry/tree/master/bin)

<br/>
