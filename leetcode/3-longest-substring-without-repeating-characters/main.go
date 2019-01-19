/**
 * 
 */
import "fmt"

func indexOf(target rune, s []rune) int {
    for index, character := range s {
        if character == target {
            return index
        }
    }
    return -1
}

func lengthOfLongestSubstring(s string) int {
    var currentString = make([]rune, len(s))
    var seen map[rune]bool = make(map[rune]bool)
    var currentLength, longestLength int
    var index int
    for _, character := range s {
        fmt.Println()
        fmt.Println(seen, currentString)
        if _, present := seen[character]; present {
            if currentLength > longestLength {
                longestLength = currentLength
            }
            delete(seen, character)
            duplicateCharacterIndex := indexOf(character, currentString)
            currentString = currentString[duplicateCharacterIndex+1:]
            index -= duplicateCharacterIndex + 1
            currentLength -= duplicateCharacterIndex + 1
        }
        currentString[index] = character
        seen[character] = true
        index++
        currentLength++
        fmt.Println(seen, currentString)
    }
    if currentLength > longestLength {
        longestLength = currentLength
    }
    fmt.Println(currentString)
    return longestLength
}
