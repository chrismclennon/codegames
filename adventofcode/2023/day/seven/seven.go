package seven

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"slices"
	"strings"
)

func Run() {
	lines := util.MustReadLines(7)

	hands := []hand{}
	for _, l := range lines {
		s := strings.Fields(l)
		h := hand{
			cards:     s[0],
			bid:       util.MustParseInt(s[1]),
			handType:  getHandType(s[0]),
			handType2: getHandType2(s[0]),
		}
		hands = append(hands, h)
	}

	fmt.Printf("PART ONE: %d\n", ptOne(hands))
	fmt.Printf("PART TWO: %d\n", ptTwo(hands))
}

type hand struct {
	cards     string
	bid       int
	handType  handType
	handType2 handType
}

type handType int

const (
	FIVE_OF_A_KIND  handType = 7
	FOUR_OF_A_KIND           = 6
	FULL_HOUSE               = 5
	THREE_OF_A_KIND          = 4
	TWO_PAIR                 = 3
	ONE_PAIR                 = 2
	HIGH_CARD                = 1
)

func getHandType(cards string) handType {
	freq := map[rune]int{}
	for _, c := range cards {
		if count, ok := freq[c]; ok {
			count++
			freq[c] = count
		} else {
			freq[c] = 1
		}
	}

	for _, v := range freq {
		if v == 5 {
			return FIVE_OF_A_KIND
		}
		if v == 4 {
			return FOUR_OF_A_KIND
		}
	}
	if len(freq) == 2 {
		return FULL_HOUSE
	}
	for _, v := range freq {
		if v == 3 {
			return THREE_OF_A_KIND
		}
	}
	{
		c := 0
		for _, v := range freq {
			if v == 2 {
				c++
			}
		}
		if c == 2 {
			return TWO_PAIR
		} else if c == 1 {
			return ONE_PAIR
		}
	}
	return HIGH_CARD
}

func getHandType2(cards string) handType {
	freq := map[rune]int{}
	for _, c := range cards {
		if count, ok := freq[c]; ok {
			count++
			freq[c] = count
		} else {
			freq[c] = 1
		}
	}

	jokers := freq['J']
	if jokers == 0 {
		return getHandType(cards)
	}

	var mk rune
	var mv int
	for k, v := range freq {
		if k == 'J' {
			continue
		}
		if v > mv {
			mk = k
			mv = v
		}
	}

	cards = strings.ReplaceAll(cards, "J", string(mk))
	return getHandType(cards)
}

func cardCmp(a, b rune) int {
	cmp := []rune{
		'A',
		'K',
		'Q',
		'J',
		'T',
		'9',
		'8',
		'7',
		'6',
		'5',
		'4',
		'3',
		'2',
	}
	if a == b {
		return 0
	}
	var aIdx, bIdx int
	for i, v := range cmp {
		if v == a {
			aIdx = i
		}
		if v == b {
			bIdx = i
		}
	}
	if aIdx < bIdx {
		// earlier in array is larger card, so return 1
		return 1
	}
	return -1
}

func cardCmp2(a, b rune) int {
	cmp := []rune{
		'A',
		'K',
		'Q',
		'T',
		'9',
		'8',
		'7',
		'6',
		'5',
		'4',
		'3',
		'2',
		'J',
	}
	if a == b {
		return 0
	}
	var aIdx, bIdx int
	for i, v := range cmp {
		if v == a {
			aIdx = i
		}
		if v == b {
			bIdx = i
		}
	}
	if aIdx < bIdx {
		// earlier in array is larger card, so return 1
		return 1
	}
	return -1
}

func ptOne(hands []hand) int {
	cmp := func(a, b hand) int {
		if a.handType < b.handType {
			return -1
		}
		if a.handType > b.handType {
			return 1
		}
		for i := range a.cards {
			c := cardCmp(rune(a.cards[i]), rune(b.cards[i]))
			if c != 0 {
				return c
			}

		}
		return 0
	}
	slices.SortFunc(hands, cmp)

	ans := 0
	for i, h := range hands {
		rank := i + 1
		ans += rank * h.bid
	}
	return ans
}

func ptTwo(hands []hand) int {
	cmp := func(a, b hand) int {
		if a.handType2 < b.handType2 {
			return -1
		}
		if a.handType2 > b.handType2 {
			return 1
		}
		for i := range a.cards {
			c := cardCmp2(rune(a.cards[i]), rune(b.cards[i]))
			if c != 0 {
				return c
			}

		}
		return 0
	}
	slices.SortFunc(hands, cmp)

	ans := 0
	for i, h := range hands {
		rank := i + 1
		ans += rank * h.bid
	}
	return ans
}
