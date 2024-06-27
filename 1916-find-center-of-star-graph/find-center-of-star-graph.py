class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # The center of the star graph will be either one of the nodes from the first edge
        # Check which one of them is also present in the second edge
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]