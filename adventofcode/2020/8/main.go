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
	partTwo(instructions)
}

func parseInput() []instruction {
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

func runProgram(instructions []instruction) (int, bool) {
	accumulatorValue := 0
	index := 0
	visitedLines := map[int]bool{}

	for index < len(instructions) {
		if _, lineWasVisited := visitedLines[index]; lineWasVisited {
			return accumulatorValue, true
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
	return accumulatorValue, false
}

func partOne(instructions []instruction) {
	accumulatorValue, _ := runProgram(instructions)
	fmt.Printf("Part one answer: %d\n", accumulatorValue)
}

func partTwo(instructions []instruction) {
	for index, currentInstruction := range instructions {
		if currentInstruction.operation == "nop" {
			instructions[index] = instruction{
				operation: "jmp",
				argument:  currentInstruction.argument,
			}
		} else {
			instructions[index] = instruction{
				operation: "nop",
				argument:  currentInstruction.argument,
			}
		}
		accumulatorValue, isLoop := runProgram(instructions)
		if !isLoop {
			fmt.Printf("Part two answer: %d\n", accumulatorValue)
			return
		}
		instructions[index] = currentInstruction
	}
}
