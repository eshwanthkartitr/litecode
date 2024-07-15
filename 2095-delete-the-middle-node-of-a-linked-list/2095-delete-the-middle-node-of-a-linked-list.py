# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return []
        tmp=head
        n=0
        while head:
            n+=1
            head=head.next
        head=tmp
        prev=None
        current = head
        for i in range(n//2):
            prev=current
            current = current.next
        if prev:
            prev.next = current.next
        return head