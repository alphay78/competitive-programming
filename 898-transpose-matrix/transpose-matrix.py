class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows , cols = len(matrix) , len(matrix[0])
        transpose =[ [0  for _ in range(rows)] for _ in range(cols) ]
        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]
        return transpose


                

        

    