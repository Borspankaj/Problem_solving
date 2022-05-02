class Solution:
    def nextPermutation(self, arr) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1] < arr[i]:
                flag = True
                break
        if flag:
            i = i-1
            val = arr [i]
            swap = i+1
            for idx in range(i+1, len(arr)):
                if arr[idx] > val :
                    swap = idx if arr[idx] <= arr[swap] else swap
            arr[swap] , arr[i] = arr[i] , arr[ swap]
            i = i+1

        else:
            i = 0
        end = len(arr) - 1
        while i <= end :

            arr [i] , arr[end] = arr[end] , arr[i]
            i += 1
            end -= 1
