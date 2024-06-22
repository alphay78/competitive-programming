import re
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        # Convert paragraph to lowercase and remove punctuation
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)  # Replace punctuation with spaces
        
        # Split paragraph into words
        words = paragraph.split()
        
        # Initialize a dictionary to store word frequencies
        word_dict = {}
        
        # Count frequencies of each word
        for word in words:
            if word in banned:
                continue
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        
        # Find the most common word
        max_word = max(word_dict, key=word_dict.get)
        
        return max_word