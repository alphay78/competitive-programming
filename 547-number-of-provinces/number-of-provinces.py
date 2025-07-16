class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        
        # Initially each city is its own parent
        parent = [i for i in range(n)]
        
        def find(x):
            # Path compression: flatten the tree
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Merge sets

        # Go through the matrix
        for i in range(n):
            for j in range(i + 1, n):  # Avoid duplicate pairs
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count unique roots (provinces)
        return len(set(find(i) for i in range(n)))
