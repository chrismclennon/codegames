package two

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"regexp"
)

func Run() {
	lines, _ := util.ReadLines(2)
	gs := convert(lines)
	fmt.Printf("PART ONE: %d\n", twoPtOne(gs))
	fmt.Printf("PART TWO: %d\n", twoPtTwo(gs))
}

type game struct {
	n     int
	red   int
	blue  int
	green int
}

func convert(lines []string) []game {
	retval := make([]game, 0, len(lines))
	for _, line := range lines {
		g := convertLine(line)
		retval = append(retval, g)
	}
	return retval
}

func convertLine(line string) game {
	r := regexp.MustCompile("Game ([0-9]+)")
	m := r.FindStringSubmatch(line)
	n := util.MustParseInt(m[1])

	return game{
		n:     n,
		red:   match(line, "red"),
		blue:  match(line, "blue"),
		green: match(line, "green"),
	}
}

func match(line, color string) int {
	r := regexp.MustCompile(fmt.Sprintf("([0-9]+) %s", color))
	matches := r.FindAllStringSubmatch(line, -1)

	maxNum := 0
	for _, m := range matches {
		num := util.MustParseInt(m[1])
		if num > maxNum {
			maxNum = num
		}
	}
	return maxNum
}

func twoPtOne(gs []game) int {
	// only 12 red cubes, 13 green cubes, and 14 blue cubes
	total := 0
	for _, g := range gs {
		if g.red <= 12 && g.green <= 13 && g.blue <= 14 {
			total += g.n
		}
	}
	return total
}

func twoPtTwo(gs []game) int {
	total := 0
	for _, g := range gs {
		total += g.red * g.blue * g.green
	}
	return total
}
