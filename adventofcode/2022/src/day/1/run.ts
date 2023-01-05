import * as fs from "fs";
import Heap from "heap-js";

export function run() {
    const input = fs.readFileSync("src/inputs/1.txt", "utf-8")
        .split("\n");

    let elves = makeElves(input);

    console.log(`Part 1 Result = ${Math.max(...elves)}`);

    const maxHeap: Heap<number> = new Heap(Heap.maxComparator);
    elves.forEach((x) => maxHeap.push(x));

    let topElvesCarry = 0;
    for (let i = 0; i < 3; i++) {
        topElvesCarry += maxHeap.pop() || 0;
    }

    console.log(`Part 2 Result = ${topElvesCarry}`);
}

function makeElves(input: string[]): number[] {
    let elves: number[] = [];

    let current = 0;
    for (let val of input) {
        if (val === "") {
            elves.push(current);
            current = 0;
            continue
        }
        current += Number(val);
    }
    elves.push(current);

    return elves
}
