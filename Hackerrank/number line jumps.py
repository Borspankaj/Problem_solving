x1=0
v1=3
x2=4
v2=2
if v2>=v1:
    print('NO')

else:
    while x1<x2:
        x1+=v1
        x2+=v2
            
        if x1==x2:
            print('YES')
            break
    else:
        print('NO')


