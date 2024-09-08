# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        le=0
        def traverse(head):
            nonlocal le
            if head is None:
                return None
            le+=1
            return traverse(head.next)
        traverse(head)
        hi = divmod(le,k)
        ref=[hi[0]]*k
        for i in range(hi[1]):
            ref[i]+=1
        fi=[]
        curr=head
        for i in ref:
            if curr:
                fi.append(curr)
                sub_part = curr
                for _ in range(i-1):
                    curr=curr.next
                sub_part = curr.next
                curr.next=None
                curr=sub_part
                
            else:
                fi.append(None)
        return fi