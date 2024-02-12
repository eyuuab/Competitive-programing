class node:
    def __init__ (self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def prt(self):
        cur =self.head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
    def __init__(self):
        self.head=None
        self.size= 0

    def get(self, index: int) -> int:
    
        if index>=self.size:
            return -1
        cur = self.head

        while index>0:
            cur = cur.next
            index-=1
        return cur.val


    def addAtHead(self, val: int) -> None:
    
        temp = node(val)
        temp.next = self.head
        self.head = temp
        self.size +=1

    def addAtTail(self, val: int) -> None:
    
        temp = node(val)
        cur = self.head
        if self.size ==0:
            self.head = temp
        else:
            while cur.next:
                cur = cur.next
            cur.next = temp

        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
    
        if index>self.size:
            return 
        temp = node(val)
        dummy = node(0)
        dummy.next = self.head
        cur = dummy
        while index>0:
            cur = cur.next
            index-=1
        temp.next = cur.next
        cur.next = temp
        self.head = dummy.next

        self.size+=1
        
    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size:
            return 
        
        dummy = node(0)
        dummy.next = self.head
        cur = dummy
        while index:
            cur = cur.next
            index-=1
        cur.next = cur.next.next
        self.head = dummy.next
        self.size-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)