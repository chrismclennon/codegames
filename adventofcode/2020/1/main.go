package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	expenseReportData := readExpenseReportData()
	partOne(expenseReportData)
	partTwo(expenseReportData)
}

func readExpenseReportData() []int {
	expenseReportFile, fileReadErr := os.Open("input.txt")
	if fileReadErr != nil {
		panic(fileReadErr)
	}
	defer expenseReportFile.Close()

	var expenseReportData []int
	scanner := bufio.NewScanner(expenseReportFile)
	for scanner.Scan() {
		value := scanner.Text()
		intValue, parseErr := strconv.Atoi(value)
		if parseErr != nil {
			panic(parseErr)
		}
		expenseReportData = append(expenseReportData, intValue)
	}
	if scannerErr := scanner.Err(); scannerErr != nil {
		panic(scannerErr)
	}
	return expenseReportData
}

func partOne(expenseReportData []int) {
	seenValues := map[int]int{}
	for _, value := range expenseReportData {
		complementValue := 2020 - value
		if _, ok := seenValues[complementValue]; ok {
			fmt.Printf("Part One Answer: %d * %d = %d\n", value, complementValue, value*complementValue)
			return
		}
		seenValues[value] = 1
	}
}

func partTwo(expenseReportData []int) {
	sort.Ints(expenseReportData)

	for currentIndex := 0; currentIndex < len(expenseReportData)-2; currentIndex++ {
		leftIndex, rightIndex := currentIndex+1, len(expenseReportData)-1
		currentValue, leftValue, rightValue := expenseReportData[currentIndex], expenseReportData[leftIndex], expenseReportData[rightIndex]
		for leftIndex < rightIndex {
			currentSum := currentValue + leftValue + rightValue
			if currentSum == 2020 {
				fmt.Printf("Part Two Answer: %d * %d * %d = %d\n", currentValue, leftValue, rightValue, currentValue*leftValue*rightValue)
				return
			} else if currentSum < 2020 {
				leftIndex++
				leftValue = expenseReportData[leftIndex]
			} else if currentSum > 2020 {
				rightIndex--
				rightValue = expenseReportData[rightIndex]
			}
		}
	}
}
