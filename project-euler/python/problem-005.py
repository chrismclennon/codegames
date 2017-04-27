# Mar 26, 2016

i = 2520
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

while True:
  if all(i % n == 0 for n in check_list):
    print i
    break
  i += 20
