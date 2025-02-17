class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        if len(s) < 4 or len(s) > 12:  # ✅ IP must be between 4 and 12 digits
            return res
        
        def backtrack(start, parts):
            print(f"\U0001f50d Exploring: start={start}, parts={parts}, remaining={s[start:]}")  # Debugging

            # ✅ Base Case: If we have 4 parts
            if len(parts) == 4:
                if start == len(s):  # ✅ If all characters are used, add to result
                    res.append(".".join(parts))
                    print(f"✅ Valid IP found: {'.'.join(parts)}\n")
                return
            
            # ✅ Try segment lengths of 1, 2, and 3
            for length in range(1, 4):
                if start + length <= len(s):
                    part = s[start:start + length]  # Extract segment

                    # ✅ Skip invalid segments (leading zeros or >255)
                    if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                        print(f"❌ Skipping invalid part: {part}\n")
                        continue
                    
                    print(f"\U0001f4cc Choosing part: {part}")  # Debugging
                    
                    # ✅ Recur with the new segment added
                    backtrack(start + length, parts + [part])
                    print(f"\U0001f519 Backtracking from: {part}")  # Debugging
        
        backtrack(0, [])
        return res

# Test case
solution = Solution()
print("Valid IPs:", solution.restoreIpAddresses("25525511135"))
