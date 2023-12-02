package two

import (
	"fmt"
	"strings"
	"testing"
)

func TestConvertLine(t *testing.T) {
	lines := []string{
		"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
		"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	}
	wants := []game{
		{
			n:     1,
			red:   4,
			blue:  6,
			green: 2,
		},
		{
			n:     3,
			red:   20,
			blue:  6,
			green: 13,
		},
	}
	for i, line := range lines {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			got := convertLine(line)
			want := wants[i]
			if got != want {
				t.Errorf("got %+v, want %+v", got, want)
			}
		})
	}

}

func TestPartOne(t *testing.T) {
	input := `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`
	lines := strings.Split(input, "\n")
	gs := convert(lines)
	got := twoPtOne(gs)
	want := 8
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPartTwo(t *testing.T) {
	input := `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`
	lines := strings.Split(input, "\n")
	gs := convert(lines)
	got := twoPtTwo(gs)
	want := 2286
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
