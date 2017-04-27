# August 1, 2016
# https://checkio.org/mission/gate-puzzles/

import string

def find_word(message):
    words = message.lower().translate(str.maketrans({key: None for key in string.punctuation})).split()
    scores = [0] * len(words)

    for index, word in enumerate(words):
        for comparison_index, comparison_word in enumerate(words):
            if index == comparison_index:
                continue
                
            current_score = 0
            if word[0] == comparison_word[0]:
                current_score += 10
            if word[-1] == comparison_word[-1]:
                current_score += 10
            current_score += (len(word) / len(comparison_word)) * 30 if len(word) <= len(comparison_word) \
                             else (len(comparison_word) / len(word)) * 30
            current_score += len(set(word) & set(comparison_word)) / len(set(word) | set(comparison_word)) * 50

            scores[index] += current_score

    max_score = max(scores)
    return words[max(index for index, score in enumerate(scores) if score == max_score)]

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

