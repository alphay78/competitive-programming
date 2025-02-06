class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row ,col = len(img), len(img[0])
        new =[[0 for _ in range(col)] for _ in range(row)]
        direction = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        def inbound(x,y):
            if 0 <= x< row and 0<=y<col:
                return True
            return False
            
        for i in range(row):
            for j in range(col):
                total,count= img[i][j],1
                for dx,dy in direction:
                    x,y = i+dx,j+dy
                    if inbound(x,y):
                        total+=img[x][y]
                        count+=1
                avg = total//count
                new[i][j] = avg
        return new
