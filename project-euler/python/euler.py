import math

def power_of_two(n):
  return int(math.log(n)/math.log(2)) if (n != 0) & ((n & (n - 1)) == 0) else False

def factors(n):
  "Returns list of factors for n"
  f = [1, n]
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      f.append(i)
      f.append(n/i)
  return sorted(list(set(f)))

def is_palindrome(n):
  "Returns true if n is a palindrome"
  return str(n) == str(n)[::-1]

def is_prime(num):
  "Returns true if num is prime"
  if num == 2 or num == 3:
    return True
  if num % 2 == 0 or num < 2:
    return False

  for i in xrange(3, int(num**0.5)+1, 2):
    if num % i == 0:
      return False
  return True

def prime_sieve(limit):
  "Returns primes using Sieve of Eratosthenes up to limit."
  a = [True] * limit
  a[0] = a[1] = False
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i,limit,i):
        a[n] = False
