def solve(s):
    n=len(s)
    count=0
    start=0
    end=2
    while end<n:
        if len(set(s[start:end+1]))==3:
            count+=1
        start+=1
        end+=1
    return count

print(solve("aababcabc"))