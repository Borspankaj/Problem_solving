n=input()
arr=list(map(int,n.split()))

for i in range(len(arr)):
    for j in range(1,len(arr)-i-1):
        if arr[j]<arr[j+1] and ((arr[j]%2==0 and arr[j+1]%2==0) or (arr[j]%2!=0 and arr[j+1]%2!=0)):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print("".join(list(map(str,arr))))

