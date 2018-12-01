import java.io.File

fun main(args: Array<String>) {
    println("Part one: " + partOne("adventofcode/2018/1/input.txt"))
    println("Part two: " + partTwo("adventofcode/2018/1/input.txt"))
}

fun partOne(filename: String): Int {
    var sum: Int = 0
    File(filename).forEachLine {
        sum += it.toInt()
    }
    return sum
}

fun partTwo(filename: String): Int {
    var sum: Int = 0
    var numbers: MutableSet<Int> = HashSet<Int>()
    val input: List<String> = File(filename).readLines()
    while (true) {
        for (line in input) {
            sum += line.toInt()
            if (numbers.contains(sum)) {
                return sum
            }
            numbers.add(sum)
        }
    }
}