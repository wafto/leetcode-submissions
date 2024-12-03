# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        aux = head
        
        while True:
            lowest = None
            index = -1

            for i in range(len(lists)):
                if not lists[i]:
                    continue

                if not lowest or lists[i].val < lowest.val:
                    lowest = lists[i]
                    index = i
                
            if not lowest:
                break
            else:
                aux.next = lowest
                aux = aux.next
                lists[index] = lists[index].next
        
        return head.next

            
