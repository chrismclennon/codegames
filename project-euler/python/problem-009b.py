# Mar 27, 2016

print [(a*b*c) for c in xrange(1000) for b in xrange(1000) for a in xrange(1000) if a < b and b < c and a+b+c==1000 and ((a**2)+(b**2)==c**2)]
