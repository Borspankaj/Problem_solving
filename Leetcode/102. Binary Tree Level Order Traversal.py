# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) :
        
        if root==None:
            return root
        l=[]
        queue=[]
        queue.append(root)
        while queue:
            lenn=len(queue)
            temp=[]
            while lenn>0:
                if queue:
                    node=queue.pop(0)
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                lenn-=1
                    
                
            l.append(temp)
            
        return l