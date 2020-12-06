package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type customsDeclaration struct {
	numResponses int
	responses    map[rune]int
}

func main() {
	customsDeclarations := parseInput()
	partOne(customsDeclarations)
	partTwo(customsDeclarations)
}

func parseInput() []customsDeclaration {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}

	declarations := []customsDeclaration{}
	declaration := customsDeclaration{
		responses: make(map[rune]int),
	}
	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		if line == "" {
			declarations = append(declarations, declaration)
			declaration = customsDeclaration{
				responses: make(map[rune]int),
			}
			continue
		}
		declaration.numResponses++
		for _, letter := range line {
			if num, ok := declaration.responses[letter]; ok {
				declaration.responses[letter] = num + 1
			} else {
				declaration.responses[letter] = 1
			}
		}
	}
	return declarations
}

func partOne(declarations []customsDeclaration) {
	count := 0
	for _, declaration := range declarations {
		count += len(declaration.responses)
	}
	fmt.Printf("Part one answer: %d\n", count)
}

func partTwo(declarations []customsDeclaration) {
	count := 0
	for _, declaration := range declarations {
		for _, value := range declaration.responses {
			if value == declaration.numResponses {
				count++
			}
		}
	}
	fmt.Printf("Part two answer: %d\n", count)
}
