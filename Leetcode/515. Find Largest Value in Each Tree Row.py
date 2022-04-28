import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        q = []
        q.append(root)
        ans = []
        if not root:
            return ans
        while q:
            l = len(q)
            print(l)
            s = -math.inf
            ele = l
            while l>0:
                node = q.pop(0)
                if node:
                    s = max( s, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l-=1
                
            ans.append(s)
            
            
        return ans