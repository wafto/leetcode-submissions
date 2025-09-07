# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Comparator:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other) -> bool:
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nhead = curr = ListNode(-1)
        minheap = []

        for node in lists:
            if node:
                heappush(minheap, Comparator(node))

        while minheap:
            node = heappop(minheap).node
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(minheap, Comparator(node.next))

        return nhead.next