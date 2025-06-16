# Angular Dev Notes

Here are my notes for Angular related topics.

**Table of Contents**

- [Angular](#angular)
- [General Notes](#angular_generalnotes)

<br/>

## Angular <a name="angular"></a>

- [Angular](https://angular.dev/)
- [Angular versioning and releases](https://angular.dev/reference/releases)
- [Angular Tutorials](https://angular.dev/tutorials)
- [Angular Documentations](https://angular.dev/overview)

<br/>

## General Notes <a name="angular_generalnotes"></a>

**Components**

A **component** is a fundamental building block of Angular applications. It controls a part of the user interface and manages the data and logic for that section. Components are used to create reusable UI elements and define the structure and behavior of the app. The purpose of `@Component` decorator in Angular.

- Defining the Component: It designates a class as an Angular component and provides metadata about the component.
- Template Association: Links the component with its HTML template, defining the view.
- Style Binding: Associates the component with its CSS styles to encapsulate and manage styling.
- Selector Definition: Defines a custom HTML tag (selector) that represents the component in the application.
- Dependency Injection Configuration: Specifies the providers for the component, providing dependency injection.

**Modules**

A module is a logical unit of the application that groups related components, directives, pipes, and services. It helps organize and manage the application by encapsulating functionality into cohesive blocks.

**Angular CLI**
[Angular CLI](https://www.geeksforgeeks.org/angular-cli-angular-project-setup/) (Command Line Interface) is a powerful tool that helps automate and streamline the development process for Angular applications. It provides a set of commands for creating, managing, and building Angular projects. Common Angular CLI commands include:

- `ng new`: Creates a new Angular project.
- `ng serve`: Serves the application locally.
- `ng generate`: Generates components, services, and more.
- `ng build`: Builds the application for production.

**Directives**

[Directives](https://www.geeksforgeeks.org/angular-js/angularjs-directives/) are special markers on a DOM element that tell Angular to do something to that DOM element or its children. Directives are used to extend HTML functionality by adding behavior to elements, such as manipulating their attributes or styling.

**Services**

A [service](https://www.geeksforgeeks.org/angular-js/angularjs-services/) is a class that encapsulates reusable logic, which can be shared across different components of an Angular application. Services are typically used for data fetching, business logic, and other operations that need to be shared.

**Angular Lifecycle Hooks**

[Angular lifecycle hooks](https://www.geeksforgeeks.org/angular-js/component-lifecycle-in-angular/) are methods that allow developers to tap into key moments in a component’s lifecycle. Key hooks include `ngOnInit` (called once when the component is initialized), `ngOnChanges` (called when input properties change), and `ngOnDestroy` (called before Angular destroys the component).

**Routers**

The Angular router is a library that enables navigation between different views or pages in a single-page application (SPA). It allows developers to define routes, handle URL changes, and load components dynamically based on the route, providing a smooth and efficient user experience without page reloads.

**Types of DOMs in Angular**

Angular uses the _Real DOM_ (Document Object Model). The _Change Detection_ mechanism is used to update only the affected parts of the DOM when data changes, improving performance. In addition, Angular uses a _Shadow DOM_ for encapsulation, which helps isolate styles and behavior of components.

- Real DOM: Updates the entire DOM when changes occur.
- Change Detection: Optimizes updates to only parts of the DOM that need re-rendering.
- Shadow DOM: Provides component style and behavior encapsulation.

**Bootstrap in Angular**

In Angular, bootstarp can be implemented by the two ways:

- Using npm (Recommended): Install Bootstrap via npm and import it into the angular.json file under the "styles" and "scripts" arrays.
- Using CDN (Content Delivery Network): Instead of installing Bootstrap locally, you can link to Bootstrap's CSS and JS files directly from a CDN in your index.html file:

**Data Passage in Angular**

Data can be passed between components using `Input` and `Output` decorators, **services**, or **router state**.

**MVVM architecture in Angular**

**MVVM (Model-View-ViewModel)** is a software architectural pattern that is commonly used in Angular applications, providing a clean separation of concerns between different components of an application. This ensures that changes in one part of the application (like in the logic or data) do not directly affect or interfere with the user interface.

- Model:

  - Represents the application's data and logic.
  - It is the part of the application that manages the state, and it can be composed of services, APIs, or even simple objects.
  - In Angular, the Model can be represented by services or interfaces that fetch data from a database or API and expose methods for interacting with that data.

- View:

  - Represents the UI (user interface) elements that the user interacts with, such as buttons, inputs, forms, etc.
  - In Angular, the View is typically defined using HTML and CSS, and it's tied to the template of a component.
  - The view listens for changes in the ViewModel and displays updated data to the user.

- ViewModel:
  - This is the key part of MVVM in Angular. It acts as a bridge between the Model and View.
  - The ViewModel holds the data and logic needed to present the Model’s data in a way that the View can easily display.
  - It is represented by the component in Angular, which binds the data and defines the behavior that will be reflected in the view.
  - Angular’s two-way data binding (via ngModel) allows the ViewModel to automatically synchronize with the View, enabling automatic updates when data changes.

**Pipes**

A pipe is a way to transform data in the template. It allows you to format or manipulate data before displaying it to the user. Angular provides several built-in pipes like DatePipe, UpperCasePipe, and CurrencyPipe, and you can also create custom pipes. Pipes are typically used to modify the display of data without altering the original data itself.

**Angular interceptors**

Angular interceptors are services that intercept and modify HTTP requests and responses. They allow you to perform actions such as adding headers (e.g., authentication tokens), logging, or handling errors globally. Interceptors are useful for managing HTTP communication centrally in Angular applications.

**NgZone**

NgZone in Angular is a service that helps Angular know when to update the view by tracking asynchronous operations. It runs change detection whenever an asynchronous operation, like a setTimeout or HTTP request, completes. NgZone ensures that Angular is aware of changes in the application state and triggers the necessary updates to the view.

**Difference between @Input() and @Output()**

| Decorator   | Purpose                                    | Example                                               |
| ----------- | ------------------------------------------ | ----------------------------------------------------- |
| `@Input()`  | Pass data from parent to child component   | `<child [childData]="parentData"></child>`            |
| `@Output()` | Emit events from child to parent component | `<child (childEvent)="parentMethod($event)"></child>` |

**Authentication in Angular**

Authentication can be implemented using **JWT tokens**, **Angular guards**, and **interceptors** to manage login and secure routes.

**Functional Components**

Functional components focus purely on rendering UI based on inputs and outputs, without requiring a class structure. This approach brings a more functional programming style to Angular, making it easier to write and test components with better performance, especially for simple and reusable components.

**Angular Elements**

- Web Component Integration: Allows Angular components to be packaged as custom elements (web components) that can be used in any HTML page or framework.
- Reusability: Enables the reuse of Angular components across different projects and frameworks, providing code sharing and consistency.
- Interoperability: Provides the integration of Angular components into non-Angular applications, enhancing flexibility and compatibility.
- Encapsulation: Provides encapsulated, self-contained components that encapsulate their logic, styles, and templates, reducing the risk of conflicts in larger applications.

**RxJS**
**RxJS (Reactive Extensions for JavaScript)** is a library for reactive programming that uses observables to work with asynchronous data streams. It's a core part of Angular, providing a way to handle asynchronous operations, events, and data streams in a more streamlined and declarative manner.
Key Concepts:

- Observables: Represent a stream of data over time. They can emit multiple values, complete, or emit an error.
- Observers: Subscribe to observables and react to emitted values, errors, or completion signals.
- Operators: Functions used to manipulate, transform, filter, and combine observables.
- Subjects: Special types of observables that can act as both an observable and an observer.

**Dependency Injection**

**Dependency Injection (DI)** is a design pattern in which a class requests its dependencies from external sources rather than creating them itself. It is a core concept in Angular that helps to keep components clean and focused on their specific tasks. Here are some key concepts of DI in Angular:

- Dependencies: Services or other resources a component needs to function.
- Dependency Provider: The entity that supplies a specific dependency.
- Dependency Consumer: The component or service that requests and consumes the provided dependency.
- Constructor injection: The most common approach, where dependencies are listed in the component's constructor.
- Injector: Angular's DI system manages the creation and provision of dependencies. It maintains a hierarchy of injectors, with the root injector at the top. When a component requests a dependency, the injector looks for the required service in its hierarchy and provides it.
- `@Injectable`: Used to mark a class as injectable, allowing it to be managed by Angular's dependency injection system.
- `@Inject`: Used to specify the token (dependency) to be injected into a class constructor or a provider definition.

_DI promotes loose coupling and modular development, making testing easier. It also allows you to replace dependencies without changing the class that uses them._

<br/>
