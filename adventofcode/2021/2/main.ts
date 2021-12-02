const fs = require("fs")

enum Direction {
    Forward,
    Up,
    Down,
    Unknown,
}

type Instruction = {
    direction: Direction
    value: number
}

type Coordinate = {
    horizontal: number
    depth: number
}

let input: Instruction[] = fs.readFileSync("input.txt")
    .toString()
    .split("\n")
    .map((line: string) => {
        const [dir, amount] = line.split(" ")

        let direction: Direction = Direction.Unknown
        switch (dir) {
            case "forward": {
                direction = Direction.Forward
                break
            }
            case "up": {
                direction = Direction.Up
                break
            }
            case "down": {
                direction = Direction.Down
                break
            }
        }
        return {direction: direction, value: Number(amount)}
    })

function processInstructions(instructions: Instruction[]): number {
    let pos: Coordinate = {horizontal: 0, depth: 0}

    for (let instruction of instructions) {
        switch (instruction.direction) {
            case Direction.Forward: {
                pos.horizontal += instruction.value
                break
            }
            case Direction.Down: {
                pos.depth += instruction.value
                break
            }
            case Direction.Up: {
                pos.depth -= instruction.value
                break
            }
        }
    }
    return pos.depth * pos.horizontal
}

function processComplexInstructions(instructions: Instruction[]): number {
    let pos: Coordinate = {horizontal: 0, depth: 0}
    let aim: number = 0

    for (let instruction of instructions) {
        switch (instruction.direction) {
            case Direction.Forward: {
                pos.horizontal += instruction.value
                pos.depth += aim * instruction.value
                break
            }
            case Direction.Down: {
                aim += instruction.value
                break
            }
            case Direction.Up: {
                aim -= instruction.value
                break
            }
        }
    }

    return pos.horizontal * pos.depth
}

console.log(`Part 1 = ${processInstructions(input)}`)
console.log(`Part 2 = ${processComplexInstructions(input)}`)
