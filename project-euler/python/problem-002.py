# Mar 25, 2016

num1, num2 = 1, 2
sum = 0

while num1 < 4000000 and num2 < 4000000:
  if num1 % 2 == 0:
    sum += num1
  num1 += num2

  if num2 % 2 == 0:
    sum += num2
  num2 += num1

print sum
