class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(val=-5000, next=head)
        last_sorted = head 
        cur = head.next 
        while cur:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy_head
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = last_sorted.next
            
        return dummy_head.next