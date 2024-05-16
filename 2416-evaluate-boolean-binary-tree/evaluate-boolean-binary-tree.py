# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if(root.left==None and root.right==None):
            return root.val
        else:
            val1 = self.dfs(root.left)
            val2 = self.dfs(root.right)
            if root.val == 2:
                return val1 or val2
            else:
                return val1 and val2 
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:       
        return self.dfs(root)