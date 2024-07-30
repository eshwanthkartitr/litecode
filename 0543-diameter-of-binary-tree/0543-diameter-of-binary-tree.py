# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        gb_val = 0
        def dfs(root):
            nonlocal gb_val
            if root is None:
                return 0

            if root.left is None and root.right is None:
                return 1
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            gb_val = max(gb_val,left_val+right_val)
            return max(left_val,right_val)+1

        return gb_val