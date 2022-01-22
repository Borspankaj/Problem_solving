
'''

#### Q 5 :->


lst=[1,1,5,100,20,20,6,0,0]
c=0
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        c+=1

print(c)

'''


##  1. Check if a list contains an element
'''
lst=[1,1,5,100,20,20,6,0,0]

a=int(input())
if a in lst:
    print("YES !!")
else: 
    print("NO !! ")
'''
'''
lst=[1,1,5,100,20,20,6,0,0]
## 2. frequency of each element in the array
fre=[]
for i in lst:
    c=lst.count(i)

    fre.append(c)

print(fre)



## 3. Rotate list to left 
lst=[1,2,3,4,5]
d=int(input())

for i in range(d):
    val=lst.pop(0)
    lst.append(val)

print(lst)

for i in range(len(lst)-1,-1,-1):
    print(lst[i])

lst=lst[::-1]
for i in lst:
    print(i)
'''
lst=[1,2,3,4,5]

for i in range(len(lst)):
    if i%2!=0:

        print(lst[i])