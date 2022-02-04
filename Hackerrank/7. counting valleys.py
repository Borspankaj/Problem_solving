steps=8
path='UDDDUDUU'


def solve(steps,path):
    valley=0
    count=0
    for i in path:
        if i=='U':
            valley+=1
        elif i=='D':
            valley-=1

        if valley==0 and i=='U':
            count+=1

    return count

print(solve(steps,path))