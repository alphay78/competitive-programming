class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        current =  head
        while current:
            temp = current.next
            current.next = first
            first = current
            current = temp
        return first
