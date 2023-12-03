package three

import (
	"strings"
	"testing"
)

func TestPtOne(t *testing.T) {
	input := `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`
	lines := strings.Fields(input)
	got := ptOne(lines)
	want := 4361
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPtTwo(t *testing.T) {
	input := `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`
	lines := strings.Fields(input)
	got := ptTwo(lines)
	want := 467835
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestGetNumberAtPosition(t *testing.T) {
	s := "467..114.."
	lines := toRuneArray([]string{s})
	got := getNumberAtPosition(lines, 0, 2)
	want := 467
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
