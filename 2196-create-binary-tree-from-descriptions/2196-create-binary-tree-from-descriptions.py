# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root=set()
        nodes={}
        for i,j,k in descriptions:
            if i not in nodes:
                nodes[i] = TreeNode(i)
            if j not in nodes:
                nodes[j] = TreeNode(j)
            if k ==1:
                nodes[i].left = nodes[j]
            else:
                nodes[i].right = nodes[j]
            root.add(j)
        for i,j,k in descriptions:
            if i not in root:
                return nodes[i]