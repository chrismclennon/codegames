const fs = require("fs")
const sampleInput: number[] = "16,1,2,0,4,2,7,1,2,14"
    .split(",")
    .map(x => Number(x))
    .sort((a, b) => a - b)
const input: number[] = fs.readFileSync("input.txt")
    .toString()
    .split(",")
    .map((x: string) => Number(x))
    .sort((a: number, b: number) => a - b)

function median(nums: number[]): number {
    const middle = Math.floor(nums.length / 2)
    return nums.length % 2 === 0 ? (nums[middle-1] + nums[middle]) / 2 : nums[middle]
}

function mean(nums: number[]): number {
    const sum = nums.reduce((a, b) => a + b)
    return Math.floor(sum / nums.length) // For this problem, it's either floor or round so mean isn't quite it
}

function totalFuelCost(crabs: number[]): number {
    const medianValue = median(crabs)
    let total = 0
    for (let crab of crabs) {
        total += Math.abs(crab - medianValue)
    }
    return total
}

function totalCrabbyFuelCost(crabs: number[]): number {
    const meanValue = mean(crabs)
    let total = 0
    for (let crab of crabs) {
        const distance = Math.abs(meanValue - crab)
        for (let i = 1; i <= distance; i++) {
            total += i
        }
    }
    return total
}

console.log(`Part 1 = ${totalFuelCost(input)}`)
console.log(`Part 2 = ${totalCrabbyFuelCost(input)}`)
