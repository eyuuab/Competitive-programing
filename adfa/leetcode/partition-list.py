# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small, large = [],[]
        if head ==None:
            return 
        cur = head
        while cur:
            if cur.val>=x:
                large.append(cur.val)
            else:
                small.append(cur.val)
            cur = cur.next
        dummy = ListNode(0)
        cur = dummy
        s = 0
        while s<len(small):
            cur.val = small[s]
            temp = ListNode(0)
            cur.next = temp
            cur = cur.next
            s+=1
        l= 0
    
        while l<len(large):
            cur.val = large[l]
            temp = ListNode()
            cur.next = temp
            cur = cur.next
            l+=1
        cur = dummy
        while cur and cur.next:
            if cur.next.next == None:
                cur.next = None
            cur =cur.next

        return dummy
            