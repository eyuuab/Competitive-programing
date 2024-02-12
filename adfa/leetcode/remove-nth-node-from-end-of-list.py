# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        left = right = dummy
        cnt = 0
        if head.next ==None:
            return 
        while cnt<=n and right:
            right = right.next
            cnt+=1
        
        while right:
            right = right.next
            left = left.next
        
        left.next  = left.next.next

        return dummy.next
