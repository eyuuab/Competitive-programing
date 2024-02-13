# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(start,end,remain):
        cur = start
        prev = None
        end.next = None
       
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            
            cur = temp
        start.next = remain
        
        return prev
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if head.next ==None or l == r:
            return head

        dummy = ListNode()
        dummy.next = head
        left = right = dummy
        while right and r:
            if l-1>0:
                left = left.next
            right = right.next
            l-=1
            r-=1
        
        prev = left
        remain = right.next
        print(remain)
        cur = reverse(prev.next,right,remain)
        prev.next = cur
        
        return dummy.next
       