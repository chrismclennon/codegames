import Day from "./day/day";
import DayOne from "./day/1";
import DayTwo from "./day/2";
import DayThree from "./day/3";

const days: Record<number, Day> = {
    1: new DayOne(),
    2: new DayTwo(),
    3: new DayThree(),
}

console.log("Hello from main.ts!");
days[3].run();
