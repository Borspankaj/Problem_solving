'''for i in range(7):
    if i==3 or i==6:
        continue
    else:
        print(i)




a=0
b=1
print(a,b,end=" ")


while True:
    c=a+b
    if c>50:
        break
    print(c,end=" ")
    a=b
    b=c
    




for i in range(50):
    c=a+b
    if c>50:
        break
    print(c,end=" ")
    a=b
    b=c

    
for i in range(1,50):
    if i%15==0:
        print(i,"fizz buzz")
    elif i%3==0:
        print(i,"fizz")

    elif i%5==0:
        print(i,"BUZZ")

    

## question 10
c=input()


if c=='a' or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U':
    print(c," VOWEL !!")

else:
    print(c, 'CONSONANT !!')
        


if c in 'aeiouAEIUO':
    print('VOWEL !!')

else:
    print('CONSONANT !!')



## Q 11

 
s=0
n=0
while True:
    val=int(input()) ## integer val
    if val==0:
        break
    s+=val
    n+=1

avg=s/n
print(s,avg)




## Q 12 !!

n=int(input())

for i in range(1,11):
    print(n,"X",i,"==",n*i)





## QUERRYYY !!! factorial
def fact(n):

    fact=1
    for i in range(1,n+1):
        fact=fact*i

    return fact

## Q 13 !!
s=0
n=int(input())
for i in range(1,n+1):
    temp=i/fact(i)
    s+=temp

print(s)

'''





