class ListNode:
    def __init__(self, val) -> None:
        self.val, self.pre, self.next = val, None, None

class BrowserHistory:
    numberOfPages: int = 0
    pointerIndex: int = 0
    
    def __init__(self, homepage: str) -> None:
        self.homepage = ListNode(homepage)
        self.pointer, self.tail = self.homepage, self.homepage
    
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.pointer.next = None
        newNode.pre = self.pointer
        self.pointer.next = newNode
        self.pointer = newNode
        self.tail = newNode
        BrowserHistory.numberOfPages = BrowserHistory.pointerIndex+1
        BrowserHistory.pointerIndex += 1

    def back(self, steps: int) -> str:
        if steps >= BrowserHistory.pointerIndex:
            self.pointer = self.homepage
            BrowserHistory.pointerIndex = 0
            return self.homepage.val
        elif steps < BrowserHistory.pointerIndex:
            BrowserHistory.pointerIndex = BrowserHistory.pointerIndex-steps
            for i in range(steps):
                self.pointer = self.pointer.pre
        return self.pointer.val
    
    def forward(self, steps: int) -> str:
        formula = BrowserHistory.numberOfPages-BrowserHistory.pointerIndex
        if steps > formula:
            self.pointer = self.tail
            BrowserHistory.pointerIndex = BrowserHistory.numberOfPages
            return self.tail
        elif steps <= formula:
            BrowserHistory.pointerIndex += steps
            for i in range(steps):
                self.pointer = self.pointer.next
            return self.pointer.val
    
    def view(self):
        curr = self.homepage
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            if curr:
                print(" <-> ", end=" ")

BHistory = BrowserHistory("LeetCode.com")
BHistory.visit("Google.com")
BHistory.visit("Facebook.com")
BHistory.visit("Youtube.com")
#################################
BHistory.back(1)
#################################
BHistory.back(1)
#################################
BHistory.forward(1)
#################################
BHistory.visit("LinkedIn.com")
#################################
BHistory.back(4)
#################################
BHistory.forward(5)
BHistory.view()
print()
print(f"head: {BHistory.homepage.val}, tail: {BHistory.tail.val}, pointer: {BHistory.pointer.val}, BrowserPages: {BHistory.numberOfPages}, PointerIndex: {BHistory.pointerIndex}")
