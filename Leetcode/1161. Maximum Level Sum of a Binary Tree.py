import math 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root):
        q = []
        q.append(root)
        ans = []
        m = -math.inf
        level = 1
        while q:
            l = len(q)
            s = 0
            while l>0:
                node = q.pop(0)
                if node :
                    s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l-=1
            if s > m:
                m = s
                ans = level
            level += 1

            
            
        return ans