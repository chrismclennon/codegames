package main

import (
	"fmt"
	"github.com/chrismclennon/adventofcode/2023/day"
)

func main() {
	days := []func(){
		day.One,
	}
	for i, d := range days {
		fmt.Printf("\n\n---\nDAY %d\n", i)
		d()
	}
}
