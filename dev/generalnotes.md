# General Development Notes

**Table of Contents**

- [Programming Language - Java](#programming_java)
- [Programming Language - C](#programming_c)
- [Markdown](#markdown)

<br/>

## Programming Language - Java <a name="programming_java"></a>

To be completed...
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

## Markdown <a name="markdown"></a>

- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Guide/Cheetsheet](https://www.markdownguide.org/cheat-sheet/)
- [Markdown Guide/Hacks](https://www.markdownguide.org/hacks/)
- [Table of Contents in Markdown](https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents)

<br/>
