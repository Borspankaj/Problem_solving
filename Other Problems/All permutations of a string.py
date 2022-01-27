def solve(string,left,right):
    if left==right:
        print("".join(string))

    else:
        for i in range(left,right+1):
            string[left],string[i]=string[i],string[left]
            solve(string,left+1,right)
            string[left],string[i]=string[i],string[left]


def permute(string):
    solve(list(string),0,len(string)-1)


permute(input())