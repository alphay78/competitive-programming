from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        count = Counter(words)
        
        # Sort by frequency first (descending), then lexicographically (ascending)
        sorted_words = sorted(count.keys(), key=lambda word: (-count[word], word))
        
        # Return the top k words
        return sorted_words[:k]
