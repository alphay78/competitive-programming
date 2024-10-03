from collections import defaultdict

# Define the Solution class
class Solution:
    def groupAnagrams(self, strs):
        # This will store the groups of anagrams
        anagrams = defaultdict(list)

        # Go through each word in the list
        for word in strs:
            # Sort the letters of the word to use as a key
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the group that matches the sorted letters
            anagrams[sorted_word].append(word)
        
        # Return all the groups of anagrams
        return list(anagrams.values())


