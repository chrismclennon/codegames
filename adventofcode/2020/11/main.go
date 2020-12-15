package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type fn func([][]rune, int, int) int

func main() {
	seats := parseInput()
	partOne(seats)
	partTwo(seats)
}

func parseInput() [][]rune {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}
	lines := strings.Split(string(data), "\n")
	retval := [][]rune{}
	for _, line := range lines {
		retval = append(retval, []rune(line))
	}
	return retval
}

func doStep(seats [][]rune, adjacentFn fn, seatTolerance int) ([][]rune, int) {
	newSeats := deepCopy(seats)
	countChanges := 0

	for rowIndex, rowSeats := range seats {
		for colIndex, seat := range rowSeats {
			if seat == '.' {
				continue
			}
			adjacentOccupied := adjacentFn(seats, rowIndex, colIndex)
			if seat == 'L' && adjacentOccupied == 0 {
				newSeats[rowIndex][colIndex] = '#'
				countChanges++
			} else if seat == '#' && adjacentOccupied >= seatTolerance {
				newSeats[rowIndex][colIndex] = 'L'
				countChanges++
			}
		}
	}

	return newSeats, countChanges
}

func deepCopy(seats [][]rune) [][]rune {
	newSeats := make([][]rune, 0, len(seats))
	for _, line := range seats {
		newLine := make([]rune, len(line))
		copy(newLine, line)
		newSeats = append(newSeats, newLine)
	}
	return newSeats
}

func countAdjacentOccupied(seats [][]rune, rowIndex, colIndex int) int {
	adjacentCoordinates := [][]int{
		{-1, 0},
		{-1, -1},
		{-1, 1},
		{0, -1},
		{0, 1},
		{1, 0},
		{1, -1},
		{1, 1},
	}

	count := 0
	for _, adjacentCoordinate := range adjacentCoordinates {
		newRowIndex := rowIndex + adjacentCoordinate[0]
		newColIndex := colIndex + adjacentCoordinate[1]
		if newRowIndex < 0 || newColIndex < 0 || newRowIndex >= len(seats) || newColIndex >= len(seats[0]) {
			continue
		}
		if seats[newRowIndex][newColIndex] == '#' {
			count++
		}
	}
	return count
}

func countSightOccupied(seats [][]rune, rowIndex, colIndex int) int {
	directions := [][]int{
		{-1, 0},
		{-1, -1},
		{-1, 1},
		{0, -1},
		{0, 1},
		{1, 0},
		{1, -1},
		{1, 1},
	}

	count := 0
	for _, direction := range directions {
		newRowIndex := rowIndex + direction[0]
		newColIndex := colIndex + direction[1]
		for newRowIndex >= 0 && newColIndex >= 0 && newRowIndex < len(seats) && newColIndex < len(seats[0]) {
			if seats[newRowIndex][newColIndex] == '#' {
				count++
				break
			} else if seats[newRowIndex][newColIndex] == 'L' {
				break
			}
			newRowIndex = newRowIndex + direction[0]
			newColIndex = newColIndex + direction[1]
		}
	}
	return count
}

func countSeats(seats [][]rune) int {
	countSeats := 0
	for _, rowSeats := range seats {
		for _, seat := range rowSeats {
			if seat == '#' {
				countSeats++
			}
		}
	}
	return countSeats
}

func printSeats(seats [][]rune) {
	for _, row := range seats {
		fmt.Println(string(row))
	}
	fmt.Println()
}

func partOne(seats [][]rune) {
	countChanges := -1
	for countChanges != 0 {
		newSeats, newCountChanges := doStep(seats, countAdjacentOccupied, 4)
		seats = newSeats
		countChanges = newCountChanges
	}
	fmt.Printf("Part one answer: %d\n", countSeats(seats))
}

func partTwo(seats [][]rune) {
	countChanges := -1
	for countChanges != 0 {
		newSeats, newCountChanges := doStep(seats, countSightOccupied, 5)
		seats = newSeats
		countChanges = newCountChanges
	}
	fmt.Printf("Part two answer: %d\n", countSeats(seats))
}
