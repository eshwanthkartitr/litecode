# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        q = [root]
        par = defaultdict(list)
        while q:
            curr = q.pop()
            if curr is None:
                continue
            if curr.left is not None:
                par[curr.val].append(curr.left.val)
                par[curr.left.val].append(curr.val)
                q.append(curr.left)
            if curr.right is not None:
                par[curr.val].append(curr.right.val)
                par[curr.right.val].append(curr.val)
                q.append(curr.right)
        
        dq = deque([start])
        vis = set([start])

        mins = -1

        while dq:
            for _ in range(len(dq)):
                val = dq.popleft()
                for nei in par[val]:
                    if nei not in vis:
                        vis.add(nei)
                        dq.append(nei)
            mins+=1
        return mins



