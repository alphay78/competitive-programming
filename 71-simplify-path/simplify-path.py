class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by "/" to get individual components
        components = path.split('/')
        
        for component in components:
            if component == "..":
                if stack:
                    stack.pop()
            elif component == "." or component == "":
                continue
            else:
                stack.append(component)
        
        # Join the stack with "/" to form the canonical path
        simplified_path = "/" + "/".join(stack)
        
        return simplified_path
