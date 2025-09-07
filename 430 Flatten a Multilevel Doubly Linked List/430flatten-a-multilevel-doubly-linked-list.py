"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        prev = Node(-1, None, head, None)

        def dfs(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            tmp = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            
            return dfs(tail, tmp)

        dfs(prev, head)

        prev.next.prev = None
        return prev.next




