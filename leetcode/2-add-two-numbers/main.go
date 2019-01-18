/**
 * Solution ran in 16 ms, faster than 100.00% of Go online submissions.
 * Time complexity: O(max(m, n)). We traverse the linked lists only once.
 * Space complexity: O(max(m, n)). We store the input at worst as the longer linked list + 1.
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var ans = &ListNode{}
    var currentNode = ans
    var carry int

    for {
        var l1Val, l2Val int

        if l1 != nil {
            l1Val = l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            l2Val = l2.Val
            l2 = l2.Next
        }
        sum := l1Val + l2Val + carry
        carry = sum / 10
        currentNode.Val = sum % 10

        if l1 != nil || l2 != nil || carry > 0 {
            currentNode.Next = &ListNode{}
            currentNode = currentNode.Next
        } else {
            break
        }
    }
    return ans
}

