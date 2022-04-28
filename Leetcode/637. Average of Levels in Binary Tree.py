# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        q = []
        q.append(root)
        ans = []
        while q:
            l = len(q)
            print(l)
            s = 0
            ele = l
            while l>0:
                node = q.pop(0)
                if node :
                    s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l-=1
                
            ans.append(s/ele)
            
            
        return ans