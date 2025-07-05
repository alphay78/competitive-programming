from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        word_len = len(beginWord)
        steps = 1

        while begin_set and end_set:
            # Always expand the smaller set
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()
            for word in begin_set:
                for i in range(word_len):
                    prefix, suffix = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = prefix + c + suffix
                        if new_word in end_set:
                            return steps + 1
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            next_level.add(new_word)

            begin_set = next_level
            steps += 1

        return 0