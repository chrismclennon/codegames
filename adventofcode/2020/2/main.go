package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type PasswordEntry struct {
	MinFrequency int
	MaxFrequency int
	Character    rune
	Password     string
}

func main() {
	passwordEntries := readInput()
	partOne(passwordEntries)
	partTwo(passwordEntries)
}

func readInput() []PasswordEntry {
	passwordEntries := []PasswordEntry{}

	inputFile, fileReadErr := os.Open("input.txt")
	if fileReadErr != nil {
		panic(fileReadErr)
	}
	defer inputFile.Close()

	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		line := scanner.Text()

		splitLine := strings.Split(line, " ")
		frequencies := strings.Split(splitLine[0], "-")
		minFrequency, _ := strconv.Atoi(frequencies[0])
		maxFrequency, _ := strconv.Atoi(frequencies[1])
		character := rune(splitLine[1][0])
		password := splitLine[2]

		entry := PasswordEntry{
			minFrequency,
			maxFrequency,
			character,
			password,
		}
		passwordEntries = append(passwordEntries, entry)
	}
	return passwordEntries
}

func partOne(passwordEntries []PasswordEntry) {
	numValidPasswordEntries := 0

	for _, passwordEntry := range passwordEntries {
		if isValidPasswordPartOne(passwordEntry) {
			numValidPasswordEntries++
		}
	}

	fmt.Printf("Part One: numValidPasswordEntries = %d\n", numValidPasswordEntries)
}

func isValidPasswordPartOne(entry PasswordEntry) bool {
	count := 0
	for _, character := range entry.Password {
		if character == entry.Character {
			count++
		}
	}
	return count >= entry.MinFrequency && count <= entry.MaxFrequency
}

func partTwo(passwordEntries []PasswordEntry) {
	numValidPasswordEntries := 0

	for _, passwordEntry := range passwordEntries {
		if isValidPasswordPartTwo(passwordEntry) {
			numValidPasswordEntries++
		}
	}

	fmt.Printf("Part Two: nuMValidPasswordEntries = %d\n", numValidPasswordEntries)
}

func isValidPasswordPartTwo(entry PasswordEntry) bool {
	firstMatch := rune(entry.Password[entry.MinFrequency-1]) == entry.Character
	secondMatch := rune(entry.Password[entry.MaxFrequency-1]) == entry.Character
	return firstMatch != secondMatch
}
