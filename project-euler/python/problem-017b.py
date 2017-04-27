# April 4, 2016

def num_to_word(n):
  if n > 9999:
    raise ValueError('num_to_word does not handle numbers greater than 9999')

  ans = list()
  powers_of_ten = [10**x for x in range(3,-1,-1)]
  use_and = False

  d_num_word = {
    1000: 'thousand',
    100: 'hundred',
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
  }

  for p in powers_of_ten:
    if n >= p:
      if n <= 20: 
        ans.append(d_num_word[n])
        return ans
      elif p == 100: 
        ans.append(num_to_word(n/p)[0])
        ans.append(d_num_word[p])
        n = remove_top_digit(n)
        if n > 0: ans.append('and')
      elif p >= 100:
        ans.append(num_to_word(n/p)[0])
        ans.append(d_num_word[p])
        n = remove_top_digit(n)
      elif p >= 10:
        try:
          ans.append(d_num_word[n])
        except KeyError:
          ans.append(num_to_word(n/10*10)[0])
          n = remove_top_digit(n)

  return ans

def remove_top_digit(n):
  return int(str(n)[1:]) if len(str(n)) > 1 else 0

def count_letters(l):
  return sum(len(s) for s in l)

ans = 0
for n in range(1,1001):
  words = num_to_word(n)
  ans += count_letters(words)
print ans
