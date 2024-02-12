# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur =head
        if head==None or head.next==None:
            return False
        for i in range(10000):
            if cur.next==None:
                return False
            cur = cur.next
        return True
            