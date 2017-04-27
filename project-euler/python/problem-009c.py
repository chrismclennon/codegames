# Mar 27, 2016

def method_three():
  m = 2
  while (m < 250):
    n = 1
    while(n < 249 and n < m):
      a = m**2 - n**2
      b = 2*m*n
      c = m**2 + n**2
      if (a+b+c == 1000):
        return a*b*c
      n += 1
    m += 1

print method_three()
