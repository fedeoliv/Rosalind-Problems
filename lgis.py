def subsequence(sequence):
    # We create arrays with 'n' positions and we start all of them with 'None'.
    m = [None] * len(sequence)
    permutations = [None] * len(sequence)

    # There is at least an increasing subsequence of length one, 
    # because it is the first element.
    last = 1
    
    # Stores the position of the lower or higher values, 
    # depending os the positions of the 'sequence'
    m[0] = 0

    for i in range(1, len(sequence)):
        # We want the largest j <= last
        #  such that sequence[m[j]] < sequence[i] (with default j = 0),
        #  hence we want the lower value.
        lower = 0
        upper = last

        # Verifying what is the upper value
        if sequence[m[upper - 1]] < sequence[i]:
            j = upper
        else:
            while (upper - lower) > 1:
                mid = (upper + lower) // 2
                if sequence[m[mid - 1]] < sequence[i]:
                    lower = mid
                else:
                    upper = mid
            
            # 'j' will also set the default value to 0.
            j = lower    

        permutations[i] = m[j - 1]

        if j == last or sequence[i] < sequence[m[j]]:
            m[j] = i
            last = max(last, j + 1)

    result = []
    pos = m[last - 1]
    
    # We use '_' when we don't want to use a variable into the loop.
    for _ in range(last):
        result.append(sequence[pos])
        pos = permutations[pos]

    return result[::-1]
    
if __name__ == "__main__":
    fid = open('rosalind_lgis.txt','r')
    
    n = int(fid.readline().strip())
    s = [int(x) for x in fid.readline().split()]
     
    increasing = subsequence(s)
    
    # We take the collection and revert the values.
    # After the results, we revert again.
    decreasing = subsequence(s[::-1])[::-1]
    
    print str(increasing).strip('[]').replace(',','')
    print str(decreasing).strip('[]').replace(',','')
