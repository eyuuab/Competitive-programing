# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt+=1
        cur = head
        cnt=cnt//2
        print(cnt)
        while cnt>0:
            cur = cur.next
            cnt-=1
        return cur