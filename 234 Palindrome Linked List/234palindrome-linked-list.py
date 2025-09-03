# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        if fast:
            slow = slow.next

        while prev:
            if prev.val != slow.val:
                return False
            slow = slow.next
            prev = prev.next

        return True