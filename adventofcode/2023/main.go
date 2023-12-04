package main

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/day/four"
	"github.com/chrismclennon/adventofcode/2023/day/one"
	"github.com/chrismclennon/adventofcode/2023/day/three"
	"github.com/chrismclennon/adventofcode/2023/day/two"
)

func main() {
	days := []func(){
		one.Run,
		two.Run,
		three.Run,
		four.Run,
	}
	for i, d := range days {
		fmt.Printf("\n\n---\nDAY %d\n", i+1)
		d()
	}
}
