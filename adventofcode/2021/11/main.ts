const fs = require("fs")

function parseInput(fileName: string): number[][] {
    return fs.readFileSync(fileName)
        .toString()
        .split("\n")
        .map((x: string) => x
            .split("")
            .map((y: string) => Number(y))
        )
}

type Coordinate = [x: number, y: number]

// mutates in-place. returns number of flashes
function performStep(octopii: number[][]): number {
    // initial increment
    for (let row of octopii) {
        for (let i = 0; i < row.length; i++) {
            row[i]++
        }
    }

    // scan for flashes
    let totalFlashes = 0
    for (let x = 0; x < octopii.length; x++) {
        for (let y = 0; y < octopii[x].length; y++) {
            totalFlashes += doFlash(octopii, x, y)
        }
    }
    return totalFlashes
}

function doFlash(octopii: number[][], x: number, y: number): number {
    if (octopii[x][y] <= 9) {
        return 0
    }
    let totalFlashes = 1
    octopii[x][y] = 0

    const coords: Coordinate[] = [
        [x-1, y],
        [x+1, y],
        [x, y-1],
        [x, y+1],
        [x-1, y-1],
        [x-1, y+1],
        [x+1, y-1],
        [x+1, y+1],
    ]
    for (let coord of coords) {
        const x_coord = coord[0]
        const y_coord = coord[1]

        const octopus = (octopii[x_coord] || [])[y_coord]
        if (octopus === undefined || octopus === 0) {
            continue
        }
        octopii[x_coord][y_coord]++
        if (octopii[x_coord][y_coord] > 9) {
            totalFlashes += doFlash(octopii, x_coord, y_coord)
        }
    }
    return totalFlashes
}

function doSteps(octopii: number[][], num: number): number {
    let totalFlashes = 0
    for (let i = 0; i < num; i++) {
        totalFlashes += performStep(octopii)
    }
    return totalFlashes
}

function doStepsUntilFullSync(octopii: number[][]): number {
    let stepNum = 0
    const totalOctopii = octopii.length * octopii[0].length
    let totalFlashes = 0

    while (totalFlashes !== totalOctopii) {
        stepNum++
        totalFlashes = performStep(octopii)
    }
    return stepNum
}

const fileName = "input.txt"
let octopii = parseInput(fileName)
console.log(`Part 1 = ${doSteps(octopii, 100)}`)

octopii = parseInput(fileName)
console.log(`Part 2 = ${doStepsUntilFullSync(octopii)}`)
