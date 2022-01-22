'''import math

for i  in range(5):
    print("*"*i+" "*((2*(5-i))-1)+"*"*i)
print('*'*9)
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=2
for i in range(1,5):
    j=1
    while j<=i:
        if isprime(n):
            print(n)
            j+=1
            n+=1
    print()

        1
      2 * 2
    3 * * * 3
  4 * * * * * 4
5 4 3 2 1 2 3 4 5   

'''

for i in range(4):
    print(" "*(4-i),end="")
    print(i+1,end="")
    print("*"*(2*i-1),end="")
    if i>0:
        print(i+1)
    else:
        print()

print(''.join(list(map(str,range(5,0,-1)))+list(map(str,range(2,6)))))

   
