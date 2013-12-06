# http://rosalind.info/problems/iprb/

f = open('rosalind_mendel.txt', 'r')
population = f.readlines()
f.close()

"""
    k = homozygous (dominant)
    m = heterozygous
    n = homozygous (recessive)
    p = sum of the individuals (population) = k + m + n
"""

for individuals in population:
    # Splitting the categories of individuals
    k, m, n = map(float, individuals.split())
    
    p = k + m + n
    homo_dominant = k / p
    heterozygous = m / p
    homo_recessive = n / p

    # Maximum probability is 1
    probability = 1
    
    # Probability of both organisms being homozygous recessive
    probability -= homo_recessive * ((n - 1) / (p - 1))
    
    # Probability of one being homozygous recessive and the other
    # one heterozygous with the recessive allele (this is the 0.5)
    probability -= 2 * homo_recessive * (m / (p - 1)) * 0.5
    
    # Probability of both being heterozygous with the recessive allele (this is the 0.25)
    probability -= heterozygous * ((m - 1) / (p - 1)) * 0.25
    
    print probability
