class Solution(object):
    def isValid(self, s):
        stack = []
        my_dict = {'(':')' , '{':'}', '[':']'}

        for i in s:
            if i in my_dict:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if my_dict[top] != i:
                        return False
        return not stack



                        


     

        


