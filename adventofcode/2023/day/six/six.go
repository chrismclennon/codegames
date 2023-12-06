package six

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"math"
	"strings"
)

func Run() {
	input := `Time:        53     91     67     68
Distance:   250   1330   1081   1025`
	lines := strings.Split(input, "\n")
	races := parse(lines)
	fmt.Printf("PART ONE: %d\n", ptOne(races))

	p2race := race{
		time:     53916768,
		distance: 250133010811025,
	}
	fmt.Printf("PART TWO: %d\n", ptTwo(p2race))
}

type race struct {
	time     int
	distance int
}

func parse(lines []string) []race {
	t := strings.Fields(strings.Split(lines[0], ":")[1])
	d := strings.Fields(strings.Split(lines[1], ":")[1])

	rs := make([]race, len(t))
	for i, t := range t {
		r := race{
			time:     util.MustParseInt(t),
			distance: util.MustParseInt(d[i]),
		}
		rs[i] = r
	}
	return rs
}

func ptOne(races []race) int {
	// (time-x)*x=distance
	// x = 1/2 (y - sqrt(y^2 - 4 z))
	// x = 1/2 (y + sqrt(y^2 - 4 z))
	mul := 1
	for _, r := range races {
		// add +1 and floor, because we need scores that are greater than, not greater than or equal to the distance
		start := math.Floor(0.5*(float64(r.time)-math.Sqrt(float64(r.time*r.time-4*r.distance))) + 1)
		end := math.Ceil(0.5 * (float64(r.time) + math.Sqrt(float64(r.time*r.time-4*r.distance))))
		interval := int(end - start)
		mul *= interval
	}
	return mul
}

func ptTwo(r race) int {
	start := math.Floor(0.5*(float64(r.time)-math.Sqrt(float64(r.time*r.time-4*r.distance))) + 1)
	end := math.Ceil(0.5 * (float64(r.time) + math.Sqrt(float64(r.time*r.time-4*r.distance))))
	return int(end - start)
}
