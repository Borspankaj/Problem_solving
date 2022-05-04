    
def solve(strs):
    res = strs[0]
    m = len(strs[0])
    for i in range(1,len(strs)):
        m = min(len(res),len(strs[i]))
        if m < 1 :
            return ""
        j = 0
        while j < m:
            if strs[i][j] != res[j]:
                break
            j += 1
        
        res = res[:j]
        
    return res

print(solve(strs = ["a", ""]))