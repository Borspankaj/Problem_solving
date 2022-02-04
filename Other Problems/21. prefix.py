n=int(input())
name=input().split()
q=int(input())
n=input().split()

for names in n:
    count=0
    for prev in name:
        if prev.startswith(names):
            count+=1
    print(count)

