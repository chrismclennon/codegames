package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("== Sample ==")
	sampleNumbers := readInput("sampleInput.txt")
	partOneResult := partOne(sampleNumbers, 5)
	fmt.Printf("Part one answer: %d\n", partOneResult)
	partTwo(sampleNumbers, partOneResult)

	fmt.Println("\n\n== Acutal ==")
	numbers := readInput("input.txt")
	partOneResult = partOne(numbers, 25)
	fmt.Printf("Part one answer: %d\n", partOneResult)
	partTwo(numbers, partOneResult)
}

func readInput(filename string) []int {
	data, readFileErr := ioutil.ReadFile(filename)
	if readFileErr != nil {
		panic(readFileErr)
	}
	lines := strings.Split(string(data), "\n")

	numbers := []int{}
	for _, line := range lines {
		number, _ := strconv.Atoi(line)
		numbers = append(numbers, number)
	}
	return numbers
}

func partOne(numbers []int, windowSize int) int {
	queue := list.New() // In retrospect, I don't need a queue. I could've just tracked some indexes on the numbers slice.
	allNumbers := map[int]bool{}

	for _, number := range numbers[:windowSize] {
		queue.PushBack(number)
		allNumbers[number] = true
	}
	for _, targetNumber := range numbers[windowSize:] {
		currentElement := queue.Front()
		complementNumberFound := false

		for i := 0; i < windowSize; i++ {
			currentNumber := currentElement.Value.(int)
			complementNumber := targetNumber - currentNumber
			if _, complementNumberExists := allNumbers[complementNumber]; complementNumberExists {
				complementNumberFound = true
				break
			}
			currentElement = currentElement.Next()
		}
		if !complementNumberFound {
			return targetNumber
		}

		frontNumber := queue.Front().Value.(int)
		delete(allNumbers, frontNumber)
		allNumbers[targetNumber] = true

		queue.Remove(queue.Front())
		queue.PushBack(targetNumber)
	}
	return -1
}

func partTwo(numbers []int, targetNumber int) {
	leftIndex, rightIndex := 0, 0
	currentSum := 0
	for rightIndex < len(numbers) {
		if currentSum < targetNumber {
			currentSum += numbers[rightIndex]
			rightIndex++
		} else if currentSum > targetNumber {
			currentSum -= numbers[leftIndex]
			leftIndex++
		} else {
			minInt, maxInt := minAndMaxInt(numbers[leftIndex:rightIndex])
			result := minInt + maxInt
			fmt.Printf("Part two answer: %d\n", result)
			return
		}
	}
}

func minAndMaxInt(numbers []int) (int, int) {
	minInt, maxInt := math.MaxInt64, math.MinInt64
	for _, number := range numbers {
		if number < minInt {
			minInt = number
		}
		if number > maxInt {
			maxInt = number
		}
	}
	return minInt, maxInt
}
