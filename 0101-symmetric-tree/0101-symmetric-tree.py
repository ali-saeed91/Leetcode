# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,left,right):
        if left == None and right == None:
            return True
        if left == None and right == None:
            return False
        if left == None or right == None:
            return False
        if left.val != None and right.val != None and left.val == right.val:
            return self.check(left.left,right.right) and self.check(left.right,right.left)
           
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None or (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        left = root.left
        right = root.right

        return self.check(left,right)
