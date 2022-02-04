
def minChanges(str):
    MAX_CHAR=[0]*26
    n = len(str )
 
  
    if (n > MAX_CHAR[0]):
        return -1
    dist_count = 0
    count = [0] * MAX_CHAR[0]
 
    for i in range(n):
        if (count[ord(str[i]) - ord('a')] == 0) :
            dist_count += 1
        count[(ord(str[i]) - ord('a'))] += 1
     
    return (n - dist_count)