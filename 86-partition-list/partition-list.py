# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head = small = ListNode(0)  # Dummy node for small values
        large_head = large = ListNode(0)  # Dummy node for large values

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next  # Move to next node
        
        large.next = None  # End large list
        small.next = large_head.next  # Merge lists

        return small_head.next  # New head of partitioned list
        