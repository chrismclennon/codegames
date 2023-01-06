import DayOne from "./day/1";
import Day from "./day/day";

const days: Record<number, Day> = {
    1: new DayOne(),
}

console.log("Hello from main.ts!");
days[1].run()
