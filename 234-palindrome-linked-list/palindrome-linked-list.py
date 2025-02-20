# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True


        slow = fast = head
        prev = None
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp


        while prev :
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True



        