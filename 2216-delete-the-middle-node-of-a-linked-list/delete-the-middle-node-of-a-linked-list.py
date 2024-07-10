# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         count =  0
#         while current:
#             count+=1
#             current=current.next
#         current = head
#         c1=0
#         while c1 < count//2:
#             current = Current.next
#         temp = current.next
#         current.next = current.next.next
#      return head


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        # Use the two-pointer technique to find the middle node
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Delete the middle node
        prev.next = slow.next
        
        return head


            



        