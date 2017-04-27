# April 25, 2016
# https://checkio.org/mission/x-o-referee/

def checkio(game_result):
  rows = game_result
  cols = map(''.join, zip(*rows))
  diags = map(''.join, zip(*[(r[i], r[2-i]) for i, r in enumerate(rows)]))
  lines = rows + cols + diags
  return 'X' if 'XXX' in lines else 'O' if 'OOO' in lines else 'D'

if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert checkio([
      "X.O",
      "XX.",
      "XOO"]) == "X", "Xs wins"
  assert checkio([
      "OO.",
      "XOX",
      "XOX"]) == "O", "Os wins"
  assert checkio([
      "OOX",
      "XXO",
      "OXX"]) == "D", "Draw"
  assert checkio([
      "O.X",
      "XX.",
      "XOO"]) == "X", "Xs wins again"
