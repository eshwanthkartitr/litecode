# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev=dummy
        curr = head
        i=0
        while curr:
            if curr.val == val:
                prev.next = curr.next
            curr = curr.next
        return dummy.next
