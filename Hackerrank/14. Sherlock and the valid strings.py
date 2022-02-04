def solve(s):
    hmap={}
    for char in s:
        if char in hmap:
            hmap[char]+=1
        else:
            hmap[char]=1
           

    
    val=set(hmap.values())
    if len(val)==1:
        return 'YES'

    elif len(val)>2:
        return 'NO'
    else:
        for char in hmap:
            hmap[char]-=1
            val=set(hmap.values())
            try:
                val.remove(0)
            except:
                pass
            if len(val)==1:
                return 'YES'
            else:
                hmap[char]+=1

        return 'NO'


            
                

        

    
print(solve("aabbc"))