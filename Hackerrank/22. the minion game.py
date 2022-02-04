def solve(s):
    vowels={'a','e','i','o','u'}
    kevin=stuart=0
    n=len(s)
    for i,char in enumerate(s):
        if char.lower() in vowels:
            kevin+=n-i

        else:
            stuart+=n-i

    if stuart>kevin:
        print('Stuart',stuart)

    elif kevin>stuart:
        print('Kevin',kevin)

    else:
        print('Draw')

solve("BANANA")