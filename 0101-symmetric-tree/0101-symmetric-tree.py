# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSimmilar(self, left, right):
        
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        return (left.val == right.val) and self.isSimmilar(left.left, right.right) and self.isSimmilar(left.right, right.left) 
    



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        
        
        else:
            return self.isSimmilar(root.left, root.right)
            
        
        
