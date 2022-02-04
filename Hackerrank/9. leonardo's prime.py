
def solve_Prime(n):
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

    val=1
    i=0
    while True:
        val*=prime[i]
        if val>n:
            return i
        i+=1