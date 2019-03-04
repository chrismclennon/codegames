// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
// Bonus: Can you do this in one pass?
package main

import (
	"fmt"
	"sort"
)

func main() {
	k := 17
	numbers := []int{10, 15, 3, 7}
	numbersCopy := make([]int, len(numbers))
	copy(numbersCopy, numbers)
	fmt.Println("Sorted solution [Runtime: O(N log N), Memory: O(1)]:", sortSolution(numbers, k))
	fmt.Println("Optimal solution [Runtime: O(N), Memory: O(N)]:", optimalSolution(numbersCopy, k))
}

// Sort the array then move the front if the number is too small, and move
// the back if the number is too large. Converge on a solution.
//
// Runtime: O(N log N)
// Memory: O(1)
func sortSolution(numbers []int, k int)  bool {
	sort.Ints(numbers)
	frontIndex, backIndex := 0, len(numbers)-1
	for frontIndex < backIndex {
		frontNum := numbers[frontIndex]
		backNum := numbers[backIndex]
		currentNum := frontNum + backNum
		if currentNum == k {
			return true
		} else if currentNum > k {
			backIndex -= 1
		} else {
			frontIndex += 1
		}
	}
	return false
}

// Store values in a set. Check for existence of complement number.
//
// Runtime: O(N)
// Memory: O(N)
func optimalSolution(numbers []int, k int) bool {
	set := make(map[int]bool)
	for _, number := range numbers {
		set[number] = true
		complementNumber := number - k
		if complementNumber < 0 {
			complementNumber *= -1
		}
		if _, ok := set[complementNumber]; ok {
			return true
		}
	}
	return false
}