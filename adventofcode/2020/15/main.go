package main

import "fmt"

type numberPair struct {
	mostRecentTurn, previousTurn int
}

func main() {
	partOne()
	partTwo()
	simpleMain()
}

func partOne() {
	fmt.Println("== Part one ==")
	testCases := []struct {
		startingNumbers []int
		expected        int
	}{
		{[]int{0, 3, 6}, 436},
		{[]int{1, 3, 2}, 1},
		{[]int{2, 1, 3}, 10},
		{[]int{1, 2, 3}, 27},
		{[]int{2, 3, 1}, 78},
		{[]int{3, 2, 1}, 438},
		{[]int{3, 1, 2}, 1836},
	}
	for _, testCase := range testCases {
		actual := playGame(testCase.startingNumbers, 2020)
		outcome := "FAIL"
		if actual == testCase.expected {
			outcome = "PASS"
		}
		fmt.Printf("Running test case: %v :: Expected %d :: Actual %d :: %s\n", testCase.startingNumbers, testCase.expected, actual, outcome)
	}

	answer := playGame([]int{16, 1, 0, 18, 12, 14, 19}, 2020)
	fmt.Printf("\nPart one answer: %d\n", answer)
}

func partTwo() {
	fmt.Println("\n== Part two ==")

	testCases := []struct {
		startingNumbers []int
		expected        int
	}{
		{[]int{0, 3, 6}, 175594},
		{[]int{1, 3, 2}, 2578},
		{[]int{2, 1, 3}, 3544142},
		{[]int{1, 2, 3}, 261214},
		{[]int{2, 3, 1}, 6895259},
		{[]int{3, 2, 1}, 18},
		{[]int{3, 1, 2}, 362},
	}
	for _, testCase := range testCases {
		actual := playGame(testCase.startingNumbers, 30000000)
		outcome := "FAIL"
		if actual == testCase.expected {
			outcome = "PASS"
		}
		fmt.Printf("Running test case: %v :: Expected %d :: Actual %d :: %s\n", testCase.startingNumbers, testCase.expected, actual, outcome)
	}

	answer := playGame([]int{16, 1, 0, 18, 12, 14, 19}, 30000000)
	fmt.Printf("\nPart two answer: %d\n", answer)
}

func playGame(startingNumbers []int, numTurns int) int {
	numbers := map[int]numberPair{}
	for index, num := range startingNumbers {
		numbers[num] = numberPair{mostRecentTurn: index + 1, previousTurn: -1}
	}

	turnNumber := len(startingNumbers) + 1
	lastNumber := startingNumbers[len(startingNumbers)-1]

	for turnNumber <= numTurns {
		if lastNumberPair, ok := numbers[lastNumber]; ok {
			if lastNumberPair.previousTurn == -1 {
				updateNumberPair(numbers, 0, turnNumber)
				lastNumber = 0
			} else {
				numTurnsSinceLastNumberSpoken := lastNumberPair.mostRecentTurn - lastNumberPair.previousTurn
				updateNumberPair(numbers, numTurnsSinceLastNumberSpoken, turnNumber)
				lastNumber = numTurnsSinceLastNumberSpoken
			}
		} else {
			updateNumberPair(numbers, 0, turnNumber)
			lastNumber = 0
		}
		turnNumber++
	}
	return lastNumber
}

func updateNumberPair(numbers map[int]numberPair, number, turnNumber int) {
	if pair, ok := numbers[number]; ok {
		pair.previousTurn = pair.mostRecentTurn
		pair.mostRecentTurn = turnNumber
		numbers[number] = pair
	} else {
		numbers[number] = numberPair{mostRecentTurn: turnNumber, previousTurn: -1}
	}
}
