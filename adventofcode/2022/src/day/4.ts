import * as fs from "fs";
import Day from "./day";

class Interval {
    public left: number;
    public right: number;

    constructor(input: string) {
        let [left, right] = input.split("-");
        this.left = Number(left);
        this.right = Number(right);
    }

    toString(): string {
        return `${this.left}-${this.right}`;
    }
}

export default class DayFour implements Day {
    isFullyOverlapping(first: Interval, second: Interval): boolean {
        return this.isFullyOverlappingHelper(first, second) || this.isFullyOverlappingHelper(second, first);
    }

    private isFullyOverlappingHelper(first: Interval, second: Interval): boolean {
        return first.left <= second.left && second.right <= first.right;
    }

    isOverlapping(first: Interval, second: Interval): boolean {
        return (
            (first.left <= second.left && first.right >= second.left) ||
            (second.left <= first.left && second.right >= first.left)
        )
    }

    run() {
        this.test();

        const input = fs.readFileSync("src/inputs/4.txt", "utf-8")
            .split("\n")
            .filter(x => x.length > 0);

        const intervals: Interval[] = []
        for (let line of input) {
            let [first, second] = line.split(",");
            intervals.push(new Interval(first));
            intervals.push(new Interval(second));
        }

        let countFullOverlaps = 0;
        let countOverlaps = 0;
        for (let i = 0; i < intervals.length; i += 2) {
            let [first, second] = [intervals[i], intervals[i+1]]
            if (this.isFullyOverlapping(first, second)) {
                countFullOverlaps++;
            }
            if (this.isOverlapping(first, second)) {
                countOverlaps++;
            }
        }
        console.log(`Part 1 Result = ${countFullOverlaps}`)
        console.log(`Part 2 Result = ${countOverlaps}`)
    }

    test() {
        let assert = require("assert");

        assert(this.isFullyOverlapping(
            new Interval("2-8"),
            new Interval("3-7"),
        ));
        assert(this.isFullyOverlapping(
            new Interval("3-7"),
            new Interval("2-8"),
        ));
        assert(!this.isFullyOverlapping(
            new Interval("2-4"),
            new Interval("6-8"),
        ));
        assert(this.isFullyOverlapping(
            new Interval("6-6"),
            new Interval("4-6"),
        ));
        assert(!this.isFullyOverlapping(
            new Interval("2-6"),
            new Interval("4-8"),
        ));
        assert(this.isFullyOverlapping(
            new Interval("1-1"),
            new Interval("1-1"),
        ));
        assert(!this.isFullyOverlapping(
            new Interval("1-2"),
            new Interval("21-22"),
        ));

        assert(this.isOverlapping(
            new Interval("5-7"),
            new Interval("7-9"),
        ));
        assert(this.isOverlapping(
            new Interval("2-8"),
            new Interval("3-7"),
        ));
        assert(this.isOverlapping(
            new Interval("6-6"),
            new Interval("4-6"),
        ));
        assert(this.isOverlapping(
            new Interval("2-6"),
            new Interval("4-8"),
        ));
        assert(!this.isOverlapping(
            new Interval("2-4"),
            new Interval("6-8"),
        ));
        assert(!this.isOverlapping(
            new Interval("2-3"),
            new Interval("4-5"),
        ));

        console.log("Tests ran successfully");
    }
}