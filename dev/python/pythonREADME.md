# Python Dev Notes

Here are my Python notes.

**Table of Contents**

- [Development Setup](#develoment_setup)
  - [Installation](#dev_setup_install)
  - [Environment setup](#dev_setup_env_setup)
  - [IDE](#dev_setup_ide)
- [Tutorials, Documentation, and More](#tutorial_doc_and_more)
- [Source Code Repository](#src_code_repo)
- [Python Notes](#python_notes)
  - [General](#python_notes_general)
  - [Data Structures](#python_notes_ds)
  - [Looping](#python_notes_loop)
  - [Conditioning](#python_notes_condi)
  - [Functions](#python_notes_funcs)
  - [Classes](./pythonREADME.md#python_notes_classes)
  - [Inputs and outputs](#python_notes_ios)
  - [Serialization](#python_notes_serial)
  - [Errors and Exceptions](#python_notes_error_exceptions)
  - [File processing](#python_notes_file_processing)
  - [Networking and interprocess communication](#python_notes_network)
  - [Access databases](#python_notes_access_db)
  - [Decorators and Python](#python_notes_decorators)
  - [Logging](#python_notes_logging)
  - [Testing](#python_notes_testing)
  - [Miscellaneous](#python_notes_miscs)

<br/>

## Development Setup <a name="develoment_setup"></a>

### Installation <a name="dev_setup_install"></a>

Get **Python** at [Python download](https://www.python.org/downloads/). Select the platform that applies to the development environment. My personal dev environment is on Windows so I choose the installer image looks like **Windows installer (64-bit)**, where 3.13.3 is the latest version as of this writing. Note the latest available version will vary as time goes.

If you are interested in the corresponding source code, you can also download Go source code on the same download page.

<br/>

### Environment setup <a name="dev_setup_env_setup"></a>

Ensure the path to where Python is installed is included in the environment variable `PATH` for proper access.

For Windows, one also need to make sure that the path to Python install path is set BEFORE the path to `WindowsApps` path since there is a python executable `%USERPROFILE%AppData\Local\Microsoft\WindowsApps\python.exe`, which is NOT the one we need.

<br/>

### IDE <a name="dev_setup_ide"></a>

[Microsoft Visual Studio Code](../devenv.md#visual-studio-code) is a good option for Python.

The **Python** extension from Microsoft is useful for Python programming with Microsoft Visual Studio Code.

<br/>

## Tutorials, Documentation, and More <a name="tutorial_doc_and_more"></a>

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (online)
- The Python Tutorial (PDF) is available at [Python documentation download](https://docs.python.org/3/download.html) in **PDF** format. The tutorial PDF is the file `docs-pdf\tutorial.pdf` in the downloaded ZIP file.
- [Python 3 Documentation](https://docs.python.org/3/)
- [The Python Standard Library](https://docs.python.org/3/library/)
- [The Python Language Reference](https://docs.python.org/3.13/reference/)
- [Python 3.13 Howtos](https://docs.python.org/3.13/howto/index.html)
  - [Logging HOWTO](https://docs.python.org/3.13/howto/logging.html#logging-howto)
  - [Logging Cookbook](https://docs.python.org/3.13/howto/logging-cookbook.html#logging-cookbook)
  - [Sorting Techniques](https://docs.python.org/3.13/howto/sorting.html#sortinghowto)
  - [Enum](https://docs.python.org/3/howto/enum.html)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Data Persistence](https://docs.python.org/3/library/persistence.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#function-and-variable-names) (for Python naming convention and code styling etc.)
- [Python Crash Course](https://www.amazon.com/Python-Crash-Course-Eric-Matthes/dp/1718502702) _Matthes, Eric. 3rd Edition (2023). No Starch Press_

<br/>

## Source Code Repository <a name="src_code_repo"></a>

My source code repository for Python related code is at my GitHub repository here under the `src` folders of the related topics such as `gui` or `rest`.

<br/>

## Python Notes <a name="python_notes"></a>

### General <a name="python_notes_general"></a>

Review the helpful Python principles from _**The Zen of Python** (by **Tim Peters**)_ by running `import this` in a python prompt.

```
C:\>python
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
... ...
Namespaces are one honking great idea -- let's do more of those!
```

#### Indentation

Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.

#### Comments

- Single-line comment: Start a like with `#`

```
# SingleCommentLine
```

- Multiple-line comment: Use three double-quotes `"""` to enclose the comment lines.

```
"""
CommentLine1
... ...
CommentLineN
"""
```

| Comments                                                                                                                                                                                                                                                                                                                                    | Docstrings                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Comments are non-executable statements in Python, which means that they are ignored by the Python interpreter; they are not stored in the memory, and cannot be accessed during program execution (i.e. they can be accessed by looking at the source code).                                                                                | Docstrings can be accessed by reading the source code, and by using the `__doc__` attribute or the `help()` function.                                                          |
| The main purpose of comments is increasing the readability and understandability of the code, and explaining the code to the user in a meaningful way. The user here means both other programmers and you (e.g. when you go back to your code after some time) – somebody who will want to or need to modify, extend, or maintain the code. | The main purpose of docstrings is documenting your code – describing its use, functionality, and capabilities to users who do not necessarily need to know how it works.       |
| Comments cannot be turned into documentation; their purpose is to simplify the code, provide precise information, and help to understand the intention of a particular snippet/line.                                                                                                                                                        | Docstrings can be easily turned into actual documentation, which describes a module's or function's behavior, the meaning of parameters, or the purpose of a specific package. |

#### PEP 8 compliant checkers

**pycodestyle** (formerly called pep8, but the name was changed to avoid confusion) - Python style guide checker; it lets you check your Python code for conformance with the style conventions in PEP 8. You can install the tool with the following command in the terminal:

`pip install pycodestyle`

You can run it on a file or files to obtain information about non-conformance (and indicate errors in the source code and their frequency).

More information: https://github.com/PyCQA/pycodestyle
Documentation: https://pycodestyle.pycqa.org/en/latest/

### Data Structures <a name="python_notes_ds"></a>

- **List**: `list = [value1, ..., valueN]`
- **Tuple**: `tuple = (value1, ..., valueN)` or `tuple=(value,)`
- **Dictionary**: `dict = {key1:value1, ..., keyN:valueN}`
- **Set**: `set = {value1, ..., valueN}`

### Looping <a name="python_notes_loop"></a>

<u>**for** loop</u>

```
for v in list | set:
    print(value)

---
for v in range(1, N):
    print(v)

---
for key, value in dict.items():
    print(f"Key: {key}; Value: {value}\n")
```

<u>**while** loop</u>

```
while condition:
    doSomething...
```

The use of `break` and `continue` for flow control is similar to other programming languages.

### Conditioning <a name="python_notes_condi"></a>

#### if statement

```
if condition:
   doSomething...

---
if condition1:
   doSomething1...
elif condition2:
   doSomething2...
else:
   doSomething3...

```

### Functions <a name="python_notes_funcs"></a>

```
[Basic]
def funcName:
    statement1
    ...
    statementN

---
[With Arguments]
def funcName(arg1, ..., argN):
    statement1
    ...
    statementN

---
[With Arguments that have default values]
def funcName(arg1='defaultValue1', ..., argN='defaultValueN'):
    statement1
    ...
    statementN

---
[With Arbitrary Number of Arguments]
(Note the args are in a tuple list.)
def funcName(*args):
    statement1
    ...
    statementN

---
[Mixing Positional and Arbitrary Arguments]
(Note the arbArgs are in a tuple list.)
def funcName(arg1, *arbArgs):
    statement1
    ...
    statementN

---
[Arbitrary Keywords Arguments]
(Note the kwArgs are in a dictionary.)
def funcName(arg1, ..., argN, *kwArgs):
    statement1
    ...
    statementN

Example:

def user_permissions(userid, username, **perms):

==> def user_permissions('1001', 'myuser', file='view', dir='view')

```

#### Packages, modules and functions

[Packages](https://docs.python.org/3/tutorial/modules.html#packages) are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

A [module](https://docs.python.org/3/tutorial/modules.html) is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.

### Classes <a name="python_notes_classes"></a>

[Classes](https://docs.python.org/3.13/tutorial/classes.html) provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state. ([Source](https://docs.python.org/3.13/tutorial/classes.html))

```
class BaseClass():

   classVar1 = value1                # Class variable shared by all instances

   def __init__(self, arg1, arg2):
      self.var1 = arg1               # instance variable unique to each instance
      self.var2 = arg2

   def clsMethod1(self):
      statement1
      ...

   def clsMethod1(self, arg1):
      statement1
      ...

---
class DerivedClass(BaseClass):

   def __init__(self, arg1, arg2):
      """Initialize the attributes in the parent class"""
      super().__init__(arg1, arg2)

   def clsMethod1(self):
      statement1
      ...

   def clsMethod2(self, arg1):
      statement1
      ...
```

#### Class methods and static methods

Using static and class methods:

- a class method requires `cls` as the first parameter and a static method does not;
- a class method has the ability to access the state or methods of the class, and a static method does not;
- a class method is decorated by `@classmethod` and a static method by `@staticmethod`;
- a class method can be used as an alternative way to create objects, and a static method is only a utility method.

#### Abstract classes

Python is considered to be a very flexible programming language, but that doesn’t mean that there are no controls to impose a set of functionalities or an order in a class hierarchy. When you develop a system in a group of programmers, it would be useful to have some means of establishing requirements for classes in matters of interfaces (methods) exposed by each class.
What is an abstract class?

An abstract class should be considered a blueprint for other classes, a kind of contract between a class designer and a programmer:

- The class designer sets requirements regarding methods that must be implemented by just declaring them, but not defining them in detail. Such methods are called abstract methods.
- The programmer has to deliver all method definitions and the completeness would be validated by another, dedicated module. The programmer delivers the method definitions by overriding the method declarations received from the class designer.

This contract assures you that a child class, built upon your abstract class, will be equipped with a set of concrete methods imposed by the abstract class.
Why do we want to use abstract classes?

The very important reason is: we want our code to be polymorphic, so all subclasses have to deliver a set of their own method implementations in order to call them by using common method names.

Furthermore, a class which contains one or more abstract methods is called an abstract class. This means that abstract classes are not limited to containing only abstract methods – some of the methods can already be defined, but if any of the methods is an abstract one, then the class becomes abstract.
What is an abstract method?

An abstract method is a method that has a declaration, but does not have any implementation. We'll give some examples of such methods to emphasize their abstract nature.

Remember that it isn’t possible to instantiate an abstract class, and it needs subclasses to provide implementations for those abstract methods which are declared in the abstract classes. This behavior is a test performed by a dedicated Python module to validate if the developer has implemented a subclass that overrides all abstract methods.

When we’re designing large functional units, in the form of classes, we should use an abstract class. When we want to provide common implemented functionality for all implementations of the class, we could also use an abstract class, because abstract classes partially allow us to implement classes by delivering concrete definitions for some of the methods, not only declarations.

We have just defined the means by which to provide a common Application Program Interface (API) for a set of subclasses. This capability is especially useful in situations where your team or third-party is going to provide implementations, such as with plugins in an application, even after the main application development is finished.

Python has come up with a module which provides the helper class for defining **Abstract Base Classes (ABC)** and that module name is abc.

The ABC allows you to mark classes as abstract ones and distinguish which methods of the base abstract class are abstract. A method becomes abstract by being decorated with an @abstractmethod decorator.

To start with ABC you should:

- import the `abc` module;
- make your base class inherit the helper class ABC, which is delivered by the abc module;
- decorate abstract methods with @abstractmethod, which is delivered by the abc module.

A simple sample code is as below.

```
import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


gf = GreenField()
gf.hello()
```

When you run the code, the output doesn’t surprise anyone:

```
Welcome to Green Field!
```

<u>Multiple inheritance</u>

When you plan to implement a multiple inheritance from abstract classes, remember that an effective subclass should override all abstract methods inherited from its super classes.

<u>Summary</u>

- Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
- ABC can only be inherited from;
- we are forced to override all abstract methods by delivering concrete method implementations.

(Source: Sec. 2.6.1.1, [Advanced OOP](https://edube.org/study/pcpp1-1) by [OpenEDG](https://edube.org/))

#### Mutliple constructors

Python does not support explicit multiple constructors. Some alternative approaches are available at [the reference 1](https://realpython.com/python-multiple-constructors/) and [the reference 2](https://www.geeksforgeeks.org/creating-multiple-constructors-python-class/).

#### Attribute encapsulation

Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized parties' direct access to them. Publicly accessible methods are provided in the class to access the values, and other objects call those methods to retrieve and modify the values within the object. This can be a way to enforce a certain amount of privacy for the attributes.

This picture presents the idea: direct access to the object attribute should not be possible, but you can always invoke methods, acting like proxies, to perform some actions on the attributes.

Python introduces the concept of properties that act like proxies to encapsulated attributes.

This concept has some interesting features:

- the code calling the proxy methods might not realize if it is "talking" to the real attributes or to the methods controlling access to the attributes;
- in Python, you can change your class implementation from a class that allows simple and direct access to attributes to a class that fully controls access to the attributes, and what is most important –consumer implementation does not have to be changed; by consumer we understand someone or something (it could be a legacy code) that makes use of your objects.

#### Inheritance and composition

To favor composition over inheritance is a design principle that gives the design higher flexibility, as you can choose which domain-specific objects should be incorporated into your ultimate object. It's like arming your base machine with tooling, dedicated to running a specific task, but not building a wide hierarchy structure of classes covering all possible hardware combinations.

In fact, with the composition approach you can more easily respond to the requirement changes regarding classes, as it does not require deep dependency investigations which you would spot while implementing code with the inheritance approach.

On the other hand, there is a clear drawback: composition transfers additional responsibilities to the developer. The developer should assure that all component classes that are used to build the composite should implement the methods named in the same manner to provide a common interface.

In the case of inheritance, if the developer forgets to implement a specific method, the inherited method with the same name will be called. Additionally, in the case of inheritance, the developer has to re-implement only the specific methods, not all of them, to gain a common interface.

Which way should you choose? Before we answer the question, let's mention a few more things:

- inheritance and composition are not mutually exclusive. Real-life problems are hardly every pure “is a” or “has a” cases;
- treat both inheritance and composition as supplementary means for solving problems;
- there is nothing wrong with composing objects of ... classes that were built using inheritance. The next example code should shed some light on this case.

You should always examine the problem your code is about to solve before you start coding. If the problem can be modeled using an **is a** relation, then the inheritance approach should be implemented.

Otherwise, if the problem can be modeled using a **has a** relation, then the choice is clear – composition is the solution.

#### Metaclasses

In Python, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a metaclass allows for the customization of class instantiation.

The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a different way than decorators:

- **decorators** bind the names of decorated functions or classes to new callable objects. Class decorators are applied when classes are instantiated;
- **metaclasses** redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.

Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation must be provided.

The typical use cases for metaclasses:

- logging;
- registering classes at creation time;
- interface checking;
- automatically adding new methods;
- automatically adding new variables.

### Inputs and outputs <a name="python_notes_ios"></a>

Information for several ways to present the output of a program; data can be printed in a human-readable form, or written to a file is available at the [link](https://docs.python.org/3.13/tutorial/inputoutput.html), including output formatting, file read and write.

For file operations, it is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

```
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

If you’re not using the with keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it.

More info about `with` is [here](https://docs.python.org/3.13/reference/compound_stmts.html#with).

File and directory access can also be implemented using [Python standard libaries](https://docs.python.org/3/library/filesys.html).

### Serialization <a name="python_notes_serial"></a>

<u>**Pickle**</u>

In Python, object **serialization** is the process of converting an object structure into a stream of bytes to store the object in a file or database, or to transmit it via a network. This byte stream contains all the information necessary to reconstruct the object in another Python script.

This reverse process is called **deserialization**.

Python objects can also be serialized using a module called **pickle**', and using this module, you can 'pickle' your Python objects for later use.

The `pickle` module is a very popular and convinient module for data serialization in the world of Pythonistas.

So, what can be pickled and then unpickled?

The following types can be pickled:

- None, booleans;
- integers, floating-point numbers, complex numbers;
- strings, bytes, bytearrays;
- tuples, lists, sets, and dictionaries containing pickleable objects;
- objects, including objects with references to other objects (remember to avoid cycles!)
- references to functions and classes, but not their definitions.

<u>**Shelve**</u>

You should treat a shelve object as a Python dictionary, with a few additional notes:

- the keys must be strings;
- Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, call the sync() method on your shelve object;
- when you call the close() method on an shelve object, it also flushes the buffers.

When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:

- the len() function;
- the in operator;
- the keys() anditems() methods;
- the update operation, which works the same as when applied to a Python dictionary;
- the del instruction, used to delete a key-value pair.

After running the code, you'll notice additionally that some files are created to support the database. Don’t try to alter those files with external utilities, because your shelve may become inconsistent, resulting in read/write errors.

The use of shelve is really easy and effective. Moreover, you should know that you could simulate the shelve by pickling the whole dictionary, but the shelve module uses the memory more efficiently, so whenever you need access to pickled objects, employ a shelve.

And the final remark is:

    because the shelve module is backed by pickle, it isn’t safe to load a shelve from an untrusted source. As with pickle, loading a shelve can execute arbitrary code.

Also see more info in [Python Data Persistence](https://docs.python.org/3/library/persistence.html)

### Errors and Exceptions <a name="python_notes_error_exceptions"></a>

Details about Python errors and exceptions is available at Python [tutorial](https://docs.python.org/3.13/tutorial/errors.html). Some notes are as below.

Case 1: Simple try-except

```
    try:
        statement1...
    except SomeError:
        statementE1...
```

Case 2: try-except-else

```
    try:
        statement1...
    except SomeError:
        statementE1...
    else:
        statementElse1
```

Case 3: try-multiple-excepts-else

```
    try:
        statement1...
    except SomeError1:
        statementE1...
    except SomeError2:
        statementE2...
    except SomeError3:
        statementE3...
    else:
        statementElse1
```

Case 4: try(raise)-except-else

```
    try:
        statement1...
        raiseSomeError...
    except SomeError:
        statementE1...
    else:
        statementElse1
```

Case 5: try-except-else with the use of `pass`

```
    try:
        statement1...
        raiseSomeError...
    except SomeError:
        pass                # Ignore the exception
    else:
        statementElse1
```

Additional exception topics are available in the related Python tutorial.

- Exception Chaining
- User-defined Exceptions
- Defining Clean-up Actions
- Predefined Clean-up Actions
- Raising and Handling Multiple Unrelated Exceptions
- Enriching Exceptions with Notes

<u>Chained exceptions</u>
This chaining concept introduces two attributes of exception instances:

- the `__context__` attribute, which is inherent for **implicitly chained exceptions**;
- the `__cause__` attribute, which is inherent for **explicitly chained exceptions**.

Those attributes help the programmer to keep a reference to the original exception object in a handy and consistent way for later processing like logging, etc.

### File processing <a name="python_notes_file_processing"></a>

<u>XML file processing</u>

The standard Python library offers some the modules for working with XML:

- **xml.etree.ElementTree** – has a very simple API for analyzing and creating XML data. It's an excellent choice for people who have never worked with the Document Object Model (DOM) before.
- **xml.dom.minidom** – is the minimum implementation of the Document Object Model (DOM). Using the DOM, the approach to an XML document is slightly different, because it's parsed into a tree structure in which each node is an object.
- **xml.sax** – SAX is an acronym for “Simple API for XML”. SAX is an interface in Python for event-driven XML document analysis. Unlike the above modules, analyzing a simple XML document using this module requires more work.

_Get the root element of an XML input_

From an XML file:

```
import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
root = tree.getroot()
```

From an XML string:

```
import xml.etree.ElementTree as ET

root = ET.fromstring(xml_as_string)
```

Access to an `xml.etree.Element`,

- `tag`: this returns the tag name as a string
- `attrib`: this returns all attributes in the tag as a dictionary. To retrieve the value of a single attribute, use its key, e.g., `elem.attrib ['attr_key']`.

_Build an XML document_

An exampe:

```
import xml.etree.ElementTree as ET

root = ET.Element('root')
elem1 = ET.SubElement(root, 'elem', {'attr_1': 'attr_value_1', 'attr_2': 'attr_value_2'})
elem2 = ET.SubElement(root, 'elem', {'attr_1': 'attr_value_1', 'attr_2': 'attr_value_2'})
ET.dump(root)
```

See [the API documentation](https://docs.python.org/3/library/xml.etree.elementtree.html) of `xml.etree.elementtree` for details.

<u>CSV file processing</u>

The Python Standard Library offers a module called `csv` that provides functions for reading and writing data in CSV format. Reading data is done using the `reader` object, while writing is done using the `writer` object.

See [the API documentation](https://docs.python.org/3/library/csv.html) of `csv` for details.

_Read from a CSV file_

```
import csv

with open('sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['attr1'], ':', row['attr2'])
```

_Write to a CSV file_

```
import csv

with open('sample.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['header1', 'header21'])
    writer.writerow(['entry1_value1', 'entry1_value2'])
    writer.writerow(['entry2_value1', 'entry2_value2'])
    writer.writerow(['entry3_value1', 'entry3_value2'])
    writer.writerow(['entry4_value1', 'entry4_value2'])
    writer.writerow(['entry5_value1', 'entry5_value2'])

---
import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['header1', 'header2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'header1': 'entry1_value1', 'header2': 'entry1_value2'})
    writer.writerow({'header1': 'entry2_value1', 'header2': 'entry2_value2'})
    writer.writerow({'header1': 'entry3_value1', 'header2': 'entry3_value2'})
    writer.writerow({'header1': 'entry4_value1', 'header2': 'entry4_value2'})
    writer.writerow({'header1': 'entry5_value1', 'header2': 'entry5_value2'})
```

### Networking and interprocess communication <a name="python_notes_network"></a>

- [Socket Programming HOWTO](https://docs.python.org/3.13/howto/sockets.html#socket-howto)
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
  - asyncio — Asynchronous I/O
  - socket — Low-level networking interface
  - ssl — TLS/SSL wrapper for socket objects
  - select — Waiting for I/O completion
  - selectors — High-level I/O multiplexing
  - signal — Set handlers for asynchronous events
  - mmap — Memory-mapped file support

### Access databases <a name="python_notes_access_db"></a>

- [Python Database Tutorial](https://www.geeksforgeeks.org/python-database-tutorial/) by Geeks for Geeks.
- [Database Access With Python](https://realpython.com/learning-paths/database-access-in-python/) by Real Python

### Decorators and Python <a name="python_notes_decorators"></a>

A decorator is one of the design patterns that describes the structure of related objects. Python is able to decorate functions, methods, and classes.

The decorator's operation is based on wrapping the original function with a new "decorating" function (or class), hence the name "decoration". This is done by passing the original function (i.e., the decorated function) as a parameter to the decorating function so that the decorating function can call the passed function. The decorating function returns a function that can be called later.

Of course, the decorating function does more, because it can take the parameters of the decorated function and perform additional actions and that make it a real decorating function.

The same principle is applied when we decorate classes. We'll talk about this a bit later.

So from now on, the term 'decorator' will be understood as a decorating class or a decorating function.

- [Decorators in Python](https://www.geeksforgeeks.org/decorators-in-python/)
- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

### Logging <a name="python_notes_logging"></a>

**Logging is a very important aspect in any software and solution**. For logging in Pythin, refer details to Python documentation:

- [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
- [logging basic tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
- [logging advanced tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
- [logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

A quick example for the Logger object

One application may have several loggers created both by us and by programmers of the modules. If your application is simple, as in the example below, you can use the root logger. To do this, call the `getLogger` function without providing a name. The root logger is at the highest point in the hierarchy. Its place in the hierarchy is assigned based on the names passed to the getLogger function.

```
import logging

root_logger = logging.getLogger()
hello_logger = logging.getLogger('logger_name')
hello_world_logger = logging.getLogger('logger_name.world')
recommended_logger = logging.getLogger(__name__)
```

Logger names are similar to the names of the Python modules in which the dot separator is used. Their format is as follows:

`hello` – creates a logger which is a child of the root logger;

`hello.world` – creates a logger which is a child of the hello logger.

If you want to make another nesting, just use the dot separator.

The `getLogger` function returns a `Logger` object. Let's look at the example code in the editor. We'll find there the ways to get the Logger object, both with and without a name.

We recommend calling the getLogger function with the `__name__` argument, which is replaced by the current module name. This allows you to easily specify the source of the logged message.

NOTE: Several calls to the getLogger function with the same name will always return the same object.

([Source](https://edube.org/learn/pcpp1-5/logging-in-python-1))

_Logging levels_

The Logger object allows you to create logs with different levels of logging that help you to distinguish between less important logs and those reporting a serious error. By default, the following logging levels are defined:
| Level name | Value |
| -------- | ------ |
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |

```
import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
```

### Testing <a name="python_notes_testing"></a>

One option for Python testing is to use the package [pytest](https://docs.pytest.org/en/stable/contents.html).

#### pytest setup

The following applies to Windows platform.

```
python -m pip install --upgrade pip

python -m install pytest
```

After `pytest` gets installed, ensure it is accessible via the updated PATH settings. For Windows, the path to `pytest` is like `%USERPROFILE\AppData\Roaming\Python\PythonXYZ\Scripts`, where XYZ is the version of the installed Python.

<u>Example to test functions with `pytest`</u>
(Source: Eric Matthes. Python Crash Course (pp. 211-214). 3rd Ed. 2023. No Starch Press.)

`name_func.py`

```
def get_formatted_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()
```

`names.py`

```
from name_func import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease enter the first name: ")
    if first == 'q':
      break
    last = input("Please enter the last name: ")
    if last == 'q':
      break

    formatted_name = get_formatted_name(first, last)
    print(f'\tNeatly formatted name: {formatted_name}')
```

Run the command `python names.py`.

---

`test_name_func.py`

```
from name_func import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('john', 'doe')
    assert formatted_name == 'John Doe'
```

Open a command prompt (on Windows platform), change the work directory to where the Python files are, then run the command `pytest`.

<u>Example to test classes with `pytest`</u>
(Source: Eric Matthes. Python Crash Course (pp. 211-214). 3rd Ed. 2023. No Starch Press.)

`survey.py`

```
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for result in self.responses:
            print(f"- {response}")
```

`test_survey.py`

```
import pytest
from survey import AnonymousSurvey


@pytest.fixture
def lang_survey():
    question = "What language did you first learn to speak?"
    lang_survey = AnonymousSurvey(question)
    return lang_survey


def test_store_single_response(lang_survey):
    lang_survey.store_response("English")
    assert "English" in lang_survey.responses


def test_store_three_response(lang_survey):
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        lang_survey.store_response(response)

    for response in responses:
        assert response in lang_survey.responses
```

### Miscellaneous <a name="python_notes_miscs"></a>

Use `Python pip` to install other packages

```
python -m pip install pkg_name
```

<br/>
