package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	passports := parseInput()
	numValidPassports := countValidPassports(passports)
	fmt.Printf("Part one answer: %d\n", numValidPassports)

	numDataValidatedPassports := countDataValidatedPassports(passports)
	fmt.Printf("Part two answer: %d\n", numDataValidatedPassports)
}

func parseInput() []map[string]string {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}

	retval := []map[string]string{}
	currentPassport := map[string]string{}
	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		if line == "" {
			retval = append(retval, currentPassport)
			currentPassport = map[string]string{}
			continue
		}
		fields := strings.Fields(line)
		for _, field := range fields {
			splitField := strings.Split(field, ":")
			currentPassport[splitField[0]] = splitField[1]
		}
	}
	retval = append(retval, currentPassport)

	return retval
}

func countValidPassports(passports []map[string]string) int {
	numValidPassports := 0
	requiredKeys := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, passport := range passports {
		missingRequiredKey := false
		for _, requiredKey := range requiredKeys {
			if _, containsKey := passport[requiredKey]; !containsKey {
				missingRequiredKey = true
				break
			}
		}
		if !missingRequiredKey {
			numValidPassports++
		}
	}
	return numValidPassports
}

func countDataValidatedPassports(passports []map[string]string) int {
	numDataValidatedPassports := 0
	for _, passport := range passports {
		// Check for all required keys
		if countValidPassports([]map[string]string{passport}) == 0 {
			continue
		}

		numValidFields := 0

		byr, _ := strconv.Atoi(passport["byr"])
		if byr >= 1920 && byr <= 2002 {
			numValidFields++
		}

		iyr, _ := strconv.Atoi(passport["iyr"])
		if iyr >= 2010 && iyr <= 2020 {
			numValidFields++
		}

		eyr, _ := strconv.Atoi(passport["eyr"])
		if eyr >= 2020 && eyr <= 2030 {
			numValidFields++
		}

		hgt := passport["hgt"]
		hgtValue, _ := strconv.Atoi(hgt[:len(hgt)-2])
		if strings.HasSuffix(hgt, "cm") && (hgtValue >= 150 && hgtValue <= 193) {
			numValidFields++
		} else if strings.HasSuffix(hgt, "in") && (hgtValue >= 59 && hgtValue <= 76) {
			numValidFields++
		}

		hcl := passport["hcl"]
		invalidHclCharacterFound := false
		if !strings.HasPrefix(hcl, "#") || len(hcl) != 7 {
			continue
		}
		for _, hclValue := range hcl[1:] {
			if !(hclValue >= '0' && hclValue <= '9') && !(hclValue >= 'a' && hclValue <= 'f') {
				invalidHclCharacterFound = true
				break
			}
		}
		if !invalidHclCharacterFound {
			numValidFields++
		}

		ecl := passport["ecl"]
		validEclValues := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
		if contains(validEclValues, ecl) {
			numValidFields++
		}

		pid := passport["pid"]
		invalidPidCharacterFound := false
		if len(pid) != 9 {
			continue
		}
		for _, digit := range pid {
			if !unicode.IsNumber(digit) {
				invalidPidCharacterFound = true
				break
			}
		}
		if !invalidPidCharacterFound {
			numValidFields++
		}

		if numValidFields == 7 {
			numDataValidatedPassports++
		}
	}
	return numDataValidatedPassports
}

func contains(slice []string, value string) bool {
	for _, val := range slice {
		if val == value {
			return true
		}
	}
	return false
}
