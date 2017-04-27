# April 23, 2016

def permutation(elements):
  if len(elements) == 1:
    return [elements]

  perm_list = []
  for e in elements:
    remaining_elements = [x for x in elements if x != e]
    perm_remainder = permutation(remaining_elements)

    for perm in perm_remainder:
      perm_list.append([e] + perm)

  return perm_list

print ''.join(sorted(permutation([str(x) for x in range(10)]))[999999])
