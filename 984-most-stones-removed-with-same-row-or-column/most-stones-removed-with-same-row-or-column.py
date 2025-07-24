class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        # Find with path compression
        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        # Union two nodes
        def union(x, y):
            parent[find(x)] = find(y)

        # Union each stone's row and column (using ~y to keep x and y in separate spaces)
        for x, y in stones:
            union(x, ~y)

        # Count number of unique connected components
        unique_roots = {find(x) for x, y in stones}
        return len(stones) - len(unique_roots)
