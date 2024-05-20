# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            while stack and head.val > stack[-1]:
                stack.pop()
            stack.append(head.val)
            head=head.next 
        dummy = ListNode()
        cur = dummy
        for i in stack:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next