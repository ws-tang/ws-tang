# General Development Notes

**Table of Contents**

- [Programming Language - Java](#programming_java)
- [Programming Language - C](#programming_c)
- [Gradle](#gradle)
- [Linux Platform](#linux_platform)
- [Markdown](#markdown)

<br/>

## Programming Language - Java <a name="programming_java"></a>

### General

- [A quick summary for the differences between Java 8, 11, 17, and 21](https://medium.com/@a.r.m.monesan_9577/java-8-vs-java-11-vs-java-17-vs-java-21-a-comprehensive-comparison-aa4635f9c3fe)

<br/>

[**Redhat OpenJDK support for Java LTS versions**](https://access.redhat.com/articles/1299013)

| OpenJDK Version | End of Full Support Date |
| --------------- | ------------------------ |
| 8               | November 30, 2026        |
| 11              | October 31, 2024         |
| 17              | October 31, 2027         |
| 21              | December 31, 2029        |

### Stream

[Streams in Java](https://www.geeksforgeeks.org/stream-in-java/)

- [`java.util.stream.Stream` Javadoc](https://devdocs.io/openjdk~17/java.base/java/util/stream/stream)
- [`java.util.Collection` Javadoc](https://devdocs.io/openjdk~17/java.base/java/util/collection)

A **stream** in Java is a sequence of objects that supports various methods that can be pipelined to produce the desired result.

**Use of Stream in Java**

The uses of Stream in Java are mentioned below:

- Stream API is a way to express and process collections of objects.
- Enable us to perform operations like _filtering, mapping, reducing, and sorting_.

Java Stream Features

The features of Java streams are mentioned below:

- A stream is not a data structure; instead, it takes input from the Collections, Arrays, or I/O channels.
- Streams don’t change the original data structure, they only provide the result as per the pipelined methods.
- Each intermediate operation is lazily executed and returns a stream as a result, hence, various intermediate operations can be pipelined. Terminal operations mark the end of the stream and return the result.

### Lambda expressions

[Java Lambda Expressions](https://www.geeksforgeeks.org/lambda-expressions-java-8/)

**Lambda expressions** represent the instances of functional interfaces (interfaces with a single abstract method). They provide a concise way to express instances of single-method interfaces using a block of code.

**Key Functionalities of Lambda Expression**

Lambda Expressions implement the only abstract function and therefore implement functional interfaces. Lambda expressions are added in Java 8 and provide the following functionalities.

- Functional Interfaces: A functional interface is an interface that contains only one abstract method.
- Code as Data: Treat functionality as a method argument.
- Class Independence: Create functions without defining a class.
- Pass and Execute: Pass lambda expressions as objects and execute on demand.

### Functional interfaces

[Java Functional Interfaces](https://www.geeksforgeeks.org/java-functional-interfaces/)

A **functional interface** in Java is _an interface that contains **only one abstract method**_. Functional interfaces can have multiple default or static methods, but only one abstract method.

**Built-In Java Functional Interfaces**

Since Java 8 onwards, there are many interfaces that are converted into functional interfaces. All these interfaces are annotated with @FunctionalInterface. These interfaces are as follows:

- **Runnable**: This interface only contains the `run()` method.
- **Comparable**: This interface only contains the `compareTo()` method.
- **ActionListener**: This interface only contains the `actionPerformed()` method.
- **Callable**: This interface only contains the `call()` method.

**Types of Functional Interfaces in Java**

Java SE 8 included four main kinds of functional interfaces which can be applied in multiple situations as mentioned below:

- [Consumer](https://www.geeksforgeeks.org/java-8-consumer-interface-in-java-with-examples/)
- [Predicate](https://www.geeksforgeeks.org/java-8-predicate-with-examples/)
- [Function](https://www.geeksforgeeks.org/function-interface-in-java-with-examples/)
- [Supplier](https://www.geeksforgeeks.org/supplier-interface-in-java-with-examples/)

<br/>

## Programming Language - C <a name="programming_c"></a>

### Struct and Union

The difference between `union` and `structure`:

- the size of the memory: in struct, it’s the sum of all members sizes; in union, only max member size is important,
- only one member of a union can be accessed at one time, and of course all members of a struct,
- a union stores only one value (except some tricky code); a struct stores all the values of members.

([Source](https://edube.org/learn/c-essentials-part-2/pointers-to-structures-and-arrays-of-structures-9))

### Pointers

References:

- [C Pointers](https://www.geeksforgeeks.org/c-pointers/)
- [Binky Pointer Fun Video C](https://www.youtube.com/watch?v=5VnDaHBi8dM)
- [you will never ask about pointers again after watching this video](https://www.youtube.com/watch?v=2ybLD6_2gKM)

---

Take a look at the following declaration:

```
int *array[10];
```

In this way, we’ve declared _a variable array which is a 10-element array of pointers to data of type `int`_.

And now let's look at a seemingly very similar, but completely different, declaration:

```
int (*array)[10];
```

It declares _array as a pointer to a 10-element array of type `int`_.

Look how the parentheses have changed the meaning of the declaration.

And now something really difficult:

```
int *(*array)[10];
```

The statement creates _a variable array, which is a pointer to a 10-element array whose elements are pointers to ints_.

([Source](https://edube.org/learn/c-essentials-part-1/declaring-arrays-traps-and-puzzles-1))

### Declaration - analysis and synthesis

The syntax adopted in the “C” language for encoding declaration statements is very concise and compact, but makes the declarations rather vague and unclear. Let’s deal with two aspects of this complexity:

- **Analytic**, when our task is to decipher a complete declaration like this one here:

```
    int *(*tab[10])[10];
```

- **Synthetic**, when our task is to code a declaration given in a verbal description, like this:

```
    declare tab as a 10-element array of pointers to 10-element arrays of pointers to int
```

The above sections describe the exact same declaration.

A **declarator** is a text used to declare an identifier.

For example:

```
int *p;
```

`*p` is the declarator used to declare the p identifier.

Generally, a “C” language declaration takes the following form:

```
T D;
```

where:

`T` is a **type** (built-in or defined by the programmer);<br/>
`D` is a **declarator**.

**Declarations: rule #1**

If the declaration takes the following form:

```
T D
```

and `D` is just a simple **identifier**, it means that `D` is an **entity of type** `T`.

**Declarations: rule #2**

If the declaration takes the following form:

```
T D[n]
```

it means that the **identifier** contained in the `D[n]` declarator is **an array of size `n` and type** `T`.

**Declarations: rule #3**

If the declaration takes the following form:

```
T *D
```

it means that the **identifier** contained in the `*D` declarator is **a pointer to data of type** `T`.

**Declarations: rule #4**

If the declaration takes the following form:

```
T D()
```

it means that the **identifier** contained in the `D()` declarator **is a function whose return value is of type** `T`.

Note that other declarators may appear inside parentheses, specifying the types of function parameters.

([Source](https://edube.org/learn/c-essentials-part-2/complex-declarations-10))

<br/>

## Gradle <a name="gradle"></a>

- [Gradle](https://gradle.org/)
- [Gradle User Guide](https://docs.gradle.org/current/userguide/userguide.html)

<br/>

## Linux Platform <a name="linux_platform"></a>

- [Unix Commands Cheatsheet](https://cheatography.com/jluis/cheat-sheets/bash-and-unix-commands/)
- [Bash Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Redirections)
- [Bash Cheatsheet](https://devhints.io/bash)
- [VIM Cheatsheet](https://devhints.io/vim)
- [Grep Cheatsheet](https://devhints.io/grep)

<br/>

## Markdown <a name="markdown"></a>

- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Guide/Cheetsheet](https://www.markdownguide.org/cheat-sheet/)
- [Markdown Guide/Hacks](https://www.markdownguide.org/hacks/)
- [Table of Contents in Markdown](https://stackoverflow.com/a/33433098)
  - At the end of each header, add an empty anchor with a chosen name — e.g. `<a name="foo"></a>`.
  - At the start of the document (i.e. the TOC section), list the headers with a link to their anchors — e.g. `[Foo](#foo)`.
- [Get underlined text with Markdown](https://stackoverflow.com/a/4019303)
  - `<span style="text-decoration:underline">underlined_text</span>`

<br/>
