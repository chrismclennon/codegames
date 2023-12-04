package four

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"strings"
)

func Run() {
	lines := util.MustReadLines(4)
	fmt.Printf("PART ONE: %d\n", ptOne(lines))
	fmt.Printf("PART TWO: %d\n", ptTwo(lines))
}

func countMatches(line string) int {
	ls := strings.Split(
		strings.Split(line, "|")[0],
		":")[1]
	rs := strings.Split(line, "|")[1]

	left := toInts(ls)
	right := toInts(rs)

	matches := 0
	nums := map[int]bool{}
	for _, i := range left {
		nums[i] = true
	}
	for _, i := range right {
		if _, ok := nums[i]; ok {
			matches++
		}
	}
	return matches
}

func toInts(s string) []int {
	l := strings.Fields(s)
	ints := make([]int, len(l))
	for i, v := range l {
		if v == "" {
			continue
		}
		ints[i] = util.MustParseInt(v)
	}
	return ints
}

func calculateScore(numMatches int) int {
	score := 0
	for i := 0; i < numMatches; i++ {
		if score == 0 {
			score = 1
		} else {
			score *= 2
		}
	}
	return score
}

func ptOne(lines []string) int {
	total := 0
	for _, line := range lines {
		numMatches := countMatches(line)
		total += calculateScore(numMatches)
	}
	return total
}

func ptTwo(lines []string) int {
	cardsCollected := map[int]int{}
	for i := 1; i <= len(lines); i++ {
		cardsCollected[i] = 1
	}

	for i, line := range lines {
		cardNum := i + 1
		numMatches := countMatches(line)
		for j := 0; j < numMatches; j++ {
			newCardNum := cardNum + j + 1
			cardsCollected[newCardNum] += cardsCollected[cardNum]
		}
	}
	retval := 0
	for _, v := range cardsCollected {
		retval += v
	}
	return retval
}
