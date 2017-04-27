# August 1, 2016
# https://checkio.org/mission/gate-puzzles/

import re

def likeness(word, compare_word):
    score = 10 * ((word[0] == compare_word[0]) + (word[-1] == compare_word[-1]))
    score += 30 * min(len(word), len(compare_word)) / max(len(word), len(compare_word))
    score += 50 * len(set(word) & set(compare_word)) / len(set(word) | set(compare_word))
    return score

def find_word(message):
    words = re.findall('[a-z]+', message.lower())[::-1]
    return max(words, key=lambda w: sum(likeness(w, x) for x in words))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Friend Fred and friend Ted.") == "friend", "Provided example"
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"


