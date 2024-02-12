# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        while cur.next:
            cur = cur.next
        cur.next = headA
        slow = headB
        fast =headB
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast== slow:
                break
        if not fast or not fast.next:
            cur.next = None
            return None
        forward = headB
        while True:
            if forward == fast:
                cur.next = None
                return fast
            fast = fast.next
            forward = forward.next
            
            
        return None
            


        
    

        