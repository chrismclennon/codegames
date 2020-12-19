package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	input := readInput()
	partOne(input)
	partTwo(input)
}

func readInput() []string {
	data, _ := ioutil.ReadFile("input.txt")
	return strings.Split(string(data), "\n")
}

func partOne(instructions []string) {
	memory := map[int]int64{}
	mask := "X"

	for _, instruction := range instructions {
		if strings.HasPrefix(instruction, "mask") {
			mask = instruction[7:]
		} else {
			memoryAddressStartIndex := strings.Index(instruction, "[") + 1
			memoryAddressEndIndex := strings.Index(instruction, "]")
			memoryAddress, memoryAddressParseErr := strconv.Atoi(instruction[memoryAddressStartIndex:memoryAddressEndIndex])
			if memoryAddressParseErr != nil {
				panic(memoryAddressParseErr)
			}
			valueStartIndex := strings.Index(instruction, "=") + 2
			value, valueParseErr := strconv.Atoi(instruction[valueStartIndex:])
			if valueParseErr != nil {
				panic(valueParseErr)
			}
			setMemoryAddress(memory, memoryAddress, value, mask)
		}
	}

	var result int64
	for _, value := range memory {
		result += value
	}
	fmt.Printf("Part one answer: %d\n", result)
}

func setMemoryAddress(memory map[int]int64, memoryAddress, value int, mask string) {
	binaryValue := strconv.FormatInt(int64(value), 2)
	binaryValue = reverseString(binaryValue)
	mask = reverseString(mask)
	result := []rune{}

	for index := 0; index < len(mask); index++ {
		maskDigit := mask[index]
		binaryDigit := '0'
		if index < len(binaryValue) {
			binaryDigit = rune(binaryValue[index])
		}

		if maskDigit != 'X' {
			result = append(result, rune(maskDigit))
		} else {
			result = append(result, binaryDigit)
		}
	}

	base10value, base10parseErr := strconv.ParseInt(reverseString(string(result)), 2, 64)
	if base10parseErr != nil {
		panic(base10parseErr)
	}
	memory[memoryAddress] = base10value
}

func reverseString(s string) string {
	runes := []rune(s)
	for i := 0; i < len(s)/2; i++ {
		runes[i], runes[len(s)-1-i] = runes[len(s)-1-i], runes[i]
	}
	retval := string(runes)
	return retval
}

func partTwo(instructions []string) {
	memory := map[int64]int{}
	mask := "X"

	for _, instruction := range instructions {
		if strings.HasPrefix(instruction, "mask") {
			mask = instruction[7:]
		} else {
			memoryAddressStartIndex := strings.Index(instruction, "[") + 1
			memoryAddressEndIndex := strings.Index(instruction, "]")
			memoryAddress, memoryAddressParseErr := strconv.Atoi(instruction[memoryAddressStartIndex:memoryAddressEndIndex])
			if memoryAddressParseErr != nil {
				panic(memoryAddressParseErr)
			}
			valueStartIndex := strings.Index(instruction, "=") + 2
			value, valueParseErr := strconv.Atoi(instruction[valueStartIndex:])
			if valueParseErr != nil {
				panic(valueParseErr)
			}
			setMemoryAddressPartTwo(memory, memoryAddress, value, mask)
		}
	}

	var result int
	for _, value := range memory {
		result += value
	}
	fmt.Printf("Part two answer: %d\n", result)
}

func setMemoryAddressPartTwo(memory map[int64]int, memoryAddress, value int, mask string) {
	binaryMemoryAddress := strconv.FormatInt(int64(memoryAddress), 2)
	binaryMemoryAddress = reverseString(binaryMemoryAddress)
	mask = reverseString(mask)
	memoryAddressTemplate := []rune{}

	for index := 0; index < len(mask); index++ {
		maskDigit := mask[index]
		binaryDigit := '0'
		if index < len(binaryMemoryAddress) {
			binaryDigit = rune(binaryMemoryAddress[index])
		}

		if maskDigit != '0' {
			memoryAddressTemplate = append(memoryAddressTemplate, rune(maskDigit))
		} else {
			memoryAddressTemplate = append(memoryAddressTemplate, binaryDigit)
		}
	}

	memoryAddressTemplate = reverseRuneSlice(memoryAddressTemplate)
	allMemoryAddresses := parseMemoryAddressTemplate(memoryAddressTemplate)

	for _, currentMemoryAddress := range allMemoryAddresses {
		base10address, base10parseErr := strconv.ParseInt(currentMemoryAddress, 2, 64)
		if base10parseErr != nil {
			panic(base10parseErr)
		}
		memory[base10address] = value
	}
}

func reverseRuneSlice(runes []rune) []rune {
	for i := 0; i < len(runes)/2; i++ {
		runes[i], runes[len(runes)-1-i] = runes[len(runes)-1-i], runes[i]
	}
	return runes
}

func parseMemoryAddressTemplate(memoryAddressTemplate []rune) []string {
	queue := list.New()
	queue.PushBack(memoryAddressTemplate)
	retval := []string{}

	for queue.Len() > 0 {
		nextItem := queue.Front()
		queue.Remove(nextItem)
		nextMemoryAddressTemplate := nextItem.Value.([]rune)

		for index, currentRune := range nextMemoryAddressTemplate {
			if currentRune == 'X' {
				newTemplate1 := make([]rune, len(nextMemoryAddressTemplate))
				copy(newTemplate1, nextMemoryAddressTemplate)
				newTemplate1[index] = '1'
				queue.PushBack(newTemplate1)

				newTemplate0 := make([]rune, len(nextMemoryAddressTemplate))
				copy(newTemplate0, nextMemoryAddressTemplate)
				newTemplate0[index] = '0'
				queue.PushBack(newTemplate0)

				break
			}

			if index == len(nextMemoryAddressTemplate)-1 {
				retval = append(retval, string(nextMemoryAddressTemplate))
			}
		}
	}
	return retval
}
