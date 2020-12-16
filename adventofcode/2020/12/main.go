package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type coordinate struct {
	X, Y int
}

type shipInstruction struct {
	direction rune
	value     int
}

func main() {
	instructions := parseInput()
	partOne(instructions)
	partTwo(instructions)
}

func parseInput() []shipInstruction {
	data, _ := ioutil.ReadFile("input.txt")

	lines := strings.Split(string(data), "\n")
	retval := make([]shipInstruction, len(lines))
	for index, line := range lines {
		direction := rune(line[0])
		value, _ := strconv.Atoi(line[1:])
		instruction := shipInstruction{
			direction: direction,
			value:     value,
		}
		retval[index] = instruction
	}
	return retval
}

func run(instructions []shipInstruction, startingCoordinate coordinate) coordinate {
	headings := map[rune]coordinate{
		'N': coordinate{X: 0, Y: 1},
		'E': coordinate{X: 1, Y: 0},
		'S': coordinate{X: 0, Y: -1},
		'W': coordinate{X: -1, Y: 0},
	}
	currentCoordinate := startingCoordinate
	shipHeading := 'E'

	for _, instruction := range instructions {
		switch instruction.direction {
		case 'F':
			currentCoordinate.X += instruction.value * headings[shipHeading].X
			currentCoordinate.Y += instruction.value * headings[shipHeading].Y
		case 'L':
			shipHeading = turnShip(shipHeading, 'L', instruction.value)
		case 'R':
			shipHeading = turnShip(shipHeading, 'R', instruction.value)
		default:
			currentCoordinate.X += instruction.value * headings[instruction.direction].X
			currentCoordinate.Y += instruction.value * headings[instruction.direction].Y
		}
	}
	return currentCoordinate
}

func turnShip(currentHeading, turnDirection rune, degrees int) rune {
	numTurns := degrees / 90
	for i := 0; i < numTurns; i++ {
		currentHeading = turnShipOnce(currentHeading, turnDirection)
	}
	return currentHeading
}

func turnShipOnce(currentHeading, turnDirection rune) rune {
	switch currentHeading {
	case 'N':
		switch turnDirection {
		case 'L':
			return 'W'
		case 'R':
			return 'E'
		}
	case 'E':
		switch turnDirection {
		case 'L':
			return 'N'
		case 'R':
			return 'S'
		}
	case 'S':
		switch turnDirection {
		case 'L':
			return 'E'
		case 'R':
			return 'W'
		}
	case 'W':
		switch turnDirection {
		case 'L':
			return 'S'
		case 'R':
			return 'N'
		}
	}
	return 'X'
}

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func partOne(instructions []shipInstruction) {
	startingCoordinate := coordinate{X: 0, Y: 0}
	destination := run(instructions, startingCoordinate)
	answer := absInt(destination.X) + absInt(destination.Y)
	fmt.Printf("Part one answer: %d\n", answer)
}

func rotateWaypoint(waypointCoordinate coordinate, direction rune, degrees int) coordinate {
	if direction == 'L' {
		for degrees != 0 {
			waypointCoordinate.X, waypointCoordinate.Y = -waypointCoordinate.Y, waypointCoordinate.X
			degrees -= 90
		}
	} else {
		for degrees != 0 {
			waypointCoordinate.X, waypointCoordinate.Y = waypointCoordinate.Y, -waypointCoordinate.X
			degrees -= 90
		}
	}
	return waypointCoordinate
}

func partTwo(instructions []shipInstruction) {
	waypointCoordinate := coordinate{X: 10, Y: 1}
	shipCoordinate := coordinate{X: 0, Y: 0}

	directions := map[rune]coordinate{
		'N': coordinate{X: 0, Y: 1},
		'E': coordinate{X: 1, Y: 0},
		'S': coordinate{X: 0, Y: -1},
		'W': coordinate{X: -1, Y: 0},
	}

	for _, instruction := range instructions {
		switch instruction.direction {
		case 'N', 'E', 'S', 'W':
			waypointCoordinate.X += instruction.value * directions[instruction.direction].X
			waypointCoordinate.Y += instruction.value * directions[instruction.direction].Y
		case 'L', 'R':
			waypointCoordinate = rotateWaypoint(waypointCoordinate, instruction.direction, instruction.value)
		case 'F':
			shipCoordinate.X += waypointCoordinate.X * instruction.value
			shipCoordinate.Y += waypointCoordinate.Y * instruction.value
		}
	}

	answer := absInt(shipCoordinate.X) + absInt(shipCoordinate.Y)
	fmt.Printf("Part two answer: %d\n", answer)
}
