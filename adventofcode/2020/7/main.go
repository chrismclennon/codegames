package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type rule struct {
	quantity int
	color    string
}

func main() {
	rawInput := readInput()
	colorToRules := parseInput(rawInput)
	partOne(colorToRules)
	partTwo(colorToRules)
}

func readInput() []string {
	data, readFileErr := ioutil.ReadFile("input.txt")
	if readFileErr != nil {
		panic(readFileErr)
	}
	return strings.Split(string(data), "\n")
}

func parseInput(rawInput []string) map[string][]rule {
	retval := map[string][]rule{}
	for _, line := range rawInput {
		parts := strings.Fields(line)
		originalBagColor := parts[0] + " " + parts[1]

		rules := []rule{}
		for index := 4; index < len(parts); index += 4 {
			quantity, _ := strconv.Atoi(parts[index])
			color := parts[index+1] + " " + parts[index+2]
			rule := rule{
				color:    color,
				quantity: quantity,
			}
			rules = append(rules, rule)
		}

		retval[originalBagColor] = rules
	}
	return retval
}

func partOne(colorToRules map[string][]rule) {
	// TODO: Memoize?
	result := []string{}
	for outsideBagColor, rules := range colorToRules {
		queue := list.New()
		for _, rule := range rules {
			queue.PushBack(rule.color)
		}

		for queue.Len() > 0 {
			nextItem := queue.Front()
			queue.Remove(nextItem)

			// It's interesting that I need a type assertion here. `nextItem` is an interface{}.
			// Type assertion necessary to declare that the interface{} is a string.
			insideBagColor := nextItem.Value.(string)
			if insideBagColor == "shiny gold" {
				result = append(result, outsideBagColor)
				break
			} else {
				for _, rule := range colorToRules[insideBagColor] {
					queue.PushBack(rule.color)
				}
			}
		}
	}

	fmt.Printf("Part one answer: %d\n", len(result))
}

func partTwo(colorToRules map[string][]rule) {
	result := dfs(colorToRules, "shiny gold", 1)
	fmt.Printf("Part two answer: %d\n", result)
}

func dfs(colorToRules map[string][]rule, bagColor string, multiplier int) int {
	retval := 0
	rules := colorToRules[bagColor]

	for _, currentRule := range rules {
		retval += currentRule.quantity*multiplier + dfs(colorToRules, currentRule.color, currentRule.quantity*multiplier)
	}
	return retval
}
