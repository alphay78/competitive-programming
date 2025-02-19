from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to handle edge cases
        dummy.next = head
        prev, current = dummy, head

        while current:
            if current.val == val:
                prev.next = current.next  # Skip the node with the target value
            else:
                prev = current
            current = current.next

        return dummy.next  # Return the new head
