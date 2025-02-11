class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = Counter(s)
        res = []

        for i, j in my_dict.items():
            res.append((i, j))  

        res = sorted(res, key=lambda x: x[1], reverse=True)  

        print(res)


        return ''.join(char * freq for char, freq in res)

