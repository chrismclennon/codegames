# April 27, 2016
# https://checkio.org/mission/pawn-brotherhood/

def adjacent_squares(pawn):
    letters = (chr(ord(pawn[0])-1), chr(ord(pawn[0])+1))
    numbers = (str(int(pawn[1])-1), str(int(pawn[1])-1))
    return map(''.join, zip(letters,numbers))

def safe_pawns(pawns):
    safe_pawns = []
    for pawn in pawns:
        if len([i for i in adjacent_squares(pawn) if i in pawns]) > 0:
            safe_pawns.append(pawn)
    return len(safe_pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

