# April 17, 2016

with open('problem-022-names.txt','rb') as f:
  raw = f.read()

all_names = sorted(raw.replace('\"','').split(','))
total_score = 0
for m, name in enumerate(all_names):
  for c in name:
    total_score += (ord(c)-64)*(m+1)
print total_score
