class StackNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class MyStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        node = StackNode(x)
        if self.empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self) -> int:
        node = self.head
        self.head = self.head.next
        return node.val      

    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return self.head == None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()