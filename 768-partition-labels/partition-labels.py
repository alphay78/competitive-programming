class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}

        for i,c in enumerate(s):
            my_dict[c] = i

        res = []
        size , end = 0 , 0
        for  i,c in enumerate(s):
            size+=1
            end = max(end , my_dict[c])

            if i == end:
                res.append(size)
                size = 0
        return res