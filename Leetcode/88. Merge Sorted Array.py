nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n=len(nums2)
i=0
m=6
n=3
for _ in range(len(nums2)):
    nums1.pop()
while len(nums1)!=m+n:
    if (nums2 and nums2[0]<nums1[i]):
        val=nums2.pop(0)
        nums1.insert(i,val)
      
    i+=1

print(nums1)
