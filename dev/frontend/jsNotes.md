# JavaScript Dev Notes

**Table of Contents**

- [Dev Environment Setup](#js_devsetup)
- [General Notes](#js_generalnotes)
- [References](#js_references)

<br/>

## Dev Environment Setup <a name="js_devsetup"></a>

**Visual Studio Code** (VS Code) is a free IDE from Microsoft. One can [download](https://code.visualstudio.com/download) it per the target platform and install it on the computer where the development takes place.

After installation of VS Code, ensure the extension \*_Code Runner_ is installed. If not, look up for the extension Code Runner and install it.

In addition to VS Code and its extension, also [download Node.js](https://nodejs.org/en/download) per the target platform and install it on the same computer.

<br/>

## General Notes <a name="js_generalnotes"></a>

<span style="text-decoration:underline">Differences between TypeScript and JavaScript</span>

|                | TypeScript                                                                                                                                                                                                                       | JavaScript                                                                                                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Typing         | Statically typed. Types are checked during compilation, catching errors early and improving code maintainability. TypeScript is a superset of JavaScript, meaning it includes all of JavaScript's features while adding its own. | Dynamically typed. Variable types are checked during runtime, allowing flexibility but potentially leading to runtime errors.                                                |
| Features       | An enhanced version of JavaScript that adds features like interfaces, classes, enums, and generics. It compiles to JavaScript, allowing it to run in any JavaScript environment.                                                 | A scripting language primarily used for front-end web development, but also runs on the server using Node.js. It is interpreted, meaning that code is executed line by line. |
| Error Handling | Errors are often detected during compilation, allowing for earlier detection and resolution.                                                                                                                                     | Errors are typically detected during runtime, which can make debugging more challenging.                                                                                     |
| Scalability    | Designed for scalability, with features that help manage complex projects and ensure code consistency.                                                                                                                           | Suitable for small to medium-sized projects but can become difficult to manage for large codebases.                                                                          |
| Syntax         | Extends JavaScript syntax by adding type annotations, allowing developers to declare variable types.                                                                                                                             | Uses a dynamic syntax, where variable types can change during runtime.                                                                                                       |
| Compilation    | Requires a compilation step to convert the TypeScript code to JavaScript before it can be executed.                                                                                                                              | Does not require a compilation step, and can be run directly in a web browser or other JavaScript environments.                                                              |
| Performance    | TypeScript's performance is primarily related to its type-checking speed during compilation, not runtime performance.                                                                                                            | Performance is generally good but can be impacted by dynamic typing and complex operations.                                                                                  |
| Learning Curve | Has a steeper learning curve because of its added features and static typing.                                                                                                                                                    | Easier to learn initially, especially for beginners.                                                                                                                         |

<br/>

**When Should You Use TypeScript?**

- Error Prevention: TypeScript catches errors at compile time, reducing the likelihood of runtime issues. This is particularly valuable in large projects where debugging can become time-consuming.
- Static Typing: With TypeScript, you can define types for variables, functions, and objects, which makes your code more predictable and easier to maintain. This is especially useful in team environments where consistency is key.
- Scalability: If you're working on a large project or planning to scale your application, TypeScript’s features like interfaces, enums, and generics can help manage complexity.

**When to Stick with JavaScript?**

- Simplicity and Speed: JavaScript is faster to get started with, especially for smaller projects or when you need to build something quickly. Since it's dynamically typed, you can write less code without worrying about types.
- Familiarity: If you're already comfortable with JavaScript and working on smaller projects, there might not be an immediate need to switch to TypeScript.

**Advantages of using TypeScript over JavaScript**

- TypeScript always points out the compilation errors at the time of development (pre-compilation). Because of this getting runtime errors is less likely, whereas JavaScript is an interpreted language.
- TypeScript supports static/strong typing. This means that type correctness can be checked at compile time. This feature is not available in JavaScript.
- TypeScript is nothing but JavaScript and some additional features i.e. ES6 features. It may not be supported in your target browser but the TypeScript compiler can compile the .ts files into ES3, ES4, and ES5 also.

**Disadvantages of using TypeScript over JavaScript**

- Compilation Time: TypeScript needs to be compiled to JavaScript, which can add an extra step to your development process.
- Learning Curve: While TypeScript’s additional features are powerful, they require time to learn and master.

([Source](https://www.geeksforgeeks.org/difference-between-typescript-and-javascript/))

<br/>

<span style="text-decoration:underline">Differences between **var** and **let**</span>

Both var and let are used to declare variables, but they differ in their scope. var is function-scoped, meaning it is accessible throughout the entire function where it is declared. let, on the other hand, is block-scoped, meaning it is only accessible within the block (e.g., inside an if statement or a loop) where it is declared.

- Scope: The primary difference lies in how variables are accessible. var variables are defined within the entire function they are declared in, regardless of where they are declared within that function. let variables, however, are limited to the block in which they are declared, meaning they are only available within that specific block of code.
- Hoisting: Both var and let are hoisted to the top of their respective scopes. However, var is hoisted and initialized with a default value of undefined, while let is also hoisted but is not initialized, leading to the "temporal dead zone" where trying to access it before declaration will result in a ReferenceError.
- Redeclaration and Reassignment: var variables can be redeclared within their scope, while let variables cannot be redeclared in the same scope. Both var and let variables can be reassigned.
- Best Practices: In modern JavaScript development, it's generally recommended to prefer let and const over var because they offer more predictable and controlled scoping behavior.

--

For `let` and `const`:

- Can't be used before it is declared
- Variable can't be redeclared
- It's scoped to the block

Variables declared with const must be assigned during declaration. If values can be reassigned, use `let`. If values don't change, use `const`.

--

**Use the backtick ` in JavaScript**

In JavaScript, the backtick symbol (\`) is used to define template literals (also known as template strings). Template literals offer a more flexible and readable way to create strings compared to single or double quotes.

Here are the primary use cases for template literals:

<span style="text-decoration:underline">String Interpolation</span>

Template literals allow you to embed expressions directly within a string using the ${expression} syntax. This makes it easy to include variables, function calls, or any other JavaScript expression inside a string without the need for concatenation.
JavaScript

```
const name = "Alice";
const age = 30;
const message = `My name is ${name} and I am ${age} years old.`;
console.log(message); // Output: My name is Alice and I am 30 years old.
```

<span style="text-decoration:underline">Multiline Strings</span>

Template literals can span multiple lines without requiring special escape characters. This is useful for creating strings containing HTML fragments or other multiline text.
JavaScript

```
const html = `

  <div>
    <h1>Hello</h1>
    <p>This is a multiline string.</p>
  </div>
`;
console.log(html);
```

<span style="text-decoration:underline">Tagged Templates</span>

Template literals can be used with a function name as a tag, allowing you to customize how the string is processed. This is useful for tasks like sanitizing user input or formatting strings in a specific way.

```
function highlight(strings, ...values) {
    let result = "";
    for (let i = 0; i < strings.length; i++) {
        result += strings[i];
        if (i < values.length) {
            result += `<b>${values[i]}</b>`;
        }
    }
    return result;
}

const name = "Bob";
const age = 25;
const highlightedMessage = highlight`My name is ${name} and I am ${age} years old.`;

console.log(highlightedMessage); // Output: My name is <b>Bob</b> and I am <b>25</b> years old.
```

In summary, backticks in JavaScript provide a powerful way to create strings with embedded expressions, multiline support, and the ability to customize string processing using tagged templates, making them a valuable tool for modern JavaScript development.

### Errors

**Best Practices for Handling Errors**

- Use Try-Catch Blocks: To handle predictable runtime errors gracefully
- Validate Inputs: Helps prevent invalid operations by checking inputs
- Use Specific Error Types: Throw custom errors where necessary, for clarity

**Distinguishing factors between Error Types**

- Syntax Errors: Prevent code execution due to invalid syntax
- Logical Errors: Allow execution but cause incorrect output
- Runtime Errors: Occur during execution and halt the program unless handled

### Functional Programming

A common coding-style/paradigm is called **functional programming**, or FP for short.

**In functional programming, we use functions extensively and often work with immutable values. Immutability is a key principle, meaning variables are not modified after their initial assignment.**

```
function getTotal(a,b) {
    return a + b
}
var num1 = 2;
var num2 = 3;

var total = getTotal(num1, num2);
```

When writing FP code, we keep data and functionality separate and pass data into functions only when we want something computed.

There are many more concepts and ideas in functional programming. Here are some of the most important ones:

- First-class functions
- Higher-order function
- Pure functions and side-effects

**First-class functions**

It is often said that functions in JavaScript are “first-class citizens”, which means that _a function in JavaScript is just another value that we can_:

- pass to other functions
- save in a variable
- return from other functions

In other words, a function in JavaScript is just a value - from this vantage point, almost no different from a string or a number. In JavaScript, it's normal to pass a function or its invocation as an argument to another function.

**Higher-order functions**

A higher-order function is a function that has either one or both of the following characteristics:

- It accepts other functions as arguments
- It returns functions when invoked, treating them as values

**Pure functions and side-effects**

A pure function returns the exact same result as long as it's given the same values.

Another rule for a function to be considered pure is that it should not have side-effects. A side-effect is any instance where a function makes a change outside of itself. This includes:

- changing variable values outside of the function itself, or even relying on outside variables
- calling a Browser API (even the console itself!)
- calling Math.random() since the value cannot be reliably repeated

### Spread and Rest

Spread Operator:

- **Expands** arrays, objects, or strings into individual elements or properties.
- Used for concatenation, copying, or passing arguments.

Rest Operator:

- **Gathers** multiple elements into a single array or object.
- Used in destructuring or collecting function arguments.

<br/>

## Testing

[Jest](https://jestjs.io/) is a JavaScript testing framework used to verify the correctness of JavaScript code. It's known for its simplicity, ease of use, and ability to work with various JavaScript projects like Babel, TypeScript, Node.js, React, Angular, and Vue

- [Getting Started](https://jestjs.io/docs/getting-started)
- [Guides](https://jestjs.io/docs/snapshot-testing)

Using Jest with:

- Code coverage
- Mocking
- Snapshot testing

Additional Resources:

- [Unit testing in JavaScript](https://www.browserstack.com/guide/unit-testing-in-javascript)

<br/>

## References

<span style="text-decoration:underline">MDN: Mozilla Developer Network</span>

- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
- [Guidelines for writing JavaScript code examples](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript)
- [JavaScript Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) by
- [Regular Expressions in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
- [Rest syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

<br/>

<span style="text-decoration:underline">Others</span>

- [ECMA262 Specification](https://tc39.es/ecma262/)

<br/>
