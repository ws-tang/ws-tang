# React.js Dev Notes

Here are my notes for React.js related topics.

**Table of Contents**

- [Development Setup](#dev_setup)
- [React](#reactjs)
- [Bootstrap](#bootstrapcss)
- [References](#references)

<br/>

## Development Setup <a name="dev_setup"></a>

**Visual Studio Code** (VS Code) is a free IDE from Microsoft. One can [download](https://code.visualstudio.com/download) it per the target platform and install it on the computer where the development takes place.

After installation of VS Code, ensure the extension **Prettier** is installed. If not, look up for the extension **Prettier** via VS Code Extensions and install it.

In addition to VS Code and its extension, also [download Node.js](https://nodejs.org/en/download) per the target platform and install it on the same computer.

Refer to the good [reference](https://handsonreact.com/docs/visual-studio-code-setup) about VS Code setup for React.

VS Code [keyboard shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) (Windows).

<br/>

## React.js <a name="reactjs"></a>

React offcial [site](https://reactjs.org/)

React builds a representation of the browser Document Object Model (**DOM**) in memory called the **virtual DOM**. As components are updated, React checks to see if the component’s HTML code in the virtual DOM matches the browser DOM. If a change is required, the browser DOM is updated. If nothing has changed, then no update is performed.

This is called the _reconciliation_ process and can be broken down into the following steps:

1. The virtual DOM is updated.
1. The virtual DOM is compared to the previous version of the virtual DOM and checks which elements have changed.
1. The changed elements are updated in the browser DOM.
1. The displayed webpage updates to match the browser DOM.

### General

<span style="text-decoration:underline">React Props</span>

- Pass data between components
- Arguments are passed like HTML attributes using JSX
- Use the keyword `props` inside functions
- Send multiple data types
- Flexible dynamic content

The component that sends the props is the **parent** component; The component that receives the props is the **child** component. This is one-directional communication from the parent to the child.

In React, it must never modify its own prompts when you declare a component using props.

#### Components

A **Component** is one of the core building blocks of React. In other words, we can say that every application you will develop in React will be made up of pieces called components. Components make the task of building UIs much easier. In React, we mainly have two types of components:

- Functional Components: Functional components are simply JavaScript functions. Initially, they were limited in terms of features like state and lifecycle methods. However, with the introduction of Hooks, functional components can now use state, manage side effects, and access other features that were once exclusive to class components.
- Class Components: Class components are more complex than functional components. They are able to manage state, handle lifecycle methods, and can also interact with other components. Class components can pass data between each other via props, similar to functional components.

| Functional Components                                                                             | Class Components                                                                              |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| A functional component is just a plain JavaScript pure function that accepts props as an argument | A class component requires you to extend from React. Component and create a render function   |
| No render method used                                                                             | It must have the render() method returning JSX                                                |
| Also known as Stateless components                                                                | Also known as Stateful components                                                             |
| React lifecycle methods (for example, componentDidMount) cannot be used in functional components. | React lifecycle methods can be used inside class components (for example, componentDidMount). |
| Constructors are not used.                                                                        | Constructor is used as it needs to store state.                                               |
| Uses hooks like useState for managing state.                                                      | Uses this.state and this.setState for state management.                                       |

A React Component can go through four stages of its life as follows.

- Initialization: This is the stage where the component is constructed with the given Props and default state. This is done in the constructor of a Component Class.
- Mounting: Mounting is the stage of rendering the JSX returned by the render method itself.
- Updating: Updating is the stage when the state of a component is updated and the application is repainted.
- Unmounting: As the name suggests Unmounting is the final step of the component lifecycle where the component is removed from the page.

#### Key

A key is a special string attribute you need to include when creating lists of elements in React. Keys are used in React to identify which items in the list are changed, updated, or deleted. In other words, we can say that keys are used to give an identity to the elements in the lists.

#### Hooks

Hooks let developers use state and other React features without writing a class. Hooks provide a direct API to react concepts such as props, state, context, refs and life-cycle.

The most used hook in React is the `useState()` hook. Using this hook we can declare a state variable inside a function but only one state variable can be declared using a single `useState()` hook. Whenever the `useState()` hook is used, the value of the state variable is changed and the new variable is stored in a new cell in the stack.

Syntax:
`const [state, setState] = useState(initialState);`

- state: The current state value.
- setState: A function used to update the state value.
- initialState: The initial value of the state.

<br/>

## Bootstrap <a name="bootstrapcss"></a>

[**Bootstrap**](https://getbootstrap.com/) is a _library_ of CSS and JavaScript code that you can combine to quickly build visually appealing websites.

Modern web development is all about **components**. Small pieces of reusable code that allow you to build websites quickly. Bootstrap comes with multiple components for very fast construction of multiple components, or parts of components.

Another important aspect of modern development is **responsive grids** which allow web pages to adapt their layout and content depending on the device in which they are viewed. Bootstrap comes with a pre-made set of CSS rules for building a responsive grid.

Bootstrap is very popular amongst developers as it saves development time and provides a way for developers to build visually appealing prototypes and websites.

Bootstrap saves significant time because all the CSS code that styles its grid and pre-built components is already written. Instead of needing a high level of expertise in various CSS concepts, you can simply use the existing Bootstrap CSS classes to create visually appealing websites. This is indispensable when you need to quickly iterate on website layouts. ([Source](https://www.coursera.org/learn/introduction-to-front-end-development/supplement/EZ1Eu/bootstrap).)

Use Bootstrapt CDN reference for CSS

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
```

Use Bootstrapt CDN reference for JavaScript

```
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
```

<br/>

## References <a name="references"></a>

- [HTML Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) by **Mozilla**
- [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) by **Mozilla**
- [HTML and CSS: Design and build websites](https://www.amazon.com/HTML-CSS-Design-Build-Websites/dp/1118008189/) by Jon Duckett
- [Responsive Web Design with HTML5 and CSS](https://www.amazon.com/Responsive-Web-Design-HTML5-CSS/dp/1839211563/) Book by Ben Frain

<br/>
