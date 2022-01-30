A=16
N=2
B=10
def solve(A,N,B):
    day=1
    slices=A
    remainder=0
    s=A//N
    while day%7!=0 or remainder-N>0:
        remainder+=slices-N
        slices-=N
        day+=1
    if day>B:
        return A%(B-s)
    else:
        return -1

print(solve(A,N,B))


