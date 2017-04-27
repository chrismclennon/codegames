# April 27, 2016
# https://checkio.org/mission/pawn-brotherhood/

def diag_pawns(pawn):
    c, r = map(ord, pawn)
    return chr(c-1)+chr(r-1),chr(c+1)+chr(r-1)

def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in diag_pawns(p))])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

