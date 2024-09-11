import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # Step 1: Convert paragraph to lowercase and remove punctuation
        lowerCase_paragraph = paragraph.lower()
        clean_paragraph = re.sub(r'[^\w\s]', ' ', lowerCase_paragraph)
        
        # Step 2: Split paragraph into words
        words = clean_paragraph.split()
        
        # Step 3: Create a dictionary to count word frequencies
        word_count = {}
        
        # Step 4: Iterate over words and update counts, skipping banned words
        banned_set = set(banned)  # Convert banned list to a set for fast lookup
        for word in words:
            if word not in banned_set:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        # Step 5: Find the word with the maximum frequency
        most_common_word = max(word_count, key=word_count.get)
        
        return most_common_word
