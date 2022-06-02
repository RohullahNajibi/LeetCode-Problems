# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = False
        pos = 0
        visited = []
        visited.append(head)
        while head:
            if head.next in visited:
                return True
            head = head.next
            visited.append(head)
        return False