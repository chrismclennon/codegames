package five

import (
	"github.com/google/go-cmp/cmp"
	"strings"
	"testing"
)

const input = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
`

func TestConstructMap(t *testing.T) {
	lines := strings.Split(input, "\n")
	got := constructMap(lines, "seed-to-soil map")
	want := islandMap{
		{50, 98, 2},
		{52, 50, 48},
	}
	if !cmp.Equal(got, want) {
		t.Errorf("got %v, want %v", got, want)
	}
}

func TestUseMap(t *testing.T) {
	im := islandMap{
		{50, 98, 2},
		{52, 50, 48},
	}
	vals := []int64{98, 99, 10}
	wants := []int64{50, 51, 10}
	for i, v := range vals {
		got := useMap(im, v)
		want := wants[i]
		if got != want {
			t.Errorf("got %d, want %d", got, want)
		}
	}
}

func TestPtOne(t *testing.T) {
	lines := strings.Split(input, "\n")
	m := constructMaps(lines)
	got := ptOne(m)
	want := int64(35)
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPtTwo(t *testing.T) {
	lines := strings.Split(input, "\n")
	m := constructMaps(lines)
	got := ptTwo(m)
	want := int64(46)
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
