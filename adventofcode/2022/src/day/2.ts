import * as fs from "fs";


export default class DayTwo {
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

    run() {
        const input = fs.readFileSync("src/inputs/2.txt", "utf-8")
            .split("\n");

        let total = 0;
        for (let game of input) {
            let gameSplit = game.split(" ");
            let opponentChoice = gameSplit[0];
            let myChoice = gameSplit[1];
            total += this.score(opponentChoice, myChoice);
        }
        console.log(`Part 1 Result = ${total}`)
    }
}