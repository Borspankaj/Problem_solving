# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def solve(root,s):
            if not root:
                return False

            
            if s==root.val and (not root.left and not root.right):
                return True
            
            return solve(root.left,s-root.val) or solve(root.right,s-root.val)
        
        return solve(root,targetSum)