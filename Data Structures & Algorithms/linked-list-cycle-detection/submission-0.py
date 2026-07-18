# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current:
            if getattr(current, 'visited', False) == False:
                current.visited = True
                current = current.next
            elif current.visited == True:
                return True
        return False