const fs = require("fs")

let input: string[] = fs.readFileSync("input.txt")
    .toString()
    .split("\n")

class Coordinate {
    horizontal!: number
    depth!: number

    constructor() {
        this.horizontal = 0
        this.depth = 0
    }
}

function processInstructions(instructions: string[]): number {
    let pos: Coordinate = new Coordinate()

    for (let instruction of instructions) {
        let [command, strVal]: string[] = instruction.split(" ")
        let val: number = Number(strVal)

        switch (command) {
            case "forward": {
                pos.horizontal += val
                break
            }
            case "down": {
                pos.depth += val
                break
            }
            case "up": {
                pos.depth -= val
                break
            }
        }
    }
    return pos.depth * pos.horizontal
}

function processComplexInstructions(instructions: string[]): number {
    let pos: Coordinate = new Coordinate()
    let aim: number = 0

    for (let instruction of instructions) {
        let [command, strVal]: string[] = instruction.split(" ")
        let val: number = Number(strVal)

        switch (command) {
            case "forward": {
                pos.horizontal += val
                pos.depth += (aim * val)
                break
            }
            case "down": {
                aim += val
                break
            }
            case "up": {
                aim -= val
                break
            }
        }
    }

    return pos.horizontal * pos.depth
}

console.log(`Part 1 = ${processInstructions(input)}`)
console.log(`Part 2 = ${processComplexInstructions(input)}`)
