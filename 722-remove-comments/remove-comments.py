class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_comment = False
        ans = []
        for line in source:
            i = 0
            if not in_comment:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_comment:
                    in_comment = True
                    i += 1
                elif line[i:i+2] == "*/" and in_comment:
                    in_comment = False
                    i += 1
                elif line[i:i+2] == '//' and not in_comment:
                    break
                elif not in_comment:
                    newline.append(line[i])
                i+=1

            if newline and not in_comment:
                ans.append("".join(newline))
        return ans

                


        