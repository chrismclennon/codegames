# July 28, 2016
# https://checkio.org/mission/find-sequence/

def checkio(matrix):
    # Horizontal
    for row in matrix:
        for index in range(len(row)-3):
            if all(row[index+increment] == row[index] for increment in range(1, 4)):
                return True

    # Vertical
    for row in range(len(matrix)-3):
        for col in range(len(matrix[0])):
            if all(matrix[row+increment][col] == matrix[row][col] for increment in range(1, 4)):
                return True

    # Diagonal \
    for row in range(len(matrix)-3):
        for col in range(len(matrix)-3):
            if all(matrix[row+increment][col+increment] == matrix[row][col] for increment in range(1, 4)):
                return True

    # Diagonal /
    for row in range(len(matrix)-3):
        for col in range(2, len(matrix[0])):
            if all(matrix[row+increment][col-increment] == matrix[row][col] for increment in range(1, 4)):
                return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
