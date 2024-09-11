import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        lowerCase_paragraph = paragraph.lower()
        clean_paragraph = re.sub(r'[^\w\s]', ' ', lowerCase_paragraph)
        
        words = clean_paragraph.split()
        
        banned_set = set(banned)
        
        word_count = Counter(word for word in words if word not in banned_set)
        
        # Find the most common word
        most_common_word = max( word_count, key= word_count.get)

        return most_common_word
