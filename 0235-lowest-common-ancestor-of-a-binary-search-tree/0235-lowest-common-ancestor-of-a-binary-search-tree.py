# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1=[]
        path2=[]
        def traverse(node,end,path):
            if not node:
                return None
            if node.val==end.val:
                return path+[node.val]
            tmp1=traverse(node.left,end,path+[node.val])
            if tmp1:
                return tmp1
            tmp2=traverse(node.right,end,path+[node.val])
            if tmp2:
                return tmp2
        path1=traverse(root,p,path1)
        path2=traverse(root,q,path2)
        p1,p2=0,0
        last_common=None
        while p1<len(path1) and p2<len(path2):
            if path1[p1]==path2[p2]:
                last_common=path1[p1]
                p1+=1
                p2+=1
            else:
                break
        return TreeNode(last_common)