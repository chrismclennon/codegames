import Day from "./day/day";
import DayOne from "./day/1";
import DayTwo from "./day/2";

const days: Record<number, Day> = {
    1: new DayOne(),
    2: new DayTwo(),
}

console.log("Hello from main.ts!");
// days[1].run()
days[2].run();
