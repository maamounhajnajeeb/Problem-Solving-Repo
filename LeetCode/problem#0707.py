# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
    # here
    def get(self, index: int) -> int:
        length: int = self.__length(self.head)
        if index >= length:
            return -1
        dummyIndex: int = 0
        curr: Optional[Node] = self.head
        while index != dummyIndex:
            curr, dummyIndex = curr.next, dummyIndex+1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode: Optional[Node] = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode: Optional[Node] = Node(val)
        if not self.head:
            self.addAtHead(val)
        elif not self.head.next:
            self.head.next = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode: Optional[Node] = Node(val)
        length: int = self.__length(self.head)
        if index > length:
            return
        elif index == 0 or not self.head:
            self.addAtHead(val)
        elif index == length:
            self.addAtTail(val)
        else:
            dummyIndex: int = 1
            pre: Optional[Node]; curr: Optional[Node]
            pre, curr = self.head, self.head.next
            while dummyIndex != index:
                pre, curr, dummyIndex = pre.next, curr.next, dummyIndex+1
            newNode.next = curr
            pre.next = newNode  
    
    def deleteAtIndex(self, index: int) -> None:
        length: int = self.__length(self.head)
        if index >= length:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            dummyIndex: int = 1
            pre: Optional[Node]; curr: Optional[Node]
            pre, curr = self.head, self.head.next
            while dummyIndex != index:
                pre, curr, dummyIndex = pre.next, curr.next, dummyIndex+1
            pre.next = curr.next
        
    # helper methods
    def __length(self, head: Optional[Node]) -> int:
        index: int = 0
        while head:
            head = head.next
            index += 1
        return index
