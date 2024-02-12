class double:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = double(homepage)
        

    def visit(self, url: str) -> None:
        temp = double(url)
        self.cur.next = temp
        temp.prev = self.cur
        self.cur = temp
       

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps-=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps-=1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)