package three

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"regexp"
	"unicode"
)

func Run() {
	lines := util.MustReadLines(3)
	fmt.Printf("PART ONE: %d\n", ptOne(lines))
	fmt.Printf("PART TWO: %d\n", ptTwo(lines))
}

func toRuneArray(s []string) [][]rune {
	var rlines [][]rune
	for _, l := range s {
		rlines = append(rlines, []rune(l))
	}
	return rlines
}

func isSymbol(r rune) bool {
	return r != '.' && !unicode.IsLetter(r) && !unicode.IsNumber(r)
}

func isValidPosition(lines [][]rune, row, col int) bool {
	if row < 0 {
		return false
	}
	if row >= len(lines) {
		return false
	}
	if col < 0 {
		return false
	}
	if col >= len(lines[row]) {
		return false
	}
	return true
}

func isPartNumber(lines [][]rune, row, col int) bool {
	retval := false
	for r := row - 1; r <= row+1; r++ {
		for c := col - 1; c <= col+1; c++ {
			if isValidPosition(lines, r, c) {
				retval = retval || isSymbol(lines[r][c])
			}
		}
	}
	return retval
}

func getNumberAtPosition(lines [][]rune, row, col int) int {
	left, right := col, col
	for left >= 0 && unicode.IsNumber(lines[row][left]) {
		left--
	}
	for right < len(lines[row]) && unicode.IsNumber(lines[row][right]) {
		right++
	}
	if left >= right {
		return 0
	}
	return util.MustParseInt(string(lines[row][left+1 : right]))
}

func ptOne(lines []string) int {
	rlines := toRuneArray(lines)
	re := regexp.MustCompile("([0-9]+)")

	total := 0
	for row, l := range lines {
		idxs := re.FindAllStringIndex(l, -1)
		for _, i := range idxs {
			left, right := i[0], i[1]
			for col := left; col < right; col++ {
				if isPartNumber(rlines, row, col) {
					num := util.MustParseInt(lines[row][left:right])
					total += num
					break
				}
			}

		}
	}
	return total
}

// This solution is jank. It does not account for:
// * if a gear has more than two numbers adjacent to it
// * if a gear has two numbers of equal value adjacent to it
func ptTwo(lines []string) int {
	rlines := toRuneArray(lines)
	re := regexp.MustCompile("([*])")

	total := 0
	for row, l := range lines {
		idxs := re.FindAllStringIndex(l, -1)
		for _, i := range idxs {
			seen := map[int]bool{}
			t := 1

			for r := row - 1; r <= row+1; r++ {
				for c := i[0] - 1; c < i[1]+1; c++ {
					if isValidPosition(rlines, r, c) {
						n := getNumberAtPosition(rlines, r, c)
						_, wasSeen := seen[n]
						if n != 0 && !wasSeen {
							seen[n] = true
							t *= n
						}
					}
				}
			}
			if len(seen) == 2 {
				total += t
			}
		}
	}
	return total
}
