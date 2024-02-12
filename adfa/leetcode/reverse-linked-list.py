class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
    
        while cur:
            
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

        """class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_head"""