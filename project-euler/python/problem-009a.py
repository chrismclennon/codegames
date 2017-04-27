# Mar 27, 2016

def method_one():
  for i in xrange(1, 1000):
    for j in xrange(i+1, 1000):
      for k in xrange(j+1, 1000):
        if i**2 + j**2 == k**2 and i+j+k == 1000:
          return i*j*k

print method_one()
