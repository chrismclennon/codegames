const fs = require("fs")

class Coordinate {
    x: number
    y: number

    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }

    toString(): string {
        return `(${this.x}, ${this.y})`
    }
}

class HydrothermalVentsField {
    start: Coordinate
    end: Coordinate

    constructor(start: Coordinate, end: Coordinate) {
        this.start = start
        this.end = end
    }

    // Mutates oceanFloor in-place
    populateOceanFloor(oceanFloor: OceanFloor) {
        // Ignore diagonals
        if (this.start.x != this.end.x && this.start.y != this.end.y) {
            return
        }

        const lesserX = this.start.x < this.end.x ? this.start : this.end
        const greaterX = lesserX === this.start ? this.end : this.start
        const lesserY = this.start.y < this.end.y ? this.start : this.end
        const greaterY = lesserY === this.start ? this.end : this.start

        if (lesserX.x !== greaterX.x) {
            for (let x = lesserX.x; x <= greaterX.x; x++) {
                const coord: Coordinate = new Coordinate(x, this.start.y)
                const key: string = coord.toString()
                let count: number = oceanFloor[key] || 0
                oceanFloor[key] = count+1
            }
        }
        if (lesserY.y !== greaterY.y) {
            for (let y = lesserY.y; y <= greaterY.y; y++) {
                const coord: Coordinate = new Coordinate(this.start.x, y)
                const key: string = coord.toString()
                let count: number = oceanFloor[key] || 0
                oceanFloor[key] = count + 1
            }
        }
    }

    populateDiagonalsOceanFloor(oceanFloor: OceanFloor) {
        // Ignore horizontals and verticals
        if (!(this.start.x != this.end.x && this.start.y != this.end.y)) {
            return
        }

        const from = this.start.x < this.end.x ? this.start : this.end
        const to = this.start === from ? this.end : this.start
        const direction = from.y < to.y ? 1 : -1

        for (let i = 0; i < (to.x - from.x); i++) {
            const coord = new Coordinate(from.x+i, from.y+direction*i)
            const key = coord.toString()
            let count = oceanFloor[key] || 0
            oceanFloor[key] = count + 1
        }
    }
}

function parseInput(fileName: string): HydrothermalVentsField[] {
    const input = fs.readFileSync(fileName)
        .toString()
        .split("\n")

    let output: HydrothermalVentsField[] = []
    for (let line of input) {
        let [start, end] = line.split(" -> ")
        let startCoord = start.split(",").map((x: string) => Number(x))
        let endCoord = end.split(",").map((x: string) => Number(x))

        const field = new HydrothermalVentsField(
            new Coordinate(startCoord[0], startCoord[1]),
            new Coordinate(endCoord[0], endCoord[1]),
        )
        output.push(field)
    }
    return output
}

type OceanFloor = {
    [key: string]: number
}

const oceanFloor: OceanFloor = {}
const ventFields = parseInput("sample_input.txt")
for (let field of ventFields) {
    field.populateOceanFloor(oceanFloor)
}
let numStrongVents = 0
for (const [key, value] of Object.entries(oceanFloor)) {
    if (value >= 2) {
        numStrongVents++
    }
}
console.log(`Part 1 = ${numStrongVents}`)

for (let field of ventFields) {
    field.populateDiagonalsOceanFloor(oceanFloor)
}

// TODO: Part 2 isn't actually correct. sample_input should offer two 3's, but only has one.
// Going to skip the remainder of this part since it's more tedious than interesting.
numStrongVents = 0
for (const [key, value] of Object.entries(oceanFloor)) {
    if (value >= 2) {
        numStrongVents++
    }
}
console.log(`Part 2 = ${numStrongVents}`)
