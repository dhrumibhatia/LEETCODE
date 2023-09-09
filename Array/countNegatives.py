class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(1 for i in grid for e in i if e < 0)