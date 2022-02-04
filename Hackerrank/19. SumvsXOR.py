def solve(n):
    b=bin(n)[2:]
    return 2**(b.count('0'))

print(solve(10))