# Golang Dev Notes

My notes for Golang is listed herein.

**Table of Contents**

- [Development Setup](#dev_setup)
  - [Installation](#dev_setup_install)
  - [Environment setup](#dev_setup_env_setup)
  - [IDE](#dev_setup_ide)
- [Tutorials, Documentation, and More](#tutorials_doc_and_more)
- [Source Code Repository](#src_code_repo)
- [Golang Notes](#golang_notes)
  - [Using Maps as Sets](#golang_notes_map_as_set)
  - [Concurrrency](#golang_notes_concurrency)
  - [Standard library](#golang_notes_std_lib)
  - [Networking](#golang_notes_network)
  - [Access databases](#golang_notes_access_db)
  - [Reflection](#golang_notes_reflection)
  - [Unsafe](#golang_notes_unsafe)
- [Testing](#golang_testing)
  - [Basic](#golang_testing_basic)
  - [Reporting](#golang_testing_reporting)
  - [Setting up and tearing down](#golang_testing_setup_teardown)
  - [Code coverage](#golang_testing_code_coverage)
  - [Benchmark](#golang_testing_benchmark)
  - [Stubs and mocks](#golang_testing_stub_and_mock)
- [Practices and Exercises](#practice_n_exercises)

<br/>

## Development Setup <a name="dev_setup"></a>

### Installation <a name="dev_setup_install"></a>

Get Go at [Go download](https://go.dev/dl/). Select the platform that applies to the development environment. My personal dev environment is on Windows so I choose the installer image looks like **go1.24.2.windows-amd64.msi**, where 1.24.2 is the version and will vary as time goes.

If you are interested in the corresponding source code, you can also download Go source code on the same download page.

You can also refer to Golang's own documentation about [Download and install](https://go.dev/doc/install).

<br/>

### Environment setup <a name="dev_setup_env_setup"></a>

Set the **GOPATH** environment variable.

    setx GOPATH %USERPROFILE%\go

<br/>

### IDE <a name="dev_setup_ide"></a>

[Microsoft Visual Studio Code](../devenv.md#visual-studio-code) is a good option for Golang.

The **Go** (Go for Visual Studio Code) extension from Go Team at Google is useful for Golang with Microsoft Visual Studio Code.

<br/>

## Tutorials, Documentation, and More <a name="tutorials_doc_and_more"></a>

- [Learning Go](https://www.amazon.com/Learning-Go-Idiomatic-Real-World-Programming/dp/1098139291/) by Jon Bodner, O'Rielly. The edition referred herein is the first edition (2021).
- [Go Documentation](https://go.dev/doc/)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go by Examples](https://gobyexample.com/)
- [Go Playground](https://go.dev/play/)
- [How Do you Structure Your Go Apps?](https://oreil.ly/0zHY4) by Kat Zien at GopherCon 2018
- [Tutorial: Getting started with generics](https://go.dev/doc/tutorial/generics)

<br/>

## Source Code Repository <a name="src_code_repo"></a>

My source code repository for Golang code is at my GitHub repository herein under [ws-tang/dev/golang/src](https://github.com/ws-tang/ws-tang/tree/main/dev/golang/src).

<br/>

## Golang Notes <a name="golang_notes"></a>

### Using Maps as Sets <a name="golang_notes_map_as_set"></a>

Golang does not have Set as other programming languages do. One approach to use Set in Golang is to use a Map to simulate a Set.

For example, we can do the following for an integer set.

```
package main

import "fmt"

func main() {
	intSet := map[int]bool{}
	vals := []int{5, 10, 2, 5, 8, 7, 3, 9, 1, 2, 10}
	for _, v := range vals {
		intSet[v] = true
	}
	fmt.Println(len(vals), len(intSet))
	fmt.Println(intSet[5])
	fmt.Println(intSet[500])
	if intSet[100] {
		fmt.Println("100 is in the set")
	}
}
```

Another option is to use struct instead of bool in the Map structure.

```
intSet := map[int]struct{}{}
vals := []int{5, 10, 2, 5, 8, 7, 3, 9, 1, 2, 10}
for _, v := range vals {
    intSet[v] = struct{}{}
}

if _, ok := intSet[5]; ok {
    fmt.Println("5 is in the set")
}
```

The advantage to use struct instead of bool is in memory footprint. An empty struct takes zero byte but a bool takes 1 byte. If the amount of data is not significant, using bool is better.

([Source](https://oreil.ly/wC6XK) from _Bodner, Jon (2021). Learning Go (pp. 55-56). 1st Ed. O'Reilly_)

### Concurrrency <a name="golang_notes_concurrency"></a>

#### General

- Goroutines
- Channels
  - Reading, writing, and buffering
  - For-range and channels
  - Closing a channel
  - How channels behave (see the table below)
- Select

How channels behave

|           | Unbuffered, Open                 | Unbuffered, Closed                                | Buffered, Open                      | Buffered, Closed                                                                                                  | Nil          |
| --------- | -------------------------------- | ------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------ |
| **Read**  | Pause until something is written | Return zero value (use comma ok to see if closed) | Pause if buffer is empty            | Return a remaining value in the buffer. If the buffer is empty, return zero value (use comma ok to see if closed) | Hang forever |
| **Write** | Pause until something is read    | **PANIC**                                         | Pause if buffer if full             | **PANIC**                                                                                                         | Hang forever |
| **Close** | Works                            | **PANIC**                                         | Works, remaining values still there | **PANIC**                                                                                                         | **PANIC**    |

(Source: Table 10-1 from _Bodner, Jon (2021). Learning Go (p. 209). 1st Ed. O'Reilly_)

#### Use of Mutex

<u>When to use mutex</u>

The decision tree to help decide whether to use channels or mutexes, from _Cox-Buday, Katherine (2017). Concurrency in Go: Tools and Techniques for Developers. 1st Ed. O'Reilly_.

- If you are coordinating goroutines or tracking a value as it is transformed by a series of goroutines, **use channels**.
- If you are sharing access to a field in a struct, **use mutexes**.
- If you discover a critical performance issue when using channels, and you cannot find any other way to fix the issue, modify your code to **use a mutex**.

<u>Nonreentrant Mutex in Go</u>

Mutexes in Go are NOT reentrant. If a goroutine tries to acquire the same lock twice, it **deadlocks**, waiting for itself to release the lock. Nonreentrant locks make it tricky to acquire a lock in a function that calls itself recursively. One must release the lock before the recursive function call.

#### Practices and Patterns

- Keep your APIs concurrency-free
- Goroutines, for loops, and varying variables
- Always clean up your goroutines
- The Done-channel pattern
- Using a Cancel function to terminate a goroutine
  - Return a cancellation function along with the channel
- When to use a buffered and unbuffered channels
  - Buffered channelss are useful when you know how many goroutines you have launched, want to limit the number of goroutines you will launch, or want to limit the amount of work that is queued up.
- Backpressure
  - Use a buffered channel and a **select** statement to limit the number of concurrent operations
- Using WaitGroups

(Source: Chapter 10 Concurrency from _Bodner, Jon (2021). Learning Go. 1st Ed. O'Reilly_)

### Standard library <a name="golang_notes_std_lib"></a>

- I/O
  - io.Reader/io.Writer
- Time
  - time.Duration and time.Time
- Encoding/JSON
  - Encoding/decoding
- Net/HTTP
  - Client/Server
  - Middleware ([chi](https://github.com/go-chi/chi))

### Networking <a name="golang_notes_network"></a>

- [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/html/split/) by **Brian Hall**
- [Network Programming with Go](https://www.amazon.com/Network-Programming-Go-Adam-Woodbeck/dp/1718500882) by _ Adam Woodbeck_ (2021)
- [Go Networking Programming](https://eli.thegreenplace.net/2021/) by **Eli Bendersky** (2021)

([Source](https://www.reddit.com/r/golang/comments/18kelrx/how_do_i_start_with_network_programming_in_go/?rdt=64924))

### Access databases <a name="golang_notes_access_db"></a>

- [Tutorial: Accessing a relational database](https://go.dev/doc/database/index)
- [Accessing relational databases](https://go.dev/doc/database/index)
- [Opening a database handle](https://go.dev/doc/database/open-handle)
- [Executing SQL statements that don't return data](https://go.dev/doc/database/change-data)
- [Querying for data](https://go.dev/doc/database/querying)
- [Using prepared statements](https://go.dev/doc/database/prepared-statements)
- [Executing transactions](https://go.dev/doc/database/execute-transactions)
- [Canceling in-progress database operations](https://go.dev/doc/database/cancel-operations)
- [Managing connections](https://go.dev/doc/database/manage-connections)
- [Avoiding SQL injection risk](https://go.dev/doc/database/sql-injection)

### Reflection <a name="golang_notes_reflection"></a>

[Reflection](https://pkg.go.dev/reflect) allows a program to manipulate objects with arbitrary types. The typical use is to take a value with static type interface{} and extract its dynamic type information by calling TypeOf, which returns a Type.

[The Laws of Reflection](https://go.dev/blog/laws-of-reflection) (Rob Pike)

- Types, Kinds, and Values

<u>Typical uses reflection in Go</u>

- Reading and writing from a database. The `database/sql` package uses reflection to send records to databases and read data back.
- Go's built-in templating libraries, `text/template` and `html/template`, use reflection to process the values that are passed to the templates.
- The `fmt` package uses reflection heavily, as all of those calls to `fmt.Println` and friends rely on reflection to detect the type of the provided parameters.
- The `errors` package uses reflection to implement `errors.Is` and `errors.As`.
- The `sort` package uses reflection to implement functions that sort and evaluate slices of any type: `sort.Slice`, `sort.SliceStable`, and `sort.SliceIsSorted`.
- Marshall and unmarshall data into JSON and XML, along with the other data formats defined in the various `encoding` packages. Struct tags are accessed via reflection, and the fields in structs are read and written using reflection as well. (A CSV marshalling/unmarshalling example is avaialble [here](https://go.dev/play/p/3kwe7ag1i1C).)

(Source: _Bodner, Jon (2021). Learning Go (pp. 302-303). 1st Ed. O'Reilly_)

A good reflection implementation is the SQL query mapping library [Proteus](https://github.com/jonbodner/proteus) (by Jon Bodner).

#### When to use reflection

- Only use reflection if it is worthwhile.
- Reflection makes your program **slower**.
- Reflection works best when it is used to map data in and out of the edge of your program.

<br/>

### Unsafe <a name="golang_notes_unsafe"></a>

The [`unsafe`](https://pkg.go.dev/unsafe) package allows to manipulate memory.

Two main reasons to use the `unsafe` package (Costa, Mujahid, Abdalkareem, and Shihab. ["Breaking Type-safety in Go: An Empirical Study on the Usage of the **unsafe** package"](https://arxiv.org/abs/2006.09973). 2020)

- **System interoperability**. The Go standard library uses **unsafe** to read data from and write data to the operating system.
- **Performance**. This is especially for reading data from a network.

The snippet below is how to check if the platform is little-endian or not.

```
var isLE bool

func init() {
  var x uint16 = 0xFF00
  xb := *(*[2]byte)(unsafe.Pointer(&x))
  isLE = (xb[0] == 0x00)
}
```

<br/>

## Testing <a name="golang_testing"></a>

[Go Testing](https://pkg.go.dev/testing)

### Basic <a name="golang_testing_basic"></a>

- libraries: the **testing** package
- tooling: the command `go test`

### Reporting <a name="golang_testing_reporting"></a>

- testing.Error/testing.Errorf: When testing several independent items in the same test function
- testing.Fatal/testing.Fatalf: If the failure of a check in a test means that further checks in the same test function will always fail or cause the test to panic.

### Setting up and tearing down <a name="golang_testing_setup_teardown"></a>

Use a [TestMain](https://pkg.go.dev/testing#hdr-Main) function.

- Use the function `TestMain` with the parameter of type `*testing.M`.
- Call the method `m.Run()` ib `*testing.M` to run test functions.
- The `Run` method returns the exit code- 0 means all tests passed.
- You must call `os.Exit()` with the exit value from the `Run` method.

```
func TestMain(m *testing.M) {
  ... ...
  // Setting up
  ... ...
  exitVal := m.Run()
  ... ...
  // Cleanup or tearing down
  ... ...
  os.Exit(exitVal)
}
```

### Code coverage <a name="golang_testing_code_coverage"></a>

Run `go test` with the options `-v` (verbose), `-cover` (coverage), and `-coverprofile=fileName`.

```
go test -v -cover -coverprofile=cov.out
go tool cover -html=cov.out
```

**Code coverage is necessary, but it is not sufficient. You can have 100% code coverage and still have bugs in your code.**

<br/>

### Benchmark <a name="golang_testing_benchmark"></a>

```
go test -bench=. -benchmem
```

where:

- `-bench=.`: run all benchmarks
- `-benchmem`: includes the memory allocation information

A sample Go benchmark output

```
BenchmarkFuncName-10 20 12345678 ns/op 65536 B/op  65000 allocs/op
```

where:

- `BenchmarkFuncName-10`: the name of the benchmark, a hyphen, and the value of GOMAXPROCS for the benchmark
- `20`: the number of times that the test ran to produce a stable result
- `12345678 ns/op`: How long it took to run a single pass for this benchmark, in nanoseconds.
- `65536 B/op`: The number of bytes allocated during a single pass of the benchmark.
- `65000 allocs/op`: The number of times bytes had to be allocated from the heap during a single pass of the benchmark. This will always be less than or equal to the number of bytes allocated.

[Profiling Go programs with pprof](https://jvns.ca/blog/2017/09/24/profiling-go-with-pprof/) by Julia Evans
<br/>

### Stubs and mocks <a name="golang_testing_stub_and_mock"></a>

#### Stubs

A stub returns a canned value for a given input. ([Martin Fowler](https://martinfowler.com/articles/mocksArentStubs.html))

Two patterns for testing code that depends on large interfaces.

- Embed the interface in a struct. Embedding an interface in a struct automatically defines all of the interface's methods on the struct.
- A better solution is to create a stub struct that proxies method calls to function fields.

#### Mocks

A mock validates that a set of calls happen in the expected order with the expected inputs. ([Martin Fowler](https://martinfowler.com/articles/mocksArentStubs.html))

- [gomock](https://github.com/golang/mock)
- [testify](https://github.com/stretchr/testify) (from Stretchar Inc.)

<br/>

## Practices and Exercises <a name="practice_n_exercises"></a>

#### The dining philosopher’s problem

    Implement the dining philosopher’s problem with the following constraints/modifications.

    There should be 5 philosophers sharing chopsticks, with one chopstick between each adjacent pair of philosophers.

    Each philosopher should eat only 3 times (not in an infinite loop as we did in lecture)

    The philosophers pick up the chopsticks in any order, not lowest-numbered first (which we did in lecture).

    In order to eat, a philosopher must get permission from a host which executes in its own goroutine.

    The host allows no more than 2 philosophers to eat concurrently.

    Each philosopher is numbered, 1 through 5.

    When a philosopher starts eating (after it has obtained necessary locks) it prints “starting to eat <number>” on a line by itself, where <number> is the number of the philosopher.

    When a philosopher finishes eating (before it has released its locks) it prints “finishing eating <number>” on a line by itself, where <number> is the number of the philosopher.

One solution is available at [diningphilosophers.go](src/diningphilosophers.go).

<br/>
