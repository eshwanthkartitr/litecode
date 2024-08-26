"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        re=[]
        def helper(node):
            if node is None:
                return None
            for i in node.children:
                helper(i)
            re.append(node.val)
        helper(root)
        return re