import * as fs from "fs";
import Day from "./day";


export default class DayTwo implements Day {
    scoring: Record<string, number> = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    wins: Record<string, string> = {
        "X": "C",
        "Y": "A",
        "Z": "B",
    }

    draws: Record<string, string> = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    winOutcome: Record<string, number> = {
        "A": 2,
        "B": 3,
        "C": 1,
    }

    drawOutcome: Record<string, number> = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    loseOutcome: Record<string, number> = {
        "A": 3,
        "B": 1,
        "C": 2,
    }

    score(opponentChoice: string, myChoice: string): number {
        let score = 0;
        if (opponentChoice === this.wins[myChoice]) {
            score += 6;
        } else if (opponentChoice === this.draws[myChoice]) {
            score += 3;
        }
        score += this.scoring[myChoice];
        return score || 0;
    }

    scoreOutcome(opponentChoice: string, desiredOutcome: string): number {
        let score = 0;
        if (desiredOutcome === "Y") {
            score += 3;
            score += this.drawOutcome[opponentChoice];
        } else if (desiredOutcome === "Z") {
            score += 6;
            score += this.winOutcome[opponentChoice];
        } else {
            score += this.loseOutcome[opponentChoice];
        }
        return score || 0;
    }

    run() {
        const input = fs.readFileSync("src/inputs/2.txt", "utf-8")
            .split("\n");

        let firstTotal = 0;
        let secondTotal = 0;
        for (let game of input) {
            let gameSplit = game.split(" ");
            let opponentChoice = gameSplit[0];
            let outcome = gameSplit[1];
            firstTotal += this.score(opponentChoice, outcome);
            secondTotal += this.scoreOutcome(opponentChoice, outcome);
        }
        console.log(`Part 1 Result = ${firstTotal}`)
        console.log(`Part 2 Result = ${secondTotal}`)
    }
}