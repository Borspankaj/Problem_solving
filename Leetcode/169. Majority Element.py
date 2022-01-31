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