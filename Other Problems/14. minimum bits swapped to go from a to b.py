a=int(input())
b=int(input())

n=a^b
count=0
while n:
    count+=1
    n&=n-1

print(count)