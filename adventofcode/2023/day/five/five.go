package five

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/util"
	"math"
	"strings"
	"sync"
	"time"
)

type maps struct {
	seeds []int64
	sts   islandMap
	stf   islandMap
	ftw   islandMap
	wtl   islandMap
	ltt   islandMap
	tth   islandMap
	htl   islandMap
}

type islandMap [][3]int64

func Run() {
	lines := util.MustReadLines(5)
	m := constructMaps(lines)
	fmt.Printf("PART ONE: %d\n", ptOne(m))
	fmt.Printf("PART TWO: %d\n", ptTwo(m))
}

func constructMaps(lines []string) maps {
	return maps{
		seeds: util.MustStringToInt64Slice(strings.Split(lines[0], ":")[1]),
		sts:   constructMap(lines, "seed-to-soil"),
		stf:   constructMap(lines, "soil-to-fertilizer"),
		ftw:   constructMap(lines, "fertilizer-to-water"),
		wtl:   constructMap(lines, "water-to-light"),
		ltt:   constructMap(lines, "light-to-temperature"),
		tth:   constructMap(lines, "temperature-to-humidity"),
		htl:   constructMap(lines, "humidity-to-location"),
	}
}

func constructMap(lines []string, mapName string) islandMap {
	im := islandMap{}
	idx := findIndex(lines, mapName) + 1
	line := lines[idx]
	for line != "" {
		sn := strings.Fields(line)
		n := [3]int64{}
		for i := 0; i < 3; i++ {
			n[i] = util.MustParseInt64(sn[i])
		}
		im = append(im, n)

		idx++
		line = lines[idx]
	}
	return im
}

func findIndex(lines []string, s string) int {
	for i, l := range lines {
		if strings.HasPrefix(l, s) {
			return i
		}
	}
	return -1
}

func useMap(im islandMap, val int64) int64 {
	for _, m := range im {
		ss := m[1]
		se := ss + m[2]

		if ss <= val && val < se {
			ds := m[0]
			dist := val - ss
			return ds + dist
		}
	}
	return val
}

func ptOne(m maps) int64 {
	ims := []islandMap{
		m.sts,
		m.stf,
		m.ftw,
		m.wtl,
		m.ltt,
		m.tth,
		m.htl,
	}
	locs := []int64{}
	for _, val := range m.seeds {
		for _, im := range ims {
			val = useMap(im, val)
		}
		locs = append(locs, val)
	}

	minVal := locs[0]
	for _, l := range locs {
		if l < minVal {
			minVal = l
		}
	}
	return minVal
}

func ptTwo(m maps) int64 {
	ims := []islandMap{
		m.sts,
		m.stf,
		m.ftw,
		m.wtl,
		m.ltt,
		m.tth,
		m.htl,
	}

	wg := sync.WaitGroup{}
	answers := make([]int64, len(m.seeds)/2)

	for i := 0; i < len(m.seeds); i += 2 {
		wg.Add(1)

		go func(i int) {
			fmt.Printf("STARTING GOROUTINE %d, DISTANCE %d\n", i, m.seeds[i+1])
			startTime := time.Now()
			ml := int64(math.MaxInt64)

			for seed := m.seeds[i]; seed < m.seeds[i]+m.seeds[i+1]; seed++ {
				val := seed
				for _, im := range ims {
					val = useMap(im, val)
				}

				if val < ml {
					ml = val
				}
			}

			answers[i/2] = ml

			endTime := time.Now().Sub(startTime)
			fmt.Printf("FINISHED GOROUTINE %d, %f SECONDS\n", i, endTime.Seconds())

			wg.Done()
		}(i)
	}
	wg.Wait()

	minLoc := int64(math.MaxInt64)
	for _, ans := range answers {
		if ans < minLoc {
			minLoc = ans
		}
	}
	return minLoc
}
