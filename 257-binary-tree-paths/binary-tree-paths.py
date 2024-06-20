# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        re=[]
        def dfs(root,usb):
            if root.left is None and root.right is None:
                usb += f'{root.val}'
                re.append(usb)
                return 
            else:
                usb +=f'{root.val}->'
                if root.left:
                    dfs(root.left,usb)
                if root.right:
                    dfs(root.right,usb)
        dfs(root,"")
        return re