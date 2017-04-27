# July 28, 2016
# https://checkio.org/mission/find-sequence/

def checkio(matrix):
    DIRECTION = {
        'down': lambda r, c: all(matrix[r][c] == matrix[r+x][c] for x in range(4)),
        'right': lambda r, c: all(matrix[r][c] == matrix[r][c+x] for x in range(4)),
        'down_right': lambda r, c: all(matrix[r][c] == matrix[r+x][c+x] for x in range(4)),
        'down_left': lambda r, c: all(matrix[r][c] == matrix[r+x][c-x] for x in range(4))
    }
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if row < num_rows - 3 and DIRECTION['down'](row, col):
                return True
            elif col < num_cols - 3 and DIRECTION['right'](row, col):
                return True
            elif row < num_rows - 3 and col >= 3 and DIRECTION['down_left'](row, col):
                return True
            elif row < num_rows - 3 and col < num_rows - 3 and DIRECTION['down_right'](row, col):
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
