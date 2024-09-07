# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nums=set(nums)
        hi=dummy
        while head:
            if head.val not in nums:
                hi.next = head
                hi=hi.next
            head = head.next
            hi.next=None
        return dummy.next