
t=1000000
cycle=3

while True:
    t-=cycle
    if t<=0:
        t+=cycle
        print(cycle-t+1)
        break

    cycle*=2

def solve(t):
    cycle=3
    while t>cycle:
        t-=cycle
        cycle*=2

    return cycle-t+1
