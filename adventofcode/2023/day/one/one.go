package one

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Run() {
	data, _ := os.ReadFile("inputs/1.txt")
	lines := strings.Split(string(data), "\n")
	fmt.Printf("PART 1: %d\n", onePtOne(lines))
	fmt.Printf("PART 2: %d\n", onePtTwo(lines))
}

func onePtOne(lines []string) int64 {
	var first, last, total int64 = -1, -1, 0
	for _, line := range lines {
		first = -1
		for _, c := range line {
			ch := string(c)
			if n, err := strconv.ParseInt(ch, 10, 8); err == nil {
				if first < 0 {
					first = n
				}
				last = n
			}
		}
		total += first*10 + last
	}
	return total
}

func onePtTwo(lines []string) int64 {
	numbers := map[string]string{
		"one":   "one1one",
		"two":   "two2two",
		"three": "three3three",
		"four":  "four4four",
		"five":  "five5five",
		"six":   "six6six",
		"seven": "seven7seven",
		"eight": "eight8eight",
		"nine":  "nine9nine",
	}
	var first, last, total int64 = -1, -1, 0
	for _, line := range lines {
		first = -1
		for k, v := range numbers {
			line = strings.Replace(line, k, v, -1)
		}
		for _, c := range line {
			ch := string(c)
			if n, err := strconv.ParseInt(ch, 10, 8); err == nil {
				if first < 0 {
					first = n
				}
				last = n
			}
		}
		total += first*10 + last
	}
	return total
}
