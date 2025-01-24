# Golang Dev Notes

My dev notes for Golang is listed herein.
<br/>

## Development Setup

### Installation

Get Go at [Go download](https://go.dev/dl/). Select the platform that applies to the development environment. My personal dev environment is on Windows so I choose the installer image looks like **go1.24.2.windows-amd64.msi**, where 1.24.2 is the version and will vary as time goes.

If you are interested in the corresponding source code, you can also download Go source code on the same download page.

You can also refer to Golang's own documentation about [Download and install](https://go.dev/doc/install).

<br/>

### Environment Setup

Set the **GOPATH** environment variable.

    setx GOPATH %USERPROFILE%\go

<br/>

### IDE

[Microsoft Visual Studio Code](../devenv.md#visual-studio-code) is a good IDE for Golang.

The **Go** (Go for Visual Studio Code) extension from Go Team at Google is useful for Golang with Microsoft Visual Studio Code.

<br/>

## Tutorials and Documentation

- [Go Documentation](https://go.dev/doc/)
- [Effective Go](https://go.dev/doc/effective_go)

<br/>

## Source Code Repository

My source code repository for Golang code is at my GitHub repository herein under [ws-tang/dev/golang/src](https://github.com/ws-tang/ws-tang/tree/main/dev/golang/src).

<br/>

## Practice and Exercise

### The dining philosopher’s problem

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

### Another example...
