/**
 * Solution ran in 4 ms, faster than 100.00% of Go online submissions.
 * Time complexity: O(n). We traverse the input list only once.
 * Space complexity: O(n). We store the input at most once.
 */

func twoSum(nums []int, target int) []int {
    var uniqueNums = make(map[int]int)
    for index, element := range nums {
        var complementNum = target - element
        if complementIndex, ok := uniqueNums[complementNum]; ok {
            return []int{complementIndex, index}
        }
        uniqueNums[element] = index
    }
    return nil
}
