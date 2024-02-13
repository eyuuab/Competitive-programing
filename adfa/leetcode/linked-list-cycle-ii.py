# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                break
        if not fast or not fast.next:
            return None
        forward = head
        idx = 0
        while True:
            if forward == fast:
                
                return fast
            fast = fast.next
            forward = forward.next
            idx+=1

        
