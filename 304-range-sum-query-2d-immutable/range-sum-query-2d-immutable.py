class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        for row in range(self.rows):
            for col in range(self.cols):
                up = self.matrix[row-1][col] if row > 0 else 0
                left = self.matrix[row][col-1] if col > 0 else 0
                diag = self.matrix[row-1][col-1] if col >0 and row >0 else 0

                self.matrix[row][col] += up + left - diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self.matrix[row1-1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        diag = self.matrix[row1 -1][col1-1] if col1 > 0 and row1 >0 else 0

        return self.matrix[row2][col2] - up - left + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)