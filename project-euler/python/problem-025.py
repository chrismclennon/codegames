# April 24, 2016

def gen_fib():
  a, b = 1, 1
  yield a
  yield b

  while True:
    b, a = a + b, b
    yield b

i = 1
for x in gen_fib():
  if len(str(x)) == 1000:
    print i, ' : ', x
    break
  i += 1
