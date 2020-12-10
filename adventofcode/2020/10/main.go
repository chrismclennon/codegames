package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func main() {
	joltages := readInput()
	partOne(joltages)
	partTwo(joltages)
}

func readInput() []int {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}

	lines := strings.Split(string(data), "\n")
	joltages := []int{}

	for _, line := range lines {
		joltage, _ := strconv.Atoi(line)
		joltages = append(joltages, joltage)
	}
	sort.Ints(joltages)
	joltages = append(joltages, joltages[len(joltages)-1]+3) // Add built-in adapter
	return joltages
}

func partOne(joltages []int) {
	differences := map[int]int{
		1: 0,
		2: 0,
		3: 0,
	}
	previous := 0
	for _, current := range joltages {
		difference := current - previous
		differences[difference]++
		previous = current
	}
	result := differences[1] * differences[3]
	fmt.Printf("Part one answer: %d\n", result)
}

func partTwo(joltages []int) {
	cache := make([]int, len(joltages))
	cache[len(joltages)-1] = 1

	fmt.Printf("Part two answer: %d\n", partTwoHelper(joltages, 0, -1, cache))
}

func partTwoHelper(joltages []int, currentValue, currentIndex int, cache []int) int {
	retval := 0
	if currentIndex > 0 && currentIndex < len(joltages) && cache[currentIndex] > 0 {
		return cache[currentIndex]
	}
	for nextIndex := currentIndex + 1; nextIndex <= nextIndex+3 && nextIndex < len(joltages); nextIndex++ {
		nextValue := joltages[nextIndex]
		if nextValue-currentValue <= 3 {
			helperValue := partTwoHelper(joltages, nextValue, nextIndex, cache)
			cache[nextIndex] = helperValue
			retval += helperValue
		}
	}
	return retval
}
