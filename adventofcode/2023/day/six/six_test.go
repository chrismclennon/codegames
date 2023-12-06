package six

import (
	"strings"
	"testing"
)

var input = `Time:      7  15   30
Distance:  9  40  200`
var lines = strings.Split(input, "\n")

func TestPtOne(t *testing.T) {
	races := parse(lines)
	got := ptOne(races)
	want := 288
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPtTwo(t *testing.T) {
	r := race{
		time:     71530,
		distance: 940200,
	}
	got := ptTwo(r)
	want := 71503
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
