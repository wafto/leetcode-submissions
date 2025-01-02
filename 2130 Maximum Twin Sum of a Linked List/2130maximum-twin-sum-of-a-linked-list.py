# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        output = 0

        while slow:
            output = max(output, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return output


        #stack = []

        #while fast and fast.next:
        #    stack.append(slow.val)
        #    fast = fast.next.next
        #    slow = slow.next

        #maxSum = -inf
        
        #while stack:
        #    last = stack.pop()
        #    maxSum = max(maxSum, last + slow.val)
        #    slow = slow.next

        #return maxSum



