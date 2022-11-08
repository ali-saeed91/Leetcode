# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        mystr = str(root.val)
        # print(mystr)
        
        if root.left:
            mystr += "(" + self.tree2str(root.left) + ")"
        
        if root.right:
            if not root.left:
                mystr += "()"
            mystr += "(" + self.tree2str(root.right) + ")"
        return mystr