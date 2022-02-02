arr=[3,2,2,6,1,2,3,1]

def solve(arr):
    cs=sum(arr)
    print(cs)
    s=0
    for i in range(len(arr)):
        if s==cs-arr[i]:
            return i
        cs-=arr[i]    
        s+=arr[i]
    return -1

print(solve(arr))