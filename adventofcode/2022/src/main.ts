import Day from "./day/day";
import DayOne from "./day/1";
import DayTwo from "./day/2";
import DayThree from "./day/3";
import DayFour from "./day/4";

const days: Record<number, Day> = {
    1: new DayOne(),
    2: new DayTwo(),
    3: new DayThree(),
    4: new DayFour(),
}

console.log("Hello from main.ts!");
days[4].run();
