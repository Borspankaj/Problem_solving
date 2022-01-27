
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1+self.minDepth(root.right)

        if not root.right:
            return 1+self.minDepth(root.left)


        left=self.minDepth(root.left)
        right=self.minDepth(root.right) 
        return min(left,right)+1