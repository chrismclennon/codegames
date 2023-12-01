package day

import (
	"strings"
	"testing"
)

func TestOne(t *testing.T) {
	t.Run("part one", func(t *testing.T) {
		input := `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`
		lines := strings.Split(input, "\n")
		got := onePtOne(lines)
		want := int64(142)
		if got != want {
			t.Errorf("want %d, got %d", want, got)
		}
	})

	t.Run("part two", func(t *testing.T) {
		input := `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
		lines := strings.Split(input, "\n")
		got := onePtTwo(lines)
		want := int64(281)
		if got != want {
			t.Errorf("want %d, got %d", want, got)
		}
	})
}
