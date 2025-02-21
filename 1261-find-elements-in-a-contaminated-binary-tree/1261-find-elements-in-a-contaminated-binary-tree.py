# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.re=set([0])
        root.val=0
        tmp = [root]
        while tmp:
            curr = tmp.pop()
            if curr.left is not None:
                self.re.add(2*curr.val+1)
                curr.left.val = 2*curr.val+1
                tmp.append(curr.left)
            if curr.right is not None:
                self.re.add(2*curr.val+2)
                curr.right.val = 2*curr.val+2
                tmp.append(curr.right)
        



    def find(self, target: int) -> bool:
        return target in self.re
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)