# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = fast.next
        return slow
    
    # [1, 2, 3, 4, 5, 6]
    # [S, F]
    # [   S,    F]
    # [      S,       F]
    # [          S, ]