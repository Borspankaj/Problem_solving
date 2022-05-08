nums = [2,2,1,1,1,2,2]

hmap={}
for i in nums:
    if i in hmap:
        hmap[i]+=1

    else:
        hmap[i]=1
max_num=0
for key in hmap:
    max_num=max(max_num,hmap[key])

for key in hmap:
    if hmap[key]==max_num:
        ans=key
        break

print(ans)




'''

time = O(n)
space = O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for i in nums:
            if count == 0:
                val = i
                
            if val == i:
                count += 1
            
            else :
                count -= 1
                    
        return val
        
'''