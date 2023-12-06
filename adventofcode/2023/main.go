package main

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/day/five"
	"github.com/chrismclennon/adventofcode/2023/day/four"
	"github.com/chrismclennon/adventofcode/2023/day/one"
	"github.com/chrismclennon/adventofcode/2023/day/six"
	"github.com/chrismclennon/adventofcode/2023/day/three"
	"github.com/chrismclennon/adventofcode/2023/day/two"
	"time"
)

func main() {
	days := []func(){
		one.Run,
		two.Run,
		three.Run,
		four.Run,
		five.Run,
		six.Run,
	}
	for i, d := range days {
		fmt.Printf("\n\n---\nDAY %d\n", i+1)
		start := time.Now()
		d()
		fmt.Printf("Time: %v\n", time.Since(start))
	}
}
