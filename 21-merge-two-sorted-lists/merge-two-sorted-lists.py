class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the head of the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of the non-exhausted list
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the merged list starting from the node next to the dummy node
        return dummy.next

# Helper function to convert list to ListNode
