package util

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func MustReadLines(dayNum int) []string {
	fileName := fmt.Sprintf("inputs/%d.txt", dayNum)
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(fmt.Sprintf("cannot read file: %s", fileName))
	}
	return strings.Split(string(data), "\n")
}

func MustParseInt(s string) int {
	n, err := strconv.ParseInt(s, 10, 32)
	if err != nil {
		panic(fmt.Sprintf("cannot parse int: %s", s))
	}
	return int(n)
}
