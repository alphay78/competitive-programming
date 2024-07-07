# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_checker = 0
        node = head
        while node:
            len_checker += 1
            node = node.next

        current = head
        
        for i in range(len_checker//2):
            current = current.next
        
        return current
