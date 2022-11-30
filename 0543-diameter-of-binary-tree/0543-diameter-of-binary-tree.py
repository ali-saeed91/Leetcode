# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0
        self.getDia(root)
        return self.maxDia
    
    def getDia(self, root):
        if not root:
            return 0
        
        left = self.getDia(root.left)
        right = self.getDia(root.right)
        
        dia = left + right
        self.maxDia = max(self.maxDia, dia)
        return max(left,right) +1