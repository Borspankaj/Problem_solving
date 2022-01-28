def smallestDivisor(n):
  
    if n % 2 == 0:
        return 2
    i=3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
 
    return n

def minimumSwaps(a, n):

    if n<=1:
        return 0
    if n==2 and a[0]>a[1]:
        if smallestDivisor(a[0])==smallestDivisor(a[1]):
            return 1
        else:
            return -1


    copy = a.copy()
    copy.sort()
    m = {}
    for i in range(n):
        m[copy[i]] = i + 1
    moves = 0
    for i in range(n):
        
        if (i + 1) != m[a[i]]:
            temp = a[i]
            pos = m[a[i] - 1]
            if smallestDivisor(a[i])==smallestDivisor(a[pos]):
                a[i] = a[pos]
                a[pos] = temp
                moves += 1
            else:
                return -1
    return moves

n=2
l=[4,2]

print(minimumSwaps(l,n))