# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        re=[]
        def postorder(x,re,to_delete):
            if x is None:
                return None
            if x.left:
                x.left = postorder(x.left,re,to_delete)
            if x.right:
                x.right = postorder(x.right,re,to_delete)
            if x.val in to_delete:
                if x.left is not None:
                    re.append(x.left)
                if x.right is not None:
                    re.append(x.right)
                x.left = None
                x.right = None
                return None
            return x
        tmp = postorder(root,re,to_delete)
        re=re[::-1]
        re.append(tmp)
        re=re[::-1]
        return re
            