## minimum oprations to make ezero
n=int(input())
arr=list(map(int,input().split()))
def solve(arr,n):
    i=count=0
    while i+1<n:
        if arr[i+1]!=arr[i]:
            count+=1

        i+=1
    print(count+1)