# April 3, 2016

def num_to_word(n):
  ans = list()
  use_and = False

  # Thousands
  if n >= 1000:
    ans.append(num_to_word(n/1000)[0])
    ans.append('thousand')
    n = remove_top_digit(n)

  # Hundreds
  if n >= 100:
    ans.append(num_to_word(n/100)[0])
    ans.append('hundred')
    n = remove_top_digit(n)
    use_and = True

  # check and
  if n >= 1 and use_and: ans.append('and')

  # teens
  if n >= 11 and n <= 19:
    if n == 11: ans.append('eleven')
    elif n == 12: ans.append('twelve')
    elif n == 13: ans.append('thirteen')
    elif n == 14: ans.append('fourteen')
    elif n == 15: ans.append('fifteen')
    elif n == 16: ans.append('sixteen')
    elif n == 17: ans.append('seventeen')
    elif n == 18: ans.append('eighteen')
    elif n == 19: ans.append('nineteen')
    return ans

  # Tens
  if n >= 10:
    digit = n/10
    if digit == 1: ans.append('ten')
    elif digit == 2: ans.append('twenty')
    elif digit == 3: ans.append('thirty')
    elif digit == 4: ans.append('forty')
    elif digit == 5: ans.append('fifty')
    elif digit == 6: ans.append('sixty')
    elif digit == 7: ans.append('seventy')
    elif digit == 8: ans.append('eighty')
    elif digit == 9: ans.append('ninety')
    n = remove_top_digit(n)

  # Ones
  if n == 1: ans.append('one')
  elif n == 2: ans.append('two')
  elif n == 3: ans.append('three')
  elif n == 4: ans.append('four')
  elif n == 5: ans.append('five')
  elif n == 6: ans.append('six')
  elif n == 7: ans.append('seven')
  elif n == 8: ans.append('eight')
  elif n == 9: ans.append('nine')

  return ans

def remove_top_digit(n):
  return int(str(n)[1:])

def count_letters(l):
  # make a list comprehension of this instead
  c = 0
  for i in l:
    c += len(i)
  return c

ans = 0
for n in range(1,1001):
  words = num_to_word(n)
  ans += count_letters(words)
print ans
