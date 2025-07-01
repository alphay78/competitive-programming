class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        # BFS function starting from a list of coordinates
        def bfs(starts):
            visited = set()
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    # Check boundaries and height condition
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        queue.append((nr, nc))
            return visited

        # Pacific starts (top row and left column)
        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]

        # Atlantic starts (bottom row and right column)
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        # Perform BFS from both oceans
        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        # Intersection of the two sets
        result = list(pacific_reach & atlantic_reach)
        return result
