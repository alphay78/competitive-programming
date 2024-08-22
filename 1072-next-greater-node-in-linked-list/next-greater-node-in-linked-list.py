# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # stack1 = []
        # ans = []


        # current = head
        # if head == None:
        #     return [0]


        # while(current != None):
        #     stack1.append(current)
        #     current = current.next


        # for i in range(len(stack1)):
        #     for j in range(i, len(stack1)):
        #         flag = True
        #         if stack1[i].val < stack1[j].val:
        #             ans.append(stack1[j].val)
        #             flag = False
        #             break
        #     if flag:
        #         ans.append(0)
        # return ans



       
        stack = []
        result = []
        current = head
        index = 0

        while current:
            while stack and current.val > stack[-1][0]:
                value, i = stack.pop()
                result[i] = current.val
            stack.append([current.val, index])
            result.append(0)
            current = current.next
            index += 1

        return result

