# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        current = head
        
        while current:
            # Shift left by 1 bit and add the current node's value
            decimal_value = (decimal_value << 1) | current.val
            current = current.next
        
        return decimal_value
        