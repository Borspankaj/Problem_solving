'''def maxcost(n,k,arr):
    if n < k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    i=0
    while i==:
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
 
    return max_sum
'''




num=int(input())
k=int(input())

a=[]
for i in range(num):
    a.append((int(input())))

a.sort(reverse=True)
min=0
i=0
while (len(a)!=0):
    if(i==k):
        i=0
        j=0
        while j<len(a):
            min=min+a[j]
            j+=1

    elif(i>=len(a)):
        break
    a.pop(0)
    i+=1

print(min)
