package seven

import (
	"github.com/chrismclennon/adventofcode/2023/util"
	"strings"
	"testing"
)

var input = `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`
var lines = strings.Split(input, "\n")

func TestPtOne(t *testing.T) {
	hands := []hand{}
	for _, l := range lines {
		s := strings.Fields(l)
		h := hand{
			cards:    s[0],
			bid:      util.MustParseInt(s[1]),
			handType: getHandType(s[0]),
		}
		hands = append(hands, h)
	}
	got := ptOne(hands)
	want := 6440
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPtTwo(t *testing.T) {
	hands := []hand{}
	for _, l := range lines {
		s := strings.Fields(l)
		h := hand{
			cards:     s[0],
			bid:       util.MustParseInt(s[1]),
			handType2: getHandType2(s[0]),
		}
		hands = append(hands, h)
	}
	got := ptTwo(hands)
	want := 5905
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestCardCmp(t *testing.T) {
	got := cardCmp('Q', 'T', "AKQJT98765432")
	want := 1
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestGetHandType2(t *testing.T) {
	cases := []struct {
		cards    string
		expected handType
	}{
		{
			"T55J5",
			FOUR_OF_A_KIND,
		},
		{
			"KTJJT",
			FOUR_OF_A_KIND,
		},
		{
			"JJJJJ",
			FIVE_OF_A_KIND,
		},
		{
			"32T3K",
			ONE_PAIR,
		},
		{
			"KK677",
			TWO_PAIR,
		},
		{
			"QQQJA",
			FOUR_OF_A_KIND,
		},
		{
			"QQQQJ",
			FIVE_OF_A_KIND,
		},
		{
			"QQQQQ",
			FIVE_OF_A_KIND,
		},
		{
			"QQQJJ",
			FIVE_OF_A_KIND,
		},
		{
			"QJJJJ",
			FIVE_OF_A_KIND,
		},
		{
			"QQJJJ",
			FIVE_OF_A_KIND,
		},
		{
			"AQJJJ",
			FOUR_OF_A_KIND,
		},
		{
			"AKQJJ",
			THREE_OF_A_KIND,
		},
		{
			"AAKJJ",
			FOUR_OF_A_KIND,
		},
		{
			"AAAJJ",
			FIVE_OF_A_KIND,
		},
		{
			"AKQTJ",
			ONE_PAIR,
		},
		{
			"AKQQJ",
			THREE_OF_A_KIND,
		},
		{
			"AQQQJ",
			FOUR_OF_A_KIND,
		},
		{
			"QQQQJ",
			FIVE_OF_A_KIND,
		},
	}
	for _, c := range cases {
		got := getHandType2(c.cards)
		want := c.expected
		if got != want {
			t.Errorf("%s: got %d, want %d", c.cards, got, want)
		}
	}
}
