const fs = require("fs")


function parseInput(fileName: string): string[] {
    return fs.readFileSync(fileName)
        .toString()
        .split("\n")
}

type ClosingChars = {
    [key: string]: ClosingChar
}

type ClosingChar = {
    openingChar: string
    points: number
}

function computeCorruptionScore(line: string): number {
    const openingChars = {
        "(": true,
        "[": true,
        "{": true,
        "<": true,
    }
    const closingChars: ClosingChars = {
        ")": {
            openingChar: "(",
            points: 3,
        },
        "]": {
            openingChar: "[",
            points: 57,
        },
        "}": {
            openingChar: "{",
            points: 1197,
        },
        ">": {
            openingChar: "<",
            points: 25137,
        }
    }

    const stack: string[] = []
    for (let currentChar of line) {
        if (openingChars.hasOwnProperty(currentChar)) {
            stack.push(currentChar)
        } else {
            const lastOpenChar = stack.pop()
            const expectedOpenChar = closingChars[currentChar]["openingChar"]

            if (lastOpenChar !== expectedOpenChar) {
                return closingChars[currentChar]["points"]
            }
        }
    }
    return 0
}

function computeCorruptionScores(lines: string[]): number {
    let total = 0
    for (let line of lines) {
        total += computeCorruptionScore(line)
    }
    return total
}

function computeAutocorrectScore(line: string): number {
    const charMap = {
        "(": ")",
        "{": "}",
        "[": "]",
        "<": ">",
    }
    const stack: string[] = []
    for (let currentChar of line) {
        if (charMap.hasOwnProperty(currentChar)) {
            stack.push(currentChar)
        } else {
            stack.pop()
        }
    }

    const scores = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    let totalScore = 0
    for (let i = stack.length-1; i >= 0; i--) {
        const currentChar = stack[i]
        const newScore: number = (scores as any)[currentChar] || 0
        totalScore = totalScore * 5 + newScore
    }
    return totalScore
}

function computeAutocorrectScores(lines: string[]): number {
    let scores: number[] = []
    for (let line of lines) {
        scores.push(computeAutocorrectScore(line))
    }
    scores.sort((a, b) => a - b)
    return scores[Math.floor(scores.length / 2)]
}

const input: string[] = parseInput("input.txt")
console.log(`Part 1 = ${computeCorruptionScores(input)}`)

const uncorruptedInputs: string[] = input
    .filter((x: string) => computeCorruptionScore(x) === 0)
console.log(`Part 2 = ${computeAutocorrectScores(uncorruptedInputs)}`)
