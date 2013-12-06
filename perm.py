import itertools

n = 6

permutations = list(itertools.permutations(range(1, n + 1)))

print str(len(permutations))

for p in permutations:
    print ' '.join(str(elem) for elem in p)
