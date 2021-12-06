const sample_input: number[] = "3,4,3,1,2"
    .split(",")
    .map(x => Number(x))
const input: number[] = "1,1,1,1,1,5,1,1,1,5,1,1,3,1,5,1,4,1,5,1,2,5,1,1,1,1,3,1,4,5,1,1,2,1,1,1,2,4,3,2,1,1,2,1,5,4,4,1,4,1,1,1,4,1,3,1,1,1,2,1,1,1,1,1,1,1,5,4,4,2,4,5,2,1,5,3,1,3,3,1,1,5,4,1,1,3,5,1,1,1,4,4,2,4,1,1,4,1,1,2,1,1,1,2,1,5,2,5,1,1,1,4,1,2,1,1,1,2,2,1,3,1,4,4,1,1,3,1,4,1,1,1,2,5,5,1,4,1,4,4,1,4,1,2,4,1,1,4,1,3,4,4,1,1,5,3,1,1,5,1,3,4,2,1,3,1,3,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,3,1,1,5,1,1,4,1,1,3,1,1,5,2,1,4,4,1,4,1,2,1,1,1,1,2,1,4,1,1,2,5,1,4,4,1,1,1,4,1,1,1,5,3,1,4,1,4,1,1,3,5,3,5,5,5,1,5,1,1,1,1,1,1,1,1,2,3,3,3,3,4,2,1,1,4,5,3,1,1,5,5,1,1,2,1,4,1,3,5,1,1,1,5,2,2,1,4,2,1,1,4,1,3,1,1,1,3,1,5,1,5,1,1,4,1,2,1"
    .split(",")
    .map(x => Number(x))

type FishPopulation = {
    [timer: number]: number
}
const fishies: FishPopulation = {}

function getTotalFishies(fishies: FishPopulation): number {
    let total: number = 0
    for (const key in fishies) {
        const timer = Number(key)
        if (timer === -1) {
            continue
        }
        total += fishies[timer]
    }
    return total
}

for (let num of input) {
    let currentNum = fishies[num] || 0
    fishies[num] = currentNum + 1
}

for (let dayNum = 1; dayNum <= 256; dayNum++) {
    for (let i = 0; i <= 8; i++) {
        fishies[i-1] = fishies[i] || 0
    }
    fishies[8] = fishies[-1]
    fishies[6] += fishies[-1]
    delete fishies[-1]

    if (dayNum === 80) {
        console.log(`Part 1 = ${getTotalFishies(fishies)}`)
    }
}

console.log(`Part 2 = ${getTotalFishies(fishies)}`)
