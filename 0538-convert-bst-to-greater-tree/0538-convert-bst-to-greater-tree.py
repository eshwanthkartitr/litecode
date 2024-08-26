# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cnt = 0
        re=[]
        def helper(root,dummy):
            nonlocal cnt
            if root is None:
                return None
            dummy.right=root.right
            dummy.left=root.left
            helper(root.right,dummy.right)
            cnt+=root.val
            dummy.val = cnt
            re.append((cnt,root.val))
            helper(root.left,dummy.left)
        dummy=TreeNode(0)
        if not root:
            return root
        helper(root,dummy)
        return dummy