# April 28, 2016
# https://checkio.org/mission/the-longest-palindromic/

def longest_palindromic(text):
    longest = str()
    for start in range(len(text)):
        for end in range(len(text)+1)[::-1]:
            current = text[start:end]
            if current == current[::-1] and len(current) > len(longest):
                longest = current
    return longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

