package main

import "fmt"

func simpleMain() {
	fmt.Println("\n== Simpler implementation ==")
	fmt.Printf(
		"Part two answer: %d\n",
		playSimpleGame([]int{16, 1, 0, 18, 12, 14, 19}, 30000000),
	)
}

func playSimpleGame(startingNumbers []int, numTurns int) (currentNumber int) {
	memory := map[int]int{}
	for i, startingNumber := range startingNumbers {
		currentNumber = startingNumber
		memory[currentNumber] = i + 1
	}

	for previousTurn := len(startingNumbers); previousTurn < numTurns; previousTurn++ {
		currentNumberSpokenAtTurn, ok := memory[currentNumber]
		memory[currentNumber] = previousTurn
		if ok {
			currentNumber = previousTurn - currentNumberSpokenAtTurn
		} else {
			currentNumber = 0
		}
	}
	return currentNumber
}
