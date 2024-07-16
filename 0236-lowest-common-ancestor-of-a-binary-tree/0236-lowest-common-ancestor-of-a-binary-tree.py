# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        l_c_a = self.lowestCommonAncestor(root.left,p,q)
        r_c_a = self.lowestCommonAncestor(root.right,p,q)
        if l_c_a and r_c_a:
            return root
        return l_c_a if l_c_a else r_c_a