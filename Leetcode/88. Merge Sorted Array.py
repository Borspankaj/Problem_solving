class Solution:
    def merge(self, nums1, m: int, nums2, n) :
        idx1 = 0
        idx2 = 0
        if n == 0:
            return nums1
        while idx1 < m  :
            if nums1[idx1] > nums2[idx2] :
                nums1[idx1] , nums2[idx2] = nums2[idx2] , nums1[idx1]
                nums2.sort()

            idx1 += 1

        for i in range(n):

            nums1[i+idx1] = nums2[i]

        return nums1