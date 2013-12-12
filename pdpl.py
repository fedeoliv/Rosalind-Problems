# http://rosalind.info/problems/pdpl/

from math import sqrt

if __name__ == "__main__":
    multiset = map(int, open('rosalind_pdpl.txt').read().strip().split())
    
    # Write n choose 2 as a quadratic, solve for n in terms of length with the quadratic formula.
    # This tells us how many items we need in our multiset.
    n = int(0.5 + 0.5 * sqrt(8.0 * len(multiset) + 1))
    
    # Pick zero to be the in our multiset.  This is a valid assumption because there are infinitely many solutions.
    # Given a solution, shifting each element by a fixed amount doesn't change the delta. Thus, there exists a solution with zero in the set.
    x = [0]
    
    # Add the largest delta to the solution. Since zero is in our multiset, the only way for it to be the largest difference if it's in the multiset.
    x.append(max(multiset))
    multiset.remove(x[1])
    
    # The other values in the multiset must come from deltaX, since zero is in our multiset.
    deltaSet = set(multiset)
    
    for candidate in deltaSet:
            # Test to see if each difference for a candidate member is our list of desired differences.
            if sum([(abs(candidate-member) in multiset) for member in x])  == len(x):
                    for member in x:
                            # Remove the differences we've already found.
                            multiset.remove(abs(candidate-member))
                    
                    # insert the new value before the largest value to keep the set sorted.
                    x.append(candidate)
    
                    if len(x) == n: break
                    
    x.sort()
    print ' '.join(map(str, x))
