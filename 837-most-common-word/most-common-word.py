import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        lowerCase_paragraph = paragraph.lower()
        clean_paragraph = re.sub(r'[^\w\s]', ' ', lowerCase_paragraph)
       
        words = clean_paragraph.split()
        
        word_count = {}
        
        banned_set = set(banned)  
        for word in words:
            if word not in banned_set:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        most_common_word = max(word_count, key=word_count.get)
        
        return most_common_word
