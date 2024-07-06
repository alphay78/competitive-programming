class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode, method='iterative') -> ListNode:
        if method == 'iterative':
            return self.reverseListIterative(head)
        elif method == 'recursive':
            return self.reverseListRecursive(head)
        else:
            raise ValueError("Unknown method. Use 'iterative' or 'recursive'.")

    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev and current one step forward
            current = next_node
        
        return prev  # prev will be the new head of the reversed list

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        reversed_list_head = self.reverseListRecursive(head.next)
        
        head.next.next = head
        head.next = None
        
        return reversed_list_head

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list of values
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
reversed_head = solution.reverseList(head, method='iterative')
print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = solution.reverseList(head, method='recursive')
print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]
