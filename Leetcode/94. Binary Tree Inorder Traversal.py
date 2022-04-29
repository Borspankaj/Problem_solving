# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        l=[]
        def pre(root,l):
            if not root:
                return
            
            pre(root.left,l)
            l.append(root.val)
            pre(root.right,l)
            
        pre(root,l)
        return l