const fs = require("fs")

enum BingoBoardValueState {
    Picked,
    Unpicked,
}

type BingoBoardValue = {
    state: BingoBoardValueState
    value: number
}

class BingoBoard {
    rows: BingoBoardValue[][]

    constructor(rows: number[][]) {
        this.rows = []
        for (let row of rows) {
            const newRow: BingoBoardValue[] = []
            for (let num of row) {
                const val: BingoBoardValue = {
                    state: BingoBoardValueState.Unpicked,
                    value: num,
                }
                newRow.push(val)
            }
            this.rows.push(newRow)
        }
    }

    // Choose a number. Return true if the board is winning.
    pick(num: number): number[] | undefined {
        for (let rowNum = 0; rowNum < this.rows.length; rowNum++) {
            const row = this.rows[rowNum]
            for (let colNum = 0; colNum < row.length; colNum++) {
                let value = row[colNum]
                if (value.value === num) {
                    value.state = BingoBoardValueState.Picked

                    const winningNumbers = this.checkWinningNumbers(rowNum, colNum)
                    if (winningNumbers !== undefined) {
                        return winningNumbers
                    }
                }
            }
        }
        return undefined
    }

    checkWinningNumbers(rowNum: number, colNum: number): number[] | undefined {
        let winningNumbers = []
        let found = true

        // Row
        for (let value of this.rows[rowNum]) {
            if (value.state === BingoBoardValueState.Unpicked) {
                found = false
                break
            } else {
                winningNumbers.push(value.value)
            }
        }
        if (found) {
            return winningNumbers
        }

        // Column
        winningNumbers = []
        found = true
        for (let row of this.rows) {
            const value = row[colNum]
            if (value.state === BingoBoardValueState.Unpicked) {
                found = false
                break
            } else {
                winningNumbers.push(value.value)
            }
        }
        if (found) {
            return winningNumbers
        }

        return undefined
    }

    addUnpickedNumbers(): number {
        let sum = 0
        for (let row of this.rows) {
            for (let val of row) {
                if (val.state === BingoBoardValueState.Unpicked) {
                    sum += val.value
                }
            }
        }
        return sum
    }
}

type parseInputResponse = {
    drawNumbers: number[]
    boards: BingoBoard[]
}

function parseInput(fileName: string): parseInputResponse {
    const input = fs.readFileSync(fileName)
        .toString()
        .split("\n")

    const numbers: number[] = input[0]
        .split(",")
        .map((x: string) => Number(x))

    const numBoards: number = Math.floor((input.length-2) / 6)
    const boards: BingoBoard[] = []
    for (let i = 0; i < numBoards; i++) {
        const rows: number[][] = []
        for (let j = 0; j < 5; j++) {
            let inputIndex = 2 + 6*i + j
            const newRow = input[inputIndex]
                .split(" ") // TODO: There's got to be a working regex to capture multiple whitespaces
                .filter((x: string) => x !== "")
                .map((x: string) => Number(x))
            rows.push(newRow)
        }
        boards.push(new BingoBoard(rows))
    }
    return {
        drawNumbers: numbers,
        boards: boards,
    }
}

type playBingoResponse = {
    board: BingoBoard
    lastNumberCalled: number
}

// Return winning bingo board
function playBingo(drawNumbers: number[], boards: BingoBoard[]): playBingoResponse | undefined {
    for (let num of drawNumbers) {
        for (let board of boards) {
            const winningNumbers = board.pick(num)
            if (winningNumbers !== undefined) {
                return {
                    board: board,
                    lastNumberCalled: num,
                }
            }
        }
    }
}

function playLosingBingo(drawNumbers: number[], boards: BingoBoard[]): playBingoResponse | undefined {
    if (boards.length === 1) {
        // Play out the remainder of the bingo game
        return playBingo(drawNumbers, boards)
    }
    let winningBoards: BingoBoard[] = []
    const num = drawNumbers[0]
    for (let board of boards) {
        const winningNumbers = board.pick(num)
        if (winningNumbers !== undefined) {
            winningBoards.push(board)
        }
    }
    const remainingBoards: BingoBoard[] = boards
        .filter(x => {
            for (let board of winningBoards) {
                if (x === board) {
                    return false
                }
            }
            return true
        })
    return playLosingBingo(
        drawNumbers.slice(1),
        remainingBoards,
    )
}

const { drawNumbers, boards } = parseInput("input.txt")
const winner = playBingo(drawNumbers, boards)
if (winner === undefined) {
    console.log("Part 1 = something went wrong")
} else {
    console.log(`Part 1 = ${winner.board.addUnpickedNumbers() * winner.lastNumberCalled}`)
}

const loser = playLosingBingo(drawNumbers, boards)
if (loser === undefined) {
    console.log("Part 2 = something went wrong")
} else {
    console.log(`Part 2 = ${loser.board.addUnpickedNumbers() * loser.lastNumberCalled}`)
}
