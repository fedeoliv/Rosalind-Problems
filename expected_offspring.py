# Dominant factor is considered equals to 1.
#     AA-AA = 1
#     AA-Aa = 1
#     AA-aa = 1
#     Aa-Aa = 0.75
#     Aa-aa = 0.5
#     aa-aa = 0 
#
# They will have two descendants, so we need to multiply by 2.

probabilities = [2., 2., 2., 1.5, 1, 0]

with open('couples.txt', 'r') as population:
    couples = map(int, population.readline().split())

print sum([a * b for a, b in zip(probabilities, couples)])
