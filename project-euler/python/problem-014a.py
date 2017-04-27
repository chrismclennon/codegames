# Mar 30, 2016

i = 1
n = i
count = 1
longest_count = 1
ans = 1
while i < 1000000:
  while n != 1:
    n = n/2 if n % 2 == 0 else 3*n+1
    count += 1
  if count > longest_count: 
    ans, longest_count = i, count
  i += 1
  count, n = 1, i

print "Ans:",ans
