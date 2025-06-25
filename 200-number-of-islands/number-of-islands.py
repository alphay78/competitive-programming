class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def in_bound(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1'
        
        def dfs(row, col):
            visited.add((row, col))
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if in_bound(new_row, new_col) and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
        
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1
        
        return island_count
