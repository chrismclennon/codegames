package util

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadLines(dayNum int) ([]string, error) {
	fileName := fmt.Sprintf("inputs/%d.txt", dayNum)
	data, err := os.ReadFile(fileName)
	if err != nil {
		return []string{}, err
	}
	return strings.Split(string(data), "\n"), nil
}

func MustParseInt(s string) int {
	n, err := strconv.ParseInt(s, 10, 32)
	if err != nil {
		panic(fmt.Sprintf("cannot parse int: %s", s))
	}
	return int(n)
}
