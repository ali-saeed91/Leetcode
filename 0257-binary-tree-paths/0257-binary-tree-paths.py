# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
    
        def dfs(root, mystr):
            if not root.left and not root.right:
                mystr = mystr + str(root.val)
                res.append(mystr)
            mystr = mystr + str(root.val) + '->'
            if root.left:
                left = dfs(root.left, mystr)
            if root.right:
                right = dfs(root.right, mystr)
            
        dfs(root,'')
        return res
            
        