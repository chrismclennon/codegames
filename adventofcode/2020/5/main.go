package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func main() {
	boardingPasses := parseInput()
	partOne(boardingPasses)
	partTwo(boardingPasses)
}

func parseInput() []string {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}
	return strings.Split(string(data), "\n")
}

func calculateSeatID(boardingPass string) int {
	leftRow, rightRow := 0, 127
	for _, value := range boardingPass[:7] {
		if value == 'F' {
			rightRow = leftRow + (rightRow-leftRow)/2
		} else {
			leftRow = 1 + leftRow + (rightRow-leftRow)/2
		}
	}
	row := leftRow

	leftSeat, rightSeat := 0, 7
	for _, value := range boardingPass[7:] {
		if value == 'L' {
			rightSeat = leftSeat + (rightSeat-leftSeat)/2
		} else {
			leftSeat = 1 + leftSeat + (rightSeat-leftSeat)/2
		}
	}
	seat := leftSeat

	seatID := row*8 + seat
	return seatID
}

func partOne(boardingPasses []string) {
	maxSeatID := -1
	for _, boardingPass := range boardingPasses {
		seatID := calculateSeatID(boardingPass)
		if seatID > maxSeatID {
			maxSeatID = seatID
		}
	}
	fmt.Printf("Part one answer: %d\n", maxSeatID)
}

func partTwo(boardingPasses []string) {
	seatIDs := []int{}
	for _, boardingPass := range boardingPasses {
		seatID := calculateSeatID(boardingPass)
		seatIDs = append(seatIDs, seatID)
	}

	sort.Ints(seatIDs)
	previousSeatID := seatIDs[0]
	for _, seatID := range seatIDs[1:] {
		if seatID-previousSeatID > 1 {
			fmt.Printf("Part two answer: %d\n", seatID-1)
			return
		}
		previousSeatID = seatID
	}
}
