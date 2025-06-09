# Spring Boot Dev Notes

**Table of Contents**

- [Spring Boot](#springboot)
- [General Notes](#"sb_generalnotes")

<br/>

## Spring Boot <a name="springboot"></a>

- [Spring Boot](https://spring.io/projects/spring-boot)
-

<br/>

## Tutorials and Learning Resources <a name="sb_learning"></a>

### Spring Academy

[Spring Academy](https://spring.academy/courses) is the resources from Broadcom for Spring related topics. The listing below is a few quick selections. Access to some resources may require (free) registration to create an account.

- [Spring Boot](https://spring.academy/courses/spring-boot)
- [Building a REST API with Spring Boot](https://spring.academy/courses/building-a-rest-api-with-spring-boot)
- [Securing a REST API with OAuth 2.0](https://spring.academy/courses/spring-academy-secure-rest-api-oauth2)

<br/>

## General Notes <a name="sb_generalnotes"></a>

**Spring Boot Features**

Some of useful features of Spring Boot are:

- Auto-configuration: Spring Boot automatically configures dependencies by using `@EnableAutoconfiguration` annotation and reduces boilerplate code.
- Spring Boot Starter POM: These Starter POMs are pre-configured dependencies for functions like database, security, maven configuration etc.
- Spring Boot CLI (Command Line Interface): This command line tool is generally for managing dependencies, creating projects and running the applications.
- Actuator: Spring Boot Actuator provides health check, metrics and monitors the endpoints of the application. It also simplifies the troubleshooting management.
- Embedded Servers: Spring Boot contains embedded servers like Tomcat and Jetty for quick application run. No need of external servers.

**Advantages of using Spring Boot**

Spring Boot is a framework that creates stand-alone, production grade Spring based applications. So, this framework has so many advantages.

- Easy to use: The majority of the boilerplate code required to create a Spring application is reduced by Spring Boot.
- Rapid Development: Spring Boot's opinionated approach and auto-configuration enable developers to quickly develop apps without the need for time-consuming setup, cutting down on development time.
- Scalable: Spring Boot apps are intended to be scalable. This implies they may be simply scaled up or down to match your application's needs.
- Production-ready: Metrics, health checks, and externalized configuration are just a few of the features that Spring Boot includes and are designed for use in production environments.

**Key Components**

- Spring Boot starters
- Auto-configuration
- Spring Boot Actuator
- Spring Boot CLI
- Embedded Servers

**How Spring Boot Works**

The main steps involved in how Spring Boot works:

- Start by creating a new Spring Boot project.
- Add the necessary dependencies to your project.
- Annotate the application with the appropriate annotations.
- Run the application.

**Spring Boot Starter Dependencies**

Spring Boot provides many starter dependencies. Some common ones are listed below:

- Data JPA starter
- Web starter
- Security starter
- Test Starter
- Thymeleaf starter

**Dependency Injection**

**Dependency Injection (DI)** is a design pattern in which a class requests its dependencies from external sources rather than creating them itself. _DI promotes loose coupling and modular development, making testing easier. It also allows you to replace dependencies without changing the class that uses them._ There three types of dependency injections in Spring Boot.

- **Constructor injection**: This is the most common type of DI in Spring Boot. In constructor injection, the dependency object is injected into the dependent object's constructor.
- **Setter injection**: In setter injection, the dependency object is injected into the dependent object's setter method.
- **Field injection**: In field injection, the dependency object is injected into the dependent object's field.

**IoC Container**

An IoC ([Inversion of Control](https://www.geeksforgeeks.org/spring-ioc-container)) Container in Spring Boot is essentially _a central manager for the application objects that controls the creation, configuration, and management of dependency injection of objects_ (often referred to as beans), also referred to as a DI (Dependency Injection) container.

**Basic Spring Boot Annotations**

- `@SpringBootApplication`: This is the main annotation used to bootstrap a Spring Boot application. It combines three annotations: `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan`. It is typically placed on the main class of the application.
- `@Configuration`: This annotation is used to indicate that a class contains configuration methods for the application context. It is typically used in combination with @Bean annotations to define beans and their dependencies.
- `@Component`: This annotation is the most generic annotation for any Spring-managed component. It is used to mark a class as a Spring bean that will be managed by the Spring container.
- `@RestController`: This annotation is used to define a RESTful web service controller. It is a specialized version of the @Controller annotation that includes the @ResponseBody annotation by default.
- `@RequestMapping`: This annotation is used to map HTTP requests to a specific method in a controller. It can be applied at the class level to define a base URL for all methods in the class, or at the method level to specify a specific URL mapping.

**Starter dependency of the Spring boot module**

[Spring Boot Starters](https://www.geeksforgeeks.org/spring-boot-starters/) are a collection of pre-configured maven dependencies that makes it easier to develop particular types of applications. These starters include,

- Dependencies
- Version control
- Configuration needed to make certain features.

To use a Spring Boot starter dependency , we simply need to add it to our project's pom.xml file. For example, to add the Spring Boot starter web dependency, add the following dependency to the pom.xml file:

```
<dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

**Spring Profiles**

Spring Profiles are like different scenarios for the application depending on the environment.

- You define sets of configurations (like database URLs) for different situations (development, testing, production).
- Use the `@Profile` annotation to clarify which config belongs to where.
- Activate profiles with environment variables or command-line options.

<br/>
