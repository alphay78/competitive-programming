class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        for i,c in enumerate(s):
            my_dict[c] = i
        print(my_dict)
        
        res = []
        size , end = 0 , 0
        for  i,c in enumerate(s):
            size+=1
            end = max(end , my_dict[c])  
            if i == end:
                res.append(size)
                size = 0
        
        return res

    '''
{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
size = 1
end = 8
res = []
    '''