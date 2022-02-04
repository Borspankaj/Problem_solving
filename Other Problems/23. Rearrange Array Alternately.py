arr=[1,2,3,4,5,6]
n=len(arr)
maxx=n-1
minn=0
temp=[0]*n
pointer=True

for i in range(len(arr)):
    if pointer==True:
        temp[i]=arr[maxx]
        maxx-=1

    else:
        temp[i]=arr[minn]
        minn+=1
    pointer= not pointer

for i in range(n):
    arr[i]=temp[i]
print(arr)





    



