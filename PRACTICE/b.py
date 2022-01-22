import itertools
def getCount(N,M,A,B):
    count=1
    for i,j in itertools.product(A,B):
        if i==j:
            count+=1
    return count
N=int(input())
M=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))

B=[]
for _ in range(M):
    B.append(int(input()))
print(getCount(N,M,A,B))