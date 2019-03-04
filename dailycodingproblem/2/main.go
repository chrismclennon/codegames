// Given an array of integers, return a new array such that each element at 
// index i of the new array is the product of all the numbers in the original 
// array except the one at i.
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
// [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
// be [2, 3, 6].
//
// Follow-up: what if you can't use division?
package main

import (
	"fmt"
)

func main() {
	caseOne := []int{1, 2, 3, 4, 5}
	caseTwo := []int{3, 2, 1}
	fmt.Println("Case one: ", solution(caseOne))
	fmt.Println("Case two: ", solution(caseTwo))

}

// Construct left array, then construct right array, and then can multiply
// left * right to get solution.
//
// Runtime: O(N)
// Memory: O(N)
func solution(numbers []int) []int {
	left := make([]int, len(numbers))
	right := make([]int, len(numbers))
	left[0], right[len(right)-1] = 1, 1
	for i := 1; i < len(left); i++ {
		left[i] = left[i-1] * numbers[i-1]
	}
	// TODO: fix this loop when more awake
	for i := len(right)-2; i > 0; i-- {
		right[i] = right[i+1] * numbers[i]
	}
	fmt.Println(left)
	fmt.Println(right)
	return nil
}