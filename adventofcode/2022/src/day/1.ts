import * as fs from "fs";
import Day from "./day";

export default class DayOne implements Day {
    makeElves(input: string[]): number[] {
        let elves: number[] = [];

        let current = 0;
        for (let val of input) {
            if (val === "") {
                elves.push(current);
                current = 0;
                continue;
            }
            current += Number(val);
        }
        elves.push(current);

        return elves;
    }

    run(): void {
        const input = fs.readFileSync("src/inputs/1.txt", "utf-8")
            .split("\n");
        let elves = this.makeElves(input);
        elves.sort((a, b) => b - a);

        console.log(`Part 1 Result = ${Math.max(...elves)}`)
        console.log(`Part 2 Result = ${elves.slice(0, 3).reduce((a, b) => a + b, 0)}`)
    }
}
