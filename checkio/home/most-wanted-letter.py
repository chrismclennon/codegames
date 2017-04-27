# April 25, 2016
# https://checkio.org/mission/most-wanted-letter/

import re
def checkio(text):
    text = re.sub('[^A-z]','',text.lower())
    tup = [(letter, text.count(letter)) for letter in sorted(set(text))]
    return max(tup,key=lambda x:x[1])[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

