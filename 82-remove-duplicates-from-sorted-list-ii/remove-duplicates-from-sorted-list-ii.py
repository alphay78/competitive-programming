from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)  
        prev = dummy 
        curr = head  
        
        while curr and curr.next:
            if curr.val == curr.next.val:  # Found duplicate
                duplicate_val = curr.val
                # Skip all nodes with this value
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr  # Link to the next unique node
            else:
                prev = curr  # Move prev forward if no duplicate
                curr = curr.next  # Move curr forward

        return dummy.next  # Return the modified list
