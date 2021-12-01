const fs = require("fs")

let input: number[] = fs.readFileSync("input.txt")
    .toString()
    .split("\n")
    .map((x: string) => parseInt(x))

function getNumberOfIncreases(data: number[]): number {
    let previous: number = Infinity
    let result: number = 0
    for (let num of data) {
        if (num > previous) {
            result++
        }
        previous = num
    }
    return result
}

function getNumberOfThreeMeasurementIncreases(): number {
    let windows: number[] = []
    for (let i = 0; i < input.length; i++) {
        let num: number = input[i]
        windows[i] = num
        windows[i-1] += num
        windows[i-2] += num
    }
    return getNumberOfIncreases(windows)
}

console.log(`Part 1 Result = ${getNumberOfIncreases(input)}`)
console.log(`Part 2 Result = ${getNumberOfThreeMeasurementIncreases()}`)

