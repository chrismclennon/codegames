import * as fs from "fs";
import Day from "./day";

export default class DayThree implements Day {
    getBadge(rucksacks: string[]): string {
        let letters: Record<string, number> = {};
        for (let rucksack of rucksacks) {
            const currentLetters = new Set();
            for (let letter of rucksack) {
                if (currentLetters.has(letter)) {
                    continue
                }
                if (!(letter in letters)) {
                    letters[letter] = 0;
                }
                letters[letter] += 1;
                currentLetters.add(letter);
            }
        }
        for (const [letter, count] of Object.entries(letters)) {
            if (count === rucksacks.length) {
                return letter;
            }
        }
        throw new Error("no badge found");
    }

    getCommonItem(rucksack: string): string {
        let first = rucksack.slice(0, rucksack.length / 2)
        let second = rucksack.slice(rucksack.length / 2, rucksack.length)

        const firstLetters = new Set();
        for (let letter of first) {
            firstLetters.add(letter);
        }
        for (let letter of second) {
            if (firstLetters.has(letter)) {
                return letter
            }
        }
        return "";
    }

    getPriority(letter: string): number {
        if ("a" <= letter && letter <= "z") {
            return letter.charCodeAt(0) - "a".charCodeAt(0) + 1;
        }
        if ("A" <= letter && letter <= "Z") {
            return letter.charCodeAt(0) - "A".charCodeAt(0) + 27;
        }
        return -1;
    }

    run() {
        this.tests();

        const input = fs.readFileSync("src/inputs/3.txt", "utf-8")
            .split("\n")
            .filter(x => x.length > 0);

        let total = 0;
        for (let rucksack of input) {
            let commonItem = this.getCommonItem(rucksack)
            total += this.getPriority(commonItem);
        }
        console.log(`Part 1 Result = ${total}`)

        total = 0;
        for (let i = 0; i < input.length; i += 3) {
            let badge = this.getBadge(input.slice(i, i+3));
            total += this.getPriority(badge);
        }
        console.log(`Part 2 Result = ${total}`)
    }

    tests() {
        let assert = require("assert");

        assert(this.getPriority("p") === 16);
        assert(this.getPriority("P") === 42);

        assert(this.getCommonItem("vJrwpWtwJgWrhcsFMMfFFhFp") === "p")
        assert(this.getCommonItem("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") === "L")

        assert(this.getBadge([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",]) === "r"
        )

        console.log("Tests ran successfully");
    }
}