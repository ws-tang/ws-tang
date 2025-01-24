package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/****
The code is referenced from the result of the Google search with the phrase below:
"solving dining philosophers problem golang".
****/

type Chopstick struct {
	sync.Mutex
}

type Philosopher struct {
	id         int
	mealsEaten int

	leftCS, rightCS *Chopstick
}

type Request struct {
	id    int
	reply chan bool
}

func host(requests chan Request, done chan int) {
	active := 0
	queue := []Request{}

	for {
		select {
		case req := <-requests:
			if active < 2 {
				active++
				req.reply <- true
			} else {
				queue = append(queue, req)
			}
		case <-done:
			active--
			if len(queue) > 0 {
				req := queue[0]
				queue = queue[1:]
				active++
				req.reply <- true
			}
		}
	}
}

func (p *Philosopher) eat(wg *sync.WaitGroup, maxMeals int, requests chan Request, done chan int) {
	defer wg.Done()

	for p.mealsEaten < maxMeals {

		req := Request{
			id:    p.id,
			reply: make(chan bool),
		}
		requests <- req
		<-req.reply

		// Get the locks of the chopsticks from the left and right sides
		p.leftCS.Lock()
		p.rightCS.Lock()

		fmt.Printf("Starting to eat <%d>.\n", p.id)
		time.Sleep(time.Duration(rand.Intn(300)+100) * time.Millisecond)
		p.mealsEaten++
		fmt.Printf("Finishing eating <%d> (Completed [%d] meals).\n", p.id, p.mealsEaten)

		p.rightCS.Unlock()
		p.leftCS.Unlock()

		done <- p.id

		time.Sleep(time.Millisecond * 200)
	}
}

func main() {
	numPhilosophers := 5
	maxMeals := 3

	chopsticks := make([]*Chopstick, numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		chopsticks[i] = new(Chopstick)
	}

	philosophers := make([]*Philosopher, numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		philosophers[i] = &Philosopher{
			id:      i + 1,
			leftCS:  chopsticks[i],
			rightCS: chopsticks[(i+1)%numPhilosophers],
		}
	}

	requests := make(chan Request)
	done := make(chan int)

	go host(requests, done)

	var wg sync.WaitGroup
	wg.Add(numPhilosophers)
	for i := range numPhilosophers {
		go philosophers[i].eat(&wg, maxMeals, requests, done)
	}

	wg.Wait()

	fmt.Println("Done...")
}
