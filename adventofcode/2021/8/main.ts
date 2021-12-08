const fs = require("fs")

const sampleInput = fs.readFileSync("sample_input.txt")
    .toString()
    .split("\n")
const sampleSignalPatterns = parseInput(sampleInput)

const input = fs.readFileSync("input.txt")
    .toString()
    .split("\n")

type SignalPattern = {
    inputs: string[]
    outputs: string[]
}

function parseInput(inputs: string[]): SignalPattern[] {
    const output: SignalPattern[] = []
    for (let input of inputs) {
        const [inputInput, inputOutput] = input.split(" | ")
        const sp: SignalPattern = {
            inputs: inputInput.split(" "),
            outputs: inputOutput.split(" "),
        }
        output.push(sp)
    }
    return output
}

function countSimpleValues(outputs: string[][]): number {
    let count = 0
    for (let output of outputs) {
        for (let num of output) {
            switch (num.length) {
                case 2:
                case 3:
                case 4:
                case 7:
                    count++
            }
        }
    }
    return count
}

const signalPatterns = parseInput(input)
const outputs = signalPatterns.map(x => x.outputs)
console.log(`Part 1 = ${countSimpleValues(outputs)}`)