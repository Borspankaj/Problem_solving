def prev(n):
    p = 1
    while p <= n :
        p <<= 1
        
    p >>= 1
    return p

def counterGame(n):
    counter=True
    while n!=1:
        if n&(n-1)==0:
            n//=2
        else:
            n=n-prev(n)

        counter=not counter

    if not counter:
        return 'Louise'

    else:
        return 'Richard'

print(counterGame(132))