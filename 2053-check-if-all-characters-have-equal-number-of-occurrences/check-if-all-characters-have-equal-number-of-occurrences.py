from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        my_dict = Counter(s)
        count = my_dict[s[0]]

        for i in my_dict.values():
            if i != count:   
                return False
        return True

       
  
    
        