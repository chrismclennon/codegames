package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type instruction struct {
	operation string
	argument  int
}

func main() {
	instructions := parseInput()
	partOne(instructions)
}

func parseInput() []instruction {
	// data, readFileErr := ioutil.ReadFile("sampleInput.txt")
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}
	lines := strings.Split(string(data), "\n")

	instructions := []instruction{}
	for _, line := range lines {
		lineSplit := strings.Split(line, " ")
		operation := lineSplit[0]
		value, _ := strconv.Atoi(lineSplit[1])
		newInstruction := instruction{
			operation: operation,
			argument:  value,
		}
		instructions = append(instructions, newInstruction)
	}
	return instructions
}

func partOne(instructions []instruction) {
	accumulatorValue := 0
	continueLoop := true
	index := 0
	visitedLines := map[int]bool{}

	for continueLoop {
		if _, lineWasVisited := visitedLines[index]; lineWasVisited {
			fmt.Printf("Part one answer: %d\n", accumulatorValue)
			return
		}
		visitedLines[index] = true

		currentInstruction := instructions[index]
		switch currentInstruction.operation {
		case "nop":
			index++
		case "jmp":
			index += currentInstruction.argument
		case "acc":
			accumulatorValue += currentInstruction.argument
			index++
		}
	}
}
