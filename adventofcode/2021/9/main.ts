const fs = require("fs")

function parseInput(fileName: string): number[][] {
    return fs.readFileSync(fileName)
        .toString()
        .split("\n")
        .map((x: string) => x.split("").map(
            (y: string) => Number(y)
        ))
}

function findLowPoints(cave: number[][]): number[] {
    const lowPoints: number[] = []
    for (let x = 0; x < cave.length; x++) {
        for (let y = 0; y < cave[x].length; y++) {
            const current = cave[x][y]
            const adjacent = [
                (cave[x-1] || [])[y],
                (cave[x+1] || [])[y],
                (cave[x] || [])[y-1],
                (cave[x] || [])[y+1]
            ]
            let lowPoint: boolean = true
            for (const val of adjacent) {
                if (val === undefined) {
                    continue
                }
                if (current >= val) {
                    lowPoint = false
                    break
                }
            }
            if (lowPoint) {
                lowPoints.push(current)
            }
        }
    }
    return lowPoints
}

function findLargestBasinSizes(cave: number[][], numBasins: number): number[] {
    const exploredCoords: number[][] = []
    const basinSizes: number[] = []

    for (let x = 0; x < cave.length; x++) {
        for (let y = 0; y < cave[x].length; y++) {
            if (isAlreadyExplored(exploredCoords, x, y)) {
                continue
            }
            const basinSize = findBasinSize(cave, exploredCoords, x, y)
            basinSizes.push(basinSize)
        }
    }

    return basinSizes
        .sort((a, b) => b - a)
        .splice(0, numBasins)
}

function findBasinSize(cave: number[][], exploredCoords: number[][], x: number, y: number, currentSize: number = 0): number {
    if (isAlreadyExplored(exploredCoords, x, y)) {
        return currentSize
    }
    exploredCoords.push([x, y])

    const currentValue = (cave[x] || [])[y]
    if (currentValue === 9 || currentValue === undefined) {
        return currentSize
    }
    return 1
        + currentSize
        + findBasinSize(cave, exploredCoords, x-1, y)
        + findBasinSize(cave, exploredCoords, x+1, y)
        + findBasinSize(cave, exploredCoords, x, y-1)
        + findBasinSize(cave, exploredCoords, x, y+1)
}

function isAlreadyExplored(exploredCoords: number[][], x: number, y: number): boolean {
    for (let coord of exploredCoords) {
        if (coord[0] === x && coord[1] === y) {
            return true
        }
    }
    return false
}

// const input = parseInput("sample_input.txt")
const input = parseInput("input.txt")

const lowPoints = findLowPoints(input)
console.log(`Part 1 = ${lowPoints.reduce((a, b) => a + b) + lowPoints.length}`)

const largestBasinSizes = findLargestBasinSizes(input, 3)
console.log(`Part 2 = ${largestBasinSizes.reduce((a, b) => a * b)}`)