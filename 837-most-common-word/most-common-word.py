class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\b\w+\b', paragraph)
        words = [word.lower() for word in words]
        words_dict = {}

        for word in words:
            if word.lower() not in banned:
                if word not in words_dict:
                    words_dict[word] = 0
                words_dict[word]+=1
        print(words_dict)
        return max(words_dict, key=words_dict.get)